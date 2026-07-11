"""Generate per-locale LP and support pages for kuu-site.

Source of truth for translations:
- KUU/Localizable.xcstrings (4 quadrant labels)
- KUU/fastlane/metadata/<locale>/*.txt (tone)
- KUU/docs/concept.md, copy_guide.md (world view / copy)

Output:
- /index.html, /support/index.html  (ja, at root)
- /<locale>/index.html, /<locale>/support/index.html  for en, es, ko, zh-Hans
- /privacy/index.html (ja), /en/privacy/index.html (en) — from content/privacy.md
  (source of truth: KUU/docs/legal/PRIVACY_POLICY.md; copy here when it changes)
- /sitemap.xml, /robots.txt

ja is the canonical locale. New marketing copy is authored in ja first; other
locales fall back to ja for any key they have not translated yet (see main()).
"""

import html as html_mod
import json
import os
import re
from pathlib import Path

import markdown as md_lib
import yaml

ROOT = Path(__file__).resolve().parent.parent
APP_STORE_ID = "6771264775"
# installUrl(構造化データ)は国コードなし canonical。CTA リンクは locale ごとの国コード付き。
APP_STORE_URL = f"https://apps.apple.com/app/id{APP_STORE_ID}"
APP_STORE_COUNTRY = {"ja": "jp", "en": "us", "es": "es", "ko": "kr", "zh-Hans": "cn",
                     "zh-Hant": "tw", "de": "de", "it": "it", "vi": "vn"}


def app_store_cta_url(code):
    country = APP_STORE_COUNTRY[code]
    return f"https://apps.apple.com/{country}/app/id{APP_STORE_ID}"
OG_IMAGE = "https://kuu-zen.com/assets/og.png"
BASE_URL = "https://kuu-zen.com"
# App Store の実評価 (社会的証明として journal 記事の CTA に表示)。
# 取得元: https://itunes.apple.com/lookup?id=6771264775&country=jp — 定期的に手動で更新する。
APP_RATING = {"score": "4.2", "count": 168}
# tips のスクショ (assets/tips/*.png) はファイル名を変えず中身を差し替えるため、
# ブラウザキャッシュ回避に日付版クエリ ?v= を付ける。スクショを更新したら日付を上げる。
ASSET_VERSION = "20260701b"
# これらの thumb 名は静止画でなく mp4 ループ動画で見せる（<name>.mp4 + <name>_poster.jpg）。
# 動き（ドラッグ&ドロップ等）は動画のほうが伝わるため。iOS Safari の自動再生条件に合わせ
# autoplay + muted + playsinline を付ける。
VIDEO_THUMBS = {"t_move", "t_theme_drag", "t_reclassify",
                "t_release", "t_theme_press", "t_remove", "t_edit"}

_TIPS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "tips")


def tips_asset(code, name, ext):
    """ロケール別 tips アセット (assets/tips/<code>/<name>.<ext>) があればそれを、
    無ければ ja (root: assets/tips/<name>.<ext>) を返す。各言語 UI で撮り直した
    スクショ/動画を assets/tips/<locale>/ に置くと自動で差し替わる (#18 の段階展開用)。"""
    sub = f"{code}/" if os.path.exists(os.path.join(_TIPS_DIR, code, f"{name}.{ext}")) else ""
    return f"/assets/tips/{sub}{name}.{ext}?v={ASSET_VERSION}"
# GA4 web stream measurement ID (G-XXXXXXXXXX). Empty = no analytics tag emitted.
# Stream: properties/539320049/dataStreams/15063638495 (kuu-zen.com)
GA4_MEASUREMENT_ID = "G-DC1R54C73B"
# Privacy policy is hosted on this site in ja/en only; other locales link to en.
PRIVACY_LOCALES = ("ja", "en")
# Usage tips page is ja-only for now (other locales added later, same pattern as PRIVACY_LOCALES).
TIPS_LOCALES = ("ja", "en", "es", "ko", "zh-Hans", "zh-Hant", "de", "it", "vi")
# Content SEO articles (/journal/<slug>/) are ja-only for now, same pattern as TIPS_LOCALES.
JOURNAL_LOCALES = ("ja",)

