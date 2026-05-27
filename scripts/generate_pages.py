"""Generate per-locale LP and support pages for kuu-site.

Source of truth for translations:
- KUU/Localizable.xcstrings (4 quadrant labels)
- KUU/fastlane/metadata/<locale>/*.txt (tone)

Output:
- /index.html, /support/index.html  (ja, at root)
- /<locale>/index.html, /<locale>/support/index.html  for en, es, ko, zh-Hans
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRIVACY_URL = "https://aerial-dogsled-ede.notion.site/KUU-3667869259cf80b59f50fdfe039b1f7b"

LOCALES = {
    "ja": {
        "subdir": "",
        "html_lang": "ja",
        "og_locale": "ja_JP",
        "label": "日本語",
        "title": "KUU — 頭の中を整える、静かなブレインダンプ",
        "description": "KUU は、頭の中を口に出すだけで「いま見る / あとで考える / 寝かせる / 手放す」に整える、静かなブレインダンプアプリです。",
        "tagline_html": "頭の中を口に出すだけ。<br />AI が、いま見る / あとで考える / 寝かせる / 手放す に静かに分けてくれます。",
        "quadrants": [
            ("いま見る", "今日ふれるもの"),
            ("あとで考える", "時間ができたら"),
            ("寝かせる", "急がない"),
            ("手放す", "気にしなくていい"),
        ],
        "quadrants_aria": "KUU マトリクス",
        "cta": "App Store 近日公開",
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
                "いいえ。KUU は音声を端末から外に出さず、認識が完了したら一時音声ファイルを削除します。残るのは文字起こしと分類結果のみです。",
            ),
            (
                "iCloud 同期は？",
                "iCloud Private DB に同期されます (Apple ID 所有者本人のみアクセス可)。開発者サーバーはありません。",
            ),
        ],
        "back": "← トップへ",
    },
    "en": {
        "subdir": "en",
        "html_lang": "en",
        "og_locale": "en_US",
        "label": "English",
        "title": "KUU — A quiet brain-dump for busy minds",
        "description": "KUU is a quiet voice-first brain-dump app. Speak what is on your mind; KUU sorts it into Now, Later, Park, and Release.",
        "tagline_html": "Speak what is on your mind.<br />KUU quietly sorts it into Now, Later, Park, and Release.",
        "quadrants": [
            ("Now", "For today"),
            ("Later", "When you have time"),
            ("Park", "No rush"),
            ("Release", "Let it go"),
        ],
        "quadrants_aria": "KUU matrix",
        "cta": "Coming soon to the App Store",
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
                "No. KUU does not send audio off the device, and temporary audio files are deleted once transcription completes. Only the transcript and classification result are kept.",
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
        "html_lang": "es",
        "og_locale": "es_ES",
        "label": "Español",
        "title": "KUU — Un volcado mental tranquilo para mentes ocupadas",
        "description": "KUU es una app silenciosa para vaciar la mente. Habla lo que tienes; KUU lo separa en Ahora, Luego, Aparcar y Soltar.",
        "tagline_html": "Habla lo que tienes en mente.<br />KUU lo separa con calma en Ahora, Luego, Aparcar y Soltar.",
        "quadrants": [
            ("Ahora", "Para hoy"),
            ("Luego", "Cuando tengas tiempo"),
            ("Aparcar", "Sin prisa"),
            ("Soltar", "Déjalo ir"),
        ],
        "quadrants_aria": "Matriz KUU",
        "cta": "Próximamente en el App Store",
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
                "No. KUU no envía el audio fuera del dispositivo y elimina los archivos de audio temporales una vez completada la transcripción. Solo se conservan la transcripción y la clasificación.",
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
        "html_lang": "ko",
        "og_locale": "ko_KR",
        "label": "한국어",
        "title": "KUU — 바쁜 머리를 조용히 비우는 브레인덤프",
        "description": "KUU는 조용한 음성 브레인덤프 앱입니다. 마음에 있는 것을 말하세요. KUU가 지금 보기, 나중에 생각, 묵히기, 놓아주기로 나눠줍니다.",
        "tagline_html": "마음에 있는 것을 그대로 말해 보세요.<br />KUU가 조용히 지금 보기, 나중에 생각, 묵히기, 놓아주기로 나눠줍니다.",
        "quadrants": [
            ("지금 보기", "오늘 다룰 것"),
            ("나중에 생각", "시간이 생기면"),
            ("묵히기", "서두르지 않아도"),
            ("놓아주기", "마음에서 내려놓아도 돼요"),
        ],
        "quadrants_aria": "KUU 매트릭스",
        "cta": "곧 App Store 출시 예정",
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
                "아닙니다. KUU는 음성을 기기 밖으로 보내지 않으며, 인식이 완료되면 임시 음성 파일을 즉시 삭제합니다. 텍스트와 분류 결과만 남습니다.",
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
        "html_lang": "zh-Hans",
        "og_locale": "zh_CN",
        "label": "简体中文",
        "title": "KUU — 让忙碌的脑袋安静下来的脑内倾倒",
        "description": "KUU 是一款安静的语音脑内倾倒应用。说出心中所想，KUU 会分到现在看、之后想、搁置、放下。",
        "tagline_html": "把脑中所想说出来。<br />KUU 会安静地分到现在看、之后想、搁置、放下。",
        "quadrants": [
            ("现在看", "今天看的"),
            ("之后想", "有时间再想"),
            ("搁置", "不急"),
            ("放下", "不用挂在心上"),
        ],
        "quadrants_aria": "KUU 矩阵",
        "cta": "即将在 App Store 上线",
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
                "不会。KUU 不会将音频传输到设备外,识别完成后会立即删除临时音频文件。仅保留转录结果和分类结果。",
            ),
            (
                "是否通过 iCloud 同步?",
                "是的。笔记会同步到只有您本人可访问的 iCloud 私有数据库。我们没有任何开发者服务器。",
            ),
        ],
        "back": "← 返回顶部",
    },
}

BASE_CSS = """\
:root {
  color-scheme: light;
  --bg: #f7faff;
  --ink: #1e2530;
  --ink-soft: #4f5b6b;
  --accent: #6c8fb5;
  --card: #ffffff;
  --line: #e4ecf4;
}
* { box-sizing: border-box; }
html, body {
  margin: 0;
  padding: 0;
  background: var(--bg);
  color: var(--ink);
  font-family: -apple-system, BlinkMacSystemFont, "Hiragino Sans", "Apple SD Gothic Neo", "PingFang SC", "Helvetica Neue", Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
}
main {
  max-width: 640px;
  margin: 0 auto;
  padding: clamp(56px, 12vw, 120px) 24px 80px;
}
h1 {
  font-size: clamp(32px, 6vw, 44px);
  font-weight: 600;
  letter-spacing: 0.02em;
  margin: 0 0 12px;
}
.tagline {
  color: var(--ink-soft);
  font-size: 17px;
  line-height: 1.7;
  margin: 0 0 40px;
}
.quadrants {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 20px;
  padding: 24px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin-bottom: 40px;
}
.q { font-size: 14px; color: var(--ink-soft); line-height: 1.6; }
.q strong { display: block; color: var(--ink); font-size: 15px; font-weight: 600; margin-bottom: 4px; }
.cta {
  display: inline-block;
  padding: 14px 28px;
  background: var(--ink);
  color: #fff;
  border-radius: 999px;
  text-decoration: none;
  font-weight: 500;
  font-size: 15px;
}
.cta[aria-disabled="true"] {
  background: var(--line);
  color: var(--ink-soft);
  pointer-events: none;
}
footer {
  margin-top: 64px;
  padding-top: 24px;
  border-top: 1px solid var(--line);
  font-size: 13px;
  color: var(--ink-soft);
}
.footer-row {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
  align-items: center;
  margin-bottom: 12px;
}
.footer-row a { color: var(--ink-soft); text-decoration: none; }
.footer-row a:hover { text-decoration: underline; }
.langs {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
  font-size: 12px;
  padding-top: 12px;
  border-top: 1px dashed var(--line);
}
.langs a { color: var(--ink-soft); text-decoration: none; }
.langs a[aria-current="true"] { color: var(--ink); font-weight: 600; }
.langs a:hover { text-decoration: underline; }
"""

SUPPORT_CSS = """\
:root {
  color-scheme: light;
  --bg: #f7faff;
  --ink: #1e2530;
  --ink-soft: #4f5b6b;
  --line: #e4ecf4;
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
    base = "https://kuu-zen.com"
    if not sub:
        return f"{base}/" if page == "index" else f"{base}/support/"
    return f"{base}/{sub}/" if page == "index" else f"{base}/{sub}/support/"


def index_html(code, d):
    url = url_for(d, "index")
    quadrants_html = "\n".join(
        f'        <div class="q"><strong>{name}</strong>{sub}</div>'
        for name, sub in d["quadrants"]
    )
    return f"""<!doctype html>
<html lang="{d["html_lang"]}">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
    <meta name="theme-color" content="#f7faff" />
    <meta name="robots" content="index,follow" />
    <title>{d["title"]}</title>
    <meta name="description" content="{d["description"]}" />
    <meta property="og:title" content="{d["title"]}" />
    <meta property="og:description" content="{d["description"]}" />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="{url}" />
    <meta property="og:locale" content="{d["og_locale"]}" />
    <link rel="canonical" href="{url}" />
    <style>
{BASE_CSS}    </style>
  </head>
  <body>
    <main>
      <h1>KUU</h1>
      <p class="tagline">
        {d["tagline_html"]}
      </p>

      <section class="quadrants" aria-label="{d["quadrants_aria"]}">
{quadrants_html}
      </section>

      <a class="cta" aria-disabled="true" href="#">{d["cta"]}</a>

      <footer>
        <div class="footer-row">
          <a href="{('/' if not d['subdir'] else f'/{d["subdir"]}/')}support/">{d["support_label"]}</a>
          <a href="{PRIVACY_URL}" rel="noopener" target="_blank">{d["privacy_label"]}</a>
          <span>© KUU</span>
        </div>
        <nav class="langs" aria-label="{d["lang_switcher_aria"]}">
{lang_switcher(code, 'index')}
        </nav>
      </footer>
    </main>
  </body>
</html>
"""


def support_html(code, d):
    url = url_for(d, "support")
    home_href = "/" if not d["subdir"] else f"/{d['subdir']}/"
    faqs_html = "\n".join(
        f'      <p>\n        <strong>{q}</strong><br />\n        {a}\n      </p>'
        for q, a in d["faqs"]
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
    <style>
{SUPPORT_CSS}    </style>
  </head>
  <body>
    <main>
      <h1>{d["support_h1"]}</h1>
      <p>{d["support_intro"]}</p>

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


def main():
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
    for path in written:
        print(path)


if __name__ == "__main__":
    main()
