#!/usr/bin/env python3
"""t_theme_drag を合成アニメで生成する。

項目→テーマチップのドラッグはライブ再現不可 (上方向 reorder が engage しない +
system .dropDestination は synthetic touch で drop しない — kuu-site PR #20 で
mobilecli / Maestro / perform_actions / drag_and_drop の 4 手法を検証済み)。
そのため Place スクショから項目行のゴーストカードを作り、チップへ滑らせる
アニメーションを PIL で描いて ffmpeg で mp4 化する。

使い方:
  python3 synthesize_theme_drag.py --src place_chips_full.png \
      --item-rect X,Y,W,H --chip-rect X,Y,W,H --out t_theme_drag.mp4
  (rect は論理 pt。内部で x3 して native px にする)
"""
import argparse
import math
import os
import subprocess
import tempfile
from PIL import Image, ImageDraw, ImageFilter

CROP = (0, 296, 1206, 1119)   # capture_videos.CROP_PLACE_CHIPS と同じ
OUT_W, OUT_H = 860, 798
FPS, DUR = 24, 1.708
N_FRAMES = int(FPS * DUR)     # 41


def ease(t):
    return 0.5 - 0.5 * math.cos(math.pi * t)


def make_ghost(base, item_px):
    """項目行を角丸カード + 影のゴーストにする。"""
    x, y, w, h = item_px
    pad_x, pad_y = 54, 30
    row = base.crop((x - pad_x, y - pad_y, x + w + pad_x, y + h + pad_y))
    gw, gh = row.size
    card = Image.new("RGBA", (gw + 40, gh + 40), (0, 0, 0, 0))
    mask = Image.new("L", (gw, gh), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, gw - 1, gh - 1], radius=34, fill=255)
    # 影
    sh = Image.new("RGBA", card.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([20, 26, 20 + gw, 26 + gh], radius=34,
                                         fill=(60, 90, 120, 90))
    sh = sh.filter(ImageFilter.GaussianBlur(12))
    card.alpha_composite(sh)
    white = Image.new("RGBA", (gw, gh), (255, 255, 255, 235))
    card.alpha_composite(white, (20, 20), )
    row_rgba = row.convert("RGBA")
    row_rgba.putalpha(mask)
    card.alpha_composite(row_rgba, (20, 20))
    return card


def synthesize(src, item_rect_pt, chip_rect_pt, out):
    base = Image.open(src).convert("RGBA")
    item_px = [round(v * 3) for v in item_rect_pt]
    chip_px = [round(v * 3) for v in chip_rect_pt]
    ghost = make_ghost(base, item_px)

    # 開始 = 項目行の中心、終了 = チップの下 ~90px (ドロップ直前で止まる見せ方)
    sx = item_px[0] + item_px[2] / 2
    sy = item_px[1] + item_px[3] / 2
    exx = chip_px[0] + chip_px[2] / 2
    eyy = chip_px[1] + chip_px[3] + 96

    frames_dir = tempfile.mkdtemp(prefix="tdrag_")
    cx0, cy0, cw, chh = CROP
    for i in range(N_FRAMES):
        t = i / (N_FRAMES - 1)
        # 最初の 15% は持ち上げ (その場でスケール)、残りで移動
        mv = ease(max(0.0, (t - 0.15) / 0.85))
        gx, gy = sx + (exx - sx) * mv, sy + (eyy - sy) * mv
        scale = 1.0 + 0.06 * min(1.0, t / 0.15)
        fr = base.copy()
        # チップ着地間際に淡いハイライト
        if t > 0.72:
            a = int(70 * (t - 0.72) / 0.28)
            hi = Image.new("RGBA", fr.size, (0, 0, 0, 0))
            ImageDraw.Draw(hi).rounded_rectangle(
                [chip_px[0] - 24, chip_px[1] - 18,
                 chip_px[0] + chip_px[2] + 24, chip_px[1] + chip_px[3] + 18],
                radius=30, fill=(114, 159, 193, a))
            fr.alpha_composite(hi)
        g = ghost.resize((int(ghost.width * scale), int(ghost.height * scale)),
                         Image.LANCZOS) if scale != 1.0 else ghost
        fr.alpha_composite(g, (int(gx - g.width / 2), int(gy - g.height / 2)))
        fr.convert("RGB").crop((cx0, cy0, cx0 + cw, cy0 + chh)) \
          .resize((OUT_W, OUT_H), Image.LANCZOS) \
          .save(os.path.join(frames_dir, f"f{i:03d}.png"))

    subprocess.run(
        ["ffmpeg", "-y", "-v", "error", "-framerate", str(FPS),
         "-i", os.path.join(frames_dir, "f%03d.png"),
         "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "23",
         "-movflags", "+faststart", out], check=True)
    subprocess.run(
        ["ffmpeg", "-y", "-v", "error", "-i", out, "-frames:v", "1", "-q:v", "4",
         out.replace(".mp4", "_poster.jpg")], check=True)
    print(f"wrote {out} ({N_FRAMES} frames)")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--src", required=True)
    p.add_argument("--item-rect", required=True, help="X,Y,W,H (pt)")
    p.add_argument("--chip-rect", required=True, help="X,Y,W,H (pt)")
    p.add_argument("--out", required=True)
    a = p.parse_args()
    synthesize(a.src, [float(v) for v in a.item_rect.split(",")],
               [float(v) for v in a.chip_rect.split(",")], a.out)
