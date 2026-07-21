# Privacy Policy for KUU

Last updated: July 21, 2026

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
