#!/usr/bin/env python3
"""tips 静止画の合成: フルスクリーンショットをクロップ → タップ円を合成 → 900x562 で出力。

使い方:
  python3 compose.py --src full.png --out t_add.png --crop X,Y,W,H --circle CX,CY[,R]

- crop / circle はスクリーンショットのネイティブ px 座標 (iPhone 17 = 1206x2622)。
- 出力は 900x562 固定 (既存アセットと同寸)。

タップ円のスタイルは既存アセット (assets/tips/en/t_add.png) と自前キャプチャの
差分から実測して再現したもの:
  - スティールブルー (114,159,193) を α0.35 で乗せた円盤
  - リング線はなく、半径の外側 ~30% がガウシアン状に減衰するソフトエッジ
  - 半径 ≈83px (ネイティブ px、900 幅出力時 ≈62px)
"""
import argparse
import numpy as np
from PIL import Image

OUT_W, OUT_H = 900, 562
CIRCLE_RGB = (114, 159, 193)
CIRCLE_ALPHA = 0.35
DEFAULT_R = 83          # native px
EDGE_SOFT = 30          # r 以降で 0 に減衰する幅 (native px)


def circle_mask(w, h, cx, cy, r):
    Y, X = np.mgrid[0:h, 0:w].astype(np.float32)
    d = np.sqrt((X - cx) ** 2 + (Y - cy) ** 2)
    m = np.clip((r + EDGE_SOFT - d) / EDGE_SOFT, 0, 1)
    m[d <= r - 8] = 1.0
    return m * CIRCLE_ALPHA


def compose(src, out, crop, circle=None):
    img = np.asarray(Image.open(src).convert("RGB"), dtype=np.float32)
    x, y, w, h = crop
    region = img[y:y + h, x:x + w].copy()

    if circle:
        cx, cy = circle[0] - x, circle[1] - y
        r = circle[2] if len(circle) > 2 else DEFAULT_R
        a = circle_mask(w, h, cx, cy, r)[..., None]
        color = np.array(CIRCLE_RGB, dtype=np.float32)
        region = region * (1 - a) + color * a

    im = Image.fromarray(np.clip(region, 0, 255).astype(np.uint8))
    im = im.resize((OUT_W, OUT_H), Image.LANCZOS)
    im.save(out, "PNG")
    print(f"wrote {out} ({OUT_W}x{OUT_H})")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--src", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--crop", required=True, help="X,Y,W,H (native px)")
    p.add_argument("--circle", help="CX,CY[,R] (native px)")
    a = p.parse_args()
    crop = [int(v) for v in a.crop.split(",")]
    circle = [int(v) for v in a.circle.split(",")] if a.circle else None
    compose(a.src, a.out, crop, circle)
