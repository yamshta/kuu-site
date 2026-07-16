# tips アセット撮影パイプライン (runbook)

## TL;DR

`assets/tips/<locale>/` の静止画 4 種・動画 7 種を各言語のアプリ実 UI で撮影・合成する手順。
実行スクリプトは `scripts/tips_capture/`。KUU リポのアプリを専用シミュレータにビルドし、
launch argument でシード状態を作り、WDA REST で要素座標を取って撮影 → PIL で合成する。

初出は kuu-site PR #20 (旧 8 言語、セッション内アドホック実行でスクリプト未保存)。
PR #20 の手法を本 runbook + `scripts/tips_capture/` として再構築・恒久化した。

## なぜ必要か

tips ページはアプリ操作画面のスクショ/動画を言語別に表示する (`tips_asset()` が
`assets/tips/<locale>/` を自動参照、無ければ ja fallback)。テキストだけ翻訳して
画像が他言語のままだとチグハグになる (#18, #25)。

## 当日の手順

- [ ] KUU リポ (main checkout) で simulator 向けビルド:
      `xcodebuild -project KUU.xcodeproj -scheme KUU-dev -destination "generic/platform=iOS Simulator" -derivedDataPath /tmp/kuu_tips_capture_dd build`
- [ ] 専用シミュレータ (iPhone 17) を作成・起動 (共用・Booted 中の他シミュレータは使わない)
- [ ] `xcrun simctl install <UDID> <KUU.app>` + `xcrun simctl spawn <UDID> defaults write com.KUU-app.dev kuu.hasOnboarded -bool true`
- [ ] WDA を起動 (Appium MCP の `prepare_ios_simulator` が手軽。`webDriverAgentUrl` を控える)
- [ ] ラベル抽出 (アプリの文言を変えた場合のみ): `labels.json` を xcstrings から再生成
- [ ] 静止画: `python3 scripts/tips_capture/capture_stills.py --udid <UDID> --wda <URL> --locales da,nb,... --workdir /tmp/tips_work`
- [ ] 全言語×全アセットを目視レビュー (行のスライス・円ズレ・未翻訳文言がないか)
- [ ] `assets/tips/<locale>/` に配置 → `python3 scripts/generate_pages.py` → ページの参照を確認

## 状態の作り方 (launch arguments)

アプリ側フック (`KUU/Support/AppStore.swift` 参照):

| 引数 | 値 | 用途 |
|---|---|---|
| `-KUUSeedScenario` | `saved` / `result` / `placed` / `empty` | シードデータ投入。**tips は `saved` を使う** |
| `-KUUScreenshotSlot` | `hero` / `result` / `place` 等 | 画面状態への直行 + ATT 抑止 |
| `-KUUPlaceExpanded` | `1` | Place シートを .large で開く |
| `-KUUHeadLevel` | `0.0-1.0` | 水円の水位 (t_keyboard は 0.9) |
| `-AppleLanguages` / `-AppleLocale` | `(da)` / `da_DK` | 言語切替 (再インストール不要、launch 単位) |

## 危険な操作 (やってはいけないこと)

| やってはいけないこと | 理由 |
|---|---|
| `-KUUSeedScenario placed` で撮る | `overflowItems` はハードコード日本語。ローカライズされるのは `saved` (`mock_saved_*` キー) |
| シナリオを跨いで再ソートせずデータ引き継ぎ | シードは永続化される。言語/シナリオを変えるときは terminate → launch (シード系は都度上書きされるが、乱れたら uninstall → install でリセット) |
| Booted 中の共用シミュレータで実行 | 並行セッションの作業を破壊する。専用シミュレータを作る |
| 旧アセットとのピクセル一致を狙う | アプリ UI は進化する (カード高さ・水の色等)。**新規言語セット内の一貫性**を優先し、クロップは要素アンカーで決める |

## 失敗時の対応

| 症状 | 状態 | 対応 |
|---|---|---|
| 要素が見つからない | ラベル不一致 | `labels.json` を再生成 (xcstrings の en 値から逆引き) |
| シード項目が日本語 | placed を使った / 古い永続データ | `saved` で launch し直す。直らなければ uninstall → install |
| タップ/長押しが効かない | WDA セッション切れ | `prepare_ios_simulator` から再実行しセッション再作成 |
| 行がクロップ線で切れる | 言語による折返し差 | 該当言語だけクロップ Y を数 px 調整して再合成 (`compose.py` 単体実行) |

## 設計の要点 (読みたい人向け)

- **クロップ/円の座標系**: iPhone 17 native 1206x2622 (論理 402x874 pt の x3)。出力は静止画 900x562。
- **タップ円のスタイル**: 既存アセットと自前キャプチャの差分から実測 — スティールブルー
  (114,159,193) α0.35、半径 83px (native)、外側 30px がガウシアン状に減衰。リング線はない。
  実装は `compose.py`。
- **クロップは要素アンカー**: 旧アセットとのテンプレートマッチはアプリ UI の進化で破綻する
  (実例: 象限カードが伸びて旧枠に + ボタンが入らない)。要素 rect (WDA) から
  「+ ボタン下端 + マージン」「キーボード行を高さ 82% に」等のルールで決める。
- **t_add のカットライン**: 左右カードの行 y は折返しで揃わない。両カードの行間ギャップに
  落ちる y を選ぶ (en は native 780)。言語によりズレたら目視レビューで補正。
- **t_theme_edit への導線**: テーマチップ長押し → context menu「テーマを編集…」。
  メニューラベルは言語別 (labels.json)。シート内の行はチップと同ラベルなので y>200pt で選別。
- **WDA REST 直叩き**: Appium MCP 経由よりスクリプト化・再実行が容易。session は
  `GET /status` の sessionId を流用。

## 動画 7 種 (t_move / t_reclassify / t_release / t_remove / t_theme_press / t_edit / t_theme_drag)

出力仕様: 860x798 h264 24fps + `<name>_poster.jpg`。実行:
`python3 scripts/tips_capture/capture_videos.py --udid <UDID> --locales ... --workdir ... --app <KUU.app>`
(7 種全部を撮影/合成する。t_theme_drag は内部で `synthesize_theme_drag.py` を呼ぶ)

- **動画 1 本ごとに fresh_install される** — ジェスチャー動画は状態を破壊する操作そのもの
  (t_release は項目を手放し、t_edit は編集状態を残す) なので、使い回すと後続の画面が壊れる
  (実例: 初回バッチで t_move が全言語「空カード」になった)
- ドラッグは hold 850ms + 200ms×8 経由点で engage する。速すぎる (90ms) とゴーストが映る前に
  終わり、遅すぎる (320ms) と reorder が engage しない
- W3C actions のディスパッチ遅延で動作が遅れて映るため、ドラッグ系はエンコード時に頭 1.8s を
  トリムして動作を尺の中央に収める (`TRIM_SS`)
- **t_theme_drag だけはライブ再現不可** (上方向 reorder が engage しない + system
  `.dropDestination` は synthetic touch で発火しない — PR #20 で 4 手法検証済み) のため、
  Place スクショ + ゴーストカードの合成アニメで作る

## 関連

- Issue: #18 (旧 8 言語・クローズ済み) / #25 (新 10 言語 + store 同期)
- 手法の初出: kuu-site PR #20
- アプリ側フック: KUU リポ `KUU/Support/AppStore.swift` (launch args)、`KUU/Models/MockData.swift` (シード)
