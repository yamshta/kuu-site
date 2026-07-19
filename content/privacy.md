# KUU プライバシーポリシー

最終更新日：2026 年 8 月 X 日（2.3.0 リリース日に確定）

**ひとことで：** あなたが話したことはあなたのものです。**音声そのものは外部に送信しません**。文字起こしは端末の中で行います。整理（AI 分類）には既定で外部の AI を使いますが、送られるのは文字にした内容だけで、整理にのみ使われ、保存されません。保存先はあなたの端末と iCloud（プライベートデータベース）だけです。開発者は内容を保存せず、受け取った内容を見ることもありません。いつでもアプリ内から全データを削除できます。アプリは Apple の課金（StoreKit）と Google AdMob の広告のために**必要最小限の通信**のみ行い、その情報には話した内容は含まれません（広告は KUU+ 加入で無効化できます）。アプリの品質改善と本番事故の即知化のために、**ユーザーが明示的に opt-in した場合に限り** Firebase Analytics / Crashlytics を利用しますが、こちらも話した内容は含みません（詳細は第 14 条）。

---

## 第 1 条（基本方針）

本アプリ「KUU」（以下「本アプリ」）は、頭の中の考えごとを声で外に出し、整理することを支援する iOS アプリです。本アプリは、機能提供に必要な最小限の範囲でのみ情報を扱い、ユーザーのプライバシー保護を最優先とします。

## 第 2 条（取得・保存する情報）

本アプリが取り扱う情報は、以下に限られます。

1. **ユーザーが話した内容（音声データ）** — 録音した音声は文字起こしの処理中のみ端末内の一時領域に保存され、処理完了後すみやかに削除されます。サーバーには送信されません。
2. **文字起こし結果と整理結果（テキスト）** — あなた自身が見返せるように、端末および iCloud（プライベートデータベース）に保存されます。
3. **アプリ内設定** — テーマ、文字サイズ、頭の水位状態などのアプリ動作に必要な設定値。

本アプリは、氏名・メールアドレス・電話番号・位置情報・連絡先・カレンダー・写真・端末識別子等の個人情報を取得しません。

## 第 3 条（音声認識と AI 分類について）

**音声認識（文字起こし）** は、すべてお使いの iOS デバイス上で完結します。

- 音声認識：Apple の Speech フレームワーク（オンデバイス）を使用します。音声そのものが端末の外に送信されることはありません

**AI 分類（カテゴリ分け）** は、既定で外部の AI を使用します。

- 送信されるのは**文字にした内容（文字起こしテキスト）だけ**です。音声は送信されません
- 送信先は外部の AI で、開発者のサーバーを経由します
- 送信された内容は**分類にのみ使用され、保存されません**。AI の学習にも使用されません
- 送信対象は、話して文字になった内容のほか、手で入力・編集した内容も含みます。テーマの自動振り分け（KUU+・任意設定）を有効にしている場合は、振り分けのために保存済みの項目のタイトル・本文とテーマ名も送信されます（いずれも分類にのみ使用され、保存されません）
- バージョン 2.3.0 より前のアプリでは、設定「オンデバイス」で端末内のみの分類を選べます（2.3.0 以降はこの設定の提供を終了しました）

## 第 4 条（iCloud への保存と同期）

本アプリは、文字起こし結果と整理結果をあなたの **iCloud のプライベートデータベース**（CloudKit Private Database）にのみ保存します。これは Apple が提供するストレージで、保存内容にアクセスできるのはあなた本人だけです。本アプリの開発者は、保存された内容を閲覧することも、取得することもできません。

iCloud の利用条件・セキュリティについては、Apple のプライバシーポリシーが適用されます。

## 第 5 条（利用目的）

取り扱う情報は、以下の目的でのみ利用します。

1. 音声から文字起こしを生成し、ユーザーに表示する
2. 文字起こしを「いま見る／あとで考える／寝かせる／手放す」に分類してユーザーに表示する
3. ユーザーが過去に話した内容を、ユーザー自身が見返せるように保存・表示する
4. アプリの動作に必要な設定値を保持する

## 第 6 条（外部サービスの利用）

本アプリは、機能提供のために以下の外部サービスを利用します。**音声そのものは、いずれのサービスにも送信されません**。

