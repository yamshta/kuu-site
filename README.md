# kuu-site

KUU の公式 LP (`https://kuu-zen.com/`)。GitHub Pages で配信。

主目的:
- App Store の マーケティング/サポート URL のホスト
- AdMob `app-ads.txt` の配信ドメイン (= AdMob 検証を通すため)

## 構成

```
.
├── index.html        # トップ LP
├── support/
│   └── index.html    # サポート (お問い合わせ / FAQ)
├── app-ads.txt       # AdMob 検証用 (必須・ルート直下)
└── CNAME             # kuu-zen.com (GitHub Pages 用)
```

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

App 情報 (5 言語ぶん) の マーケティング URL / サポート URL を変更:

- マーケティング URL: `https://kuu-zen.com/`
- サポート URL: `https://kuu-zen.com/support/`

保存後、AdMob で「アップデートを確認」を押す (最大 24h)。
