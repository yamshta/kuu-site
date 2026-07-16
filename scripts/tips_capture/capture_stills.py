#!/usr/bin/env python3
"""tips 静止画 4 種 (t_keyboard / t_resort / t_add / t_theme_edit) を各言語で撮影・合成する。

前提:
- KUU-dev がシミュレータにインストール済み・kuu.hasOnboarded=true
- WDA が起動済みでセッションが存在する (prepare_ios_simulator 済み)
- labels.json (xcstrings から抽出したローカライズ済みラベル) が同 dir にある

使い方:
  python3 capture_stills.py --udid <UDID> --wda http://127.0.0.1:50318 \
      --locales da,nb,sv --workdir /tmp/tips_work

各静止画のクロップ/円は iPhone 17 (native 1206x2622) 前提の校正値。
円座標はローカライズで動く要素 (キーボード行・分け直す行・テーマ行) は
WDA の element rect から言語ごとに解決する。
"""
import argparse
import json
import os
import subprocess
import sys
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from compose import compose  # noqa: E402

BUNDLE = "com.KUU-app.dev"
LABELS = json.load(open(os.path.join(HERE, "labels.json")))["labels"]
REGION = {"nl": "nl_NL", "id": "id_ID", "ms": "ms_MY", "da": "da_DK",
          "nb": "nb_NO", "sv": "sv_SE", "fi": "fi_FI", "fr": "fr_FR",
          "th": "th_TH", "ru": "ru_RU", "en": "en_US"}

# t_add のクロップ上端 (native)。既定 780 は「左右カードとも行を切らない」カットラインだが、
# 折返しの多い言語は行帯域が変わるため目視レビューで調整した値を持つ
# (fr は全行 2 行折返しで安全地帯がなく、アイテム行の下・+ ボタン中心の構図にする)。
TADD_CROP_Y = {"id": 856, "fr": 1008}


class WDA:
    def __init__(self, base):
        self.base = base
        st = self._req("GET", "/status")
        self.sid = st["sessionId"]

    def _req(self, method, path, body=None):
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(self.base + path, data=data, method=method,
                                     headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)

    def find_all(self, predicate):
        r = self._req("POST", f"/session/{self.sid}/elements",
                      {"using": "predicate string", "value": predicate})
        return [list(e.values())[0] for e in r["value"]]

    def rect(self, el):
        return self._req("GET", f"/session/{self.sid}/element/{el}/rect")["value"]

    def click(self, el):
        self._req("POST", f"/session/{self.sid}/element/{el}/click", {})

    def touch_and_hold(self, el, duration=0.9):
        self._req("POST", f"/session/{self.sid}/wda/element/{el}/touchAndHold",
                  {"duration": duration})


def fresh_install(udid, app_path):
    """シード (seedItems) は DB が空のときしか走らないため、言語を変えるたびに
    アプリを入れ直して永続データを消す (前言語のシード項目が残ると画面が旧言語になる)。"""
    subprocess.run(["xcrun", "simctl", "terminate", udid, BUNDLE],
                   capture_output=True)
    subprocess.run(["xcrun", "simctl", "uninstall", udid, BUNDLE],
                   capture_output=True)
    subprocess.run(["xcrun", "simctl", "install", udid, app_path],
                   check=True, capture_output=True)
    subprocess.run(["xcrun", "simctl", "spawn", udid, "defaults", "write",
                    BUNDLE, "kuu.hasOnboarded", "-bool", "true"],
                   check=True, capture_output=True)


def launch(udid, lang, *args):
    subprocess.run(["xcrun", "simctl", "terminate", udid, BUNDLE],
                   capture_output=True)
    cmd = ["xcrun", "simctl", "launch", udid, BUNDLE,
           "-AppleLanguages", f"({lang})", "-AppleLocale", REGION[lang]] + list(args)
    subprocess.run(cmd, check=True, capture_output=True)
    time.sleep(3.5)


def shot(udid, path):
    subprocess.run(["xcrun", "simctl", "io", udid, "screenshot", path],
                   check=True, capture_output=True)