- **iCloud / CloudKit**（Apple 提供。あなた自身のプライベートデータベースにのみ保存・同期）
- **Speech フレームワーク**（Apple 提供。完全に端末上で実行）
- **外部の AI（クラウド）**（既定の AI 分類。文字にした内容のみ送信。分類にのみ使用され、保存もされず、AI の学習にも使用されません。詳細は第 3 条）
- **Apple StoreKit**（KUU+ サブスクリプションの購入・更新・解約管理。話した内容は送信されません）
- **Google AdMob（Google Mobile Ads SDK）**（KUU+ 未加入時のみ、「話したこと」画面に節間のネイティブ広告 1 枠を表示。話した内容は送信されません。詳細は第 13 条）
- **Firebase Analytics / Crashlytics**（Google 提供。アプリの品質改善・安定性監視のため、**ユーザーが Settings で明示的に opt-in した場合にのみ**利用します。話した内容は送信されません。詳細は第 14 条）

本アプリのサーバーは AI 分類の中継のみを行う最小限のもので、内容を一切保存しません（ステートレス）。個人アカウントを要する認証サービスは使用しません。アクセス解析・クラッシュレポートはユーザーの opt-in を前提としてのみ動作します。

## 第 7 条（第三者提供）

本アプリの開発者は、ユーザーが話した内容、文字起こし結果、整理結果にアクセスする手段を持たず、これらを第三者に提供しません。

KUU+ 未加入のユーザーに広告を配信する目的で、Google AdMob に対して端末識別子・広告 ID・端末の言語・地域・概略の位置情報・広告のクリック情報など、AdMob が広告配信のために必要とする情報が Google に送信されます（詳細は第 13 条、Google の AdMob プライバシーポリシーが適用されます）。KUU+ に加入している間は、この情報送信は発生しません。

法令に基づき開示が義務付けられた場合に限り、所定の手続きに従い対応します。

## 第 8 条（データの削除）

ユーザーは、アプリ内の「設定 → 声とデータ → 保存していることの削除」からいつでも全データを削除できます。削除を行うと、端末上のデータおよび iCloud（プライベートデータベース）上のデータが完全に消去されます。消去したデータの復元はできません。

本アプリをアンインストールした場合、端末上のデータは削除されます。iCloud 上のデータは、Apple の設定（設定 → Apple ID → iCloud → ストレージ管理）から削除できます。

## 第 9 条（安全管理措置）

- 録音中の一時音声ファイルは、iOS のファイル保護機能（`FileProtectionType.complete`）により暗号化され、デバイスロック中はアクセスできません
- iCloud との通信は Apple が SSL/TLS で暗号化します
- 本アプリは独自サーバーを持たないため、開発者側で取り扱う情報そのものが存在しません

## 第 10 条（未成年者の利用）

本アプリは年齢区分 4+ で提供されますが、思考の整理という性質上、文字を読み書きできる年齢以上での利用を想定しています。未成年者が利用する場合は、保護者の同意を得たうえで利用してください。

## 第 11 条（プライバシーポリシーの変更）

本ポリシーは、法令の変更、機能の追加、Apple のフレームワーク仕様変更等により、改定されることがあります。重要な変更がある場合は、アプリのアップデート時または本ポリシーの公開ページで告知します。

## 第 12 条（お問い合わせ）

本ポリシーに関するお問い合わせは、App Store のアプリページ内「開発元」セクションよりご連絡ください。

## 第 13 条（広告と App Tracking Transparency について）

本アプリは KUU+ サブスクリプションに加入していない期間のみ、Google AdMob によるネイティブ広告を「話したこと」画面で 1 枠だけ表示します。広告そのものは KUU の世界観を保つため、画面の節間に控えめに表示されます。

