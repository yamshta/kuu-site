#!/usr/bin/env python3
"""tips 動画 6 種 (ライブ撮影分) を各言語で録画・エンコードする。

t_move / t_edit / t_release / t_theme_press : Place 画面 (saved シード)
t_remove / t_reclassify                     : 分類結果画面 (result シード)
t_theme_drag                                : ライブ再現不可 → synthesize_theme_drag.py で合成

出力: 860x798 h264 24fps mp4 + 先頭フレームの <name>_poster.jpg
録画: simctl io recordVideo (native 1206x2622) → ffmpeg で crop/scale/fps/trim。

使い方:
  python3 capture_videos.py --udid <UDID> --locales da,nb --workdir /tmp/tips_work \
      --app <KUU.app>
"""
import argparse
import json
import os
import signal
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from capture_stills import WDA, fresh_install, launch, esc, LABELS, BUNDLE  # noqa: E402,F401

# クロップ (native px)。Place 系はカード領域 (チップ行の要否で 2 種)、result 系は結果カード領域。
CROP_PLACE = (0, 436, 1206, 1119)        # チップ行なし・カード下端まで (t_move/t_edit/t_release)
CROP_PLACE_CHIPS = (0, 296, 1206, 1119)  # チップ行あり (t_theme_press / t_theme_drag 素材)
CROP_RESULT = (0, 470, 1206, 1119)       # 結果カード領域 (t_remove/t_reclassify)
OUT_W, OUT_H = 860, 798

# 各動画の尺 (旧アセットに合わせる) と頭のトリム秒 (ドラッグ系は W3C actions の
# ディスパッチ遅延で動作が遅れて映るため、頭を落として動作を尺の中央に収める)
DURATION = {"t_move": 4.3, "t_reclassify": 5.3, "t_release": 2.6,
            "t_remove": 2.6, "t_theme_press": 4.0, "t_edit": 4.0}
TRIM_SS = {"t_move": 1.8, "t_reclassify": 1.8}