LOCALES = {
    "ja": {
        "subdir": "",
        "html_lang": "ja",
        "og_locale": "ja_JP",
        "label": "日本語",
        "title": "KUU — 考えごとを話すだけ。AIが4つに分ける音声思考整理アプリ",
        "description": "KUU は、考えごとを声に出すだけで、AI が「いま見る / あとで考える / 寝かせる / 手放す」の4つに整える音声思考整理アプリ。忙しい頭を空っぽにする、静かなAIメモです。",
        # Hero
        "hero_headline": "話して、あたまに余白を。",
        "hero_sub": "考えごとでいっぱいになった頭から、いま持たなくていいものを、声に出すだけ。",
        "cta": "App Store で入手",
        "scroll_cue": "下へ",
        # Why
        "why_eyebrow": "なぜ KUU か",
        "why_headline": "頭の中には、いろんな思考が混ざっている。",
        "why_scenario": "作業の途中で、別のことがふと浮かぶ。忘れたくないのに、いま向き合うものでもない。",
        "why_lead": "タスク管理に入れると「やること」になり、メモに書くと埋もれる。散らかるのは、思考そのものより「どう扱うか」の判断のほう。",
        "thoughts": [
            "やらなきゃいけない気がすること",
            "あとで考えたいこと",
            "まだ形になっていないアイデア",
            "なんとなく気になる違和感",
            "今は考えても仕方ない心配ごと",
        ],
        "why_note": "KUU は、片づける前に、まず受け止める。声に出すほど、頭の水位が下がっていく。",
        # How
        "steps_eyebrow": "使い方",
        "steps_headline": "やることは、話すだけ。",
        "steps": [
            ("話す", "まとまっていなくて大丈夫。声にすると、忘れていたことまで連なって出てくる。"),
            ("分ける", "KUU が、いま見る / あとで考える / 寝かせる / 手放す に静かに分ける。"),
            ("棚卸しする", "落ち着いたころ、見返して扱いを整える。積み上げっぱなしにしない。"),
        ],
        # App showcase
        "app_eyebrow": "アプリ",
        "app_headline": "これが、KUU。",
        "screen_alt": "KUU の画面",
        # Matrix
        "matrix_eyebrow": "KUU マトリクス",
        "matrix_headline": "思考の、置き場所。",
        "matrix_lead": "タスク分類ではなく、頭の中にあるものの扱い方で分ける。",
        "quadrants": [
            ("いま見る", "今、少し目を向けると軽くなること"),
            ("あとで考える", "今ではなく、別のタイミングで"),
            ("寝かせる", "まだ結論を出さず、置いておく"),
            ("手放す", "もう持ち続けなくてよさそうなこと"),
        ],
        "quadrants_aria": "KUU マトリクス",
        # Privacy
        "privacy_eyebrow": "プライバシー",
        "privacy_headline": "あなたの声は、外に出ない。",
        "privacy_body": "音声の聞きとりはすべて端末の中だけ。声そのものは残さず、送りません。整理には AI を使い、送るのは文字にした内容だけ。それも保存されません（設定で端末内のみにもできます）。話したことは、あなたの iCloud（プライベート）にだけ同期されます。",
        # Closing
        "closing_headline": "話したあと、すこし頭が軽い。",
        "closing_sub": "それだけのための、静かなアプリです。",
        # Footer
        "support_label": "サポート",
        "privacy_label": "プライバシー",
        "lang_switcher_aria": "言語",
        # Support page
        "support_title": "サポート — KUU",
        "support_description": "KUU のサポートに関するお問い合わせ先と FAQ。",
        "support_h1": "サポート",
        "support_intro": "KUU をご利用いただきありがとうございます。ご不明な点や不具合のご報告は、下記までご連絡ください。",
        "contact_h2": "お問い合わせ",
        "contact_body": "サポート窓口は近日公開予定です。",
        "faq_h2": "よくある質問",
        "faqs": [
            (
                "声は保存されますか？",
                "いいえ。KUU は音声を端末から外に出さず、認識が完了したら一時音声ファイルを削除します。整理のために外部の AI に送るのは文字にした内容だけで、それも保存されません。残るのは、あなたの端末と iCloud にある文字起こしと分類結果だけです。",
            ),
            (
                "iCloud 同期は？",
                "iCloud Private DB に同期されます (Apple ID 所有者本人のみアクセス可)。開発者サーバーはありません。",
            ),
        ],
        # Tips / usage page (ja-only for now; see TIPS_LOCALES)
        "tips_title": "使い方のコツ — KUU",
        "tips_description": "KUU の気づきにくい操作のまとめ。音声入力のあとの書き直し、自分での仕分け、テーマの使い方を静かに紹介します。",
        "tips_eyebrow": "使い方のコツ",
        "tips_h1": "声にしたあとも、自分の手で。",
        "tips_lead": "KUU は画面を静かに保つために、操作の多くを表に出していません。でも、聞き取りを直したり、自分の手で仕分けたりは、ちゃんとできます。気づきにくいものを、ここにまとめました。",
        # 画面単位でセクション分け（アプリを使う人の「いまこの画面で何ができる？」に合わせる）
        "tips_screens": [
            {
                "heading": "考えの置き場で",
                "lead": "ホームから引き上げる、いちばん使う画面。声で分けたものは、4つの置き場に集まります。気づきにくい操作も、ほとんどがここに。",
                "groups": [
                    {
                        "subhead": "項目をひとつずつ整える",
                        "items": [
                            ("タップ", "タイトルをタップして書き直す", "項目の文字をそのままタップすると、その場で書き直せます。聞き取りの小さなズレは、ここで整えられます。", "t_edit"),
                            ("長押し → ドラッグ", "別の場所へ移す", "項目を長押ししてドラッグすると、いま見る / あとで考える / 寝かせる / 手放す のあいだを自由に移し替えられます。", "t_move"),
                            ("ドラッグ", "テーマへ移す", "同じドラッグで、上のテーマチップへも移せます。そのテーマに入り、「未分類」へ落とすと外れます。", "t_theme_drag"),
                            ("タップ", "○をタップして手放す", "項目の先頭にある小さな○をタップすると、その場でそっと「手放す」へ。すぐ取り消すこともできます。", "t_release"),
                            ("タップ", "「＋」で手入力を足す", "各ブロックの右下にある淡い「＋」から、その場所に項目を文字で書き足せます。", "t_add"),
                        ],
                    },
                    {
                        "subhead": "テーマでまとめる",
                        "items": [
                            ("長押し", "テーマを長押しでメニュー", "上のテーマチップを長押しすると、常に表示（ピン留め）/ 名前や色を編集 / 手放す が出ます。テーマの設定は、ここが入口です。", "t_theme_press"),
                            ("タップ", "名前・色・並びを変える", "テーマの編集画面では、名前をタップして書き直し、色の丸から淡い色を選び、左の持ち手で並び替えられます。", "t_theme_edit"),
                        ],
                    },
                ],
            },
            {
                "heading": "分けた直後の画面で",
                "lead": "話して分けた、すぐあと。KUU の分け方がしっくりこなければ、ここで整えてから残せます。",
                "groups": [
                    {
                        "items": [
                            ("タップ", "いらないものはタップで外す", "ピンとこない項目はタップすると淡くなって外れます。もう一度タップで戻せます。", "t_remove"),
                            ("ドラッグ", "ドラッグして分類を変更する", "項目を別のブロックへドラッグすると、その場で分類を変えられます。", "t_reclassify"),
                            ("ボタン", "「分け直す」で全文を直す", "聞き間違いがあれば「分け直す」から、文字起こし全体を直して、もう一度分けられます。", "t_resort"),
                        ],
                    },
                ],
            },
            {
                "heading": "ホームで",
                "lead": "声が出しにくい日もある。そんなときは、文字でも。",
                "groups": [
                    {
                        "items": [
                            ("タップ", "キーボードで書く", "ホーム下の「キーボードで書く」から、声を使わず文字でも、同じように分けられます。", "t_keyboard"),
                        ],
                    },
                ],
            },
        ],
        "tips_note": "これらの案内は、最初の一度だけ画面にそっと出ます。見落としても大丈夫。このページは、いつでも見返せます。",
        "tips_closing_sub": "まだ KUU を試していなければ、こちらから。",
        "tips_label": "使い方のコツ",
        # 不満ベースのよくある問い合わせ（可視セクション + FAQPage 構造化データで共用）
        "tips_faq_heading": "よくある問い合わせ",
        # answer は「文（。）ごとの行」リスト。可視は 1 行 = 1 段落で余白を出し、
        # FAQPage 構造化データは "".join で 1 文に戻す。
        "tips_faqs": [
            (
                "思ったように分けてくれない。精度がいまひとつ。",
                [
                    "KUU の見立ては、いつも完璧ではありません。",
                    "だから、あとから自分の手で直せるようにしています（タップで書き直す／長押しドラッグで移す／「分け直す」）。",
                    "聞きとりと仕分けの精度は、これからも少しずつ良くしていきます。",
                    "あなたが使ってくれることが、その励みになっています。",
                ],
            ),
            (
                "長く話すと、ぜんぶひとつにまとめられてしまう。",
                [
                    "文が続くと、区切りを見つけにくいことがあります。",
                    "話すときは「〜して、（ひと呼吸）〜して」と少し間を置くと、分かれやすくなります。",
                    "すでに入力したものは、「分け直す」で文章に読点や句点（、。）を足すと、区切られやすくなります。",
                    "それでもまとまるときは、長押しドラッグで分けたり、タップで書き直したりできます。",
                ],
            ),
            (
                "すぐ課金に誘われている気がする。",
                [
                    "話して、分けて、見返す——KUU の中心は、ずっと無料で使えます。",
                    "KUU+ は、広告をオフにしたい・Face ID ロックをかけたい方への、そっとした追加です。",
                ],
            ),
            (
                "声を出せない場面では使いにくい。",
                [
                    "ホーム下の「キーボードで書く」から、声を使わず文字でも、同じように分けられます。",
                ],
                "t_keyboard",
            ),
            # 自動テーマ振り分けが正式リリースされたら復活（今は非表示）:
            # (
            #     "テーマを勝手につけてほしくない。",
            #     [
            #         "既定では、AI はテーマを付けません（すべて「未分類」から始まります）。",
            #         "付くのは、あなたが付けたときか、KUU+ で「自動で振り分け」をオンにしたときだけ。いつでも解除できます。",
            #     ],
            # ),
        ],
        "tips_support_before": "音声入力のあとの書き直しや、自分での仕分けなど、気づきにくい操作は",
        "tips_support_after": "にまとめています。",
        "back": "← トップへ",
        # Journal (content SEO articles): pain/method/persona/scene archetypes, KUU-first ではなく悩み起点。
        "journal_eyebrow": "読みもの",
        "journal_hub_title": "読みもの — KUU",
        "journal_hub_description": "頭の中がいっぱいになったときの、考えごととの付き合い方。",
        "journal_hub_lead": "頭の中がいっぱいになったときに、少し軽くするためのヒント。",
        "journal_updated_label": "更新:",
        "journal_pitch_headline": "声に出すと、少し軽くなる。",
        "journal_pitch_body": "KUU は、話すだけで頭の中を「いま見る / あとで考える / 寝かせる / 手放す」に整える、静かなアプリです。",
        "journal_pitch_note": "無料でダウンロードできます。",
        "journal_rating_suffix": "件の評価",
        "journal_related_label": "あわせて読みたい",
        "journal_back_label": "読みものへ戻る",
    },
    "en": {
        "subdir": "en",
        # Tips / usage page (en)
        "tips_title": "Tips — KUU",
        "tips_description": "A round-up of KUU's easy-to-miss moves — a quiet look at editing after you speak, sorting by hand, and using themes.",
        "tips_eyebrow": "Tips",
        "tips_h1": "After you speak, it's still in your hands.",
        "tips_lead": "To keep the screen quiet, KUU keeps most of its controls out of sight. But you can always fix what was heard, or sort things by hand. Here are the ones that are easy to miss.",
        "tips_screens": [
            {
                "heading": "At the place for your thoughts",
                "lead": "The screen you'll use most, pulled up from Home. What you sorted by voice gathers into four places. Most of the easy-to-miss moves are here, too.",
                "groups": [
                    {
                        "subhead": "Tend to items one by one",
                        "items": [
                            [
                                "Tap",
                                "Tap a title to rewrite it",
                                "Tap the words of an item to rewrite them on the spot. Small mishearings can be smoothed out right here.",
                                "t_edit"
                            ],
                            [
                                "Long-press → drag",
                                "Move it elsewhere",
                                "Long-press an item and drag to move it freely between Now, Later, Park, and Let go.",
                                "t_move"
                            ],
                            [
                                "Drag",
                                "Move it to a theme",
                                "The same drag also moves it onto a theme chip above. It joins that theme; drop it onto “Uncategorized” to remove it.",
                                "t_theme_drag"
                            ],
                            [
                                "Tap",
                                "Tap the ○ to let go",
                                "Tap the small ○ at the start of an item to gently send it to Let go. You can undo it right away.",
                                "t_release"
                            ],
                            [
                                "Tap",
                                "Add by hand with “+”",
                                "From the faint “+” at the bottom-right of each block, you can add an item there in text.",
                                "t_add"
                            ]
                        ]
                    },
                    {
                        "subhead": "Group with themes",
                        "items": [
                            [
                                "Long-press",
                                "Long-press a theme for its menu",
                                "Long-press a theme chip above to bring up Always show (pin), Edit name or color, and Let go. This is the way into a theme's settings.",
                                "t_theme_press"
                            ],
                            [
                                "Tap",
                                "Change name, color, and order",
                                "In the theme editor, tap the name to rewrite it, pick a soft color from the color dots, and reorder using the handle on the left.",
                                "t_theme_edit"
                            ]
                        ]
                    }
                ]
            },
            {
                "heading": "Right after sorting",
                "lead": "The moment just after you speak and it's sorted. If KUU's sorting doesn't sit right, tidy it here before you keep it.",
                "groups": [
                    {
                        "items": [
                            [
                                "Tap",
                                "Tap to drop what you don't need",
                                "Tap an item that doesn't fit and it fades out and drops away. Tap again to bring it back.",
                                "t_remove"
                            ],
                            [
                                "Drag",
                                "Drag to change where it goes",
                                "Drag an item to another block to change where it goes, right there.",
                                "t_reclassify"
                            ],
                            [
                                "Button",
                                "“Sort again” to fix the whole text",
                                "If something was misheard, “Sort again” lets you fix the whole transcript and sort it once more.",
                                "t_resort"
                            ]
                        ]
                    }
                ]
            },
            {
                "heading": "On Home",
                "lead": "Some days, speaking aloud is hard. On those days, text works too.",
                "groups": [
                    {
                        "items": [
                            [
                                "Tap",
                                "Write with the keyboard",
                                "From “Write with the keyboard” at the bottom of Home, you can sort the same way in text, without using your voice.",
                                "t_keyboard"
                            ]
                        ]
                    }
                ]
            }
        ],
        "tips_note": "These hints appear gently on screen just once, the first time. If you miss them, that's fine — this page is always here to revisit.",
        "tips_closing_sub": "If you haven't tried KUU yet, start here.",
        "tips_label": "Tips",
        "tips_faq_heading": "Common questions",
        "tips_faqs": [
            [
                "It doesn't sort the way I expected. The accuracy isn't quite there.",
                [
                    "KUU's read on things isn't always perfect.",
                    "That's why you can always fix it by hand afterward (tap to rewrite, long-press and drag to move, or “Sort again”).",
                    "We'll keep improving how it hears and sorts, little by little.",
                    "You using it is what encourages us."
                ]
            ],
            [
                "When I talk for a while, it all gets merged into one.",
                [
                    "When sentences run on, the breaks can be hard to find.",
                    "As you speak, leaving a small pause — “this, (a breath) then that” — helps it split more easily.",
                    "For something you've already entered, adding commas and periods in “Sort again” helps it break into pieces.",
                    "If it still stays merged, you can split it with a long-press drag, or rewrite it with a tap."
                ]
            ],
            [
                "It feels like I'm pushed to pay right away.",
                [
                    "Speak, sort, look back — the heart of KUU stays free, always.",
                    "KUU+ is a quiet extra, for those who'd like to turn off ads or add a Face ID lock."
                ]
            ],
            [
                "It's hard to use when I can't speak aloud.",
                [
                    "From “Write with the keyboard” at the bottom of Home, you can sort the same way in text, without using your voice."
                ],
                "t_keyboard"
            ]
        ],
        "tips_support_before": "Rewriting after you speak, sorting by hand — the moves that are easy to miss are gathered in",
        "tips_support_after": ".",

        "html_lang": "en",
        "og_locale": "en_US",
        "label": "English",
        "title": "KUU — A quiet brain-dump for busy minds",
        "description": "KUU is a quiet voice-first brain-dump app. Speak what is on your mind; KUU sorts it into Now, Later, Park, and Let go.",
        "hero_headline": "Speak, and free your mind.",
        "hero_sub": "From a head full of thoughts, just say out loud what you don't need to carry right now.",
        "cta": "Download on the App Store",
        "scroll_cue": "Scroll",
        "why_eyebrow": "Why KUU",
        "why_headline": "Your head holds all kinds of thoughts.",
        "why_scenario": "Mid-task, something unrelated pops up. You don't want to forget it, but it isn't for right now either.",
        "why_lead": "Put it in a to-do app and it becomes a “task”; jot it in notes and it gets buried. What gets cluttered isn’t the notes — it’s deciding how to handle each one.",
        "thoughts": [
            "Something you feel you ought to do",
            "Something to think about later",
            "An idea not yet in shape",
            "A vague unease you can't place",
            "A worry there's no point dwelling on now",
        ],
        "why_note": "KUU receives it first, before you sort anything. The more you speak, the lower the water in your head.",
        "steps_eyebrow": "How it works",
        "steps_headline": "All you do is talk.",
        "steps": [
            ("Speak", "It doesn’t need to be tidy. Saying it aloud pulls up things you’d forgotten, one after another."),
            ("Sort", "KUU quietly sorts it into Now, Later, Park, and Let go."),
            ("Look back", "When things settle, revisit and tend to them. Nothing just piles up."),
        ],
        "app_eyebrow": "The app",
        "app_headline": "This is KUU.",
        "screen_alt": "KUU app screen",
        "matrix_eyebrow": "The KUU matrix",
        "matrix_headline": "A place for each thought.",
        "matrix_lead": "Not task buckets — a way to hold what's in your head.",
        "quadrants": [
            ("Now", "Worth a glance today to feel lighter"),
            ("Later", "Not now — another time"),
            ("Park", "Set it down without deciding yet"),
            ("Let go", "No longer worth carrying"),
        ],
        "quadrants_aria": "KUU matrix",
        "privacy_eyebrow": "Privacy",
        "privacy_headline": "Your voice stays with you.",
        "privacy_body": "Listening happens entirely on your device — your voice is never kept or sent. Sorting uses AI, so only the text is sent, and it is never kept (you can switch to on-device only). Your notes sync only to your private iCloud.",
        "closing_headline": "After you speak, your head feels lighter.",
        "closing_sub": "A quiet app, made only for that.",
        "support_label": "Support",
        "privacy_label": "Privacy",
        "lang_switcher_aria": "Language",
        "support_title": "Support — KUU",
        "support_description": "Contact and FAQ for KUU.",
        "support_h1": "Support",
        "support_intro": "Thanks for using KUU. For questions or to report an issue, please use the contact below.",
        "contact_h2": "Contact",
        "contact_body": "A dedicated support contact will be available soon.",
        "faq_h2": "Frequently asked questions",
        "faqs": [
            (
                "Is my voice saved?",
                "No. KUU does not send audio off the device, and temporary audio files are deleted once transcription completes. Only the text is sent to an external AI for sorting, and it is not kept either. What remains is the transcript and classification on your device and iCloud.",
            ),
            (
                "Does it sync via iCloud?",
                "Yes. Your notes sync to your private iCloud database, accessible only to you. There is no developer-owned server.",
            ),
        ],
        "back": "← Back to top",
    },
    "es": {
        "subdir": "es",
        # Tips / usage page (es)
        "tips_title": "Consejos de uso — KUU",
        "tips_description": "Un resumen de los gestos discretos de KUU. Te mostramos con calma cómo reescribir lo que dictaste, separar las cosas a tu manera y usar los temas.",
        "tips_eyebrow": "Consejos de uso",
        "tips_h1": "Después de hablar, también con tus manos.",
        "tips_lead": "Para mantener la pantalla en calma, KUU no muestra muchos de sus gestos. Pero corregir lo que oyó o separarlo a tu manera sí que se puede. Aquí hemos reunido lo que cuesta descubrir.",
        "tips_screens": [
            {
                "heading": "En el lugar de tus pensamientos",
                "lead": "La pantalla que subes desde el inicio, la que más usarás. Lo que separaste con la voz se reúne en los cuatro lugares. Y casi todos los gestos discretos están aquí.",
                "groups": [
                    {
                        "subhead": "Ajustar los elementos uno a uno",
                        "items": [
                            [
                                "Toca",
                                "Toca el título para reescribirlo",
                                "Toca el texto de un elemento y podrás reescribirlo ahí mismo. Los pequeños desajustes de la transcripción se arreglan aquí.",
                                "t_edit"
                            ],
                            [
                                "Mantén pulsado → arrastra",
                                "Muévelo a otro lugar",
                                "Mantén pulsado un elemento y arrástralo para moverlo libremente entre Ahora, Más tarde, Reposar y Soltar.",
                                "t_move"
                            ],
                            [
                                "Arrastra",
                                "Muévelo a un tema",
                                "Con el mismo arrastre también puedes llevarlo a los chips de tema de arriba. Entra en ese tema; y al soltarlo en «Sin categoría», sale.",
                                "t_theme_drag"
                            ],
                            [
                                "Toca",
                                "Toca el ○ para soltar",
                                "Toca el pequeño ○ al inicio de un elemento y pasará con suavidad a «Soltar». También puedes deshacerlo enseguida.",
                                "t_release"
                            ],
                            [
                                "Toca",
                                "Añade a mano con «＋»",
                                "Desde el «＋» tenue de la esquina inferior derecha de cada bloque, puedes añadir un elemento escribiéndolo en ese lugar.",
                                "t_add"
                            ]
                        ]
                    },
                    {
                        "subhead": "Agrupar por temas",
                        "items": [
                            [
                                "Mantén pulsado",
                                "Mantén pulsado un tema para el menú",
                                "Mantén pulsado un chip de tema de arriba y aparecerán: Mostrar siempre (fijar), Editar nombre y color, y Soltar. Los ajustes del tema empiezan aquí.",
                                "t_theme_press"
                            ],
                            [
                                "Toca",
                                "Cambia el nombre, el color y el orden",
                                "En la pantalla de edición del tema, toca el nombre para reescribirlo, elige un color suave en el círculo de color y reordena con el asa de la izquierda.",
                                "t_theme_edit"
                            ]
                        ]
                    }
                ]
            },
            {
                "heading": "En la pantalla, justo tras separar",
                "lead": "Justo después de hablar y separar. Si la manera en que KUU separó no te convence, aquí puedes ajustarla antes de guardarla.",
                "groups": [
                    {
                        "items": [
                            [
                                "Toca",
                                "Quita lo que no necesitas con un toque",
                                "Toca un elemento que no encaje y se atenuará hasta salir. Toca otra vez para recuperarlo.",
                                "t_remove"
                            ],
                            [
                                "Arrastra",
                                "Arrastra para cambiar la clasificación",
                                "Arrastra un elemento a otro bloque y cambiarás su clasificación ahí mismo.",
                                "t_reclassify"
                            ],
                            [
                                "Botón",
                                "Corrige todo el texto con «Separar de nuevo»",
                                "Si algo se oyó mal, desde «Separar de nuevo» puedes corregir toda la transcripción y volver a separar.",
                                "t_resort"
                            ]
                        ]
                    }
                ]
            },
            {
                "heading": "En el inicio",
                "lead": "Hay días en que cuesta hablar en voz alta. Entonces, también por escrito.",
                "groups": [
                    {
                        "items": [
                            [
                                "Toca",
                                "Escribir con el teclado",
                                "Desde «Escribir con el teclado», en la parte inferior del inicio, puedes separar igual por escrito, sin usar la voz.",
                                "t_keyboard"
                            ]
                        ]
                    }
                ]
            }
        ],
        "tips_note": "Estos avisos aparecen con suavidad en pantalla solo la primera vez. No pasa nada si se te escapan: esta página está aquí siempre que quieras volver.",
        "tips_closing_sub": "Si aún no has probado KUU, empieza aquí.",
        "tips_label": "Consejos de uso",
        "tips_faq_heading": "Consultas frecuentes",
        "tips_faqs": [
            [
                "No separa como yo esperaba. La precisión no acaba de convencerme.",
                [
                    "El criterio de KUU no siempre es perfecto.",
                    "Por eso puedes corregirlo después con tus manos (tocar para reescribir, mantener pulsado y arrastrar para mover, «Separar de nuevo»).",
                    "La precisión al escuchar y al separar seguirá mejorando poco a poco.",
                    "Que la uses es lo que nos anima a seguir."
                ]
            ],
            [
                "Cuando hablo mucho rato, todo acaba junto en una sola cosa.",
                [
                    "Cuando las frases se encadenan, a veces cuesta encontrar los cortes.",
                    "Al hablar, deja un pequeño respiro entre una idea y otra —por ejemplo «… y luego, (respira) … y luego»— y se separará mejor.",
                    "Lo que ya escribiste puedes editarlo desde «Separar de nuevo»: al añadir comas y puntos al texto, se separa mejor.",
                    "Si aun así queda todo junto, puedes separarlo manteniendo pulsado y arrastrando, o reescribirlo con un toque."
                ]
            ],
            [
                "Siento que me invitan a pagar demasiado pronto.",
                [
                    "Hablar, separar, repasar —el corazón de KUU es gratis para siempre.",
                    "KUU+ es un extra discreto para quien quiera quitar los anuncios o poner el bloqueo con Face ID."
                ]
            ],
            [
                "Cuesta usarlo cuando no puedo hablar en voz alta.",
                [
                    "Desde «Escribir con el teclado», en la parte inferior del inicio, puedes separar igual por escrito, sin usar la voz."
                ],
                "t_keyboard"
            ]
        ],
        "tips_support_before": "Los gestos discretos —como reescribir lo dictado o separar a tu manera— están reunidos en",
        "tips_support_after": ".",

        "html_lang": "es",
        "og_locale": "es_ES",
        "label": "Español",
        "title": "KUU — Un volcado mental tranquilo para mentes ocupadas",
        "description": "KUU es una app silenciosa para vaciar la mente. Habla lo que tienes; KUU lo separa en Ahora, Más tarde, Reposar y Soltar.",
        "hero_headline": "Habla y deja espacio en tu cabeza.",
        "hero_sub": "Desde una cabeza llena de pensamientos, solo di en voz alta lo que ahora no necesitas cargar.",
        "cta": "Descargar en el App Store",
        "scroll_cue": "Desliza",
        "why_eyebrow": "Por qué KUU",
        "why_headline": "En la cabeza se mezclan toda clase de pensamientos.",
        "why_scenario": "A mitad de una tarea, surge otra cosa. No quieres olvidarla, pero tampoco es para ahora.",
        "why_lead": "Si lo metes en una app de tareas, se vuelve un “pendiente”; si lo anotas, queda sepultado. Lo que se desordena no son las notas, sino decidir cómo tratar cada cosa.",
        "thoughts": [
            "Algo que sientes que deberías hacer",
            "Algo para pensar más tarde",
            "Una idea que aún no toma forma",
            "Una vaga inquietud que no ubicas",
            "Una preocupación que de nada sirve rumiar ahora",
        ],
        "why_note": "KUU lo recibe primero, antes de ordenar nada. Cuanto más hablas, más baja el agua en tu cabeza.",
        "steps_eyebrow": "Cómo funciona",
        "steps_headline": "Lo único que haces es hablar.",
        "steps": [
            ("Habla", "No tiene que estar ordenado. Al decirlo en voz alta, salen incluso cosas que habías olvidado, una tras otra."),
            ("Separa", "KUU lo separa con calma en Ahora, Más tarde, Reposar y Soltar."),
            ("Repasa", "Cuando todo se calma, vuelve a verlo y ordénalo. Nada se acumula sin más."),
        ],
        "app_eyebrow": "La app",
        "app_headline": "Esto es KUU.",
        "screen_alt": "Pantalla de KUU",
        "matrix_eyebrow": "La matriz KUU",
        "matrix_headline": "Un lugar para cada pensamiento.",
        "matrix_lead": "No son casillas de tareas, sino una forma de sostener lo que tienes en la cabeza.",
        "quadrants": [
            ("Ahora", "Vale un vistazo hoy para aligerar"),
            ("Más tarde", "Ahora no — en otro momento"),
            ("Reposar", "Déjalo sin decidir todavía"),
            ("Soltar", "Ya no vale la pena cargarlo"),
        ],
        "quadrants_aria": "Matriz KUU",
        "privacy_eyebrow": "Privacidad",
        "privacy_headline": "Tu voz se queda contigo.",
        "privacy_body": "Escuchar ocurre por completo en tu dispositivo: tu voz nunca se guarda ni se envía. La organización usa IA, así que solo se envía el texto, y este nunca se guarda (puedes cambiar a solo en el dispositivo). Tus notas se sincronizan solo con tu iCloud privado.",
        "closing_headline": "Tras hablar, la cabeza se siente más ligera.",
        "closing_sub": "Una app tranquila, hecha solo para eso.",
        "support_label": "Soporte",
        "privacy_label": "Privacidad",
        "lang_switcher_aria": "Idioma",
        "support_title": "Soporte — KUU",
        "support_description": "Contacto y preguntas frecuentes de KUU.",
        "support_h1": "Soporte",
        "support_intro": "Gracias por usar KUU. Para dudas o reportar un fallo, escríbenos al contacto de abajo.",
        "contact_h2": "Contacto",
        "contact_body": "Pronto estará disponible un contacto de soporte dedicado.",
        "faq_h2": "Preguntas frecuentes",
        "faqs": [
            (
                "¿Se guarda mi voz?",
                "No. KUU no envía el audio fuera del dispositivo y elimina los archivos de audio temporales una vez completada la transcripción. Solo se envía el texto a una IA externa para organizarlo, y tampoco se guarda. Lo que queda es la transcripción y la clasificación en tu dispositivo e iCloud.",
            ),
            (
                "¿Se sincroniza con iCloud?",
                "Sí. Tus notas se sincronizan con tu base de datos privada de iCloud, accesible solo para ti. No hay ningún servidor del desarrollador.",
            ),
        ],
        "back": "← Volver al inicio",
    },
    "ko": {
        "subdir": "ko",
        # Tips / usage page (ko)
        "tips_title": "사용 팁 — KUU",
        "tips_description": "KUU에서 눈에 잘 띄지 않는 조작을 모았습니다. 음성 입력 뒤의 고쳐 쓰기, 직접 나누기, 테마 사용법을 조용히 소개합니다.",
        "tips_eyebrow": "사용 팁",
        "tips_h1": "말한 뒤에도, 내 손으로.",
        "tips_lead": "KUU는 화면을 조용히 두기 위해, 많은 조작을 겉으로 드러내지 않습니다. 하지만 인식된 내용을 고치거나, 직접 나누는 일은 얼마든지 할 수 있습니다. 눈에 잘 띄지 않는 것들을, 여기에 모았습니다.",
        "tips_screens": [
            {
                "heading": "생각의 자리에서",
                "lead": "홈에서 끌어올리는, 가장 자주 쓰는 화면. 목소리로 나눈 것은 네 개의 자리에 모입니다. 눈에 잘 띄지 않는 조작도, 대부분 여기에 있습니다.",
                "groups": [
                    {
                        "subhead": "항목을 하나씩 다듬기",
                        "items": [
                            [
                                "탭",
                                "제목을 탭해서 고쳐 쓰기",
                                "항목의 글자를 그대로 탭하면, 그 자리에서 고쳐 쓸 수 있습니다. 인식이 살짝 어긋난 부분은, 여기서 다듬을 수 있습니다.",
                                "t_edit"
                            ],
                            [
                                "길게 눌러 드래그",
                                "다른 자리로 옮기기",
                                "항목을 길게 눌러 드래그하면, 지금 보기 / 나중에 생각하기 / 묵히기 / 내려놓기 사이를 자유롭게 옮길 수 있습니다.",
                                "t_move"
                            ],
                            [
                                "드래그",
                                "테마로 옮기기",
                                "같은 드래그로 위쪽 테마 칩에도 넣을 수 있습니다. 테마에 들어간 항목은, ‘미분류’로 옮기면 빠집니다.",
                                "t_theme_drag"
                            ],
                            [
                                "탭",
                                "○을 탭해서 내려놓기",
                                "항목 맨 앞의 작은 ○을 탭하면, 그 자리에서 살며시 ‘내려놓기’로. 바로 되돌릴 수도 있습니다.",
                                "t_release"
                            ],
                            [
                                "탭",
                                "‘＋’로 직접 입력 더하기",
                                "각 블록 오른쪽 아래의 옅은 ‘＋’에서, 그 자리에 항목을 글자로 적어 넣을 수 있습니다.",
                                "t_add"
                            ]
                        ]
                    },
                    {
                        "subhead": "테마로 묶기",
                        "items": [
                            [
                                "길게 누르기",
                                "테마를 길게 눌러 메뉴 열기",
                                "위쪽 테마 칩을 길게 누르면, 항상 표시(고정) / 이름과 색 편집 / 내려놓기가 나옵니다. 테마 설정은, 여기가 입구입니다.",
                                "t_theme_press"
                            ],
                            [
                                "탭",
                                "이름·색·순서 바꾸기",
                                "테마 편집 화면에서는, 이름을 탭해서 고쳐 쓰고, 색 동그라미에서 옅은 색을 고르고, 왼쪽 손잡이로 순서를 바꿀 수 있습니다.",
                                "t_theme_edit"
                            ]
                        ]
                    }
                ]
            },
            {
                "heading": "막 나눈 직후 화면에서",
                "lead": "말하고 나눈, 바로 뒤. KUU가 나눈 방식이 마음에 들지 않으면, 여기서 다듬은 뒤 남길 수 있습니다.",
                "groups": [
                    {
                        "items": [
                            [
                                "탭",
                                "필요 없는 건 탭해서 빼기",
                                "와닿지 않는 항목은 탭하면 옅어지며 빠집니다. 다시 한번 탭하면 되돌아옵니다.",
                                "t_remove"
                            ],
                            [
                                "드래그",
                                "드래그해서 분류 바꾸기",
                                "항목을 다른 블록으로 드래그하면, 그 자리에서 분류를 바꿀 수 있습니다.",
                                "t_reclassify"
                            ],
                            [
                                "버튼",
                                "‘다시 나누기’로 전체 고치기",
                                "잘못 들은 부분이 있으면 ‘다시 나누기’에서, 인식된 텍스트 전체를 고쳐 다시 나눌 수 있습니다.",
                                "t_resort"
                            ]
                        ]
                    }
                ]
            },
            {
                "heading": "홈에서",
                "lead": "목소리를 내기 어려운 날도 있어요. 그럴 땐, 글자로도.",
                "groups": [
                    {
                        "items": [
                            [
                                "탭",
                                "키보드로 쓰기",
                                "홈 아래쪽 ‘키보드로 쓰기’에서, 목소리 없이 글자로도 똑같이 나눌 수 있습니다.",
                                "t_keyboard"
                            ]
                        ]
                    }
                ]
            }
        ],
        "tips_note": "이 안내들은, 처음 한 번만 화면에 살며시 나타납니다. 놓쳐도 괜찮아요. 이 페이지는, 언제든 다시 볼 수 있습니다.",
        "tips_closing_sub": "아직 KUU를 써 보지 않았다면, 여기서.",
        "tips_label": "사용 팁",
        "tips_faq_heading": "자주 받는 문의",
        "tips_faqs": [
            [
                "생각한 대로 나눠 주지 않아요. 정확도가 아쉬워요.",
                [
                    "KUU의 판단이, 늘 완벽하지는 않습니다.",
                    "그래서 나중에 직접 고칠 수 있도록 해 두었습니다(탭해서 고쳐 쓰기 / 길게 눌러 드래그해서 옮기기 / ‘다시 나누기’).",
                    "인식과 분류의 정확도는, 앞으로도 조금씩 나아지게 하겠습니다.",
                    "당신이 써 주시는 것이, 그 힘이 됩니다."
                ]
            ],
            [
                "길게 말하면, 전부 하나로 묶여 버려요.",
                [
                    "말이 이어지면, 나눌 지점을 찾기 어려울 때가 있습니다.",
                    "말할 때 ‘~하고, (한 호흡) ~하고’처럼 잠깐 사이를 두면, 더 잘 나뉩니다.",
                    "이미 입력한 것은, ‘다시 나누기’에서 문장에 쉼표(,)나 마침표(.)를 넣으면, 더 잘 나뉩니다.",
                    "그래도 하나로 묶일 때는, 길게 눌러 드래그해서 나누거나, 탭해서 고쳐 쓸 수 있습니다."
                ]
            ],
            [
                "너무 빨리 결제로 이끄는 것 같아요.",
                [
                    "말하기, 나누기, 돌아보기. KUU의 중심은 언제나 무료로 쓸 수 있습니다.",
                    "KUU+는, 광고를 끄고 싶거나 Face ID 잠금을 걸고 싶은 분을 위한, 조용한 추가 기능입니다."
                ]
            ],
            [
                "소리를 낼 수 없는 상황에서는 쓰기 불편해요.",
                [
                    "홈 아래쪽 ‘키보드로 쓰기’에서, 목소리 없이 글자로도 똑같이 나눌 수 있습니다."
                ],
                "t_keyboard"
            ]
        ],
        "tips_support_before": "음성 입력 뒤의 고쳐 쓰기나, 직접 나누기 등, 눈에 잘 띄지 않는 조작은",
        "tips_support_after": "에 모아 두었습니다.",

        "html_lang": "ko",
        "og_locale": "ko_KR",
        "label": "한국어",
        "title": "KUU — 바쁜 머리를 조용히 비우는 브레인덤프",
        "description": "KUU는 조용한 음성 브레인덤프 앱입니다. 마음에 있는 것을 말하세요. KUU가 지금 보기, 나중에 생각하기, 묵히기, 내려놓기로 나눠줍니다.",
        "hero_headline": "말하고, 머릿속에 여백을.",
        "hero_sub": "생각으로 가득 찬 머리에서, 지금 가지고 있지 않아도 될 것을 소리 내어 말하기만 하면 됩니다.",
        "cta": "App Store에서 받기",
        "scroll_cue": "아래로",
        "why_eyebrow": "왜 KUU인가",
        "why_headline": "머릿속에는 온갖 생각이 뒤섞여 있습니다.",
        "why_scenario": "작업 중에 문득 다른 게 떠오릅니다. 잊고 싶진 않은데, 지금 마주할 것도 아닙니다.",
        "why_lead": "할 일 앱에 넣으면 ‘해야 할 일’이 되고, 메모에 적으면 묻혀 버립니다. 어질러지는 건 메모가 아니라, ‘어떻게 다룰지’의 판단 쪽입니다.",
        "thoughts": [
            "해야 할 것 같은 일",
            "나중에 생각하고 싶은 것",
            "아직 형태가 잡히지 않은 아이디어",
            "왠지 마음에 걸리는 위화감",
            "지금 걱정해 봐야 소용없는 일",
        ],
        "why_note": "KUU는 정리하기 전에, 먼저 받아 둡니다. 말할수록, 머릿속 수위가 내려갑니다.",
        "steps_eyebrow": "사용법",
        "steps_headline": "할 일은, 말하는 것뿐.",
        "steps": [
            ("말하기", "정리되어 있지 않아도 괜찮아요. 소리 내어 말하면, 잊고 있던 것까지 줄줄이 떠올라요."),
            ("나누기", "KUU가 지금 보기, 나중에 생각하기, 묵히기, 내려놓기로 조용히 나눕니다."),
            ("돌아보기", "마음이 가라앉으면 다시 보고 정리해요. 쌓아두기만 하지 않아요."),
        ],
        "app_eyebrow": "앱",
        "app_headline": "이것이 KUU.",
        "screen_alt": "KUU 화면",
        "matrix_eyebrow": "KUU 매트릭스",
        "matrix_headline": "생각의, 자리.",
        "matrix_lead": "할 일 분류가 아니라, 머릿속에 있는 것을 다루는 방식으로 나눕니다.",
        "quadrants": [
            ("지금 보기", "지금 잠깐 보면 가벼워질 것"),
            ("나중에 생각하기", "지금 말고, 다른 타이밍에"),
            ("묵히기", "아직 결론 내지 않고 두기"),
            ("내려놓기", "더는 안고 있지 않아도 될 것"),
        ],
        "quadrants_aria": "KUU 매트릭스",
        "privacy_eyebrow": "개인정보",
        "privacy_headline": "당신의 목소리는, 밖으로 나가지 않습니다.",
        "privacy_body": "듣기는 모두 기기 안에서만 이루어지며, 음성 자체는 남기거나 보내지 않습니다. 정리에는 AI를 사용하므로 텍스트만 보내며, 그것도 남지 않습니다(기기 내 전용으로 바꿀 수도 있습니다). 말한 것은 당신의 iCloud(프라이빗)에만 동기화됩니다.",
        "closing_headline": "말하고 나면, 머리가 조금 가볍습니다.",
        "closing_sub": "오직 그것을 위한, 조용한 앱입니다.",
        "support_label": "지원",
        "privacy_label": "개인정보처리방침",
        "lang_switcher_aria": "언어",
        "support_title": "지원 — KUU",
        "support_description": "KUU 문의 및 자주 묻는 질문.",
        "support_h1": "지원",
        "support_intro": "KUU를 이용해 주셔서 감사합니다. 문의나 문제 신고는 아래로 연락 주세요.",
        "contact_h2": "문의",
        "contact_body": "곧 전용 지원 창구를 안내드립니다.",
        "faq_h2": "자주 묻는 질문",
        "faqs": [
            (
                "음성이 저장되나요?",
                "아닙니다. KUU는 음성을 기기 밖으로 보내지 않으며, 인식이 완료되면 임시 음성 파일을 즉시 삭제합니다. 정리를 위해 외부 AI로 보내는 것은 텍스트뿐이며, 그것도 저장되지 않습니다. 남는 것은 기기와 iCloud에 있는 텍스트와 분류 결과뿐입니다.",
            ),
            (
                "iCloud 동기화는 되나요?",
                "네. 노트는 사용자 본인만 접근할 수 있는 iCloud Private DB에 동기화됩니다. 개발자가 운영하는 서버는 없습니다.",
            ),
        ],
        "back": "← 처음으로",
    },
    "zh-Hans": {
        "subdir": "zh-Hans",
        # Tips / usage page (zh-Hans)
        "tips_title": "使用技巧 — KUU",
        "tips_description": "汇总 KUU 中不易察觉的操作。语音输入之后的修改、自己动手的分类、主题的用法，静静地一一介绍。",
        "tips_eyebrow": "使用技巧",
        "tips_h1": "说出来之后，也能自己动手。",
        "tips_lead": "KUU 为了让画面保持安静，没有把大多数操作摆在明面上。不过，修改听写、亲手分类，都做得到。这些不易察觉的，我们汇总在这里。",
        "tips_screens": [
            {
                "heading": "在念头的去处",
                "lead": "从主页向上拉出的、最常用的画面。用声音分好的念头，会汇集到四个去处。不易察觉的操作，也大多在这里。",
                "groups": [
                    {
                        "subhead": "逐一整理每个念头",
                        "items": [
                            [
                                "轻点",
                                "轻点标题即可改写",
                                "直接轻点念头的文字，就能当场改写。听写的细小偏差，都可以在这里修整。",
                                "t_edit"
                            ],
                            [
                                "长按 → 拖动",
                                "移到别的去处",
                                "长按念头并拖动，就能在现在看／之后想／搁置／放下之间自由挪动。",
                                "t_move"
                            ],
                            [
                                "拖动",
                                "移到主题",
                                "用同样的拖动，也能移到上方的主题标签。移进那个主题就归入其中；把它落到“未分类”，就会移出。",
                                "t_theme_drag"
                            ],
                            [
                                "轻点",
                                "轻点○来放下",
                                "轻点念头开头的小○，就能当场轻轻地把它放下。也可以马上撤销。",
                                "t_release"
                            ],
                            [
                                "轻点",
                                "用“＋”手动补记",
                                "从每个区块右下角淡淡的“＋”，就能在那个位置用文字补记一条念头。",
                                "t_add"
                            ]
                        ]
                    },
                    {
                        "subhead": "用主题归拢",
                        "items": [
                            [
                                "长按",
                                "长按主题打开菜单",
                                "长按上方的主题标签，会出现始终显示（固定）／编辑名称或颜色／放下。主题的设置，入口就在这里。",
                                "t_theme_press"
                            ],
                            [
                                "轻点",
                                "更改名称、颜色和排序",
                                "在主题的编辑界面，轻点名称即可改写，从色点里挑选淡色，用左侧的手柄调整排序。",
                                "t_theme_edit"
                            ]
                        ]
                    }
                ]
            },
            {
                "heading": "在刚分好的画面",
                "lead": "说完、分好，紧接着的那一刻。若 KUU 分得不合心意，可以在这里整理好，再留下来。",
                "groups": [
                    {
                        "items": [
                            [
                                "轻点",
                                "不需要的，轻点移除",
                                "没什么感觉的念头，轻点一下就会变淡、移出。再轻点一次便能恢复。",
                                "t_remove"
                            ],
                            [
                                "拖动",
                                "拖动改变分类",
                                "把念头拖到别的区块，就能当场改变分类。",
                                "t_reclassify"
                            ],
                            [
                                "按钮",
                                "用“重新分类”修正全文",
                                "若有听错，可以从“重新分类”把整段文字都改好，再分一次。",
                                "t_resort"
                            ]
                        ]
                    }
                ]
            },
            {
                "heading": "在主页",
                "lead": "也有不方便出声的日子。那样的时候，用文字也可以。",
                "groups": [
                    {
                        "items": [
                            [
                                "轻点",
                                "用键盘写",
                                "从主页下方的“用键盘写”，不出声、用文字，也能一样地分好。",
                                "t_keyboard"
                            ]
                        ]
                    }
                ]
            }
        ],
        "tips_note": "这些提示，只在最初的那一次静静出现在画面上。错过也没关系。这个页面，随时都能回看。",
        "tips_closing_sub": "如果还没试过 KUU，可以从这里开始。",
        "tips_label": "使用技巧",
        "tips_faq_heading": "常见咨询",
        "tips_faqs": [
            [
                "分得不像我想的那样。准确度还差一点。",
                [
                    "KUU 的判断，并非总是完美。",
                    "所以，我们让它之后可以亲手修改（轻点改写／长按拖动移动／“重新分类”）。",
                    "听写与分类的准确度，今后也会一点点变好。",
                    "有你在用，就是我们前进的动力。"
                ]
            ],
            [
                "说得一长，就全被并到一起了。",
                [
                    "句子一连下去，有时就不容易找到断点。",
                    "说的时候，像“说完一句，（喘口气）再说一句”这样，稍微留些停顿，就更容易分开。",
                    "已经输入的内容，可以用“重新分类”给句子加上逗号和句号，就更容易断开。",
                    "如果还是被并在一起，可以长按拖动来分开，或轻点改写。"
                ]
            ],
            [
                "总感觉很快就被引去付费。",
                [
                    "说出来、分好、回看——KUU 的核心，一直都能免费使用。",
                    "KUU+ 是给想关掉广告、想加上 Face ID 锁的人，悄悄准备的一点补充。"
                ]
            ],
            [
                "在不方便出声的场合，不太好用。",
                [
                    "从主页下方的“用键盘写”，不出声、用文字，也能一样地分好。"
                ],
                "t_keyboard"
            ]
        ],
        "tips_support_before": "语音输入之后的修改、自己动手的分类等不易察觉的操作，都汇总在",
        "tips_support_after": "里。",

        "html_lang": "zh-Hans",
        "og_locale": "zh_CN",
        "label": "简体中文",
        "title": "KUU — 让忙碌的脑袋安静下来的脑内倾倒",
        "description": "KUU 是一款安静的语音脑内倾倒应用。说出心中所想，KUU 会分到现在看、之后想、搁置、放下。",
        "hero_headline": "说出来，给脑子留点空。",
        "hero_sub": "从塞满念头的脑袋里，把此刻不必扛着的事，说出来就好。",
        "cta": "在 App Store 下载",
        "scroll_cue": "向下",
        "why_eyebrow": "为什么是 KUU",
        "why_headline": "脑袋里，混着各种各样的念头。",
        "why_scenario": "做事做到一半，别的念头忽然冒出来。不想忘掉，可现在也不是面对它的时候。",
        "why_lead": "放进待办应用就成了“要做的事”，写进笔记又被埋没。乱的不是笔记，而是“怎么处置”的判断。",
        "thoughts": [
            "总觉得该做的事",
            "想之后再想的事",
            "还没成形的灵感",
            "莫名在意的违和感",
            "此刻想也无益的担忧",
        ],
        "why_note": "KUU 先接住，再谈整理。说得越多，脑子里的水位就越低。",
        "steps_eyebrow": "怎么用",
        "steps_headline": "要做的，只有说。",
        "steps": [
            ("说", "不必整理。一说出口，连忘掉的事也会一件接一件冒出来。"),
            ("分", "KUU 会安静地分到现在看、之后想、搁置、放下。"),
            ("回看", "等心定下来，再回看、整理。不会只是一味堆着。"),
        ],
        "app_eyebrow": "应用",
        "app_headline": "这就是 KUU。",
        "screen_alt": "KUU 界面",
        "matrix_eyebrow": "KUU 矩阵",
        "matrix_headline": "念头的，去处。",
        "matrix_lead": "不是待办分类，而是看待脑中之物的方式。",
        "quadrants": [
            ("现在看", "今天看一眼就会轻一些"),
            ("之后想", "不是现在，换个时间"),
            ("搁置", "先不下结论，放着"),
            ("放下", "已经不必再扛着"),
        ],
        "quadrants_aria": "KUU 矩阵",
        "privacy_eyebrow": "隐私",
        "privacy_headline": "你的声音，不会出去。",
        "privacy_body": "聆听全都只在你的设备里完成——语音本身从不保留或发送。整理会使用 AI，因此只发送文字内容，而且不会保留（也可切换为仅在设备端）。记录只同步到你私人的 iCloud。",
        "closing_headline": "说完之后，脑袋轻一点。",
        "closing_sub": "一款只为此而生的、安静的应用。",
        "support_label": "支持",
        "privacy_label": "隐私",
        "lang_switcher_aria": "语言",
        "support_title": "支持 — KUU",
        "support_description": "KUU 的联系方式和常见问题。",
        "support_h1": "支持",
        "support_intro": "感谢使用 KUU。如有疑问或需要反馈问题,请通过下面的方式联系。",
        "contact_h2": "联系",
        "contact_body": "我们将很快开放支持渠道。",
        "faq_h2": "常见问题",
        "faqs": [
            (
                "我的语音会被保存吗?",
                "不会。KUU 不会将音频传输到设备外,识别完成后会立即删除临时音频文件。为整理而发送给外部 AI 的只有文字内容,且不会保留。留下的只有你设备和 iCloud 中的转录结果和分类结果。",
            ),
            (
                "是否通过 iCloud 同步?",
                "是的。笔记会同步到只有您本人可访问的 iCloud 私有数据库。我们没有任何开发者服务器。",
            ),
        ],
        "back": "← 返回顶部",
    },
    "de": {
        "subdir": "de",
        "html_lang": "de",
        "og_locale": "de_DE",
        "label": "Deutsch",
        "title": "KUU — der stille Brain-Dump, der den Kopf ordnet",
        "description": "KUU ist eine stille Brain-Dump-App: Sprich einfach aus, was dir im Kopf ist, und KUU ordnet es in „Jetzt ansehen / Später darüber nachdenken / Ruhen lassen / Loslassen“.",
        "hero_headline": "Sprich, und schaff Raum im Kopf.",
        "hero_sub": "Aus einem Kopf voller Gedanken sprichst du einfach aus, was du gerade nicht tragen musst.",
        "cta": "Laden im App Store",
        "scroll_cue": "Nach unten",
        "why_eyebrow": "Warum KUU",
        "why_headline": "Im Kopf vermischen sich die unterschiedlichsten Gedanken.",
        "why_scenario": "Mitten in der Arbeit taucht plötzlich etwas anderes auf. Du willst es nicht vergessen – doch jetzt ist nicht der Moment dafür.",
        "why_lead": "Trägst du es in eine To-do-App ein, wird eine „Aufgabe“ daraus; schreibst du es in Notizen, geht es unter. Was sich anhäuft, sind nicht die Gedanken selbst, sondern die Entscheidung, wie du mit ihnen umgehst.",
        "thoughts": [
            "Etwas, das du glaubst tun zu müssen",
            "Etwas, worüber du später nachdenken willst",
            "Eine Idee, die noch keine Form hat",
            "Ein vages Unbehagen, das du nicht einordnen kannst",
            "Eine Sorge, über die jetzt nachzudenken nichts bringt"
        ],
        "why_note": "KUU nimmt es erst einmal an, bevor du etwas aufräumst. Je mehr du aussprichst, desto weiter sinkt der Wasserstand im Kopf.",
        "steps_eyebrow": "So funktioniert es",
        "steps_headline": "Alles, was du tust, ist sprechen.",
        "steps": [
            [
                "Sprechen",
                "Es muss nicht geordnet sein. Sprichst du es aus, kommt eins nach dem anderen hervor – bis hin zu Dingen, die du vergessen hattest."
            ],
            [
                "Sortieren",
                "KUU sortiert es still in „Jetzt ansehen / Später darüber nachdenken / Ruhen lassen / Loslassen“."
            ],
            [
                "Sichten",
                "Wenn Ruhe eingekehrt ist, siehst du es durch und ordnest den Umgang damit. Nichts bleibt einfach liegen."
            ]
        ],
        "app_eyebrow": "Die App",
        "app_headline": "Das ist KUU.",
        "screen_alt": "Bildschirm der KUU-App",
        "matrix_eyebrow": "Die KUU-Matrix",
        "matrix_headline": "Ein Ort für jeden Gedanken.",
        "matrix_lead": "Keine Aufgaben-Einteilung, sondern eine Art, mit dem umzugehen, was im Kopf ist.",
        "quadrants": [
            [
                "Jetzt ansehen",
                "Wofür sich jetzt ein kurzer Blick lohnt, damit es leichter wird"
            ],
            [
                "Später darüber nachdenken",
                "Nicht jetzt – zu einem anderen Zeitpunkt"
            ],
            [
                "Ruhen lassen",
                "Noch keine Entscheidung treffen, einfach liegen lassen"
            ],
            [
                "Loslassen",
                "Was du wohl nicht länger mit dir tragen musst"
            ]
        ],
        "quadrants_aria": "KUU-Matrix",
        "privacy_eyebrow": "Datenschutz",
        "privacy_headline": "Deine Stimme bleibt bei dir.",
        "privacy_body": "Das Zuhören geschieht vollständig auf deinem Gerät. Deine Stimme selbst wird nicht gespeichert und nicht gesendet. Zum Sortieren kommt KI zum Einsatz, gesendet wird nur der verschriftlichte Inhalt – und auch der wird nicht gespeichert (in den Einstellungen lässt sich das auf „nur auf dem Gerät“ umstellen). Was du gesprochen hast, wird ausschließlich mit deiner privaten iCloud synchronisiert.",
        "closing_headline": "Nach dem Sprechen fühlt sich der Kopf leichter an.",
        "closing_sub": "Eine stille App, allein dafür gemacht.",
        "support_label": "Support",
        "privacy_label": "Datenschutz",
        "lang_switcher_aria": "Sprache",
        "support_title": "Support — KUU",
        "support_description": "Kontakt und FAQ zu KUU.",
        "support_h1": "Support",
        "support_intro": "Danke, dass du KUU nutzt. Bei Fragen oder um einen Fehler zu melden, wende dich bitte an den untenstehenden Kontakt.",
        "contact_h2": "Kontakt",
        "contact_body": "Eine eigene Anlaufstelle für den Support steht in Kürze bereit.",
        "faq_h2": "Häufig gestellte Fragen",
        "faqs": [
            [
                "Wird meine Stimme gespeichert?",
                "Nein. KUU gibt keine Audiodaten aus dem Gerät heraus und löscht die temporäre Audiodatei, sobald die Erkennung abgeschlossen ist. Zum Sortieren wird nur der verschriftlichte Inhalt an eine externe KI gesendet, und auch der wird nicht gespeichert. Es bleiben nur die Abschrift und das Sortierergebnis auf deinem Gerät und in deiner iCloud."
            ],
            [
                "Wie ist das mit der iCloud-Synchronisierung?",
                "Die Daten werden mit deiner privaten iCloud-Datenbank synchronisiert (Zugriff nur für den Inhaber der Apple-ID). Es gibt keinen Entwickler-Server."
            ]
        ],
        "tips_title": "Tipps — KUU",
        "tips_description": "Eine Übersicht der leicht zu übersehenden Bedienschritte in KUU – ein stiller Blick auf das Überarbeiten nach dem Sprechen, das Sortieren von Hand und den Umgang mit Themen.",
        "tips_eyebrow": "Tipps",
        "tips_h1": "Auch nach dem Sprechen – in deiner Hand.",
        "tips_lead": "Um den Bildschirm still zu halten, zeigt KUU die meisten Bedienelemente nicht offen an. Doch das Erkannte korrigieren oder von Hand sortieren – das geht jederzeit. Die leicht zu übersehenden Schritte haben wir hier zusammengestellt.",
        "tips_screens": [
            {
                "heading": "Am Ort für deine Gedanken",
                "lead": "Der Bildschirm, den du am häufigsten nutzt – vom Home-Screen heraufgezogen. Was per Stimme sortiert wurde, sammelt sich an vier Orten. Auch die meisten leicht zu übersehenden Schritte sind hier.",
                "groups": [
                    {
                        "subhead": "Einträge einzeln ordnen",
                        "items": [
                            [
                                "Tippen",
                                "Auf den Titel tippen, um ihn zu überarbeiten",
                                "Tippe direkt auf den Text eines Eintrags, um ihn an Ort und Stelle zu überarbeiten. Kleine Hörfehler lassen sich genau hier glätten.",
                                "t_edit"
                            ],
                            [
                                "Lange drücken → ziehen",
                                "An einen anderen Ort verschieben",
                                "Drücke lange auf einen Eintrag und ziehe ihn, um ihn frei zwischen „Jetzt ansehen / Später darüber nachdenken / Ruhen lassen / Loslassen“ zu verschieben.",
                                "t_move"
                            ],
                            [
                                "Ziehen",
                                "Zu einem Thema verschieben",
                                "Mit derselben Ziehbewegung lässt er sich auch auf einen Thema-Chip oben verschieben. Er wird Teil dieses Themas; ziehst du ihn auf „Nicht zugeordnet“, wird er wieder herausgenommen.",
                                "t_theme_drag"
                            ],
                            [
                                "Tippen",
                                "Auf das ○ tippen, um loszulassen",
                                "Tippe auf das kleine ○ am Anfang eines Eintrags, um ihn sanft ins „Loslassen“ zu geben. Du kannst es sofort wieder rückgängig machen.",
                                "t_release"
                            ],
                            [
                                "Tippen",
                                "Mit „＋“ von Hand hinzufügen",
                                "Über das blasse „＋“ unten rechts an jedem Block kannst du dort einen Eintrag als Text ergänzen.",
                                "t_add"
                            ]
                        ]
                    },
                    {
                        "subhead": "Mit Themen bündeln",
                        "items": [
                            [
                                "Lange drücken",
                                "Für das Menü lange auf ein Thema drücken",
                                "Drücke lange auf einen Thema-Chip oben, und es erscheinen „Immer anzeigen (anheften)“, „Name oder Farbe bearbeiten“ und „Loslassen“. Hier geht es zu den Einstellungen eines Themas.",
                                "t_theme_press"
                            ],
                            [
                                "Tippen",
                                "Name, Farbe und Reihenfolge ändern",
                                "Im Bearbeitungsbildschirm eines Themas tippst du auf den Namen, um ihn zu überarbeiten, wählst über die Farbpunkte eine zarte Farbe und ordnest die Reihenfolge mit dem Griff links neu.",
                                "t_theme_edit"
                            ]
                        ]
                    }
                ]
            },
            {
                "heading": "Direkt nach dem Sortieren",
                "lead": "Der Moment gleich nach dem Sprechen und Sortieren. Wenn KUUs Aufteilung nicht recht passt, kannst du sie hier ordnen, bevor du sie behältst.",
                "groups": [
                    {
                        "items": [
                            [
                                "Tippen",
                                "Nicht Benötigtes durch Tippen entfernen",
                                "Tippe auf einen Eintrag, der nicht passt, und er wird blasser und fällt heraus. Ein erneutes Tippen holt ihn zurück.",
                                "t_remove"
                            ],
                            [
                                "Ziehen",
                                "Durch Ziehen die Einordnung ändern",
                                "Ziehe einen Eintrag in einen anderen Block, um seine Einordnung gleich an Ort und Stelle zu ändern.",
                                "t_reclassify"
                            ],
                            [
                                "Schaltfläche",
                                "Mit „Neu sortieren“ den ganzen Text korrigieren",
                                "Wurde etwas falsch verstanden, kannst du über „Neu sortieren“ die gesamte Abschrift korrigieren und noch einmal sortieren.",
                                "t_resort"
                            ]
                        ]
                    }
                ]
            },
            {
                "heading": "Auf dem Home-Screen",
                "lead": "An manchen Tagen fällt das laute Sprechen schwer. Dann geht es auch mit Text.",
                "groups": [
                    {
                        "items": [
                            [
                                "Tippen",
                                "Mit Tastatur schreiben",
                                "Über „Mit Tastatur schreiben“ unten auf dem Home-Screen kannst du auch ohne Stimme als Text genauso sortieren.",
                                "t_keyboard"
                            ]
                        ]
                    }
                ]
            }
        ],
        "tips_note": "Diese Hinweise erscheinen nur beim ersten Mal ganz sanft auf dem Bildschirm. Wenn du sie übersiehst, ist das kein Problem – diese Seite kannst du jederzeit wieder aufrufen.",
        "tips_closing_sub": "Wenn du KUU noch nicht ausprobiert hast, geht es hier los.",
        "tips_label": "Tipps",
        "tips_faq_heading": "Häufige Fragen",
        "tips_faqs": [
            [
                "Es sortiert nicht so, wie ich es erwartet habe. Die Genauigkeit ist noch nicht ganz da.",
                [
                    "KUUs Einschätzung ist nicht immer perfekt.",
                    "Deshalb kannst du es hinterher jederzeit von Hand korrigieren (zum Überarbeiten tippen, zum Verschieben lange drücken und ziehen oder „Neu sortieren“).",
                    "Wie es hört und sortiert, verbessern wir weiterhin Schritt für Schritt.",
                    "Dass du es nutzt, ist uns dabei Ansporn."
                ]
            ],
            [
                "Wenn ich länger spreche, wird alles zu einem Einzigen zusammengefasst.",
                [
                    "Wenn Sätze ineinander übergehen, sind die Grenzen manchmal schwer zu finden.",
                    "Wenn du beim Sprechen eine kleine Pause lässt – „dies, (ein Atemzug) dann das“ –, lässt es sich leichter aufteilen.",
                    "Bei bereits Eingegebenem hilft es, im „Neu sortieren“ Kommas und Punkte in den Text einzufügen, damit er sich besser aufteilt.",
                    "Bleibt es trotzdem zusammen, kannst du es per langem Drücken und Ziehen aufteilen oder mit einem Tippen überarbeiten."
                ]
            ],
            [
                "Ich habe das Gefühl, gleich zum Bezahlen gedrängt zu werden.",
                [
                    "Sprechen, sortieren, durchsehen – der Kern von KUU bleibt für immer kostenlos.",
                    "KUU+ ist eine leise Ergänzung für alle, die Werbung ausschalten oder eine Face-ID-Sperre hinzufügen möchten."
                ]
            ],
            [
                "In Situationen, in denen ich nicht laut sprechen kann, ist es schwer zu nutzen.",
                [
                    "Über „Mit Tastatur schreiben“ unten auf dem Home-Screen kannst du auch ohne Stimme als Text genauso sortieren."
                ],
                "t_keyboard"
            ]
        ],
        "tips_support_before": "Das Überarbeiten nach der Spracheingabe, das Sortieren von Hand und andere leicht zu übersehende Schritte sind gesammelt in",
        "tips_support_after": ".",
        "back": "← Zurück nach oben",
    },
    "it": {
        "subdir": "it",
        "html_lang": "it",
        "og_locale": "it_IT",
        "label": "Italiano",
        "title": "KUU — il brain-dump silenzioso per riordinare la mente",
        "description": "KUU è un'app di brain-dump silenziosa: basta dire ad alta voce ciò che hai in mente e KUU lo ordina in «Vedere ora / Pensarci dopo / Lasciare riposare / Lasciare andare».",
        "hero_headline": "Parla, e fai spazio nella mente.",
        "hero_sub": "Da una mente piena di pensieri, di' ad alta voce ciò che non devi portare con te adesso.",
        "cta": "Scarica su App Store",
        "scroll_cue": "Scorri",
        "why_eyebrow": "Perché KUU",
        "why_headline": "Nella mente si mescolano pensieri di ogni tipo.",
        "why_scenario": "Mentre lavori, ti viene in mente qualcos'altro. Non vuoi dimenticarlo, ma non è nemmeno il momento di affrontarlo.",
        "why_lead": "Se lo metti in un gestore di attività diventa una «cosa da fare»; se lo annoti tra le note, finisce sepolto. A ingombrare non sono i pensieri in sé, ma il decidere «come trattarli».",
        "thoughts": [
            "Qualcosa che senti di dover fare",
            "Qualcosa a cui pensare più tardi",
            "Un'idea che non ha ancora preso forma",
            "Un disagio vago che non sai spiegare",
            "Una preoccupazione su cui adesso è inutile soffermarsi"
        ],
        "why_note": "Prima di mettere in ordine, KUU accoglie. Più parli, più il livello dell'acqua nella mente si abbassa.",
        "steps_eyebrow": "Come funziona",
        "steps_headline": "Devi solo parlare.",
        "steps": [
            [
                "Parla",
                "Non serve che sia ordinato. Dirlo ad alta voce fa emergere, una dopo l'altra, anche le cose che avevi dimenticato."
            ],
            [
                "Dividi",
                "KUU lo divide con calma in Vedere ora / Pensarci dopo / Lasciare riposare / Lasciare andare."
            ],
            [
                "Rivedi",
                "Quando le cose si calmano, torna a guardarle e sistema come trattarle. Niente resta lì ad accumularsi."
            ]
        ],
        "app_eyebrow": "L'app",
        "app_headline": "Questo è KUU.",
        "screen_alt": "La schermata di KUU",
        "matrix_eyebrow": "La matrice KUU",
        "matrix_headline": "Un posto per ogni pensiero.",
        "matrix_lead": "Non categorie di attività, ma un modo di trattare ciò che hai in mente.",
        "quadrants": [
            [
                "Vedere ora",
                "Ciò che, guardandolo un attimo adesso, ti alleggerisce"
            ],
            [
                "Pensarci dopo",
                "Non adesso, in un altro momento"
            ],
            [
                "Lasciare riposare",
                "Metterlo da parte senza decidere ancora"
            ],
            [
                "Lasciare andare",
                "Ciò che forse non serve più portare con sé"
            ]
        ],
        "quadrants_aria": "Matrice KUU",
        "privacy_eyebrow": "Privacy",
        "privacy_headline": "La tua voce non esce da qui.",
        "privacy_body": "Il riconoscimento vocale avviene interamente sul dispositivo: la voce non viene conservata né inviata. Per l'ordinamento usiamo l'AI, quindi inviamo solo il testo trascritto, e nemmeno quello viene conservato (dalle impostazioni puoi limitare tutto al dispositivo). Ciò che dici si sincronizza solo con il tuo iCloud privato.",
        "closing_headline": "Dopo aver parlato, la mente è un po' più leggera.",
        "closing_sub": "Un'app silenziosa, fatta solo per questo.",
        "support_label": "Assistenza",
        "privacy_label": "Privacy",
        "lang_switcher_aria": "Lingua",
        "support_title": "Assistenza — KUU",
        "support_description": "Contatti e domande frequenti per KUU.",
        "support_h1": "Assistenza",
        "support_intro": "Grazie per usare KUU. Per domande o per segnalare un problema, scrivici ai contatti qui sotto.",
        "contact_h2": "Contatti",
        "contact_body": "Un canale di assistenza dedicato sarà disponibile a breve.",
        "faq_h2": "Domande frequenti",
        "faqs": [
            [
                "La mia voce viene salvata?",
                "No. KUU non invia l'audio fuori dal dispositivo e, una volta completato il riconoscimento, elimina i file audio temporanei. Per l'ordinamento inviamo a un'AI esterna solo il testo trascritto, e nemmeno quello viene conservato. Restano soltanto la trascrizione e il risultato dell'ordinamento, sul tuo dispositivo e su iCloud."
            ],
            [
                "E la sincronizzazione iCloud?",
                "I dati si sincronizzano con il database privato di iCloud (accessibile solo al titolare dell'Apple ID). Non esiste alcun server dello sviluppatore."
            ]
        ],
        "tips_title": "Consigli d'uso — KUU",
        "tips_description": "Una raccolta dei gesti di KUU più facili da non notare: come riscrivere dopo aver parlato, ordinare a mano e usare i temi, raccontati con calma.",
        "tips_eyebrow": "Consigli d'uso",
        "tips_h1": "Anche dopo aver parlato, con le tue mani.",
        "tips_lead": "Per mantenere lo schermo silenzioso, KUU tiene molti comandi fuori dalla vista. Ma correggere ciò che è stato riconosciuto, o ordinare a mano, si può sempre fare. Qui abbiamo raccolto i gesti più facili da non notare.",
        "tips_screens": [
            {
                "heading": "Nel posto dei tuoi pensieri",
                "lead": "La schermata che userai di più, che si tira su dalla Home. Ciò che hai diviso con la voce si raccoglie in quattro posti. Anche la maggior parte dei gesti nascosti è qui.",
                "groups": [
                    {
                        "subhead": "Sistemare le voci una a una",
                        "items": [
                            [
                                "Tocca",
                                "Tocca un titolo per riscriverlo",
                                "Tocca il testo di una voce per riscriverlo lì per lì. Le piccole imprecisioni del riconoscimento si sistemano proprio qui.",
                                "t_edit"
                            ],
                            [
                                "Tieni premuto → trascina",
                                "Spostala altrove",
                                "Tieni premuta una voce e trascinala per spostarla liberamente tra Vedere ora / Pensarci dopo / Lasciare riposare / Lasciare andare.",
                                "t_move"
                            ],
                            [
                                "Trascina",
                                "Spostala su un tema",
                                "Con lo stesso trascinamento puoi portarla anche su un chip di tema in alto. Entra in quel tema; rilasciandola su «Senza categoria» la rimuovi.",
                                "t_theme_drag"
                            ],
                            [
                                "Tocca",
                                "Tocca il ○ per lasciare andare",
                                "Tocca il piccolo ○ all'inizio di una voce per mandarla con delicatezza in «Lasciare andare». Puoi annullare subito.",
                                "t_release"
                            ],
                            [
                                "Tocca",
                                "Aggiungi a mano con «＋»",
                                "Dal «＋» tenue in basso a destra di ogni blocco puoi aggiungere una voce in quel posto scrivendola.",
                                "t_add"
                            ]
                        ]
                    },
                    {
                        "subhead": "Raggruppare con i temi",
                        "items": [
                            [
                                "Tieni premuto",
                                "Tieni premuto un tema per il menu",
                                "Tieni premuto un chip di tema in alto per far comparire Mostra sempre (fissa), Modifica nome o colore e Lasciare andare. Da qui si accede alle impostazioni del tema.",
                                "t_theme_press"
                            ],
                            [
                                "Tocca",
                                "Cambia nome, colore e ordine",
                                "Nella schermata di modifica del tema, tocca il nome per riscriverlo, scegli un colore tenue dai pallini colorati e riordina con la maniglia a sinistra.",
                                "t_theme_edit"
                            ]
                        ]
                    }
                ]
            },
            {
                "heading": "Nella schermata subito dopo la divisione",
                "lead": "Il momento subito dopo aver parlato e diviso. Se il modo in cui KUU ha diviso non ti convince, puoi sistemarlo qui prima di conservarlo.",
                "groups": [
                    {
                        "items": [
                            [
                                "Tocca",
                                "Togli con un tocco ciò che non serve",
                                "Tocca una voce che non ti convince: sbiadisce e viene tolta. Tocca di nuovo per riportarla.",
                                "t_remove"
                            ],
                            [
                                "Trascina",
                                "Trascina per cambiare categoria",
                                "Trascina una voce in un altro blocco per cambiarne la categoria, lì per lì.",
                                "t_reclassify"
                            ],
                            [
                                "Pulsante",
                                "«Dividi di nuovo» per correggere tutto il testo",
                                "Se c'è stato un errore di ascolto, con «Dividi di nuovo» puoi correggere l'intera trascrizione e dividerla un'altra volta.",
                                "t_resort"
                            ]
                        ]
                    }
                ]
            },
            {
                "heading": "Nella Home",
                "lead": "Ci sono giorni in cui parlare ad alta voce è difficile. In quei giorni, va bene anche il testo.",
                "groups": [
                    {
                        "items": [
                            [
                                "Tocca",
                                "Scrivi con la tastiera",
                                "Da «Scrivi con la tastiera» in fondo alla Home puoi dividere allo stesso modo scrivendo, senza usare la voce.",
                                "t_keyboard"
                            ]
                        ]
                    }
                ]
            }
        ],
        "tips_note": "Questi suggerimenti compaiono con discrezione sullo schermo una sola volta, la prima volta. Se ti sfuggono, va bene: questa pagina resta sempre qui da rivedere.",
        "tips_closing_sub": "Se non hai ancora provato KUU, comincia da qui.",
        "tips_label": "Consigli d'uso",
        "tips_faq_heading": "Domande ricorrenti",
        "tips_faqs": [
            [
                "Non divide come mi aspetto. La precisione non è granché.",
                [
                    "Il modo in cui KUU interpreta le cose non è sempre perfetto.",
                    "Per questo puoi sempre correggere a mano dopo (tocca per riscrivere / tieni premuto e trascina per spostare / «Dividi di nuovo»).",
                    "Continueremo a migliorare, poco alla volta, la precisione con cui ascolta e ordina.",
                    "Il fatto che tu lo usi è ciò che ci incoraggia."
                ]
            ],
            [
                "Quando parlo a lungo, viene tutto unito in una cosa sola.",
                [
                    "Quando le frasi si susseguono senza pause, i punti di stacco possono essere difficili da trovare.",
                    "Mentre parli, lasciare una piccola pausa — «questo, (un respiro) poi quello» — aiuta a dividere più facilmente.",
                    "Per ciò che hai già inserito, aggiungere virgole e punti al testo con «Dividi di nuovo» aiuta a suddividerlo.",
                    "Se resta comunque unito, puoi dividerlo tenendo premuto e trascinando, oppure riscriverlo con un tocco."
                ]
            ],
            [
                "Ho l'impressione di essere spinto a pagare subito.",
                [
                    "Parlare, dividere, rivedere: il cuore di KUU resta gratuito, per sempre.",
                    "KUU+ è un'aggiunta discreta, per chi desidera disattivare gli annunci o mettere il blocco con Face ID."
                ]
            ],
            [
                "È scomodo da usare quando non posso parlare ad alta voce.",
                [
                    "Da «Scrivi con la tastiera» in fondo alla Home puoi dividere allo stesso modo scrivendo, senza usare la voce."
                ],
                "t_keyboard"
            ]
        ],
        "tips_support_before": "Riscrivere dopo aver parlato, ordinare a mano e altri gesti facili da non notare sono raccolti in",
        "tips_support_after": ".",
        "back": "← Torna all'inizio",
    },
    "vi": {
        "subdir": "vi",
        "html_lang": "vi",
        "og_locale": "vi_VN",
        "label": "Tiếng Việt",
        "title": "KUU — Sắp xếp tâm trí, khoảng lặng để trút suy nghĩ",
        "description": "KUU là ứng dụng trút suy nghĩ tĩnh lặng: chỉ cần nói ra những gì trong đầu, KUU sẽ sắp xếp chúng vào “Xem lúc này / Nghĩ sau / Ủ lại / Buông xuống”.",
        "hero_headline": "Nói ra, cho tâm trí một khoảng trống.",
        "hero_sub": "Từ một cái đầu đầy ắp suy nghĩ, chỉ cần nói ra những gì lúc này bạn chưa cần mang theo.",
        "cta": "Tải trên App Store",
        "scroll_cue": "Cuộn xuống",
        "why_eyebrow": "Vì sao là KUU",
        "why_headline": "Trong đầu, đủ loại suy nghĩ trộn lẫn vào nhau.",
        "why_scenario": "Đang làm dở việc, một điều khác bỗng hiện lên. Bạn không muốn quên, nhưng cũng chưa phải điều cần đối diện ngay lúc này.",
        "why_lead": "Đưa vào ứng dụng quản lý công việc, nó thành “việc phải làm”; ghi vào ghi chú, nó bị chìm đi. Thứ trở nên bừa bộn không phải bản thân suy nghĩ, mà là việc quyết định “xử lý nó thế nào”.",
        "thoughts": [
            "Điều bạn cảm thấy mình phải làm",
            "Điều muốn nghĩ đến sau",
            "Một ý tưởng còn chưa thành hình",
            "Một cảm giác gợn nhẹ khó gọi tên",
            "Một nỗi lo lúc này có nghĩ cũng chưa ích gì"
        ],
        "why_note": "KUU đón nhận trước đã, rồi mới dọn dẹp. Càng nói ra, mực nước trong đầu càng hạ xuống.",
        "steps_eyebrow": "Cách dùng",
        "steps_headline": "Bạn chỉ cần nói.",
        "steps": [
            [
                "Nói",
                "Chưa mạch lạc cũng không sao. Khi nói ra, cả những điều đã quên cũng nối nhau hiện lên."
            ],
            [
                "Chia",
                "KUU lặng lẽ chia chúng vào Xem lúc này / Nghĩ sau / Ủ lại / Buông xuống."
            ],
            [
                "Nhìn lại",
                "Khi đã lắng xuống, xem lại và sắp xếp cho gọn. Không để mọi thứ cứ chất đống mãi."
            ]
        ],
        "app_eyebrow": "Ứng dụng",
        "app_headline": "Đây là KUU.",
        "screen_alt": "Màn hình KUU",
        "matrix_eyebrow": "Ma trận KUU",
        "matrix_headline": "Nơi để đặt từng suy nghĩ.",
        "matrix_lead": "Không phải phân loại công việc, mà chia theo cách bạn muốn xử lý những gì trong đầu.",
        "quadrants": [
            [
                "Xem lúc này",
                "Nhìn qua một chút bây giờ sẽ thấy nhẹ hơn"
            ],
            [
                "Nghĩ sau",
                "Không phải bây giờ, mà vào một lúc khác"
            ],
            [
                "Ủ lại",
                "Chưa vội kết luận, cứ để đó đã"
            ],
            [
                "Buông xuống",
                "Có lẽ không cần giữ mãi nữa"
            ]
        ],
        "quadrants_aria": "Ma trận KUU",
        "privacy_eyebrow": "Quyền riêng tư",
        "privacy_headline": "Giọng nói của bạn không rời khỏi thiết bị.",
        "privacy_body": "Việc nhận diện giọng nói diễn ra hoàn toàn trong thiết bị. Giọng nói của bạn không được lưu lại và cũng không được gửi đi. Việc sắp xếp có dùng AI, nhưng chỉ gửi đi phần nội dung đã chuyển thành chữ, và phần đó cũng không được lưu (bạn có thể chuyển sang chỉ xử lý trong thiết bị ở phần cài đặt). Những gì bạn nói chỉ được đồng bộ vào iCloud riêng tư của bạn.",
        "closing_headline": "Sau khi nói ra, đầu óc nhẹ hơn một chút.",
        "closing_sub": "Một ứng dụng tĩnh lặng, chỉ để dành cho điều đó.",
        "support_label": "Hỗ trợ",
        "privacy_label": "Quyền riêng tư",
        "lang_switcher_aria": "Ngôn ngữ",
        "support_title": "Hỗ trợ — KUU",
        "support_description": "Thông tin liên hệ hỗ trợ và các câu hỏi thường gặp về KUU.",
        "support_h1": "Hỗ trợ",
        "support_intro": "Cảm ơn bạn đã sử dụng KUU. Nếu có thắc mắc hoặc muốn báo lỗi, vui lòng liên hệ theo thông tin bên dưới.",
        "contact_h2": "Liên hệ",
        "contact_body": "Kênh hỗ trợ sẽ sớm được công bố.",
        "faq_h2": "Câu hỏi thường gặp",
        "faqs": [
            [
                "Giọng nói có được lưu lại không?",
                "Không. KUU không gửi âm thanh ra khỏi thiết bị, và khi nhận diện xong sẽ xóa tệp âm thanh tạm. Để sắp xếp, phần gửi đến AI bên ngoài chỉ là nội dung đã chuyển thành chữ, và phần đó cũng không được lưu. Thứ còn lại chỉ là bản chép chữ và kết quả phân loại nằm trong thiết bị và iCloud của bạn."
            ],
            [
                "Có đồng bộ qua iCloud không?",
                "Có. Dữ liệu được đồng bộ vào cơ sở dữ liệu iCloud riêng tư (chỉ chủ nhân Apple ID mới truy cập được). Không có máy chủ nào của nhà phát triển."
            ]
        ],
        "tips_title": "Mẹo sử dụng — KUU",
        "tips_description": "Tổng hợp những thao tác dễ bị bỏ sót của KUU. Giới thiệu nhẹ nhàng cách chỉnh lại sau khi nhập bằng giọng nói, tự tay phân loại, và cách dùng chủ đề.",
        "tips_eyebrow": "Mẹo sử dụng",
        "tips_h1": "Sau khi nói ra, mọi thứ vẫn trong tay bạn.",
        "tips_lead": "Để giữ màn hình tĩnh lặng, KUU không phô bày phần lớn các thao tác. Nhưng bạn vẫn có thể chỉnh lại phần nghe được, hay tự tay phân loại. Những thao tác dễ bị bỏ sót, chúng tôi gom lại ở đây.",
        "tips_screens": [
            {
                "heading": "Ở nơi đặt suy nghĩ",
                "lead": "Màn hình bạn dùng nhiều nhất, kéo lên từ Trang chủ. Những gì đã chia bằng giọng nói sẽ tụ về bốn nơi. Phần lớn thao tác dễ bỏ sót cũng nằm ở đây.",
                "groups": [
                    {
                        "subhead": "Chỉnh từng mục một",
                        "items": [
                            [
                                "Chạm",
                                "Chạm vào tiêu đề để viết lại",
                                "Chạm thẳng vào chữ của một mục là có thể viết lại ngay tại chỗ. Những sai lệch nhỏ khi nghe có thể chỉnh lại ở đây.",
                                "t_edit"
                            ],
                            [
                                "Nhấn giữ → kéo",
                                "Chuyển sang nơi khác",
                                "Nhấn giữ một mục rồi kéo, bạn có thể tự do chuyển nó qua lại giữa Xem lúc này / Nghĩ sau / Ủ lại / Buông xuống.",
                                "t_move"
                            ],
                            [
                                "Kéo",
                                "Chuyển vào một chủ đề",
                                "Cũng bằng thao tác kéo đó, bạn có thể đưa mục lên thẻ chủ đề ở trên. Nó sẽ vào chủ đề ấy; thả vào “Chưa phân loại” thì nó rời ra.",
                                "t_theme_drag"
                            ],
                            [
                                "Chạm",
                                "Chạm vào ○ để buông xuống",
                                "Chạm vào dấu ○ nhỏ ở đầu mỗi mục, nó sẽ nhẹ nhàng chuyển sang “Buông xuống” ngay tại chỗ. Bạn cũng có thể hoàn tác ngay.",
                                "t_release"
                            ],
                            [
                                "Chạm",
                                "Thêm thủ công bằng “＋”",
                                "Từ dấu “＋” mờ ở góc dưới bên phải mỗi khối, bạn có thể thêm một mục bằng chữ vào đúng nơi đó.",
                                "t_add"
                            ]
                        ]
                    },
                    {
                        "subhead": "Gom nhóm theo chủ đề",
                        "items": [
                            [
                                "Nhấn giữ",
                                "Nhấn giữ chủ đề để mở menu",
                                "Nhấn giữ thẻ chủ đề ở trên sẽ hiện ra Luôn hiển thị (ghim) / Sửa tên hoặc màu / Buông xuống. Đây là lối vào phần cài đặt của chủ đề.",
                                "t_theme_press"
                            ],
                            [
                                "Chạm",
                                "Đổi tên, màu và thứ tự",
                                "Trong màn hình chỉnh sửa chủ đề, chạm vào tên để viết lại, chọn màu nhạt từ các chấm màu, và sắp xếp lại bằng tay cầm bên trái.",
                                "t_theme_edit"
                            ]
                        ]
                    }
                ]
            },
            {
                "heading": "Ở màn hình ngay sau khi chia",
                "lead": "Ngay sau khi nói và được chia. Nếu cách chia của KUU chưa thật vừa ý, bạn có thể chỉnh lại ở đây rồi mới lưu.",
                "groups": [
                    {
                        "items": [
                            [
                                "Chạm",
                                "Chạm để bỏ những gì không cần",
                                "Chạm vào mục chưa thấy hợp, nó sẽ mờ đi rồi rời ra. Chạm lần nữa để đưa nó trở lại.",
                                "t_remove"
                            ],
                            [
                                "Kéo",
                                "Kéo để đổi phân loại",
                                "Kéo một mục sang khối khác là có thể đổi phân loại ngay tại chỗ.",
                                "t_reclassify"
                            ],
                            [
                                "Nút",
                                "“Chia lại” để sửa toàn bộ văn bản",
                                "Nếu có chỗ nghe nhầm, từ “Chia lại” bạn có thể sửa toàn bộ bản chép chữ rồi chia lại một lần nữa.",
                                "t_resort"
                            ]
                        ]
                    }
                ]
            },
            {
                "heading": "Ở Trang chủ",
                "lead": "Có những ngày khó cất tiếng. Những lúc như vậy, viết chữ cũng được.",
                "groups": [
                    {
                        "items": [
                            [
                                "Chạm",
                                "Viết bằng bàn phím",
                                "Từ “Viết bằng bàn phím” ở dưới Trang chủ, bạn có thể chia y như vậy bằng chữ mà không cần dùng giọng nói.",
                                "t_keyboard"
                            ]
                        ]
                    }
                ]
            }
        ],
        "tips_note": "Những gợi ý này chỉ hiện ra nhẹ nhàng trên màn hình đúng một lần đầu tiên. Có bỏ lỡ cũng không sao. Trang này lúc nào bạn cũng có thể xem lại.",
        "tips_closing_sub": "Nếu bạn chưa thử KUU, hãy bắt đầu từ đây.",
        "tips_label": "Mẹo sử dụng",
        "tips_faq_heading": "Những thắc mắc thường gặp",
        "tips_faqs": [
            [
                "Không chia đúng như tôi nghĩ. Độ chính xác chưa được như mong đợi.",
                [
                    "Cách nhìn nhận của KUU không phải lúc nào cũng hoàn hảo.",
                    "Vì vậy, chúng tôi luôn để bạn có thể tự tay chỉnh lại về sau (chạm để viết lại / nhấn giữ rồi kéo để chuyển / “Chia lại”).",
                    "Độ chính xác khi nghe và khi phân loại sẽ được cải thiện dần dần.",
                    "Việc bạn sử dụng chính là nguồn động viên cho chúng tôi."
                ]
            ],
            [
                "Khi nói dài, mọi thứ bị gộp hết vào làm một.",
                [
                    "Khi các câu nối liền nhau, đôi khi khó tìm ra chỗ ngắt.",
                    "Khi nói, hãy để một khoảng nghỉ nhỏ, kiểu “... rồi, (một hơi thở) ... rồi”, thì sẽ dễ được tách ra hơn.",
                    "Với những gì đã nhập, bạn thêm dấu phẩy và dấu chấm vào câu ở “Chia lại” thì sẽ dễ được ngắt ra hơn.",
                    "Nếu vẫn bị gộp, bạn có thể nhấn giữ rồi kéo để tách, hoặc chạm để viết lại."
                ]
            ],
            [
                "Tôi có cảm giác bị mời mua ngay lập tức.",
                [
                    "Nói ra, chia, xem lại — phần cốt lõi của KUU luôn miễn phí.",
                    "KUU+ chỉ là phần thêm nhẹ nhàng, dành cho ai muốn tắt quảng cáo hoặc muốn khóa bằng Face ID."
                ]
            ],
            [
                "Khó dùng trong những lúc không thể nói ra tiếng.",
                [
                    "Từ “Viết bằng bàn phím” ở dưới Trang chủ, bạn có thể chia y như vậy bằng chữ mà không cần dùng giọng nói."
                ],
                "t_keyboard"
            ]
        ],
        "tips_support_before": "Những thao tác dễ bị bỏ sót — như chỉnh lại sau khi nhập bằng giọng nói, hay tự tay phân loại — được gom lại trong",
        "tips_support_after": ".",
        "back": "← Về đầu trang",
    },
    "zh-Hant": {
        "subdir": "zh-Hant",
        "html_lang": "zh-Hant",
        "og_locale": "zh_TW",
        "label": "繁體中文",
        "title": "KUU — 整理腦中思緒，安靜的腦內傾倒",
        "description": "KUU 是一款安靜的腦內傾倒 App，只要把腦中的思緒說出口，就會替你整理成「現在看看／之後再想／先放著／放下」。",
        "hero_headline": "說出來，給腦袋一點餘白。",
        "hero_sub": "從塞滿思緒的腦袋裡，把此刻不必扛著的事，說出來就好。",
        "cta": "在 App Store 下載",
        "scroll_cue": "往下",
        "why_eyebrow": "為什麼是 KUU",
        "why_headline": "腦袋裡，混雜著各種思緒。",
        "why_scenario": "做事做到一半，別的念頭忽然冒出來。不想忘掉，可現在也不是面對它的時候。",
        "why_lead": "放進待辦 App 就成了「要做的事」，寫進筆記又被埋沒。亂的不是思緒本身，而是「該怎麼處置」的判斷。",
        "thoughts": [
            "總覺得非做不可的事",
            "想留到之後再想的事",
            "還沒成形的靈感",
            "莫名在意的違和感",
            "此刻想也無益的擔憂"
        ],
        "why_note": "KUU 先接住，再談整理。說得越多，腦中的水位就越低。",
        "steps_eyebrow": "使用方式",
        "steps_headline": "要做的，只有說。",
        "steps": [
            [
                "說",
                "不必整理得有條理。一說出口，連忘掉的事也會一件接一件浮現。"
            ],
            [
                "分",
                "KUU 會安靜地分成現在看看／之後再想／先放著／放下。"
            ],
            [
                "回看",
                "等平靜下來，再回頭看看、整理它們。不會只是一味堆著。"
            ]
        ],
        "app_eyebrow": "App",
        "app_headline": "這就是 KUU。",
        "screen_alt": "KUU 的畫面",
        "matrix_eyebrow": "KUU 矩陣",
        "matrix_headline": "思緒的，去處。",
        "matrix_lead": "不是待辦分類，而是依你看待腦中之物的方式來分。",
        "quadrants": [
            [
                "現在看看",
                "現在稍微看一眼，就會輕鬆一些的事"
            ],
            [
                "之後再想",
                "不是現在，換個時機再說"
            ],
            [
                "先放著",
                "還不急著下結論，先擱著"
            ],
            [
                "放下",
                "已經不必再一直扛著的事"
            ]
        ],
        "quadrants_aria": "KUU 矩陣",
        "privacy_eyebrow": "隱私",
        "privacy_headline": "你的聲音，不會外流。",
        "privacy_body": "聆聽全都只在你的裝置裡完成——語音本身從不保留、也不會傳送。整理會用到 AI，因此只傳送轉成文字的內容，而且同樣不會保存（也可以在設定裡改為只在裝置內處理）。你說過的話，只會同步到你私人的 iCloud。",
        "closing_headline": "說完之後，腦袋輕一點。",
        "closing_sub": "一款只為此而生的、安靜的 App。",
        "support_label": "支援",
        "privacy_label": "隱私",
        "lang_switcher_aria": "語言",
        "support_title": "支援 — KUU",
        "support_description": "KUU 的支援聯絡方式與常見問題。",
        "support_h1": "支援",
        "support_intro": "感謝你使用 KUU。若有疑問或想回報問題，請透過下方的方式與我們聯絡。",
        "contact_h2": "聯絡我們",
        "contact_body": "支援窗口即將開放。",
        "faq_h2": "常見問題",
        "faqs": [
            [
                "聲音會被保存嗎？",
                "不會。KUU 不會把語音傳出裝置，辨識完成後就會刪除暫存的語音檔。為了整理而傳送給外部 AI 的只有轉成文字的內容，而且同樣不會保存。留下的，只有你裝置與 iCloud 中的文字記錄與分類結果。"
            ],
            [
                "iCloud 同步呢？",
                "會同步到 iCloud 私人資料庫（只有 Apple ID 擁有者本人能存取）。沒有開發者伺服器。"
            ]
        ],
        "tips_title": "使用訣竅 — KUU",
        "tips_description": "彙整 KUU 中不易察覺的操作。語音輸入之後的修改、自己動手的分類、主題的用法，靜靜地一一介紹。",
        "tips_eyebrow": "使用訣竅",
        "tips_h1": "說出來之後，也能自己動手。",
        "tips_lead": "KUU 為了讓畫面保持安靜，沒有把大多數操作擺在明面上。不過，修改聽寫、親手分類，都做得到。這些不易察覺的，我們彙整在這裡。",
        "tips_screens": [
            {
                "heading": "在思緒的去處",
                "lead": "從主畫面向上拉出的、最常用的畫面。用聲音分好的思緒，會匯集到四個去處。不易察覺的操作，也大多在這裡。",
                "groups": [
                    {
                        "subhead": "逐一整理每個項目",
                        "items": [
                            [
                                "輕點",
                                "輕點標題即可改寫",
                                "直接輕點項目的文字，就能當場改寫。聽寫的細小偏差，都可以在這裡修整。",
                                "t_edit"
                            ],
                            [
                                "長按 → 拖曳",
                                "移到別的去處",
                                "長按項目並拖曳，就能在現在看看／之後再想／先放著／放下之間自由挪移。",
                                "t_move"
                            ],
                            [
                                "拖曳",
                                "移到主題",
                                "用同樣的拖曳，也能移到上方的主題標籤。移進那個主題就歸入其中；把它放到「未分類」，就會移出。",
                                "t_theme_drag"
                            ],
                            [
                                "輕點",
                                "輕點○即可放下",
                                "輕點項目開頭的小○，就能當場輕輕地把它放下。也可以馬上撤銷。",
                                "t_release"
                            ],
                            [
                                "輕點",
                                "用「＋」手動補記",
                                "從每個區塊右下角淡淡的「＋」，就能在那個位置用文字補記一則項目。",
                                "t_add"
                            ]
                        ]
                    },
                    {
                        "subhead": "用主題歸整",
                        "items": [
                            [
                                "長按",
                                "長按主題開啟選單",
                                "長按上方的主題標籤，會出現始終顯示（釘選）／編輯名稱或顏色／放下。主題的設定，入口就在這裡。",
                                "t_theme_press"
                            ],
                            [
                                "輕點",
                                "更改名稱、顏色與排序",
                                "在主題的編輯畫面，輕點名稱即可改寫，從色點裡挑選淡色，用左側的握把調整排序。",
                                "t_theme_edit"
                            ]
                        ]
                    }
                ]
            },
            {
                "heading": "在剛分好的畫面",
                "lead": "說完、分好，緊接著的那一刻。若 KUU 分得不合心意，可以在這裡整理好，再留下來。",
                "groups": [
                    {
                        "items": [
                            [
                                "輕點",
                                "不需要的，輕點移除",
                                "沒什麼感覺的項目，輕點一下就會變淡、移出。再輕點一次便能復原。",
                                "t_remove"
                            ],
                            [
                                "拖曳",
                                "拖曳改變分類",
                                "把項目拖到別的區塊，就能當場改變分類。",
                                "t_reclassify"
                            ],
                            [
                                "按鈕",
                                "用「重新分類」修正全文",
                                "若有聽錯，可以從「重新分類」把整段文字都改好，再分一次。",
                                "t_resort"
                            ]
                        ]
                    }
                ]
            },
            {
                "heading": "在主畫面",
                "lead": "也有不方便出聲的日子。那樣的時候，用文字也可以。",
                "groups": [
                    {
                        "items": [
                            [
                                "輕點",
                                "用鍵盤寫",
                                "從主畫面下方的「用鍵盤寫」，不出聲、用文字，也能一樣地分好。",
                                "t_keyboard"
                            ]
                        ]
                    }
                ]
            }
        ],
        "tips_note": "這些提示，只在最初的那一次靜靜出現在畫面上。錯過也沒關係。這個頁面，隨時都能回看。",
        "tips_closing_sub": "如果還沒試過 KUU，可以從這裡開始。",
        "tips_label": "使用訣竅",
        "tips_faq_heading": "常見疑問",
        "tips_faqs": [
            [
                "分得不像我想的那樣。準確度還差一點。",
                [
                    "KUU 的判斷，並非總是完美。",
                    "所以，我們讓它之後可以親手修改（輕點改寫／長按拖曳移動／「重新分類」）。",
                    "聽寫與分類的準確度，今後也會一點一點變好。",
                    "有你在用，就是我們前進的動力。"
                ]
            ],
            [
                "說得一長，就全被併到一起了。",
                [
                    "句子一連下去，有時就不容易找到斷點。",
                    "說的時候，像「說完一句，（喘口氣）再說一句」這樣，稍微留些停頓，就更容易分開。",
                    "已經輸入的內容，可以用「重新分類」替句子加上逗號和句號，就更容易斷開。",
                    "如果還是被併在一起，可以長按拖曳來分開，或輕點改寫。"
                ]
            ],
            [
                "總覺得很快就被引去付費。",
                [
                    "說出來、分好、回看——KUU 的核心，一直都能免費使用。",
                    "KUU+ 是給想關掉廣告、想加上 Face ID 鎖的人，悄悄準備的一點補充。"
                ]
            ],
            [
                "在不方便出聲的場合，不太好用。",
                [
                    "從主畫面下方的「用鍵盤寫」，不出聲、用文字，也能一樣地分好。"
                ],
                "t_keyboard"
            ]
        ],
        "tips_support_before": "語音輸入之後的修改、自己動手的分類等不易察覺的操作，都彙整在",
        "tips_support_after": "裡。",
        "back": "← 返回頂部",
    },
}

