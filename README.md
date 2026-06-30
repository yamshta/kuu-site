# kuu-site

KUU の公式 LP (`https://kuu-zen.com/`)。GitHub Pages で配信。

主目的:
- App Store の マーケティング/サポート URL のホスト (5 言語)
- AdMob `app-ads.txt` の配信ドメイン (= AdMob 検証を通すため)

## 構成

```
.
├── index.html              # ja (root)
├── support/index.html      # ja support
├── en/index.html           # en
├── en/support/index.html
├── es/index.html           # es
├── es/support/index.html
├── ko/index.html           # ko
├── ko/support/index.html
├── zh-Hans/index.html      # zh-Hans
├── zh-Hans/support/index.html
├── tips/index.html         # 使い方のコツ (ja-only, TIPS_LOCALES。privacy と同じ一部言語パターン)
├── privacy/index.html      # ja / en/privacy/ のみ (PRIVACY_LOCALES)
├── app-ads.txt             # AdMob 検証用 (ルート直下)
├── CNAME                   # kuu-zen.com
└── scripts/
    └── generate_pages.py   # 全ページ + sitemap/robots の一括生成 (翻訳の SSoT)
```

翻訳/コピーを変更する場合は `scripts/generate_pages.py` の `LOCALES` dict を編集 → `python3 scripts/generate_pages.py` で再生成。
個別 HTML を直接編集しない (次回生成で上書きされる)。

## App Store Connect URL マッピング

| locale | marketing | support |
|---|---|---|
| ja | `https://kuu-zen.com/` | `https://kuu-zen.com/support/` |
| en-US | `https://kuu-zen.com/en/` | `https://kuu-zen.com/en/support/` |
| es-ES | `https://kuu-zen.com/es/` | `https://kuu-zen.com/es/support/` |
| ko | `https://kuu-zen.com/ko/` | `https://kuu-zen.com/ko/support/` |
| zh-Hans | `https://kuu-zen.com/zh-Hans/` | `https://kuu-zen.com/zh-Hans/support/` |

## デプロイ手順 (初回 owner 作業)

### 1. ドメイン購入

`kuu-zen.com` を Cloudflare Registrar または Porkbun などで取得。

### 2. GitHub Pages 設定

リポジトリ Settings → Pages:
- Source: `Deploy from a branch`
- Branch: `main` / root
- Custom domain: `kuu-zen.com`
- **Enforce HTTPS** をオン (DNS 反映後)

### 3. DNS 設定 (Apex + www)

Apex (`kuu-zen.com`) は GitHub の 4 つの A レコードに向ける。Cloudflare DNS なら **Proxy は OFF (灰色雲)** にすること (GitHub Pages の cert 発行を邪魔しない)。

```
A      kuu-zen.com        185.199.108.153
A      kuu-zen.com        185.199.109.153
A      kuu-zen.com        185.199.110.153
A      kuu-zen.com        185.199.111.153
CNAME  www.kuu-zen.com    yamshta.github.io
```

### 4. 検証

```sh
curl -sSL -o /dev/null -w "%{http_code}\n" https://kuu-zen.com/app-ads.txt
curl -sSL https://kuu-zen.com/app-ads.txt
```

期待値:
```
google.com, pub-6031760637647284, DIRECT, f08c47fec0942fa0
```

### 5. App Store Connect 更新

上記マッピングどおりに 5 言語ぶんの URL を設定。保存後、AdMob で「アップデートを確認」(最大 24h)。

## 翻訳ソース

- 4 象限の正規ラベル: `KUU/Localizable.xcstrings` (xcstrings)
- トーン参照: `KUU/fastlane/metadata/<locale>/{subtitle,promotional_text,description}.txt`
- 世界観: `docs/copy_guide.md` (静寂・余白)
