# KUU プライバシーポリシー

最終更新日：2026 年 7 月 21 日

本ポリシーは **iOS 版・Android 版**の両方に適用されます。プラットフォーム間で挙動が異なる箇所は、その都度明記します。

**ひとことで：** あなたが話したことはあなたのものです。**音声そのものは外部に送信しません**。文字起こしは端末の中で行います。整理（AI 分類）には外部の AI を使いますが、送られるのは文字にした内容だけで、整理にのみ使われ、保存されません（iOS 版は設定「オンデバイス」で端末内のみの整理に変更できます。**Android 版は外部 AI 送信のみで、オンデバイス整理はありません**）。保存先はあなたの端末と、iOS 版では iCloud（プライベートデータベース）です（Android 版は端末内のみ）。開発者は内容を保存せず、受け取った内容を見ることもありません。いつでもアプリ内から全データを削除できます。アプリは課金（iOS=StoreKit／Android=RevenueCat）と Google AdMob の広告のために**必要最小限の通信**のみ行い、その情報には話した内容は含まれません（広告は KUU+ 加入で無効化できます）。品質改善のため利用状況の計測を行いますが、こちらも話した内容は含みません（iOS はユーザー opt-in、Android は content-free な計測を既定で実施。詳細は第 14 条）。

---

## 第 1 条（基本方針）

本アプリ「KUU」（以下「本アプリ」）は、頭の中の考えごとを声で外に出し、整理することを支援するアプリです。**iOS 版・Android 版**があり、本ポリシーは両方に適用されます。本アプリは、機能提供に必要な最小限の範囲でのみ情報を扱い、ユーザーのプライバシー保護を最優先とします。

## 第 2 条（取得・保存する情報）

本アプリが取り扱う情報は、以下に限られます。

1. **ユーザーが話した内容（音声データ）** — 録音した音声は文字起こしの処理中のみ端末内の一時領域に保存され、処理完了後すみやかに削除されます。サーバーには送信されません。
2. **文字起こし結果と整理結果（テキスト）** — あなた自身が見返せるように保存されます（iOS 版は端末および iCloud プライベートデータベース、Android 版は端末内のみ。詳細は第 4 条）。
3. **アプリ内設定** — テーマ、文字サイズ、頭の水位状態などのアプリ動作に必要な設定値。

本アプリは、氏名・メールアドレス・電話番号・位置情報・連絡先・カレンダー・写真・端末識別子等の個人情報を取得しません。

## 第 3 条（音声認識と AI 分類について）

**音声認識（文字起こし）** は、すべてお使いの iOS デバイス上で完結します。

- 音声認識：Apple の Speech フレームワーク（オンデバイス）を使用します。音声そのものが端末の外に送信されることはありません

**AI 分類（カテゴリ分け）** は、外部の AI を使用します。

- 送信されるのは**文字にした内容（文字起こしテキスト）だけ**です。音声は送信されません
- 送信先は外部の AI で、開発者のサーバー（バックエンド経由で Google の Gemini）を経由します
- 送信された内容は**分類にのみ使用され、保存されません**。AI の学習にも使用されません
- **iOS 版**は、設定の「オンデバイス」から、**端末内のみの分類**（Apple の FoundationModels / 端末内ルール）へいつでも変更できます。この場合、文字も端末の外に出ません

**Android 版について：** Android 版は、端末内のみで完結する整理（分類）方式を提供していません。整理を行うと、文字起こしされたテキストは**必ず**外部の AI（当社のバックエンド経由で Google の Gemini）に送信されます。iOS 版のような「オンデバイス」への切り替えはありません。送信されるのは文字にした内容のみで、音声そのものは送信されず、送信されたテキストは分類にのみ使用され、保存も AI 学習にも使用されません。文字起こし（音声認識）自体は端末内で完結します。

## 第 4 条（保存と同期）

**iOS 版：** 文字起こし結果と整理結果を、あなたの **iCloud のプライベートデータベース**（CloudKit Private Database）にのみ保存します。これは Apple が提供するストレージで、保存内容にアクセスできるのはあなた本人だけです。本アプリの開発者は、保存された内容を閲覧することも、取得することもできません。iCloud の利用条件・セキュリティについては、Apple のプライバシーポリシーが適用されます。