# KUU palette — sourced from KUU/Theme/KUUColors.swift (the app's design tokens).
BASE_CSS = """\
:root {
  color-scheme: light;
  --bg: #f6f9fc;
  --surface: #ffffff;
  --surface-quiet: #eff4f8;
  --ink: #353b41;
  --ink-soft: #6b737b;
  --ink-faint: #939aa2;
  --primary: #7fb2d6;
  --primary-deep: #5e97c2;
  --primary-soft: #dceaf4;
  --water-action: #bfddef;
  --water-ink: #255069;
  --water-top: #cfe4f2;
  --water-bottom: #9cc6e2;
  --line: #e7edf3;
  --cat-now: #5e97c2;
  --cat-later: #4fa39a;
  --cat-parked: #8c8ab8;
  --cat-release: #aab2ba;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  padding: 0;
  background: var(--bg);
  color: var(--ink);
  font-family: -apple-system, BlinkMacSystemFont, "Hiragino Sans", "Apple SD Gothic Neo", "PingFang SC", "Helvetica Neue", Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
  line-height: 1.7;
  /* CJK 句読点 (、。) を proportional alternate で詰め組み＝中央寄せの見た目を均す。
     "halt" は「、」を潰す副作用があるため使わない (スクショ editor と同方針)。 */
  font-feature-settings: "palt" 1, "kern" 1;
  font-kerning: normal;
}
.wrap { max-width: 660px; margin: 0 auto; padding: 0 24px; }
section { padding: clamp(64px, 13vw, 132px) 0; }

/* ---- hero ---- */
.hero {
  min-height: 100svh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: clamp(48px, 10vw, 96px) 24px clamp(40px, 8vw, 72px);
  position: relative;
}
.wordmark {
  font-size: 15px;
  font-weight: 600;
  letter-spacing: 0.42em;
  color: var(--primary-deep);
  margin: 0 0 clamp(24px, 5vw, 40px) 0.42em;
}
.hero h1 {
  font-size: clamp(30px, 7vw, 46px);
  font-weight: 600;
  letter-spacing: 0.01em;
  line-height: 1.35;
  margin: 0;
}
.hero .sub {
  color: var(--ink-soft);
  font-size: clamp(15px, 4vw, 17px);
  max-width: 30em;
  margin: clamp(16px, 4vw, 22px) auto 0;
}

/* ---- water orb (the KUU signature) ---- */
.orb {
  position: relative;
  width: clamp(176px, 46vw, 248px);
  aspect-ratio: 1;
  margin: clamp(36px, 8vw, 60px) auto;
  border-radius: 50%;
  overflow: hidden;
  background: radial-gradient(125% 120% at 50% 16%, #ffffff, var(--surface-quiet));
  border: 1px solid var(--line);
  box-shadow: 0 30px 64px -30px rgba(94, 151, 194, 0.55), inset 0 1px 0 rgba(255, 255, 255, 0.9);
}
.orb__water {
  position: absolute;
  left: -28%;
  right: -28%;
  bottom: -12%;
  /* 水位はスクロールで静かに下がる (--wl: JS, 0〜) ＝ 余白が増える world view */
  height: calc(60% - var(--wl, 0px));
  background: linear-gradient(180deg, var(--water-top), var(--water-bottom));
  border-radius: 42% 44% 0 0 / 58% 56% 0 0;
  animation: orb-bob 7.5s ease-in-out infinite, orb-sway 11s ease-in-out infinite;
}
.orb__water::before {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  top: -10px;
  height: 26px;
  background: var(--water-top);
  opacity: 0.5;
  border-radius: 46%;
  animation: orb-sway 9s ease-in-out infinite reverse;
}
@keyframes orb-bob {
  0%, 100% { transform: translateY(5px); }
  50% { transform: translateY(-7px); }
}
@keyframes orb-sway {
  0%, 100% { border-radius: 42% 44% 0 0 / 58% 56% 0 0; }
  50% { border-radius: 47% 39% 0 0 / 54% 60% 0 0; }
}

/* 水中を下から上へ昇る泡 (アプリ WaterLevelView.Bubbles を CSS で再現) */
.orb__bubbles { position: absolute; inset: 0; pointer-events: none; }
.bubble {
  position: absolute;
  bottom: 0;
  left: var(--bx);
  width: var(--bs);
  height: var(--bs);
  border-radius: 50%;
  /* 明るい芯＋淡いリム＝空気泡らしく、薄水色の上でも視認できる */
  background: radial-gradient(circle at 50% 38%, rgba(255, 255, 255, 0.92), rgba(255, 255, 255, 0.28) 70%, rgba(255, 255, 255, 0) 100%);
  box-shadow: 0 0 1.5px rgba(255, 255, 255, 0.6);
  opacity: 0;
  animation: bubble-rise var(--bdur) var(--bd) linear infinite;
}
@keyframes bubble-rise {
  0% { bottom: 3%; opacity: 0; transform: translateX(0); }
  18% { opacity: 0.85; }
  50% { transform: translateX(4px); }
  82% { opacity: 0.5; }
  100% { bottom: 55%; opacity: 0; transform: translateX(-3px); }
}

/* ---- cta ---- */
.cta {
  display: inline-block;
  margin-top: clamp(28px, 6vw, 40px);
  padding: 15px 30px;
  background: var(--water-action);
  color: var(--water-ink);
  border-radius: 999px;
  text-decoration: none;
  font-weight: 600;
  font-size: 15px;
  letter-spacing: 0.02em;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.cta:hover { transform: translateY(-1px); box-shadow: 0 10px 24px -12px rgba(37, 80, 105, 0.5); }
.scroll-cue {
  margin-top: clamp(36px, 8vw, 64px);
  font-size: 11px;
  letter-spacing: 0.3em;
  color: var(--ink-faint);
  writing-mode: vertical-rl;
  animation: cue 2.4s ease-in-out infinite;
}
@keyframes cue {
  0%, 100% { transform: translateY(0); opacity: 0.5; }
  50% { transform: translateY(6px); opacity: 1; }
}

/* ---- shared section type ---- */
.eyebrow {
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.24em;
  color: var(--primary-deep);
  text-transform: uppercase;
  margin: 0 0 14px;
}
h2 {
  font-size: clamp(22px, 5.2vw, 30px);
  font-weight: 600;
  line-height: 1.45;
  letter-spacing: 0.01em;
  margin: 0;
}
.lead { color: var(--ink-soft); font-size: clamp(15px, 4vw, 16px); margin: 16px 0 0; }
.scenario { color: var(--ink); font-size: clamp(16px, 4.4vw, 18px); line-height: 1.7; margin: 18px 0 0; }

/* ---- why: thought list ---- */
.thoughts { list-style: none; padding: 0; margin: 32px 0 0; }
.thoughts li {
  position: relative;
  padding: 14px 0 14px 26px;
  color: var(--ink);
  font-size: clamp(15px, 4vw, 16px);
  border-top: 1px solid var(--line);
}
.thoughts li:last-child { border-bottom: 1px solid var(--line); }
.thoughts li::before {
  content: "";
  position: absolute;
  left: 2px;
  top: 50%;
  width: 8px;
  height: 8px;
  margin-top: -4px;
  border-radius: 50%;
  background: var(--primary-soft);
}
.note {
  margin: 30px 0 0;
  padding: 22px 24px;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 18px;
  color: var(--ink-soft);
  font-size: clamp(15px, 4vw, 16px);
}

/* ---- steps ---- */
.steps { display: grid; gap: 16px; margin-top: 36px; }
.step {
  display: flex;
  gap: 18px;
  align-items: flex-start;
  padding: 22px 24px;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 18px;
}
.step .n {
  flex: none;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: var(--primary-soft);
  color: var(--primary-deep);
  font-weight: 600;
  font-size: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.step h3 { margin: 0 0 4px; font-size: 17px; font-weight: 600; }
.step p { margin: 0; color: var(--ink-soft); font-size: 15px; }

/* ---- app showcase (App Store style gallery) ---- */
.app .wrap { margin-bottom: 4px; }
.showcase {
  display: flex;
  gap: 18px;
  margin-top: 28px;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  padding: 6px max(24px, calc((100vw - 660px) / 2)) 10px;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: none;
  cursor: grab;
}
.showcase::-webkit-scrollbar { display: none; }
.shot {
  flex: 0 0 auto;
  width: min(64vw, 272px);
  height: auto;
  display: block;
  border-radius: 28px;
  border: 1px solid var(--line);
  box-shadow: 0 26px 54px -30px rgba(94, 151, 194, 0.55);
  background: var(--surface);
  scroll-snap-align: center;
}

/* ---- matrix ---- */
.matrix {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
  margin-top: 36px;
}
.q {
  padding: 22px 20px;
  border-radius: 20px;
  /* アプリの象限カードと同じ: 白地 + カテゴリ色の縦グラデ (0.10→0.24) + ラベルはカテゴリ色
     (ResultView.swift / PlaceView.swift の tint.opacity(0.10..0.24) を再現) */
  background:
    linear-gradient(180deg,
      color-mix(in srgb, var(--q, var(--primary)) 10%, #fff),
      color-mix(in srgb, var(--q, var(--primary)) 24%, #fff));
  border: 1px solid color-mix(in srgb, var(--q, var(--primary)) 20%, var(--line));
}
.q strong { display: block; color: var(--q, var(--primary)); font-size: 16px; font-weight: 600; margin-bottom: 6px; }
.q span { color: var(--ink-soft); font-size: 13.5px; line-height: 1.6; }

/* ---- privacy ---- */
.privacy { text-align: center; }
.privacy .lead { max-width: 30em; margin-left: auto; margin-right: auto; }

/* ---- closing ---- */
.closing { text-align: center; padding-bottom: clamp(40px, 9vw, 80px); }
.closing h2 { font-size: clamp(24px, 6vw, 34px); }
.closing .sub { color: var(--ink-soft); margin: 14px 0 0; font-size: clamp(15px, 4vw, 17px); }

/* ---- footer ---- */
footer {
  border-top: 1px solid var(--line);
  font-size: 13px;
  color: var(--ink-soft);
  padding: 40px 0 56px;
}
.footer-row { display: flex; gap: 20px; flex-wrap: wrap; align-items: center; margin-bottom: 14px; }
.footer-row a { color: var(--ink-soft); text-decoration: none; }
.footer-row a:hover { text-decoration: underline; }
.langs { display: flex; gap: 14px; flex-wrap: wrap; font-size: 12px; padding-top: 14px; border-top: 1px dashed var(--line); }
.langs a { color: var(--ink-soft); text-decoration: none; }
.langs a[aria-current="true"] { color: var(--ink); font-weight: 600; }
.langs a:hover { text-decoration: underline; }

/* ---- scroll reveal (progressive enhancement) ---- */
.js .reveal { opacity: 0; transform: translateY(22px); transition: opacity 0.8s cubic-bezier(0.22, 0.61, 0.36, 1), transform 0.8s cubic-bezier(0.22, 0.61, 0.36, 1); }
.js .reveal.in { opacity: 1; transform: none; }

/* staggered reveal: children settle in one after another */
.js .reveal .stagger > * { opacity: 0; transform: translateY(14px); transition: opacity 0.6s cubic-bezier(0.22, 0.61, 0.36, 1), transform 0.6s cubic-bezier(0.22, 0.61, 0.36, 1); }
.js .reveal.in .stagger > * { opacity: 1; transform: none; }
.js .reveal.in .stagger > *:nth-child(2) { transition-delay: 0.07s; }
.js .reveal.in .stagger > *:nth-child(3) { transition-delay: 0.14s; }
.js .reveal.in .stagger > *:nth-child(4) { transition-delay: 0.21s; }
.js .reveal.in .stagger > *:nth-child(5) { transition-delay: 0.28s; }
.js .reveal.in .stagger > *:nth-child(6) { transition-delay: 0.35s; }

/* hero entrance on first load */
.js .hero .wordmark { animation: enter 0.8s 0.05s both cubic-bezier(0.22, 0.61, 0.36, 1); }
.js .hero h1 { animation: enter 0.8s 0.16s both cubic-bezier(0.22, 0.61, 0.36, 1); }
.js .hero .sub { animation: enter 0.8s 0.28s both cubic-bezier(0.22, 0.61, 0.36, 1); }
.js .hero .orb { animation: enter 1s 0.4s both cubic-bezier(0.22, 0.61, 0.36, 1); }
.js .hero .cta { animation: enter 0.8s 0.58s both cubic-bezier(0.22, 0.61, 0.36, 1); }
@keyframes enter { from { opacity: 0; transform: translateY(18px); } to { opacity: 1; transform: none; } }

@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  .orb__water, .orb__water::before, .scroll-cue, .bubble { animation: none; }
  .bubble { opacity: 0; }
  .js .hero .wordmark, .js .hero h1, .js .hero .sub, .js .hero .orb, .js .hero .cta { animation: none; }
  .js .reveal, .js .reveal .stagger > * { opacity: 1; transform: none; transition: none; }
}
"""

