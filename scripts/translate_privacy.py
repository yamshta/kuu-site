#!/usr/bin/env python3
"""Auto-translate the privacy policy into all supported locales via Gemini.

ja (content/privacy/ja.md) is the authoritative legal text. This script keeps the
other locales (content/privacy/<code>.md) in sync as *reference translations*,
re-translating a locale only when the ja source changed (hash tracked in
content/privacy/.source_hash.json) — the same "only what changed" idea as the
iOS xcstrings i18n automation.

Usage:
  GEMINI_API_KEY=... python3 scripts/translate_privacy.py            # stale/missing only
  GEMINI_API_KEY=... python3 scripts/translate_privacy.py --force    # all
  GEMINI_API_KEY=... python3 scripts/translate_privacy.py --locales fr,de

en is authored by hand (kept as the primary reference) and is not overwritten.
Meta (title/description per locale) is written to content/privacy/meta.json.
"""
import argparse
import hashlib
import json
import os
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRIV = ROOT / "content" / "privacy"
HASH_FILE = PRIV / ".source_hash.json"
META_FILE = PRIV / "meta.json"

# code -> (language name for the prompt, localized "Article" word hint)
TARGETS = {
    "es": ("Spanish (Español)", "Artículo"),
    "ko": ("Korean (한국어)", "제N조"),
    "zh-Hans": ("Simplified Chinese (简体中文)", "第N条"),
    "zh-Hant": ("Traditional Chinese (繁體中文)", "第N條"),
    "de": ("German (Deutsch)", "Artikel"),
    "it": ("Italian (Italiano)", "Articolo"),
    "vi": ("Vietnamese (Tiếng Việt)", "Điều"),
    "nl": ("Dutch (Nederlands)", "Artikel"),
    "id": ("Indonesian (Bahasa Indonesia)", "Pasal"),
    "ms": ("Malay (Bahasa Melayu)", "Perkara"),
    "da": ("Danish (Dansk)", "Artikel"),
    "nb": ("Norwegian Bokmål (Norsk)", "Artikkel"),
    "sv": ("Swedish (Svenska)", "Artikel"),
    "fi": ("Finnish (Suomi)", "Artikla"),
    "fr": ("French (Français)", "Article"),
    "th": ("Thai (ไทย)", "ข้อ"),
    "ru": ("Russian (Русский)", "Статья"),
}

# ja/en meta seed (en authored by hand; ja is the source of truth for the doc).
SEED_META = {
    "ja": {
        "title": "プライバシーポリシー — KUU",
        "description": "KUU のプライバシーポリシー。音声はすべて端末内で処理し外部に送信しません。整理の AI 分類は文字だけを送信し保存しません。",
    },
    "en": {
        "title": "Privacy Policy — KUU",
        "description": "KUU's privacy policy. Audio is processed entirely on device and never sent outside. AI organization sends only the text, and the provider does not retain it.",
    },
}

GEMINI = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"


def gemini(prompt, key, models=("gemini-2.5-pro", "gemini-2.5-flash")):
    body = json.dumps({"contents": [{"parts": [{"text": prompt}]}]}).encode()
    last = None
    for model in models:
        for attempt in range(3):
            try:
                req = urllib.request.Request(
                    GEMINI.format(model=model, key=key),
                    data=body, headers={"Content-Type": "application/json"},
                )
                with urllib.request.urlopen(req, timeout=180) as r:
                    d = json.load(r)
                return d["candidates"][0]["content"]["parts"][0]["text"]
            except Exception as e:  # noqa: BLE001 - retry across models
                last = e
                time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"Gemini failed: {last}")


def translate_body(ja, en, name, article, key):
    prompt = (
        f"You are a professional legal translator. Translate the following privacy "
        f"policy from Japanese (authoritative) into {name}. Use the English version "
        f"only as a phrasing reference.\n"
        f"Rules:\n"
        f"- Preserve the Markdown structure exactly: headings (# / ##), lists (-), "
        f"bold (**), and links [text](url). DO NOT change any URL.\n"
        f"- Render article headings naturally in the target language "
        f"(e.g. '{article}').\n"
        f"- Keep KUU's calm, quiet tone but stay precise and legally clear.\n"
        f"- CRITICAL: never blur Article 3 — the Android version ALWAYS sends the "
        f"transcribed text to the external AI (Google's Gemini) when organizing, "
        f"with no on-device option.\n"
        f"- At the very top, before the H1, add one blockquote line, translated into "
        f"the target language, meaning: 'This is a reference translation for "
        f"convenience. The Japanese version is the authoritative text.'\n"
        f"Output ONLY the translated Markdown, nothing else.\n\n"
        f"=== Japanese (authoritative) ===\n{ja}\n\n"
        f"=== English (reference) ===\n{en}\n"
    )
    return gemini(prompt, key).strip() + "\n"


def translate_meta(name, key):
    prompt = (
        f"Translate these two short strings for a privacy policy page into {name}. "
        f'Return ONLY compact JSON {{"title":"...","description":"..."}}.\n'
        f'title (ja): "プライバシーポリシー — KUU"\n'
        f'description (ja): "KUU のプライバシーポリシー。音声はすべて端末内で処理し外部に'
        f'送信しません。整理の AI 分類は文字だけを送信し保存しません。"\n'
        f"Keep 'KUU' as-is in the title."
    )
    raw = gemini(prompt, key).strip()
    raw = raw.removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    return json.loads(raw)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="re-translate all targets")
    ap.add_argument("--locales", help="comma-separated subset (e.g. fr,de)")
    args = ap.parse_args()

    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        sys.exit("GEMINI_API_KEY not set")

    ja = (PRIV / "ja.md").read_text()
    en = (PRIV / "en.md").read_text()
    src_hash = hashlib.sha256(ja.encode()).hexdigest()
    hashes = json.loads(HASH_FILE.read_text()) if HASH_FILE.exists() else {}
    meta = json.loads(META_FILE.read_text()) if META_FILE.exists() else {}
    meta.update(SEED_META)

    only = set(args.locales.split(",")) if args.locales else None
    todo = []
    for code, (name, article) in TARGETS.items():
        if only and code not in only:
            continue
        target = PRIV / f"{code}.md"
        if args.force or not target.exists() or hashes.get(code) != src_hash:
            todo.append((code, name, article))
        else:
            print(f"skip {code} (up to date)")

    def work(item):
        code, name, article = item
        print(f"translate {code} ({name}) ...", flush=True)
        body = translate_body(ja, en, name, article, key)
        m = translate_meta(name, key)
        return code, body, m

    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=6) as ex:
        for code, body, m in ex.map(work, todo):
            (PRIV / f"{code}.md").write_text(body)
            meta[code] = m
            hashes[code] = src_hash
            print(f"  wrote {code}", flush=True)

    HASH_FILE.write_text(json.dumps(hashes, ensure_ascii=False, indent=2) + "\n")
    META_FILE.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n")
    print("done.")


if __name__ == "__main__":
    main()