def esc(s):
    return s.replace('"', '\\"')


def center3(rect):
    """論理 pt rect → native px 中心 (x3)。"""
    return (round((rect["x"] + rect["width"] / 2) * 3),
            round((rect["y"] + rect["height"] / 2) * 3))


def capture_locale(udid, wda, lc, outdir, app_path):
    os.makedirs(outdir, exist_ok=True)
    fresh_install(udid, app_path)
    L = {k: v[lc] for k, v in LABELS.items()}

    # 1. t_keyboard: ホーム (水位高め)。円 = キーボード行 (icon+text 全体) の中心
    launch(udid, lc, "-KUUSeedScenario", "saved", "-KUUScreenshotSlot", "hero",
           "-KUUHeadLevel", "0.9")
    els = wda.find_all(f'label == "{esc(L["keyboard"])}"')
    r = wda.rect(els[0])
    # icon はテキスト左 ~19pt: 行全体の中心に寄せる
    cx, cy = center3(r)
    src = os.path.join(outdir, "_home_full.png")
    shot(udid, src)
    compose(src, os.path.join(outdir, "t_keyboard.png"),
            (0, 1231, 1206, 753), (cx - 28, cy))

    # 2. t_resort: 分類結果。円 = 「分け直す」中心
    launch(udid, lc, "-KUUSeedScenario", "result", "-KUUScreenshotSlot", "result")
    els = wda.find_all(f'label == "{esc(L["sort_again"])}"')
    r = wda.rect(els[0])
    cx, cy = center3(r)
    src = os.path.join(outdir, "_result_full.png")
    shot(udid, src)
    compose(src, os.path.join(outdir, "t_resort.png"),
            (0, 1810, 1206, 753), (cx, cy))

    # 3. t_add: Place 展開。レイアウト固定なので円座標は共通 (左象限の + 中心)
    launch(udid, lc, "-KUUSeedScenario", "saved", "-KUUPlaceExpanded", "1",
           "-KUUScreenshotSlot", "place")
    src = os.path.join(outdir, "_place_full.png")
    shot(udid, src)
    compose(src, os.path.join(outdir, "t_add.png"),
            (0, TADD_CROP_Y.get(lc, 780), 1206, 753), (492, 1428))

    # 4. t_theme_edit: チップ長押し → テーマを編集… → シート。円 = 1 行目の色ドット
    chips = wda.find_all(
        f'label CONTAINS "{esc(L["theme_work"])}" AND type == "XCUIElementTypeStaticText"')
    wda.touch_and_hold(chips[0], 0.9)
    time.sleep(0.8)
    menu = wda.find_all(f'label BEGINSWITH "{esc(L["edit_themes"])}"')
    wda.click(menu[0])
    time.sleep(1.5)
    # シート内の行テキスト (チップと同ラベルなので y>200pt で行側を選ぶ)
    rows = wda.find_all(
        f'label == "{esc(L["theme_work"])}" AND type == "XCUIElementTypeStaticText"')
    row = next(r for r in (wda.rect(e) for e in rows) if r["y"] > 200)
    src = os.path.join(outdir, "_themeedit_full.png")
    shot(udid, src)
    compose(src, os.path.join(outdir, "t_theme_edit.png"),
            (0, 368, 1206, 753), (240, round((row["y"] + row["height"] / 2) * 3)))


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--udid", required=True)
    p.add_argument("--wda", default="http://127.0.0.1:50318")
    p.add_argument("--locales", required=True, help="comma separated (e.g. da,nb)")
    p.add_argument("--workdir", required=True)
    p.add_argument("--app", required=True, help="KUU.app のパス")
    a = p.parse_args()
    wda = WDA(a.wda)
    for lc in a.locales.split(","):
        print(f"=== {lc} ===", file=sys.stderr)
        capture_locale(a.udid, wda, lc, os.path.join(a.workdir, lc), a.app)
    print(json.dumps({"ok": True, "locales": a.locales.split(",")}))