REVEAL_SCRIPT = """\
<script>
  document.documentElement.classList.add('js');
  var prefersReduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  addEventListener('DOMContentLoaded', function () {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.16 });
    document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });

    if (prefersReduce) return;
    var water = document.querySelector('.orb__water');
    var ticking = false;
    function update() {
      var y = window.scrollY || 0;
      var vh = window.innerHeight || 1;
      // hero の水位はスクロール最初の 1 画面で静かに下がる＝余白が増える
      if (water) water.style.setProperty('--wl', (Math.min(y / vh, 1) * 16).toFixed(1) + 'px');
      ticking = false;
    }
    addEventListener('scroll', function () {
      if (!ticking) { ticking = true; requestAnimationFrame(update); }
    }, { passive: true });
    update();
  });
</script>
"""

# Tips page reveal: sections are tall, so a 16% threshold never fires for the first
# section within the initial viewport → it stayed hidden until scroll (blank first view).
# threshold 0 + slight bottom rootMargin: reveal as soon as any part enters (first
# section shows on load). No water-orb logic (tips has no orb).
TIPS_REVEAL_SCRIPT = """\
<script>
  document.documentElement.classList.add('js');
  addEventListener('DOMContentLoaded', function () {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0, rootMargin: '0px 0px -8% 0px' });
    document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });
  });
</script>
"""