- **話した内容を広告のために使うことはありません**（広告は文字起こし・分類結果・テーマを参照しません）
- 広告配信のために Google AdMob は端末識別子（IDFA を含む）、広告 ID、Coarse Location（概略の位置情報）、Diagnostics、Product Interaction（アプリ内の広告との接触情報）等を収集する場合があります
- iOS の **App Tracking Transparency**（ATT）プロンプトを最初の広告表示直前に 1 回だけ表示します。ユーザーが許諾しない場合でも広告は表示されますが、Google に送信される情報は限定的な範囲（パーソナライズなし）になります
- ATT 許諾状態は iOS の「設定」→「プライバシーとセキュリティ」→「トラッキング」からいつでも変更できます
- **KUU+ に加入すると広告と関連する情報送信はすべて停止します**
- Google AdMob によるデータ取り扱いの詳細は [Google AdMob プライバシーポリシー](https://support.google.com/admob/answer/6128543) をご確認ください

## 第 14 条（Firebase Analytics / Crashlytics の利用について）

本アプリは、アプリの品質改善および本番事故の即知化のために、Google の Firebase Analytics（利用状況の集計）および Firebase Crashlytics（クラッシュレポート）を利用することがあります。**本機能は既定で OFF（送信なし）であり、ユーザーが「設定 → データと診断」で明示的に opt-in した場合に限り動作します。**

- **送信される情報**:
  - Firebase が自動的に発行する匿名化された install ID（IDFV に基づく。個人を直接特定する識別子ではありません）
  - アプリ内の操作 event の集計シグナル（録音セッションの完走有無、Paywall の表示・購入転換、Onboarding 完了等の集計用 event。数値はバケット化された粗い粒度で送信）
  - アプリが異常終了した際の crash stack trace（symbol 化済み）
- **送信されない情報**: 話した内容（音声）、文字起こし結果、AI 分類結果のテキスト、ユーザーが設定したテーマ名は**型レベルで送信できない設計**になっています（実装上、計測 SDK に文字列値を渡せない API になっています）
- **opt-in されていない期間は、上記の情報を含む一切の通信が Firebase に対して発生しません**
- **送信を停止する手段**: 「設定 → データと診断」のトグルをいつでも OFF にできます。OFF にした時点で過去の install ID は破棄され、端末ローカルに保存されていた未送信の crash log も削除されます
- 送信先は Google LLC（米国）です。Google の [Firebase Privacy Information](https://firebase.google.com/support/privacy) が適用されます

---

# Privacy Policy for KUU

Last updated: August X, 2026 (to be finalized to the 2.3.0 release date)

**In short:** What you spoke is yours. **Your voice itself is never sent outside your device.** Transcription happens on your device. AI organization uses an external AI by default, but only the transcribed text is sent. It is used solely for organizing and is not retained by the AI provider. What is stored lives only on your device and in your iCloud (private database). The developer does not store your content and cannot view what is received. You can delete all data from inside the app at any time. The app makes only **minimal network requests** for Apple's billing (StoreKit) and Google AdMob ads, and that information never includes what you said (ads disappear with KUU+). For app quality improvement and immediate awareness of production incidents, Firebase Analytics / Crashlytics are used **only if you explicitly opt in**, and this too never includes what you said (see Article 14).

---

## Article 1 (General)

KUU (the "App") is an iOS application that helps you offload thoughts from your head by speaking them out loud and organizing them. The App processes information only to the minimum extent necessary to provide its features, prioritizing user privacy.

## Article 2 (Information Handled)

The App handles only the following:

1. **Audio you record** — Stored temporarily in a device-local cache only during transcription. Deleted immediately after processing. Never sent to any server.
2. **Transcribed and organized text** — Saved locally on your device and in your iCloud private database so you can review what you have said.
3. **App settings** — Theme, text size, head-water-level state, and other values required to run the App.

The App does not collect names, email addresses, phone numbers, location, contacts, calendar, photos, or device identifiers.

## Article 3 (Speech Recognition and AI Organization)

**Speech recognition (transcription)** is performed entirely on your iOS device:

- Speech recognition: Apple's Speech framework (on-device). Your voice itself is never sent off the device.

**AI organization (categorization)** uses an external AI by default:

- Only the **text of what you said (the transcript)** is sent. Your voice is never sent.
- It is sent to an external cloud AI, relayed through the developer's server.
- The sent text is **used only for categorization and is never stored**. It is not used to train the AI either.
- What is sent includes not only what you spoke and transcribed, but also anything you typed or edited by hand. If automatic theme assignment (KUU+, opt-in) is enabled, the saved titles, text, and theme names of items are also sent for assignment purposes (both are used only for classification and are not stored).
- Versions of the App before 2.3.0 let you choose on-device-only classification via "On-device" in Settings (this setting is no longer offered as of 2.3.0).

## Article 4 (iCloud Storage and Sync)

The App stores transcribed and organized text in your **iCloud Private Database** (CloudKit Private Database). This is Apple-provided storage that only you can access. The developer cannot view or retrieve any stored content.

The use of iCloud is subject to Apple's privacy policy.

## Article 5 (Purpose of Use)

Handled information is used only for:

1. Generating transcriptions from your voice and displaying them to you
2. Categorizing transcriptions into Now / Later / Park / Release and displaying them
3. Storing and displaying what you have spoken so you can review it
4. Maintaining app settings

## Article 6 (External Services)

The App uses the following external services. **Your voice itself is not sent to any of them.**

- **iCloud / CloudKit** (Apple, only your own private database)
- **Speech framework** (Apple, runs entirely on-device)
- **An external cloud AI** (default AI organization. Only the text of what you said is sent; used solely for categorization, never stored, never used for AI training. See Article 3.)
- **Apple StoreKit** (KUU+ subscription purchase, renewal, cancellation. No spoken content is sent.)
- **Google AdMob (Google Mobile Ads SDK)** (Only when KUU+ is not active: one native ad slot between sections in the "What you said" screen. No spoken content is sent. See Article 13.)
- **Firebase Analytics / Crashlytics** (Google. For app quality improvement and stability monitoring. **Used only when you explicitly opt in via Settings.** No spoken content is sent. See Article 14.)

The App operates a minimal stateless server only to relay AI organization requests (no content is stored). It does not use authentication services requiring personal accounts. Analytics and crash reporting are gated on user opt-in.

## Article 7 (Third-Party Disclosure)

The developer has no means to access your spoken content, transcripts, or organized results, and discloses none of them to any third party.

To deliver ads to users not subscribed to KUU+, the App sends information required by Google AdMob for ad delivery — including device identifiers, advertising ID, device language and region, coarse location, and ad interaction data — to Google (see Article 13; Google's AdMob privacy policy applies). While KUU+ is active, this transmission does not occur.

Information will only be disclosed when required by law.

## Article 8 (Data Deletion)

You can delete all data at any time from "Settings → Voice & Data → Delete what's stored" inside the App. This permanently removes data both on the device and in iCloud (Private Database). Deleted data cannot be recovered.

Uninstalling the App deletes local data. iCloud data can be removed via Settings → Apple ID → iCloud → Manage Storage.

## Article 9 (Security)

- Temporary audio files during recording are encrypted by iOS file protection (`FileProtectionType.complete`) and inaccessible while the device is locked
- Communication with iCloud is encrypted by Apple via SSL/TLS
- The App operates without any developer-managed server, so no developer-side information exists

## Article 10 (Use by Minors)

The App is rated 4+, but its nature (thought organization) presumes literacy. Minors should use it with the consent of their guardian.

## Article 11 (Changes to This Policy)

This policy may be updated due to changes in law, additions to features, or changes to Apple's framework specifications. Significant changes will be announced via an app update or on the public page of this policy.

## Article 12 (Contact)

For inquiries regarding this policy, please contact us through the "Developer" section on the App Store page of the App.

## Article 13 (Ads and App Tracking Transparency)

When you are not subscribed to KUU+, the App displays one native ad slot between sections in the "What you said" screen, served by Google AdMob. Ads are rendered quietly to fit KUU's tone.

- **Your spoken content is never used for ads.** Ads do not consult your transcripts, organized results, or themes.
- For ad delivery, Google AdMob may collect device identifiers (including IDFA), advertising ID, coarse location, diagnostics, and product interactions (ad-related interactions within the App).
- An iOS **App Tracking Transparency** (ATT) prompt is shown once, right before the first ad. Ads will still be shown if you decline, but the information sent to Google is restricted (non-personalized).
- You can change ATT permission at any time in iOS "Settings → Privacy & Security → Tracking".
- **Subscribing to KUU+ stops all ads and their related data transmission.**
- For details on AdMob's data handling, see the [Google AdMob privacy policy](https://support.google.com/admob/answer/6128543).

## Article 14 (Use of Firebase Analytics / Crashlytics)

For app quality improvement and immediate awareness of production incidents, the App may use Google's Firebase Analytics (aggregated usage signals) and Firebase Crashlytics (crash reporting). **This feature is OFF by default (no data sent) and only operates when you explicitly opt in via "Settings → Data & Diagnostics".**

- **Information sent**:
  - Anonymized install ID auto-issued by Firebase (derived from IDFV; not a direct personal identifier)
  - Aggregated in-app event signals (recording-session completion, paywall view / conversion, onboarding completion etc. Numeric values are bucketed into coarse granularity.)
  - Symbolicated crash stack traces when the App terminates abnormally
- **Information not sent**: Your spoken content (audio), transcripts, AI-organized result text, and theme names you set are **made unsendable at the type level** (the implementation's API prevents passing string values to the analytics SDK).
- **While opt-in is OFF, no communication with Firebase occurs at all** (including all of the above categories).
- **How to stop sending**: Toggle "Settings → Data & Diagnostics" OFF at any time. When turned OFF, past install IDs are discarded and any unsent crash logs stored on-device are deleted.
- The recipient is Google LLC (United States). Google's [Firebase Privacy Information](https://firebase.google.com/support/privacy) applies.