class Recorder:
    def __init__(self, udid, path):
        self.proc = subprocess.Popen(
            ["xcrun", "simctl", "io", udid, "recordVideo",
             "--codec", "h264", "--force", path],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(1.2)  # 録画立ち上がり

    def stop(self):
        self.proc.send_signal(signal.SIGINT)
        self.proc.wait(timeout=15)
        time.sleep(0.3)


def encode(raw, out, crop, dur, ss=0.0):
    x, y, w, h = crop
    subprocess.run(
        ["ffmpeg", "-y", "-v", "error", "-ss", str(ss), "-i", raw,
         "-vf", f"crop={w}:{h}:{x}:{y},scale={OUT_W}:{OUT_H},fps=24",
         "-t", str(dur), "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p",
         "-crf", "23", "-movflags", "+faststart", out],
        check=True)
    subprocess.run(
        ["ffmpeg", "-y", "-v", "error", "-i", out, "-frames:v", "1",
         "-q:v", "4", out.replace(".mp4", "_poster.jpg")], check=True)


def w3c_drag(wda, path_pts, hold_ms=850, step_ms=320):
    """long-press で持ち上げてから path_pts (論理 pt) を辿るドラッグ。"""
    acts = [{"type": "pointerMove", "duration": 0, "x": path_pts[0][0], "y": path_pts[0][1]},
            {"type": "pointerDown", "button": 0},
            {"type": "pause", "duration": hold_ms}]
    for x, y in path_pts[1:]:
        acts.append({"type": "pointerMove", "duration": step_ms, "x": x, "y": y})
    acts += [{"type": "pause", "duration": 250}, {"type": "pointerUp", "button": 0}]
    wda._req("POST", f"/session/{wda.sid}/actions",
             {"actions": [{"type": "pointer", "id": "finger1",
                           "parameters": {"pointerType": "touch"}, "actions": acts}]})


def tap_at(wda, x, y):
    w3c = [{"type": "pointerMove", "duration": 0, "x": x, "y": y},
           {"type": "pointerDown", "button": 0},
           {"type": "pause", "duration": 60},
           {"type": "pointerUp", "button": 0}]
    wda._req("POST", f"/session/{wda.sid}/actions",
             {"actions": [{"type": "pointer", "id": "finger1",
                           "parameters": {"pointerType": "touch"}, "actions": w3c}]})


def rect_of(wda, predicate, min_y=None):
    els = wda.find_all(predicate)
    for e in els:
        r = wda.rect(e)
        if min_y is None or r["y"] > min_y:
            return r
    raise RuntimeError(f"not found: {predicate}")


def item_rect(wda, label):
    return rect_of(wda, f'label == "{esc(label)}" AND type == "XCUIElementTypeStaticText"')


def capture_locale(udid, wda, lc, outdir, app_path, item_labels):
    os.makedirs(outdir, exist_ok=True)
    L = {k: v[lc] for k, v in LABELS.items()}
    IT = {k: v[lc] for k, v in item_labels.items()}

    def record(name, crop, prepare, act, *launch_args):
        """prepare() は録画前に要素座標を解決して act に渡す (録画中の find 待ちを避け、
        アクションが動画尺の前半に入るようにする)。
        動画ごとに fresh_install してシードを作り直す — 前の動画のジェスチャーが
        状態を変える (t_release が項目を手放す等) ため、使い回すと画面が壊れる。"""
        fresh_install(udid, app_path)
        launch(udid, lc, *launch_args)
        ctx = prepare()
        raw = os.path.join(outdir, f"_{name}_raw.mov")
        rec = Recorder(udid, raw)
        try:
            time.sleep(0.7)
            act(ctx)
        finally:
            rec.stop()
        encode(raw, os.path.join(outdir, f"{name}.mp4"), crop, DURATION[name],
               TRIM_SS.get(name, 0.0))

    place_args = ("-KUUSeedScenario", "saved", "-KUUPlaceExpanded", "1",
                  "-KUUScreenshotSlot", "place")
    result_args = ("-KUUSeedScenario", "result", "-KUUScreenshotSlot", "result")

    def center(r):
        return (r["x"] + r["width"] / 2, r["y"] + r["height"] / 2)

    # t_edit: タイトルをタップ → 展開して書き直し (現仕様は原文引用つき展開)
    def act_edit(c):
        tap_at(wda, *c)
        time.sleep(2.8)
    record("t_edit", CROP_PLACE,
           lambda: center(item_rect(wda, IT["now1"])), act_edit, *place_args)

    # t_release: 項目先頭の○をタップ → 手放すへ
    def act_release(c):
        tap_at(wda, c[0], c[1])
        time.sleep(1.6)
    record("t_release", CROP_PLACE,
           lambda: (lambda r: (r["x"] - 18, r["y"] + r["height"] / 2))(
               item_rect(wda, IT["now1"])),
           act_release, *place_args)

    # t_move: 項目を長押し → 右の象限へドラッグ
    def act_move(c):
        sx, sy = c
        n = 8
        pts = [(sx, sy)] + [(sx + 190 * i / n, sy + 80 * i / n)
                            for i in range(1, n + 1)]
        w3c_drag(wda, pts, hold_ms=850, step_ms=200)
        time.sleep(2.2)
    record("t_move", CROP_PLACE,
           lambda: center(item_rect(wda, IT["now1"])), act_move, *place_args)

    # t_theme_press: テーマチップ長押し → メニュー表示
    def act_theme_press(el):
        wda.touch_and_hold(el, 0.9)
        time.sleep(2.2)
    record("t_theme_press", CROP_PLACE_CHIPS,
           lambda: wda.find_all(f'label CONTAINS "{esc(L["theme_work"])}" '
                                'AND type == "XCUIElementTypeStaticText"')[0],
           act_theme_press, *place_args)

    # t_remove: 分類結果で項目タップ → 淡くなって外れる
    def act_remove(c):
        tap_at(wda, *c)
        time.sleep(1.6)
    record("t_remove", CROP_RESULT,
           lambda: center(item_rect(wda, IT["res_now2"])), act_remove, *result_args)

    # t_reclassify: 分類結果で項目を隣の象限へドラッグ
    def act_reclassify(c):
        sx, sy = c
        n = 8
        pts = [(sx, sy)] + [(sx + 205 * i / n, sy + 50 * i / n)
                            for i in range(1, n + 1)]
        w3c_drag(wda, pts, hold_ms=1100, step_ms=200)
        time.sleep(2.6)
    record("t_reclassify", CROP_RESULT,
           lambda: center(item_rect(wda, IT["res_now1"])), act_reclassify,
           *result_args)

    # t_theme_drag: ライブ再現不可のため合成 (詳細は synthesize_theme_drag.py docstring)
    import synthesize_theme_drag as std
    fresh_install(udid, app_path)
    launch(udid, lc, *place_args)
    item = item_rect(wda, IT["now1"])
    chip = rect_of(wda, f'label CONTAINS "{esc(L["theme_work"])}" '
                        'AND type == "XCUIElementTypeStaticText"')
    src = os.path.join(outdir, "_place_chips_full.png")
    subprocess.run(["xcrun", "simctl", "io", udid, "screenshot", src],
                   check=True, capture_output=True)
    std.synthesize(src, [item["x"], item["y"], item["width"], item["height"]],
                   [chip["x"], chip["y"], chip["width"], chip["height"]],
                   os.path.join(outdir, "t_theme_drag.mp4"))


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--udid", required=True)
    p.add_argument("--wda", default="http://127.0.0.1:50318")
    p.add_argument("--locales", required=True)
    p.add_argument("--workdir", required=True)
    p.add_argument("--app", required=True)
    a = p.parse_args()
    item_labels = json.load(open(os.path.join(HERE, "item_labels.json")))
    wda = WDA(a.wda)
    for lc in a.locales.split(","):
        print(f"=== {lc} ===", file=sys.stderr)
        capture_locale(a.udid, wda, lc, os.path.join(a.workdir, lc), a.app,
                       item_labels)
    print(json.dumps({"ok": True}))