# Horizontal shot galleries (.showcase / .pitch-shots) scroll natively via touch/trackpad,
# but a plain mouse has no way to drag them — this adds click-and-drag for mouse only,
# leaving touch/trackpad's native momentum scroll untouched.
# Uses classic mouse events (not Pointer Events): a scrollable + scroll-snap element makes
# Chromium hijack the pointer capture as a native pan gesture and fire pointercancel instead
# of pointerup mid-drag, snapping the scroll back to 0. Plain mousemove/mouseup on document
# (not the element) isn't subject to that native takeover and keeps tracking past the element's edge.
DRAG_SCROLL_SCRIPT = """\
<script>
  document.querySelectorAll('.showcase, .pitch-shots').forEach(function (el) {
    var down = false, startX = 0, startScroll = 0, raf = null, lastX = 0;
    function apply() {
      raf = null;
      el.scrollLeft = startScroll - (lastX - startX);
    }
    el.addEventListener('mousedown', function (e) {
      down = true;
      startX = lastX = e.clientX;
      startScroll = el.scrollLeft;
      // mandatory snap fights the per-frame scrollLeft write and stutters — suspend while dragging.
      el.style.scrollSnapType = 'none';
      el.style.cursor = 'grabbing';
      e.preventDefault();
    });
    document.addEventListener('mousemove', function (e) {
      if (!down) return;
      lastX = e.clientX;
      // batch to one write per frame instead of one per mousemove (which fires far more often
      // than the display refreshes) — the latter is what caused the choppy motion.
      if (raf == null) raf = requestAnimationFrame(apply);
    });
    document.addEventListener('mouseup', function () {
      if (!down) return;
      down = false;
      el.style.cursor = '';
      el.style.scrollSnapType = '';
    });
  });
</script>
"""

