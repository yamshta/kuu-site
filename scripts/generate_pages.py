"""Generate per-locale LP and support pages for kuu-site.

Source of truth for translations:
- KUU/Localizable.xcstrings (4 quadrant labels)
- KUU/fastlane/metadata/<locale>/*.txt (tone)
- KUU/docs/concept.md, copy_guide.md (world view / copy)

Output:
- /index.html, /support/index.html  (ja, at root)
- /<locale>/index.html, /<locale>/support/index.html  for en, es, ko, zh-Hans

ja is the canonical locale. New marketing copy is authored in ja first; other
locales fall back to ja for any key they have not translated yet (see main()).
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRIVACY_URL = "https://aerial-dogsled-ede.notion.site/KUU-3667869259cf80b59f50fdfe039b1f7b"
# No country code: Apple auto-redirects to the visitor's storefront.
APP_STORE_URL = "https://apps.apple.com/app/id6771264775"
OG_IMAGE = "https://kuu-zen.com/assets/og.png"

LOCALES = {
    "ja": {
        "subdir": "",
        "html_lang": "ja",
        "og_locale": "ja_JP",
        "label": "日本語",
        "title": "KUU — 頭の中を整える、静かなブレインダンプ",
        "description": "KUU は、頭の中を口に出すだけで「いま見る / あとで考える / 寝かせる / 手放す」に整える、静かなブレインダンプアプリです。",
        # Hero
        "hero_headline": "話して、あたまに余白を。",
        "hero_sub": "考えごとでいっぱいになった頭から、いま持たなくていいものを、声に出すだけ。",
        "cta": "App Store で入手",
        "scroll_cue": "下へ",
        # Why
        "why_eyebrow": "なぜ KUU か",
        "why_headline": "頭の中には、いろんな思考が混ざっている。",
        "why_lead": "タスク、悩み、アイデア、違和感、心配ごと。メモにもタスクにも、しっくりこないまま溜まっていく。",
        "thoughts": [
            "やらなきゃいけない気がすること",
            "あとで考えたいこと",
            "まだ形になっていないアイデア",
            "なんとなく気になる違和感",
            "今は考えても仕方ない心配ごと",
        ],
        "why_note": "KUU は、それを声に出して頭の外へ。水位が下がるように、すこし軽くなる。",
        # How
        "steps_eyebrow": "使い方",
        "steps_headline": "やることは、話すだけ。",
        "steps": [
            ("話す", "まとまっていなくて大丈夫。思いついたまま、声に出す。"),
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
        "privacy_headline": "話した内容は、外に出ない。",
        "privacy_body": "音声の聞きとりも整理も、すべて端末の中だけ。音声そのものは残しません。話したことは、あなたの iCloud（プライベート）にだけ同期されます。",
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
        "description": "KUU is a quiet voice-first brain-dump app. Speak what is on your mind; KUU sorts it into Now, Later, Park, and Let go.",
        "hero_headline": "Speak, and free your mind.",
        "hero_sub": "From a head full of thoughts, just say out loud what you don't need to carry right now.",
        "cta": "Download on the App Store",
        "scroll_cue": "Scroll",
        "why_eyebrow": "Why KUU",
        "why_headline": "Your head holds all kinds of thoughts.",
        "why_lead": "Tasks, worries, ideas, small doubts, anxieties. They pile up — fitting neither a to-do list nor a notebook.",
        "thoughts": [
            "Something you feel you ought to do",
            "Something to think about later",
            "An idea not yet in shape",
            "A vague unease you can't place",
            "A worry there's no point dwelling on now",
        ],
        "why_note": "KUU lets you say it out loud and set it down. Like a water line dropping, your head gets a little lighter.",
        "steps_eyebrow": "How it works",
        "steps_headline": "All you do is talk.",
        "steps": [
            ("Speak", "It doesn't need to be tidy. Just say it as it comes."),
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
        "privacy_headline": "What you say stays with you.",
        "privacy_body": "Listening and sorting happen entirely on your device. The audio itself is never kept. Your notes sync only to your private iCloud.",
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
        "description": "KUU es una app silenciosa para vaciar la mente. Habla lo que tienes; KUU lo separa en Ahora, Más tarde, Reposar y Soltar.",
        "hero_headline": "Habla y deja espacio en tu cabeza.",
        "hero_sub": "Desde una cabeza llena de pensamientos, solo di en voz alta lo que ahora no necesitas cargar.",
        "cta": "Descargar en el App Store",
        "scroll_cue": "Desliza",
        "why_eyebrow": "Por qué KUU",
        "why_headline": "En la cabeza se mezclan toda clase de pensamientos.",
        "why_lead": "Tareas, preocupaciones, ideas, dudas, inquietudes. Se acumulan, y no encajan ni en una lista de tareas ni en una nota.",
        "thoughts": [
            "Algo que sientes que deberías hacer",
            "Algo para pensar más tarde",
            "Una idea que aún no toma forma",
            "Una vaga inquietud que no ubicas",
            "Una preocupación que de nada sirve rumiar ahora",
        ],
        "why_note": "KUU te deja decirlo en voz alta y dejarlo ir. Como un nivel de agua que baja, la cabeza se aligera un poco.",
        "steps_eyebrow": "Cómo funciona",
        "steps_headline": "Lo único que haces es hablar.",
        "steps": [
            ("Habla", "No tiene que estar ordenado. Dilo tal como surge."),
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
        "privacy_headline": "Lo que dices se queda contigo.",
        "privacy_body": "Escuchar y separar ocurren por completo en tu dispositivo. El audio nunca se guarda. Tus notas se sincronizan solo con tu iCloud privado.",
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
        "description": "KUU는 조용한 음성 브레인덤프 앱입니다. 마음에 있는 것을 말하세요. KUU가 지금 보기, 나중에 생각하기, 묵히기, 내려놓기로 나눠줍니다.",
        "hero_headline": "말하고, 머릿속에 여백을.",
        "hero_sub": "생각으로 가득 찬 머리에서, 지금 가지고 있지 않아도 될 것을 소리 내어 말하기만 하면 됩니다.",
        "cta": "App Store에서 받기",
        "scroll_cue": "아래로",
        "why_eyebrow": "왜 KUU인가",
        "why_headline": "머릿속에는 온갖 생각이 뒤섞여 있습니다.",
        "why_lead": "할 일, 고민, 아이디어, 위화감, 걱정. 메모에도 할 일 목록에도 들어맞지 않은 채 쌓여 갑니다.",
        "thoughts": [
            "해야 할 것 같은 일",
            "나중에 생각하고 싶은 것",
            "아직 형태가 잡히지 않은 아이디어",
            "왠지 마음에 걸리는 위화감",
            "지금 걱정해 봐야 소용없는 일",
        ],
        "why_note": "KUU는 그것을 소리 내어 머리 밖으로. 수위가 내려가듯, 조금 가벼워집니다.",
        "steps_eyebrow": "사용법",
        "steps_headline": "할 일은, 말하는 것뿐.",
        "steps": [
            ("말하기", "정리되어 있지 않아도 괜찮아요. 떠오르는 대로 소리 내어."),
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
        "privacy_headline": "말한 내용은, 밖으로 나가지 않습니다.",
        "privacy_body": "듣기도 정리도 모두 기기 안에서만. 음성 자체는 남기지 않습니다. 말한 것은 당신의 iCloud(프라이빗)에만 동기화됩니다.",
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
        "hero_headline": "说出来，给脑子留点空。",
        "hero_sub": "从塞满念头的脑袋里，把此刻不必扛着的事，说出来就好。",
        "cta": "在 App Store 下载",
        "scroll_cue": "向下",
        "why_eyebrow": "为什么是 KUU",
        "why_headline": "脑袋里，混着各种各样的念头。",
        "why_lead": "待办、烦恼、灵感、违和感、担忧。它们既不像待办，也不像笔记，就这样堆着。",
        "thoughts": [
            "总觉得该做的事",
            "想之后再想的事",
            "还没成形的灵感",
            "莫名在意的违和感",
            "此刻想也无益的担忧",
        ],
        "why_note": "KUU 让你把它说出口，移到脑外。像水位下降一样，轻一些。",
        "steps_eyebrow": "怎么用",
        "steps_headline": "要做的，只有说。",
        "steps": [
            ("说", "不必整理，想到什么就说出来。"),
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
        "privacy_headline": "你说的内容，不会出去。",
        "privacy_body": "聆听与整理，全都只在你的设备里完成。语音本身从不保留。记录只同步到你私人的 iCloud。",
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

/* soft ambient background wash */
body::before {
  content: "";
  position: fixed;
  inset: 0;
  z-index: -1;
  background:
    radial-gradient(60% 50% at 78% 8%, rgba(127, 178, 214, 0.10), transparent 70%),
    radial-gradient(70% 55% at 12% 96%, rgba(156, 198, 226, 0.12), transparent 72%);
}

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
/* parallax: hero layers lag behind the scroll (--hy set by JS, 0 without JS / reduced-motion) */
.js .hero .orb { transform: translateY(var(--hy, 0px)); }
.js .hero h1,
.js .hero .sub { transform: translateY(calc(var(--hy, 0px) * 0.45)); }
.js .hero .wordmark { transform: translateY(calc(var(--hy, 0px) * 0.3)); }

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
  height: 60%;
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
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 18px;
  border-top: 3px solid var(--q, var(--primary));
}
.q strong { display: block; color: var(--ink); font-size: 16px; font-weight: 600; margin-bottom: 6px; }
.q span { color: var(--ink-soft); font-size: 13.5px; line-height: 1.6; }

/* ---- privacy ---- */
.privacy {
  text-align: center;
  background:
    radial-gradient(80% 90% at 50% 0%, rgba(220, 234, 244, 0.6), transparent 70%);
}
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

@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  .orb__water, .orb__water::before, .scroll-cue { animation: none; }
  .js .reveal { opacity: 1; transform: none; transition: none; }
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
    var hero = document.querySelector('.hero');
    if (!hero) return;
    var ticking = false;
    function update() {
      var y = window.scrollY || 0;
      if (y < window.innerHeight * 1.2) hero.style.setProperty('--hy', (y * 0.22) + 'px');
      ticking = false;
    }
    addEventListener('scroll', function () {
      if (!ticking) { ticking = true; requestAnimationFrame(update); }
    }, { passive: true });
    update();
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

QUADRANT_VARS = ["--cat-now", "--cat-later", "--cat-parked", "--cat-release"]


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
        f'width="600" height="1303" loading="lazy" alt="{d["screen_alt"]} {n}" />'
        for n in range(1, 7)
    )
    support_href = "/support/" if not d["subdir"] else f'/{d["subdir"]}/support/'
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
    <style>
{BASE_CSS}    </style>
  </head>
  <body>
    <header class="hero">
      <p class="wordmark">KUU</p>
      <h1>{d["hero_headline"]}</h1>
      <p class="sub">{d["hero_sub"]}</p>
      <div class="orb" aria-hidden="true"><div class="orb__water"></div></div>
      <a class="cta" href="{APP_STORE_URL}" rel="noopener">{d["cta"]}</a>
      <div class="scroll-cue" aria-hidden="true">{d["scroll_cue"]}</div>
    </header>

    <main>
      <section class="why">
        <div class="wrap reveal">
          <p class="eyebrow">{d["why_eyebrow"]}</p>
          <h2>{d["why_headline"]}</h2>
          <p class="lead">{d["why_lead"]}</p>
          <ul class="thoughts">
{thoughts_html}
          </ul>
          <p class="note">{d["why_note"]}</p>
        </div>
      </section>

      <section class="how">
        <div class="wrap reveal">
          <p class="eyebrow">{d["steps_eyebrow"]}</p>
          <h2>{d["steps_headline"]}</h2>
          <div class="steps">
{steps_html}
          </div>
        </div>
      </section>

      <section class="app reveal">
        <div class="wrap">
          <p class="eyebrow">{d["app_eyebrow"]}</p>
          <h2>{d["app_headline"]}</h2>
        </div>
        <div class="showcase" aria-label="{d["app_eyebrow"]}">
{screens_html}
        </div>
      </section>

      <section class="matrix-section">
        <div class="wrap reveal">
          <p class="eyebrow">{d["matrix_eyebrow"]}</p>
          <h2>{d["matrix_headline"]}</h2>
          <p class="lead">{d["matrix_lead"]}</p>
          <div class="matrix" aria-label="{d["quadrants_aria"]}">
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
          <a class="cta" href="{APP_STORE_URL}" rel="noopener">{d["cta"]}</a>
        </div>
      </section>
    </main>

    <footer>
      <div class="wrap">
        <div class="footer-row">
          <a href="{support_href}">{d["support_label"]}</a>
          <a href="{PRIVACY_URL}" rel="noopener" target="_blank">{d["privacy_label"]}</a>
          <span>© KUU</span>
        </div>
        <nav class="langs" aria-label="{d["lang_switcher_aria"]}">
{lang_switcher(code, 'index')}
        </nav>
      </div>
    </footer>
{REVEAL_SCRIPT}  </body>
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
    # ja is canonical; fill any missing key on other locales from ja.
    ja = LOCALES["ja"]
    for code, d in LOCALES.items():
        for key, val in ja.items():
            d.setdefault(key, val)

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