**Android 版：** 文字起こし結果と整理結果は、**この端末にのみ**保存されます。自動的なクラウド同期は行っていません。機種変更の際は、アプリ内の「声とデータ」からファイルへ書き出し、新しい端末で読み込むことができます。書き出し先はユーザーご自身が選択します（端末内・お使いのクラウドストレージアプリ等）。開発者はこのファイルにアクセスできません。

## 第 5 条（利用目的）

取り扱う情報は、以下の目的でのみ利用します。

1. 音声から文字起こしを生成し、ユーザーに表示する
2. 文字起こしを「いま見る／あとで考える／寝かせる／手放す」に分類してユーザーに表示する
3. ユーザーが過去に話した内容を、ユーザー自身が見返せるように保存・表示する
4. アプリの動作に必要な設定値を保持する

## 第 6 条（外部サービスの利用）

本アプリは、機能提供のために以下の外部サービスを利用します。**音声そのものは、いずれのサービスにも送信されません**。

- **iCloud / CloudKit**（iOS 版のみ。Apple 提供。あなた自身のプライベートデータベースにのみ保存・同期）
- **音声認識**（iOS 版は Apple の Speech フレームワーク、Android 版は端末内の音声認識エンジン。いずれも端末上で実行し、音声は端末外に送信しません）
- **外部の AI（クラウド）**（AI 分類。文字にした内容のみ送信。分類にのみ使用され、保存もされず、AI の学習にも使用されません。iOS 版は設定「オンデバイス」でオフにできますが、**Android 版は外部 AI 送信のみ**です。詳細は第 3 条）
- **FoundationModels**（iOS 版のみ。Apple 提供。完全に端末上で実行。「オンデバイス」設定時と、外部 AI が使えないときのフォールバックで使用）
- **課金サービス**（iOS 版は **Apple StoreKit**、Android 版は **RevenueCat**。KUU+ サブスクリプションの購入・更新・解約・権利状態の管理。話した内容は送信されません。RevenueCat については第 7 条・[RevenueCat プライバシーポリシー](https://www.revenuecat.com/privacy)）
- **Play Integrity API（Firebase App Check 経由。Android 版のみ）**（分類 API へのリクエストが正規のアプリから送られたことを確認するための、端末・アプリの完全性証明。話した内容やユーザーを特定する情報は含まれません）
- **Google AdMob（Google Mobile Ads SDK）**（KUU+ 未加入時のみ、「話したこと」画面に節間のネイティブ広告 1 枠を表示。話した内容は送信されません。詳細は第 13 条）
- **Firebase Analytics**（Google 提供。アプリの品質改善のため。iOS 版は**ユーザーが Settings で明示的に opt-in した場合にのみ**、Android 版は content-free な利用状況イベントを**既定で**送信します（いずれも話した内容は送信しません）。iOS 版は **Crashlytics** も opt-in で利用しますが、**Android 版は Crashlytics を搭載していません**。詳細は第 14 条）

本アプリのサーバーは AI 分類の中継のみを行う最小限のもので、内容を一切保存しません（ステートレス）。個人アカウントを要する認証サービスは使用しません。

## 第 7 条（第三者提供）

本アプリの開発者は、ユーザーが話した内容、文字起こし結果、整理結果にアクセスする手段を持たず、これらを第三者に提供しません。

KUU+ 未加入のユーザーに広告を配信する目的で、Google AdMob に対して端末識別子・広告 ID・端末の言語・地域・概略の位置情報・広告のクリック情報など、AdMob が広告配信のために必要とする情報が Google に送信されます（詳細は第 13 条、Google の AdMob プライバシーポリシーが適用されます）。KUU+ に加入している間は、この情報送信は発生しません。

**Android 版**で KUU+ にご加入いただく際は、購入処理と権利（有効／無効の判定）の管理のため、RevenueCat, Inc. に購入情報（商品 ID・価格・購入日時等）が送信されます。話した内容は送信されません。RevenueCat のデータ取り扱いの詳細は [RevenueCat プライバシーポリシー](https://www.revenuecat.com/privacy) をご確認ください。

法令に基づき開示が義務付けられた場合に限り、所定の手続きに従い対応します。

## 第 8 条（データの削除）

ユーザーは、アプリ内の「設定 → 声とデータ → 保存していることの削除」からいつでも全データを削除できます。削除を行うと、端末上のデータ（iOS 版は iCloud プライベートデータベース上のデータも含む）が完全に消去されます。消去したデータの復元はできません。

本アプリをアンインストールした場合、端末上のデータは削除されます。iOS 版の iCloud 上のデータは、Apple の設定（設定 → Apple ID → iCloud → ストレージ管理）から削除できます。Android 版は端末内保存のみのため、アンインストールで削除されます。

## 第 9 条（安全管理措置）

- **iOS 版**：録音中の一時音声ファイルは、iOS のファイル保護機能（`FileProtectionType.complete`）により暗号化され、デバイスロック中はアクセスできません。iCloud との通信は Apple が SSL/TLS で暗号化します
- **Android 版**：録音した音声は一時ファイルとしてもディスクに書き出さず、メモリ上でのみ処理し、認識処理後にただちに破棄します。保存された文字起こし・整理結果は Android のアプリ専用領域に保存され、他のアプリからはアクセスできません。また Android の自動クラウドバックアップの対象から除外しています
- 外部の AI への通信はすべて暗号化（HTTPS/TLS）されます。開発者のサーバーは分類の中継のみで内容を保存しません（ステートレス）

## 第 10 条（未成年者の利用）

本アプリは年齢区分 4+ で提供されますが、思考の整理という性質上、文字を読み書きできる年齢以上での利用を想定しています。未成年者が利用する場合は、保護者の同意を得たうえで利用してください。

## 第 11 条（プライバシーポリシーの変更）

本ポリシーは、法令の変更、機能の追加、各プラットフォーム（Apple / Google）のフレームワークやポリシーの仕様変更等により、改定されることがあります。重要な変更がある場合は、アプリのアップデート時または本ポリシーの公開ページで告知します。

## 第 12 条（お問い合わせ）

本ポリシーに関するお問い合わせは、App Store または Google Play のアプリページ内「開発元」セクション、あるいはアプリ内「設定 → お問い合わせ」よりご連絡ください。

## 第 13 条（広告と App Tracking Transparency について）

本アプリは KUU+ サブスクリプションに加入していない期間のみ、Google AdMob によるネイティブ広告を「話したこと」画面で 1 枠だけ表示します。広告そのものは KUU の世界観を保つため、画面の節間に控えめに表示されます。

- **話した内容を広告のために使うことはありません**（広告は文字起こし・分類結果・テーマを参照しません）
- 広告配信のために Google AdMob は端末識別子（IDFA を含む）、広告 ID、Coarse Location（概略の位置情報）、Diagnostics、Product Interaction（アプリ内の広告との接触情報）等を収集する場合があります
- **iOS 版**：**App Tracking Transparency**（ATT）プロンプトを最初の広告表示直前に 1 回だけ表示します。ユーザーが許諾しない場合でも広告は表示されますが、Google に送信される情報は限定的な範囲（パーソナライズなし）になります。ATT 許諾状態は iOS の「設定」→「プライバシーとセキュリティ」→「トラッキング」からいつでも変更できます
- **Android 版**：ATT は iOS 専有の仕組みのため Android にはありません。代わりに Google の**広告 ID（Advertising ID）**が広告配信に使用されます。端末の「設定 → プライバシー → 広告」（端末や Android バージョンにより文言は異なります）から、広告のパーソナライズをオプトアウトしたり、広告 ID をリセットしたりできます。あわせて、Android 版では EU 等の対象地域で表示される同意管理（UMP）に従います
- **KUU+ に加入すると広告と関連する情報送信はすべて停止します**
- Google AdMob によるデータ取り扱いの詳細は [Google AdMob プライバシーポリシー](https://support.google.com/admob/answer/6128543) をご確認ください

## 第 14 条（Firebase Analytics / Crashlytics の利用について）

**本条の opt-in 方式は iOS 版に適用されます。Android 版については本条末尾の「Android 版について」をご覧ください。**

**iOS 版**は、アプリの品質改善および本番事故の即知化のために、Google の Firebase Analytics（利用状況の集計）および Firebase Crashlytics（クラッシュレポート）を利用することがあります。**本機能は既定で OFF（送信なし）であり、ユーザーが「設定 → データと診断」で明示的に opt-in した場合に限り動作します。**

- **送信される情報**:
  - Firebase が自動的に発行する匿名化された install ID（IDFV に基づく。個人を直接特定する識別子ではありません）
  - アプリ内の操作 event の集計シグナル（録音セッションの完走有無、Paywall の表示・購入転換、Onboarding 完了等の集計用 event。数値はバケット化された粗い粒度で送信）
  - アプリが異常終了した際の crash stack trace（symbol 化済み）
- **送信されない情報**: 話した内容（音声）、文字起こし結果、AI 分類結果のテキスト、ユーザーが設定したテーマ名は**型レベルで送信できない設計**になっています（実装上、計測 SDK に文字列値を渡せない API になっています）
- **opt-in されていない期間は、上記の情報を含む一切の通信が Firebase に対して発生しません**
- **送信を停止する手段**: 「設定 → データと診断」のトグルをいつでも OFF にできます。OFF にした時点で過去の install ID は破棄され、端末ローカルに保存されていた未送信の crash log も削除されます
- 送信先は Google LLC（米国）です。Google の [Firebase Privacy Information](https://firebase.google.com/support/privacy) が適用されます

**Android 版について：** Android 版は Firebase Analytics を利用し、プロダクト改善のための **content-free（内容を含まない）な利用状況イベント**（画面の遷移や機能の利用回数などのバケット値）と、Firebase が発行する匿名の App Instance ID を送信します。**iOS 版と異なり、これは既定で有効です。** 話した内容（音声）・文字起こし・整理結果のテキスト・テーマ名は、計測 SDK に文字列値を渡せない設計により**送信できません**。**Android 版は Crashlytics を搭載しておらず、クラッシュレポートは送信しません。** 送信先は Google LLC（米国）で、Google の [Firebase Privacy Information](https://firebase.google.com/support/privacy) が適用されます。

---

# Privacy Policy for KUU

Last updated: July 21, 2026

This policy applies to both the **iOS and Android** versions. Platform-specific differences are noted where relevant.

**In short:** What you spoke is yours. **Your voice itself is never sent outside your device.** Transcription happens on your device. AI organization uses an external AI, but only the transcribed text is sent. It is used solely for organizing and is not retained by the AI provider (on iOS you can switch to on-device-only organization via "On-device" in Settings; **the Android version sends to the external AI only — there is no on-device organization**). What is stored lives only on your device, and on iOS also in your iCloud private database (Android stores on the device only). The developer does not store your content and cannot view what is received. You can delete all data from inside the app at any time. The app makes only **minimal network requests** for billing (StoreKit on iOS / RevenueCat on Android) and Google AdMob ads, and that information never includes what you said (ads disappear with KUU+). Usage is measured to improve quality, but this too never includes what you said (iOS is user opt-in; Android sends content-free measurement by default — see Article 14).

---

## Article 1 (General)

KUU (the "App") is an application (available on **iOS and Android**) that helps you offload thoughts from your head by speaking them out loud and organizing them. This policy applies to both versions. The App processes information only to the minimum extent necessary to provide its features, prioritizing user privacy.

## Article 2 (Information Handled)

The App handles only the following:

1. **Audio you record** — Stored temporarily in a device-local cache only during transcription. Deleted immediately after processing. Never sent to any server.
2. **Transcribed and organized text** — Saved so you can review what you have said (iOS: on your device and in your iCloud private database; Android: on the device only — see Article 4).
3. **App settings** — Theme, text size, head-water-level state, and other values required to run the App.

The App does not collect names, email addresses, phone numbers, location, contacts, calendar, photos, or device identifiers.

## Article 3 (Speech Recognition and AI Organization)

**Speech recognition (transcription)** is performed entirely on your iOS device:

- Speech recognition: Apple's Speech framework (on-device). Your voice itself is never sent off the device.

**AI organization (categorization)** uses an external AI:

- Only the **text of what you said (the transcript)** is sent. Your voice is never sent.
- It is sent to an external cloud AI (Google's Gemini via the developer's backend), relayed through the developer's server.
- The sent text is **used only for categorization and is never stored**. It is not used to train the AI either.
- **On iOS**, you can switch to **on-device-only organization** (Apple's FoundationModels / on-device rules) anytime via "On-device" in Settings. In that case, the transcript never leaves the device.

**About the Android version:** The Android version does not offer on-device-only organization. When you organize, the transcribed text is **always** sent to the external AI (Google's Gemini via our backend). There is no "On-device" switch as on iOS. Only the transcribed text is sent — your voice itself is never sent, and the sent text is used solely for categorization and is neither stored nor used to train the AI. Transcription (speech recognition) itself runs entirely on the device.

## Article 4 (Storage and Sync)

**iOS:** The App stores transcribed and organized text in your **iCloud Private Database** (CloudKit Private Database). This is Apple-provided storage that only you can access. The developer cannot view or retrieve any stored content. The use of iCloud is subject to Apple's privacy policy.

**Android:** Transcribed and organized text is stored **on this device only**. There is no automatic cloud sync. When switching devices, you can export to a file from "Voice & Data" in the App and import it on the new device. You choose where the file is saved (on device, in your cloud storage app, etc.). The developer cannot access that file.

## Article 5 (Purpose of Use)

Handled information is used only for:

1. Generating transcriptions from your voice and displaying them to you
2. Categorizing transcriptions into Now / Later / Park / Release and displaying them
3. Storing and displaying what you have spoken so you can review it
4. Maintaining app settings

## Article 6 (External Services)

The App uses the following external services. **Your voice itself is not sent to any of them.**

- **iCloud / CloudKit** (iOS only. Apple, only your own private database)
- **Speech recognition** (iOS: Apple's Speech framework; Android: the device's on-device speech engine. Both run on the device; your voice is never sent off the device.)
- **An external cloud AI** (AI organization. Only the text of what you said is sent; used solely for categorization, never stored, never used for AI training. On iOS it can be turned off via "On-device" in Settings, but **the Android version sends to the external AI only**. See Article 3.)
- **FoundationModels** (iOS only. Apple, runs entirely on-device. Used when "On-device" is enabled, or as fallback.)
- **Billing** (iOS: **Apple StoreKit**; Android: **RevenueCat**. KUU+ subscription purchase, renewal, cancellation, and entitlement management. No spoken content is sent. For RevenueCat see Article 7 and the [RevenueCat privacy policy](https://www.revenuecat.com/privacy).)
- **Play Integrity API (via Firebase App Check; Android only)** (Verifies that requests to the classification API come from a legitimate app — a device/app integrity attestation. Contains no spoken content and no user-identifying information.)
- **Google AdMob (Google Mobile Ads SDK)** (Only when KUU+ is not active: one native ad slot between sections in the "What you said" screen. No spoken content is sent. See Article 13.)
- **Firebase Analytics** (Google. For app quality improvement. On iOS, **used only when you explicitly opt in via Settings**; on Android, content-free usage events are sent **by default** (in both cases no spoken content is sent). iOS also uses **Crashlytics** on opt-in, but **the Android version does not include Crashlytics**. See Article 14.)

The App operates a minimal stateless server only to relay AI organization requests (no content is stored). It does not use authentication services requiring personal accounts.

## Article 7 (Third-Party Disclosure)

The developer has no means to access your spoken content, transcripts, or organized results, and discloses none of them to any third party.

To deliver ads to users not subscribed to KUU+, the App sends information required by Google AdMob for ad delivery — including device identifiers, advertising ID, device language and region, coarse location, and ad interaction data — to Google (see Article 13; Google's AdMob privacy policy applies). While KUU+ is active, this transmission does not occur.

When you subscribe to KUU+ on the **Android** version, purchase information (product ID, price, purchase date, etc.) is sent to RevenueCat, Inc. to manage the purchase and your entitlement (active/inactive). No spoken content is sent. See the [RevenueCat privacy policy](https://www.revenuecat.com/privacy) for details.

Information will only be disclosed when required by law.

## Article 8 (Data Deletion)

You can delete all data at any time from "Settings → Voice & Data → Delete what's stored" inside the App. This permanently removes data on the device (and, on iOS, also in the iCloud Private Database). Deleted data cannot be recovered.

Uninstalling the App deletes local data. On iOS, iCloud data can be removed via Settings → Apple ID → iCloud → Manage Storage. The Android version stores data on the device only, so it is removed on uninstall.

## Article 9 (Security)

- **iOS:** Temporary audio files during recording are encrypted by iOS file protection (`FileProtectionType.complete`) and inaccessible while the device is locked. Communication with iCloud is encrypted by Apple via SSL/TLS
- **Android:** Recorded audio is never written to disk even as a temporary file; it is processed in memory only and discarded immediately after recognition. Stored transcripts and organized results live in the app's private storage, inaccessible to other apps, and are excluded from Android's automatic cloud backup
- All communication with the external AI is encrypted (HTTPS/TLS). The developer's server only relays organization requests and stores no content (stateless)

## Article 10 (Use by Minors)

The App is rated 4+, but its nature (thought organization) presumes literacy. Minors should use it with the consent of their guardian.

## Article 11 (Changes to This Policy)

This policy may be updated due to changes in law, additions to features, or changes to each platform's (Apple / Google) framework or policy specifications. Significant changes will be announced via an app update or on the public page of this policy.

## Article 12 (Contact)

For inquiries regarding this policy, please contact us through the "Developer" section on the App's App Store or Google Play page, or via "Settings → Contact" inside the App.

## Article 13 (Ads and App Tracking Transparency)

When you are not subscribed to KUU+, the App displays one native ad slot between sections in the "What you said" screen, served by Google AdMob. Ads are rendered quietly to fit KUU's tone.

- **Your spoken content is never used for ads.** Ads do not consult your transcripts, organized results, or themes.
- For ad delivery, Google AdMob may collect device identifiers (including IDFA), advertising ID, coarse location, diagnostics, and product interactions (ad-related interactions within the App).
- **iOS:** An **App Tracking Transparency** (ATT) prompt is shown once, right before the first ad. Ads will still be shown if you decline, but the information sent to Google is restricted (non-personalized). You can change ATT permission at any time in iOS "Settings → Privacy & Security → Tracking".
- **Android:** ATT is iOS-only and does not exist on Android. Instead, Google's **Advertising ID** is used for ad delivery. You can opt out of ad personalization or reset your Advertising ID from your device's "Settings → Privacy → Ads" (wording varies by device and Android version). The Android version also follows the consent management (UMP) shown in applicable regions such as the EU.
- **Subscribing to KUU+ stops all ads and their related data transmission.**
- For details on AdMob's data handling, see the [Google AdMob privacy policy](https://support.google.com/admob/answer/6128543).

## Article 14 (Use of Firebase Analytics / Crashlytics)

**The opt-in model in this Article applies to the iOS version. For the Android version, see "About the Android version" at the end of this Article.**

**On iOS**, for app quality improvement and immediate awareness of production incidents, the App may use Google's Firebase Analytics (aggregated usage signals) and Firebase Crashlytics (crash reporting). **This feature is OFF by default (no data sent) and only operates when you explicitly opt in via "Settings → Data & Diagnostics".**

- **Information sent**:
  - Anonymized install ID auto-issued by Firebase (derived from IDFV; not a direct personal identifier)
  - Aggregated in-app event signals (recording-session completion, paywall view / conversion, onboarding completion etc. Numeric values are bucketed into coarse granularity.)
  - Symbolicated crash stack traces when the App terminates abnormally
- **Information not sent**: Your spoken content (audio), transcripts, AI-organized result text, and theme names you set are **made unsendable at the type level** (the implementation's API prevents passing string values to the analytics SDK).
- **While opt-in is OFF, no communication with Firebase occurs at all** (including all of the above categories).
- **How to stop sending**: Toggle "Settings → Data & Diagnostics" OFF at any time. When turned OFF, past install IDs are discarded and any unsent crash logs stored on-device are deleted.
- The recipient is Google LLC (United States). Google's [Firebase Privacy Information](https://firebase.google.com/support/privacy) applies.

**About the Android version:** The Android version uses Firebase Analytics to send **content-free usage events** for product improvement (bucketed values such as screen transitions and feature-usage counts) plus an anonymous App Instance ID issued by Firebase. **Unlike iOS, this is enabled by default.** Your spoken content (audio), transcripts, organized result text, and theme names **cannot be sent** — the analytics SDK's API is designed so that string values cannot be passed to it. **The Android version does not include Crashlytics and sends no crash reports.** The recipient is Google LLC (United States); Google's [Firebase Privacy Information](https://firebase.google.com/support/privacy) applies.