SUPPORT_CSS = """\
:root {
  color-scheme: light;
  --bg: #f6f9fc;
  --ink: #353b41;
  --ink-soft: #6b737b;
  --line: #e7edf3;
}
body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font-family: -apple-system, BlinkMacSystemFont, "Hiragino Sans", "Apple SD Gothic Neo", "PingFang SC", "Helvetica Neue", Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
}
main {
  max-width: 640px;
  margin: 0 auto;
  padding: clamp(48px, 10vw, 96px) 24px 80px;
}
h1 { font-size: 28px; font-weight: 600; margin: 0 0 24px; }
h2 { font-size: 18px; font-weight: 600; margin: 32px 0 8px; }
p { line-height: 1.7; color: var(--ink-soft); margin: 0 0 12px; }
a { color: var(--ink); }
.back {
  display: inline-block;
  margin-top: 48px;
  padding-top: 24px;
  border-top: 1px solid var(--line);
  color: var(--ink-soft);
  text-decoration: none;
  font-size: 14px;
}
.langs {
  margin-top: 48px;
  padding-top: 16px;
  border-top: 1px dashed var(--line);
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
  font-size: 12px;
}
.langs a { color: var(--ink-soft); text-decoration: none; }
.langs a[aria-current="true"] { color: var(--ink); font-weight: 600; }
.langs a:hover { text-decoration: underline; }
"""

# Journal (content SEO article + hub) pages: long-form reading layout on top of SUPPORT_CSS,
# plus the LP's pill CTA and a card grid for the /journal/ hub listing.
# 直帰対策: 読みやすさのリズム（リード強調・マーカー付き strong・目立つ h2）を優先する。
JOURNAL_CSS = SUPPORT_CSS + """\
:root {
  --primary: #7fb2d6;
  --primary-deep: #5e97c2;
  --primary-soft: #dceaf4;
}
main { max-width: 680px; }
.eyebrow {
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.2em;
  color: var(--primary-deep);
  text-transform: uppercase;
  margin: 0 0 14px;
}
h1 { font-size: clamp(24px, 6vw, 30px); line-height: 1.5; letter-spacing: 0.01em; }
.updated { display: flex; gap: 14px; font-size: 13px; color: var(--ink-soft); margin: 0 0 36px; }
article p { line-height: 2.0; color: #4d545b; margin: 0 0 20px; }
/* リード（最初の段落）は少し大きく濃く: 冒頭で「自分の話だ」と思わせる。
   .updated を p にすると first-of-type がそちらに当たるため div にしている */
article > p:first-of-type { font-size: 17px; color: var(--ink); }
article h2 {
  font-size: 20px;
  line-height: 1.6;
  margin: 56px 0 16px;
}
article h3 { font-size: 16.5px; margin: 32px 0 10px; }
/* 蛍光マーカー風の強調: 流し読みでも要点が拾える */
article strong {
  font-weight: 600;
  color: var(--ink);
  background: linear-gradient(transparent 62%, var(--primary-soft) 62%);
  padding: 0 1px;
}
article ul, article ol { line-height: 2.0; color: #4d545b; padding-left: 1.5em; margin: 0 0 20px; }
article li { margin: 6px 0; }
article li::marker { color: var(--primary-deep); font-weight: 600; }
article blockquote {
  margin: 0 0 20px;
  padding: 14px 20px;
  background: #eff4f8;
  border-radius: 14px;
  color: var(--ink);
}
article blockquote p { margin: 0; font-family: ui-monospace, "SF Mono", Menlo, monospace; font-size: 14px; line-height: 1.9; }
article a { color: var(--primary-deep); }
.cta {
  display: inline-block;
  margin-top: 18px;
  padding: 15px 34px;
  background: var(--primary-deep);
  color: #fff;
  border-radius: 999px;
  text-decoration: none;
  font-weight: 600;
  font-size: 16px;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.cta:hover { transform: translateY(-1px); box-shadow: 0 10px 24px -12px rgba(37, 80, 105, 0.5); }
.kuu-pitch {
  margin-top: 56px;
  padding: 32px 28px;
  background: #fff;
  border-radius: 24px;
  box-shadow: 0 2px 8px rgba(37, 80, 105, 0.07);
  text-align: center;
}
.kuu-pitch h2 { margin-top: 0; font-size: 19px; }
.kuu-pitch p { color: var(--ink-soft); }
.pitch-shots {
  display: flex;
  gap: 14px;
  margin: 0 0 16px;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: none;
  cursor: grab;
}
.pitch-shots::-webkit-scrollbar { display: none; }
.pitch-shot {
  flex: 0 0 auto;
  width: min(48vw, 180px);
  height: auto;
  display: block;
  border-radius: 20px;
  border: 1px solid var(--line);
  box-shadow: 0 16px 32px -20px rgba(94, 151, 194, 0.55);
  scroll-snap-align: start;
}
.rating {
  font-size: 13px;
  font-weight: 600;
  color: var(--primary-deep);
  margin: 0 0 16px;
}
.rating .rating-count { font-weight: 400; color: var(--ink-soft); }
.kuu-pitch .note { margin: 12px 0 0; font-size: 13px; color: var(--ink-soft); }
.related { margin-top: 48px; }
.related h2 { font-size: 13px; text-transform: uppercase; letter-spacing: 0.08em; color: var(--ink-soft); margin: 0 0 12px; }
.related ul { list-style: none; padding: 0; margin: 0; }
.related li { margin: 8px 0; }
.footer-links { display: flex; gap: 20px; margin-top: 24px; font-size: 13px; }
.footer-links a { color: var(--ink-soft); text-decoration: none; }
.footer-links a:hover { text-decoration: underline; }
.cards { list-style: none; padding: 0; margin: 32px 0 0; display: grid; gap: 16px; }
.card {
  border-radius: 20px;
  background: #fff;
  box-shadow: 0 2px 6px rgba(37, 80, 105, 0.06);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.card:hover { transform: translateY(-2px); box-shadow: 0 6px 18px rgba(37, 80, 105, 0.1); }
.card a { display: block; padding: 22px 24px; text-decoration: none; color: inherit; }
.card .card-meta { display: flex; gap: 10px; align-items: center; margin: 0 0 10px; }
.card .tag {
  font-size: 11.5px;
  font-weight: 600;
  letter-spacing: 0.04em;
  color: var(--primary-deep);
  background: var(--primary-soft);
  padding: 3px 10px;
  border-radius: 999px;
}
.card .read-min { font-size: 12px; color: var(--ink-soft); }
.card h2 { margin: 0 0 8px; font-size: 17px; line-height: 1.6; color: var(--ink); }
.card p { margin: 0; font-size: 14px; line-height: 1.8; color: var(--ink-soft); }
.card .more { display: block; margin-top: 12px; font-size: 13px; font-weight: 600; color: var(--primary-deep); }
"""

# Tips page: lighter than the LP (no orb), card-per-gesture. Tokens mirror KUUColors.
TIPS_CSS = """\
:root {
  color-scheme: light;
  --bg: #f6f9fc;
  --surface: #ffffff;
  --surface-quiet: #eff4f8;
  --ink: #353b41;
  --ink-soft: #6b737b;
  --ink-faint: #939aa2;
  --primary-deep: #5e97c2;
  --primary-soft: #dceaf4;
  --water-action: #bfddef;
  --water-ink: #255069;
  --line: #e7edf3;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  padding: 0;
  background: var(--bg);
  color: var(--ink);
  font-family: -apple-system, BlinkMacSystemFont, "Hiragino Sans", "Apple SD Gothic Neo", "PingFang SC", "Helvetica Neue", Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
  line-height: 1.7;
  font-feature-settings: "palt" 1, "kern" 1;
  font-kerning: normal;
}
.wrap { max-width: 660px; margin: 0 auto; padding: 0 24px; }

/* ---- header ---- */
.tips-hero { text-align: center; padding: clamp(40px, 8vw, 64px) 24px clamp(4px, 3vw, 14px); }
.wordmark {
  font-size: 15px;
  font-weight: 600;
  letter-spacing: 0.42em;
  color: var(--primary-deep);
  margin: 0 0 clamp(14px, 3vw, 22px) 0.42em;
}
.eyebrow {
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.24em;
  color: var(--primary-deep);
  text-transform: uppercase;
  margin: 0 0 14px;
}
.tips-hero h1 {
  font-size: clamp(26px, 6vw, 38px);
  font-weight: 600;
  line-height: 1.4;
  letter-spacing: 0.01em;
  margin: 0;
}
.tips-hero .lead { color: var(--ink-soft); font-size: clamp(15px, 4vw, 16px); max-width: 32em; margin: 16px auto 0; }

/* ---- screen sections ---- */
.screen { padding: clamp(44px, 9vw, 68px) 0 0; }
.screen h2 { font-size: clamp(20px, 5vw, 25px); font-weight: 600; line-height: 1.45; margin: 0; }
.screen .screen-lead { color: var(--ink-soft); font-size: clamp(14px, 3.8vw, 15px); margin: 10px 0 0; max-width: 32em; }
.subhead {
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.04em;
  color: var(--primary-deep);
  margin: 22px 0 0;
}
/* extra separation only when a subhead follows a previous group's cards */
.tips + .subhead { margin-top: clamp(40px, 8vw, 56px); }

/* ---- figure (annotated real screenshot) ---- */
.figure {
  display: block;
  width: 100%;
  height: auto;
  margin-top: 18px;
  border-radius: 20px;
  border: 1px solid var(--line);
  box-shadow: 0 22px 48px -28px rgba(94, 151, 194, 0.55);
  background: var(--surface);
}
.figure + .figure { margin-top: 12px; }

/* ---- tip cards ---- */
.tips { display: grid; gap: 14px; margin-top: 18px; }
.tip {
  padding: 20px 22px;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 18px;
}
.tip .thumb {
  display: block;
  width: 100%;
  height: auto;
  margin: -2px 0 14px;
  border-radius: 12px;
  border: 1px solid var(--line);
  background: var(--surface-quiet);
}
.tip .badge {
  display: inline-block;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.02em;
  color: var(--primary-deep);
  background: var(--primary-soft);
  padding: 4px 12px;
  border-radius: 999px;
  margin-bottom: 11px;
}
.tip h3 { margin: 0 0 6px; font-size: 16.5px; font-weight: 600; color: var(--ink); }
.tip p { margin: 0; color: var(--ink-soft); font-size: 14.5px; line-height: 1.72; }

/* ---- note ---- */
.note {
  margin: clamp(40px, 8vw, 64px) 0 0;
  padding: 22px 24px;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 18px;
  color: var(--ink-soft);
  font-size: clamp(15px, 4vw, 16px);
}

/* ---- FAQ (よくある問い合わせ) ---- */
.faq { padding: clamp(44px, 9vw, 68px) 0 0; }
.faq h2 { font-size: clamp(20px, 5vw, 25px); font-weight: 600; line-height: 1.45; margin: 0; }
.faq-list { display: grid; gap: 14px; margin-top: 22px; }
.faq-item {
  padding: 20px 22px;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 18px;
}
.faq-q { margin: 0 0 10px; font-size: 15.5px; font-weight: 600; color: var(--ink); line-height: 1.55; }
.faq-a { margin: 0; font-size: 14.5px; color: var(--ink-soft); line-height: 1.7; }
.faq-a + .faq-a { margin-top: 8px; }
.faq-item .thumb {
  display: block;
  width: 100%;
  height: auto;
  margin: 16px 0 0;
  border-radius: 12px;
  border: 1px solid var(--line);
  background: var(--surface-quiet);
}

/* ---- closing cta ---- */
.closing { text-align: center; padding: clamp(48px, 10vw, 80px) 0 clamp(8px, 3vw, 24px); }
.closing .sub { color: var(--ink-soft); margin: 0 0 22px; font-size: clamp(15px, 4vw, 16px); }
.cta {
  display: inline-block;
  padding: 15px 30px;
  background: var(--water-action);
  color: var(--water-ink);
  border-radius: 999px;
  text-decoration: none;
  font-weight: 600;
  font-size: 15px;
  letter-spacing: 0.02em;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.cta:hover { transform: translateY(-1px); box-shadow: 0 10px 24px -12px rgba(37, 80, 105, 0.5); }

/* ---- footer ---- */
footer {
  border-top: 1px solid var(--line);
  font-size: 13px;
  color: var(--ink-soft);
  margin-top: clamp(40px, 8vw, 72px);
  padding: 40px 0 56px;
}
.footer-row { display: flex; gap: 20px; flex-wrap: wrap; align-items: center; }
.footer-row a { color: var(--ink-soft); text-decoration: none; }
.footer-row a:hover { text-decoration: underline; }

/* ---- scroll reveal (progressive enhancement) ---- */
.js .reveal { opacity: 0; transform: translateY(20px); transition: opacity 0.7s cubic-bezier(0.22, 0.61, 0.36, 1), transform 0.7s cubic-bezier(0.22, 0.61, 0.36, 1); }
.js .reveal.in { opacity: 1; transform: none; }
.js .reveal .stagger > * { opacity: 0; transform: translateY(12px); transition: opacity 0.6s cubic-bezier(0.22, 0.61, 0.36, 1), transform 0.6s cubic-bezier(0.22, 0.61, 0.36, 1); }
.js .reveal.in .stagger > * { opacity: 1; transform: none; }
.js .reveal.in .stagger > *:nth-child(2) { transition-delay: 0.06s; }
.js .reveal.in .stagger > *:nth-child(3) { transition-delay: 0.12s; }
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  .js .reveal, .js .reveal .stagger > * { opacity: 1; transform: none; transition: none; }
}
"""

QUADRANT_VARS = ["--cat-now", "--cat-later", "--cat-parked", "--cat-release"]

# Rising bubbles inside the water orb (deterministic seeds; matches app's Bubbles).
BUBBLES_HTML = "".join(
    f'<span class="bubble" style="--bx:{bx};--bs:{bs};--bdur:{dur};--bd:{delay}"></span>'
    for bx, bs, dur, delay in [
        ("18%", "6px", "4.6s", "0s"),
        ("34%", "4px", "5.4s", "1.4s"),
        ("50%", "8px", "4.0s", "2.2s"),
        ("62%", "5px", "5.8s", "0.8s"),
        ("76%", "7px", "4.4s", "3.0s"),
        ("44%", "4px", "6.2s", "2.6s"),
    ]
)


def lang_switcher(current_locale, page="index"):
    items = []
    for code, data in LOCALES.items():
        href = "/" if not data["subdir"] else f"/{data['subdir']}/"
        if page == "support":
            href = href + "support/"
        attr = ' aria-current="true"' if code == current_locale else ""
        items.append(f'      <a href="{href}" hreflang="{data["html_lang"]}"{attr}>{data["label"]}</a>')
    return "\n".join(items)


def url_for(locale_data, page="index"):
    sub = locale_data["subdir"]
    if not sub:
        return f"{BASE_URL}/" if page == "index" else f"{BASE_URL}/{page}/"
    return f"{BASE_URL}/{sub}/" if page == "index" else f"{BASE_URL}/{sub}/{page}/"


# JSON-LD offers requires priceCurrency even for a free app.
CURRENCIES = {"ja": "JPY", "en": "USD", "es": "EUR", "ko": "KRW", "zh-Hans": "CNY",
              "zh-Hant": "TWD", "de": "EUR", "it": "EUR", "vi": "VND"}

ICON_LINKS = """\
    <link rel="icon" href="/favicon.ico" sizes="32x32" />
    <link rel="icon" type="image/png" sizes="192x192" href="/assets/favicon-192.png" />
    <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png" />"""

# Safari-only smart banner pointing to the App Store listing.
SMART_BANNER = f'    <meta name="apple-itunes-app" content="app-id={APP_STORE_ID}" />'


def ga4_snippet():
    if not GA4_MEASUREMENT_ID:
        return ""
    return f"""
    <script async src="https://www.googletagmanager.com/gtag/js?id={GA4_MEASUREMENT_ID}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag() {{ dataLayer.push(arguments); }}
      gtag('js', new Date());
      gtag('config', '{GA4_MEASUREMENT_ID}');
      // LP 唯一のゴール = App Store 遷移を計測。link_location は CTA の ct= (lp_hero/lp_footer/lp_tips)。
      // GA4 は sendBeacon で送るため同一タブ遷移でも欠落しない。capture で stopPropagation 耐性を持たせる。
      document.addEventListener('click', function (e) {{
        var a = e.target.closest && e.target.closest('a[href*="apps.apple.com"]');
        if (!a) return;
        var m = a.href.match(/[?&]ct=([^&]+)/);
        gtag('event', 'app_store_click', {{ link_location: m ? m[1] : 'other' }});
      }}, true);
    </script>"""


def hreflang_links(page="index", locales=None):
    """<link rel=alternate hreflang> cluster. x-default points to ja (site root)."""
    codes = locales or list(LOCALES)
    lines = []
    for code in codes:
        d = LOCALES[code]
        lines.append(
            f'    <link rel="alternate" hreflang="{d["html_lang"]}" href="{url_for(d, page)}" />'
        )
    lines.append(
        f'    <link rel="alternate" hreflang="x-default" href="{url_for(LOCALES["ja"], page)}" />'
    )
    return "\n".join(lines)


def app_jsonld(code, d, url):
    data = {
        "@context": "https://schema.org",
        "@type": "MobileApplication",
        "name": "KUU",
        "description": d["description"],
        "url": url,
        "image": OG_IMAGE,
        "operatingSystem": "iOS",
        "applicationCategory": "LifestyleApplication",
        "installUrl": APP_STORE_URL,
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": CURRENCIES[code]},
    }
    return (
        '    <script type="application/ld+json">\n'
        + json.dumps(data, ensure_ascii=False, indent=2)
        + "\n    </script>"
    )


def faq_jsonld(d):
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in d["faqs"]
        ],
    }
    return (
        '    <script type="application/ld+json">\n'
        + json.dumps(data, ensure_ascii=False, indent=2)
        + "\n    </script>"
    )


def index_html(code, d):
    url = url_for(d, "index")
    cta_base = app_store_cta_url(code)
    thoughts_html = "\n".join(f"        <li>{t}</li>" for t in d["thoughts"])
    steps_html = "\n".join(
        f'        <div class="step"><div class="n">{i + 1}</div>'
        f'<div><h3>{title}</h3><p>{body}</p></div></div>'
        for i, (title, body) in enumerate(d["steps"])
    )
    matrix_html = "\n".join(
        f'        <div class="q" style="--q: var({QUADRANT_VARS[i]})">'
        f"<strong>{name}</strong><span>{sub}</span></div>"
        for i, (name, sub) in enumerate(d["quadrants"])
    )
    screens_html = "\n".join(
        f'        <img class="shot" src="/assets/store/{code}/{n:02d}.png" '
        f'width="1320" height="2868" loading="lazy" alt="{d["screen_alt"]} {n}" />'
        for n in range(1, 10)
    )
    support_href = "/support/" if not d["subdir"] else f'/{d["subdir"]}/support/'
    privacy_href = "/privacy/" if code == "ja" else "/en/privacy/"
    # Tips page exists only for TIPS_LOCALES; link it from the footer where it does.
    tips_href = "/tips/" if not d["subdir"] else f'/{d["subdir"]}/tips/'
    tips_link = (
        f'<a href="{tips_href}">{d["tips_label"]}</a>\n          '
        if code in TIPS_LOCALES
        else ""
    )
    return f"""<!doctype html>
<html lang="{d["html_lang"]}">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
    <meta name="theme-color" content="#f6f9fc" />
    <meta name="robots" content="index,follow" />
    <title>{d["title"]}</title>
    <meta name="description" content="{d["description"]}" />
    <meta property="og:title" content="{d["title"]}" />
    <meta property="og:description" content="{d["description"]}" />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="{url}" />
    <meta property="og:locale" content="{d["og_locale"]}" />
    <meta property="og:image" content="{OG_IMAGE}" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{d["title"]}" />
    <meta name="twitter:description" content="{d["description"]}" />
    <meta name="twitter:image" content="{OG_IMAGE}" />
    <link rel="canonical" href="{url}" />
{hreflang_links("index")}
{ICON_LINKS}
{SMART_BANNER}
{app_jsonld(code, d, url)}{ga4_snippet()}
    <style>
{BASE_CSS}    </style>
  </head>
  <body>
    <header class="hero">
      <p class="wordmark">KUU</p>
      <h1>{d["hero_headline"]}</h1>
      <p class="sub">{d["hero_sub"]}</p>
      <div class="orb" aria-hidden="true"><div class="orb__water"></div><div class="orb__bubbles">{BUBBLES_HTML}</div></div>
      <a class="cta" href="{cta_base}?ct=lp_hero" rel="noopener">{d["cta"]}</a>
      <div class="scroll-cue" aria-hidden="true">{d["scroll_cue"]}</div>
    </header>

    <main>
      <section class="why">
        <div class="wrap reveal">
          <p class="eyebrow">{d["why_eyebrow"]}</p>
          <h2>{d["why_headline"]}</h2>
          <p class="scenario">{d["why_scenario"]}</p>
          <p class="lead">{d["why_lead"]}</p>
          <ul class="thoughts stagger">
{thoughts_html}
          </ul>
          <p class="note">{d["why_note"]}</p>
        </div>
      </section>

      <section class="how">
        <div class="wrap reveal">
          <p class="eyebrow">{d["steps_eyebrow"]}</p>
          <h2>{d["steps_headline"]}</h2>
          <div class="steps stagger">
{steps_html}
          </div>
        </div>
      </section>

      <section class="app reveal">
        <div class="wrap">
          <p class="eyebrow">{d["app_eyebrow"]}</p>
          <h2>{d["app_headline"]}</h2>
        </div>
        <div class="showcase stagger" aria-label="{d["app_eyebrow"]}">
{screens_html}
        </div>
      </section>

      <section class="matrix-section">
        <div class="wrap reveal">
          <p class="eyebrow">{d["matrix_eyebrow"]}</p>
          <h2>{d["matrix_headline"]}</h2>
          <p class="lead">{d["matrix_lead"]}</p>
          <div class="matrix stagger" aria-label="{d["quadrants_aria"]}">
{matrix_html}
          </div>
        </div>
      </section>

      <section class="privacy">
        <div class="wrap reveal">
          <p class="eyebrow">{d["privacy_eyebrow"]}</p>
          <h2>{d["privacy_headline"]}</h2>
          <p class="lead">{d["privacy_body"]}</p>
        </div>
      </section>

      <section class="closing">
        <div class="wrap reveal">
          <h2>{d["closing_headline"]}</h2>
          <p class="sub">{d["closing_sub"]}</p>
          <a class="cta" href="{cta_base}?ct=lp_footer" rel="noopener">{d["cta"]}</a>
        </div>
      </section>
    </main>

    <footer>
      <div class="wrap">
        <div class="footer-row">
          {tips_link}<a href="{support_href}">{d["support_label"]}</a>
          <a href="{privacy_href}">{d["privacy_label"]}</a>
          <span>© KUU</span>
        </div>
        <nav class="langs" aria-label="{d["lang_switcher_aria"]}">
{lang_switcher(code, 'index')}
        </nav>
      </div>
    </footer>
{REVEAL_SCRIPT}{DRAG_SCROLL_SCRIPT}  </body>
</html>
"""


def support_html(code, d):
    url = url_for(d, "support")
    home_href = "/" if not d["subdir"] else f"/{d['subdir']}/"
    faqs_html = "\n".join(
        f'      <p>\n        <strong>{q}</strong><br />\n        {a}\n      </p>'
        for q, a in d["faqs"]
    )
    tips_href = "/tips/" if not d["subdir"] else f'/{d["subdir"]}/tips/'
    tips_prompt = (
        f'\n      <p>{d["tips_support_before"]} '
        f'<a href="{tips_href}">{d["tips_label"]}</a>{d["tips_support_after"]}</p>'
        if code in TIPS_LOCALES
        else ""
    )
    return f"""<!doctype html>
<html lang="{d["html_lang"]}">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
    <title>{d["support_title"]}</title>
    <meta name="description" content="{d["support_description"]}" />
    <link rel="canonical" href="{url}" />
    <meta property="og:locale" content="{d["og_locale"]}" />
{hreflang_links("support")}
{ICON_LINKS}
{SMART_BANNER}
{faq_jsonld(d)}{ga4_snippet()}
    <style>
{SUPPORT_CSS}    </style>
  </head>
  <body>
    <main>
      <h1>{d["support_h1"]}</h1>
      <p>{d["support_intro"]}</p>{tips_prompt}

      <h2>{d["contact_h2"]}</h2>
      <p>{d["contact_body"]}</p>

      <h2>{d["faq_h2"]}</h2>
{faqs_html}

      <a class="back" href="{home_href}">{d["back"]}</a>

      <nav class="langs" aria-label="{d["lang_switcher_aria"]}">
{lang_switcher(code, 'support')}
      </nav>
    </main>
  </body>
</html>
"""


def tips_jsonld(d):
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": "".join(a)},
            }
            for q, a, *_ in d["tips_faqs"]
        ],
    }
    return (
        '    <script type="application/ld+json">\n'
        + json.dumps(data, ensure_ascii=False, indent=2)
        + "\n    </script>"
    )


def tips_html(code, d):
    url = url_for(d, "tips")
    cta_base = app_store_cta_url(code)
    home_href = "/" if not d["subdir"] else f"/{d['subdir']}/"
    support_href = "/support/" if not d["subdir"] else f"/{d['subdir']}/support/"
    privacy_href = "/privacy/" if code == "ja" else "/en/privacy/"
    def card(it):
        badge, title, body = it[0], it[1], it[2]
        thumb = it[3] if len(it) > 3 else ""
        if thumb in VIDEO_THUMBS:
            media = (
                f'<video class="thumb" autoplay loop muted playsinline preload="metadata" '
                f'width="860" height="798" '
                f'poster="{tips_asset(code, thumb + "_poster", "jpg")}">'
                f'<source src="{tips_asset(code, thumb, "mp4")}" type="video/mp4" />'
                f"</video>"
            )
        elif thumb:
            media = (
                f'<img class="thumb" src="{tips_asset(code, thumb, "png")}" '
                f'width="900" height="562" loading="lazy" alt="" />'
            )
        else:
            media = ""
        return (
            f'            <div class="tip">{media}<span class="badge">{badge}</span>'
            f"<h3>{title}</h3><p>{body}</p></div>"
        )

    def render_group(g):
        parts = []
        if g.get("subhead"):
            parts.append(f'          <p class="subhead">{g["subhead"]}</p>')
        for name, alt in g.get("figures", []):
            parts.append(
                f'          <img class="figure" src="/assets/tips/{name}.png?v={ASSET_VERSION}" '
                f'width="1000" height="1029" loading="lazy" alt="{alt}" />'
            )
        cards = "\n".join(card(it) for it in g["items"])
        parts.append(f'          <div class="tips stagger">\n{cards}\n          </div>')
        return "\n".join(parts)

    screens = []
    for s in d["tips_screens"]:
        body = "\n".join(render_group(g) for g in s["groups"])
        screens.append(
            '      <section class="screen reveal">\n'
            "        <div class=\"wrap\">\n"
            f"          <h2>{s['heading']}</h2>\n"
            f"          <p class=\"screen-lead\">{s['lead']}</p>\n"
            f"{body}\n"
            "        </div>\n"
            "      </section>"
        )
    groups_block = "\n\n".join(screens)

    def faq_item(item):
        q, lines = item[0], item[1]
        thumb = item[2] if len(item) > 2 else ""
        answer = "".join(f'<p class="faq-a">{line}</p>' for line in lines)
        thumb_html = (
            f'<img class="thumb" src="{tips_asset(code, thumb, "png")}" '
            f'width="900" height="562" loading="lazy" alt="" />'
            if thumb
            else ""
        )
        return (
            f'            <div class="faq-item"><p class="faq-q">{q}</p>'
            f"{answer}{thumb_html}</div>"
        )

    faq_items = "\n".join(faq_item(it) for it in d["tips_faqs"])
    faq_block = (
        '      <section class="faq reveal">\n'
        "        <div class=\"wrap\">\n"
        f"          <h2>{d['tips_faq_heading']}</h2>\n"
        f'          <div class="faq-list stagger">\n{faq_items}\n          </div>\n'
        "        </div>\n"
        "      </section>"
    )
    return f"""<!doctype html>
<html lang="{d["html_lang"]}">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
    <meta name="theme-color" content="#f6f9fc" />
    <meta name="robots" content="index,follow" />
    <title>{d["tips_title"]}</title>
    <meta name="description" content="{d["tips_description"]}" />
    <meta property="og:title" content="{d["tips_title"]}" />
    <meta property="og:description" content="{d["tips_description"]}" />
    <meta property="og:type" content="article" />
    <meta property="og:url" content="{url}" />
    <meta property="og:locale" content="{d["og_locale"]}" />
    <meta property="og:image" content="{OG_IMAGE}" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{d["tips_title"]}" />
    <meta name="twitter:description" content="{d["tips_description"]}" />
    <meta name="twitter:image" content="{OG_IMAGE}" />
    <link rel="canonical" href="{url}" />
{hreflang_links("tips", locales=TIPS_LOCALES)}
{ICON_LINKS}
{SMART_BANNER}
{tips_jsonld(d)}{ga4_snippet()}
    <style>
{TIPS_CSS}    </style>
  </head>
  <body>
    <header class="tips-hero">
      <p class="wordmark">KUU</p>
      <p class="eyebrow">{d["tips_eyebrow"]}</p>
      <h1>{d["tips_h1"]}</h1>
      <p class="lead">{d["tips_lead"]}</p>
    </header>

    <main>
{groups_block}

{faq_block}

      <section class="closing-note reveal">
        <div class="wrap">
          <p class="note">{d["tips_note"]}</p>
        </div>
      </section>

      <section class="closing reveal">
        <div class="wrap">
          <p class="sub">{d["tips_closing_sub"]}</p>
          <a class="cta" href="{cta_base}?ct=lp_tips" rel="noopener">{d["cta"]}</a>
        </div>
      </section>
    </main>

    <footer>
      <div class="wrap">
        <div class="footer-row">
          <a href="{home_href}">{d["back"]}</a>
          <a href="{support_href}">{d["support_label"]}</a>
          <a href="{privacy_href}">{d["privacy_label"]}</a>
          <span>© KUU</span>
        </div>
      </div>
    </footer>
{TIPS_REVEAL_SCRIPT}  </body>
</html>
"""


PRIVACY_META = {
    "ja": {
        "title": "プライバシーポリシー — KUU",
        "description": "KUU のプライバシーポリシー。音声はすべて端末内で処理し外部に送信しません。整理の AI 分類は既定で文字だけを送信し保存しません（設定で端末内のみにもできます）。",
    },
    "en": {
        "title": "Privacy Policy — KUU",
        "description": "KUU's privacy policy. Audio is processed entirely on device and never sent outside. AI organization sends only the text by default, and the AI provider does not retain it (you can switch to on-device only in Settings).",
    },
}


def md_inline(s):
    s = html_mod.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2" rel="noopener">\1</a>', s)
    return s


def md_to_html(md):
    """Minimal converter for content/privacy.md (h1/h2, hr, p, ul/ol with one nest level)."""
    out = []
    para = []
    # stack of open list tags, innermost last; index = nest depth
    lists = []

    def flush_para():
        if para:
            out.append("      <p>" + md_inline(" ".join(para)) + "</p>")
            para.clear()

    def close_lists(depth=0):
        while len(lists) > depth:
            out.append("      " + "</li></%s>" % lists.pop())

    for line in md.splitlines():
        stripped = line.strip()
        if not stripped:
            flush_para()
            close_lists()
            continue
        if stripped == "---":
            flush_para()
            close_lists()
            out.append("      <hr />")
            continue
        if stripped.startswith("## "):
            flush_para()
            close_lists()
            out.append("      <h2>" + md_inline(stripped[3:]) + "</h2>")
            continue
        if stripped.startswith("# "):
            flush_para()
            close_lists()
            out.append("      <h1>" + md_inline(stripped[2:]) + "</h1>")
            continue
        m = re.match(r"^(\s*)(-|\d+\.)\s+(.*)$", line)
        if m:
            flush_para()
            depth = 1 if m.group(1) else 0
            tag = "ul" if m.group(2) == "-" else "ol"
            if len(lists) <= depth:
                out.append("      " + f"<{tag}>")
                lists.append(tag)
            else:
                close_lists(depth + 1)
                out.append("      </li>")
            out.append("      <li>" + md_inline(m.group(3)))
            continue
        para.append(stripped)
    flush_para()
    close_lists()
    return "\n".join(out)


PRIVACY_CSS = SUPPORT_CSS + """\
main { max-width: 720px; }
h1 { font-size: 26px; }
h2 { font-size: 17px; }
li { line-height: 1.7; color: var(--ink-soft); margin: 4px 0; }
hr { border: 0; border-top: 1px solid var(--line); margin: 32px 0; }
code { font-size: 0.9em; background: #eff4f8; padding: 1px 5px; border-radius: 4px; }
"""


def privacy_html(code, body_html):
    d = LOCALES[code]
    meta = PRIVACY_META[code]
    url = url_for(d, "privacy")
    home_href = "/" if not d["subdir"] else f"/{d['subdir']}/"
    langs = []
    for c in PRIVACY_LOCALES:
        ld = LOCALES[c]
        href = "/privacy/" if c == "ja" else f"/{ld['subdir']}/privacy/"
        attr = ' aria-current="true"' if c == code else ""
        langs.append(f'      <a href="{href}" hreflang="{ld["html_lang"]}"{attr}>{ld["label"]}</a>')
    return f"""<!doctype html>
<html lang="{d["html_lang"]}">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
    <title>{meta["title"]}</title>
    <meta name="description" content="{meta["description"]}" />
    <link rel="canonical" href="{url}" />
    <meta property="og:locale" content="{d["og_locale"]}" />
{hreflang_links("privacy", locales=PRIVACY_LOCALES)}
{ICON_LINKS}{ga4_snippet()}
    <style>
{PRIVACY_CSS}    </style>
  </head>
  <body>
    <main>
{body_html}

      <a class="back" href="{home_href}">{d["back"]}</a>

      <nav class="langs" aria-label="{d["lang_switcher_aria"]}">
{chr(10).join(langs)}
      </nav>
    </main>
  </body>
</html>
"""


def split_privacy_md():
    """content/privacy.md holds ja then en, separated by the en h1."""
    md = (ROOT / "content" / "privacy.md").read_text()
    marker = "# Privacy Policy for KUU"
    ja_md, en_md = md.split(marker, 1)
    # drop the trailing hr that separated the two documents
    ja_md = re.sub(r"-{3,}\s*$", "", ja_md.rstrip())
    return {"ja": ja_md, "en": marker + en_md}


# content/<lang>/journal/<slug>.md: YAML front matter + Markdown body.
FRONT_MATTER_RE = re.compile(r"\A---\n(.*?)\n---\n(.*)\Z", re.DOTALL)


ARCHETYPE_LABELS = {"pain": "悩み", "method": "方法", "scene": "場面"}


def parse_article_md(path):
    raw = path.read_text()
    m = FRONT_MATTER_RE.match(raw)
    if not m:
        raise ValueError(f"{path}: missing YAML front matter (--- ... ---)")
    meta = yaml.safe_load(m.group(1)) or {}
    body_md = m.group(2).strip()
    meta["body_html"] = md_lib.markdown(body_md, extensions=["extra", "sane_lists"])
    # 読了時間: 日本語 ~550字/分。記号込みの概算で十分
    plain = re.sub(r"[#*>\-\[\]()`|]", "", body_md)
    meta["read_min"] = max(1, round(len(plain) / 550))
    return meta


def load_articles():
    """content/<lang>/journal/*.md -> {locale: [article_dict, ...]}, newest first."""
    articles = {}
    for code in JOURNAL_LOCALES:
        journal_dir = ROOT / "content" / code / "journal"
        items = [parse_article_md(p) for p in sorted(journal_dir.glob("*.md"))] if journal_dir.exists() else []
        # hub 記事（他記事の親、spokes を持つ）を先頭に固定し、以降は新しい順
        items.sort(key=lambda a: (bool(a.get("spokes")), str(a["updated"])), reverse=True)
        articles[code] = items
    return articles


def article_jsonld(code, d, meta, url):
    home_url = url_for(d, "index")
    hub_url = url_for(d, "journal")
    article = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": meta["title"],
        "description": meta["description"],
        "url": url,
        "image": OG_IMAGE,
        "datePublished": str(meta["updated"]),
        "dateModified": str(meta["updated"]),
        "inLanguage": d["html_lang"],
        "author": {"@type": "Organization", "name": "KUU", "url": BASE_URL},
        "publisher": {"@type": "Organization", "name": "KUU", "url": BASE_URL},
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
    }
    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": d["title"], "item": home_url},
            {"@type": "ListItem", "position": 2, "name": d["journal_hub_title"], "item": hub_url},
            {"@type": "ListItem", "position": 3, "name": meta["title"], "item": url},
        ],
    }
    return (
        '    <script type="application/ld+json">\n'
        + json.dumps(article, ensure_ascii=False, indent=2)
        + "\n    </script>\n"
        '    <script type="application/ld+json">\n'
        + json.dumps(breadcrumb, ensure_ascii=False, indent=2)
        + "\n    </script>"
    )


def article_html(code, meta, articles_by_slug):
    d = LOCALES[code]
    slug = meta["slug"]
    url = url_for(d, f"journal/{slug}")
    cta_base = app_store_cta_url(code)
    home_href = "/" if not d["subdir"] else f"/{d['subdir']}/"
    journal_href = home_href + "journal/"
    support_href = home_href + "support/"
    privacy_href = "/privacy/" if code == "ja" else "/en/privacy/"

    related = []
    hub_slug = meta.get("hub")
    if hub_slug and hub_slug != slug and hub_slug in articles_by_slug:
        related.append((hub_slug, articles_by_slug[hub_slug]["title"]))
    for s in meta.get("spokes") or []:
        if s in articles_by_slug and s != slug:
            related.append((s, articles_by_slug[s]["title"]))
    related_html = ""
    if related:
        items = "\n".join(
            f'          <li><a href="{journal_href}{s}/">{t}</a></li>' for s, t in related
        )
        related_html = f"""
      <nav class="related" aria-label="{d['journal_related_label']}">
        <h2>{d["journal_related_label"]}</h2>
        <ul>
{items}
        </ul>
      </nav>"""

    pitch_shots_html = "\n".join(
        f'          <img class="pitch-shot" src="/assets/store/{code}/{n:02d}.png" '
        f'width="1320" height="2868" loading="lazy" alt="{d["screen_alt"]} {n}" />'
        for n in range(1, 10)
    )

    return f"""<!doctype html>
<html lang="{d["html_lang"]}">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
    <meta name="theme-color" content="#f6f9fc" />
    <meta name="robots" content="index,follow" />
    <title>{meta["title"]} — KUU</title>
    <meta name="description" content="{meta["description"]}" />
    <meta property="og:title" content="{meta["title"]}" />
    <meta property="og:description" content="{meta["description"]}" />
    <meta property="og:type" content="article" />
    <meta property="og:url" content="{url}" />
    <meta property="og:locale" content="{d["og_locale"]}" />
    <meta property="og:image" content="{OG_IMAGE}" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{meta["title"]}" />
    <meta name="twitter:description" content="{meta["description"]}" />
    <meta name="twitter:image" content="{OG_IMAGE}" />
    <link rel="canonical" href="{url}" />
{hreflang_links(f"journal/{slug}", locales=list(JOURNAL_LOCALES))}
{ICON_LINKS}
{SMART_BANNER}
{article_jsonld(code, d, meta, url)}{ga4_snippet()}
    <style>
{JOURNAL_CSS}    </style>
  </head>
  <body>
    <main>
      <p class="eyebrow">{d["journal_eyebrow"]}</p>
      <article>
        <h1>{meta["title"]}</h1>
        <div class="updated"><span>{d["journal_updated_label"]} {meta["updated"]}</span><span>約{meta["read_min"]}分で読めます</span></div>
{meta["body_html"]}
      </article>

      <div class="kuu-pitch">
        <div class="pitch-shots" aria-label="{d["app_eyebrow"]}">
{pitch_shots_html}
        </div>
        <p class="rating">★ {APP_RATING["score"]}<span class="rating-count"> ・ {APP_RATING["count"]}{d["journal_rating_suffix"]}</span></p>
        <h2>{d["journal_pitch_headline"]}</h2>
        <p>{d["journal_pitch_body"]}</p>
        <a class="cta" href="{cta_base}?ct=journal_{slug}" rel="noopener">{d["cta"]}</a>
        <p class="note">{d["journal_pitch_note"]}</p>
      </div>
{related_html}

      <a class="back" href="{journal_href}">{d["journal_back_label"]}</a>

      <nav class="footer-links" aria-label="{d['lang_switcher_aria']}">
        <a href="{support_href}">{d["support_label"]}</a>
        <a href="{privacy_href}">{d["privacy_label"]}</a>
      </nav>
    </main>
{DRAG_SCROLL_SCRIPT}  </body>
</html>
"""


def journal_index_html(code, items):
    d = LOCALES[code]
    url = url_for(d, "journal")
    home_href = "/" if not d["subdir"] else f"/{d['subdir']}/"
    journal_href = home_href + "journal/"
    cards = "\n".join(
        f'''        <li class="card">
          <a href="{journal_href}{a["slug"]}/">
            <p class="card-meta"><span class="tag">{ARCHETYPE_LABELS.get(a.get("archetype"), "読みもの")}</span><span class="read-min">約{a["read_min"]}分</span></p>
            <h2>{a["title"]}</h2>
            <p>{a["description"]}</p>
            <span class="more">読む →</span>
          </a>
        </li>'''
        for a in items
    )
    return f"""<!doctype html>
<html lang="{d["html_lang"]}">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
    <meta name="theme-color" content="#f6f9fc" />
    <meta name="robots" content="index,follow" />
    <title>{d["journal_hub_title"]}</title>
    <meta name="description" content="{d["journal_hub_description"]}" />
    <meta property="og:title" content="{d["journal_hub_title"]}" />
    <meta property="og:description" content="{d["journal_hub_description"]}" />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="{url}" />
    <meta property="og:locale" content="{d["og_locale"]}" />
    <meta property="og:image" content="{OG_IMAGE}" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{d["journal_hub_title"]}" />
    <meta name="twitter:description" content="{d["journal_hub_description"]}" />
    <meta name="twitter:image" content="{OG_IMAGE}" />
    <link rel="canonical" href="{url}" />
{hreflang_links("journal", locales=list(JOURNAL_LOCALES))}
{ICON_LINKS}
{SMART_BANNER}{ga4_snippet()}
    <style>
{JOURNAL_CSS}    </style>
  </head>
  <body>
    <main>
      <p class="eyebrow">KUU</p>
      <h1>{d["journal_hub_title"]}</h1>
      <p class="lead">{d["journal_hub_lead"]}</p>
      <ul class="cards">
{cards}
      </ul>

      <a class="back" href="{home_href}">{d["back"]}</a>
    </main>
  </body>
</html>
"""


def sitemap_xml(articles_by_locale=None):
    clusters = [
        ("index", list(LOCALES)),
        ("support", list(LOCALES)),
        ("tips", list(TIPS_LOCALES)),
        ("privacy", list(PRIVACY_LOCALES)),
    ]
    urls = []
    for page, codes in clusters:
        alts = "".join(
            f'\n    <xhtml:link rel="alternate" hreflang="{LOCALES[c]["html_lang"]}" href="{url_for(LOCALES[c], page)}" />'
            for c in codes
        )
        alts += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{url_for(LOCALES["ja"], page)}" />'
        for c in codes:
            urls.append(f"  <url>\n    <loc>{url_for(LOCALES[c], page)}</loc>{alts}\n  </url>")

    articles_by_locale = articles_by_locale or {}
    if any(articles_by_locale.values()):
        hub_alts = "".join(
            f'\n    <xhtml:link rel="alternate" hreflang="{LOCALES[c]["html_lang"]}" href="{url_for(LOCALES[c], "journal")}" />'
            for c in JOURNAL_LOCALES
        )
        hub_alts += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{url_for(LOCALES["ja"], "journal")}" />'
        for c in JOURNAL_LOCALES:
            urls.append(f"  <url>\n    <loc>{url_for(LOCALES[c], 'journal')}</loc>{hub_alts}\n  </url>")
        for c in JOURNAL_LOCALES:
            for a in articles_by_locale[c]:
                page = f"journal/{a['slug']}"
                alts = "".join(
                    f'\n    <xhtml:link rel="alternate" hreflang="{LOCALES[cc]["html_lang"]}" href="{url_for(LOCALES[cc], page)}" />'
                    for cc in JOURNAL_LOCALES
                )
                alts += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{url_for(LOCALES["ja"], page)}" />'
                urls.append(
                    f"  <url>\n    <loc>{url_for(LOCALES[c], page)}</loc>{alts}"
                    f"\n    <lastmod>{a['updated']}</lastmod>\n  </url>"
                )

    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )


ROBOTS_TXT = f"""User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""


def main():
    # 未翻訳キーは英語にフォールバックする（国際的な既定として ja より en を優先。
    # 非日本語ユーザーには日本語より英語のほうが読める）。en が持たないキー
    # （journal_* 等 ja 専用）だけ ja で補う。ja は canonical なので全キーを持つ。
    ja = LOCALES["ja"]
    en = LOCALES["en"]
    for code, d in LOCALES.items():
        for key in ja:
            if key not in d:
                d[key] = en.get(key, ja[key])

    written = []
    for code, d in LOCALES.items():
        sub = d["subdir"]
        base = ROOT / sub if sub else ROOT
        (base / "support").mkdir(parents=True, exist_ok=True)
        idx = base / "index.html"
        sup = base / "support" / "index.html"
        idx.write_text(index_html(code, d))
        sup.write_text(support_html(code, d))
        written.append(str(idx.relative_to(ROOT)))
        written.append(str(sup.relative_to(ROOT)))

    for code in TIPS_LOCALES:
        sub = LOCALES[code]["subdir"]
        base = ROOT / sub if sub else ROOT
        (base / "tips").mkdir(parents=True, exist_ok=True)
        page = base / "tips" / "index.html"
        page.write_text(tips_html(code, LOCALES[code]))
        written.append(str(page.relative_to(ROOT)))

    privacy_md = split_privacy_md()
    for code in PRIVACY_LOCALES:
        sub = LOCALES[code]["subdir"]
        base = ROOT / sub if sub else ROOT
        (base / "privacy").mkdir(parents=True, exist_ok=True)
        page = base / "privacy" / "index.html"
        page.write_text(privacy_html(code, md_to_html(privacy_md[code])))
        written.append(str(page.relative_to(ROOT)))

    articles_by_locale = load_articles()
    for code in JOURNAL_LOCALES:
        items = articles_by_locale[code]
        by_slug = {a["slug"]: a for a in items}
        sub = LOCALES[code]["subdir"]
        base = ROOT / sub if sub else ROOT
        journal_dir = base / "journal"
        for a in items:
            art_dir = journal_dir / a["slug"]
            art_dir.mkdir(parents=True, exist_ok=True)
            page = art_dir / "index.html"
            page.write_text(article_html(code, a, by_slug))
            written.append(str(page.relative_to(ROOT)))
        journal_dir.mkdir(parents=True, exist_ok=True)
        hub_page = journal_dir / "index.html"
        hub_page.write_text(journal_index_html(code, items))
        written.append(str(hub_page.relative_to(ROOT)))

    (ROOT / "sitemap.xml").write_text(sitemap_xml(articles_by_locale))
    (ROOT / "robots.txt").write_text(ROBOTS_TXT)
    written += ["sitemap.xml", "robots.txt"]

    for path in written:
        print(path)


if __name__ == "__main__":
    main()
