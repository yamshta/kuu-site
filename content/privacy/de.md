> Dies ist eine Referenzübersetzung. Maßgeblich ist die japanische Fassung.

# KUU Datenschutzrichtlinie

Letzte Aktualisierung: 21. Juli 2026

**Kurz gesagt:** Was Sie sagen, gehört Ihnen. **Ihre Stimme selbst wird niemals nach außen gesendet.** Die Transkription erfolgt auf Ihrem Gerät. Für die Organisation (KI-Kategorisierung) wird eine externe KI verwendet, aber es wird nur der transkribierte Text gesendet. Dieser wird ausschließlich für die Organisation verwendet und nicht gespeichert (in der iOS-Version können Sie in den Einstellungen unter „Auf dem Gerät“ zu einer rein geräteinternen Organisation wechseln. **Die Android-Version sendet immer an die externe KI; es gibt keine Option für eine Organisation auf dem Gerät**). Gespeichert wird auf Ihrem Gerät und in der iOS-Version zusätzlich in Ihrer iCloud (private Datenbank) (die Android-Version speichert nur auf dem Gerät). Der Entwickler speichert Ihre Inhalte nicht und kann die empfangenen Inhalte nicht einsehen. Sie können jederzeit alle Daten innerhalb der App löschen. Die App führt nur **absolut notwendige Netzwerkkommunikation** für Abrechnungen (iOS=StoreKit／Android=RevenueCat) und Werbung von Google AdMob durch, wobei diese Informationen niemals Ihre gesprochenen Inhalte umfassen (Werbung wird durch ein KUU+-Abonnement deaktiviert). Zur Qualitätsverbesserung wird die Nutzung gemessen, aber auch dies schließt Ihre gesprochenen Inhalte nicht ein (iOS erfordert ein Opt-in des Nutzers, Android führt standardmäßig eine inhaltsfreie Messung durch. Details in Artikel 14).

---

## Artikel 1 (Grundlegendes)

Diese Anwendung „KUU“ (nachfolgend „diese App“) ist eine App, die Sie dabei unterstützt, Ihre Gedanken laut auszusprechen und zu ordnen. Es gibt eine **iOS- und eine Android-Version**, und diese Richtlinie gilt für beide. Diese App verarbeitet Informationen nur im für die Bereitstellung der Funktionen absolut notwendigen Umfang und räumt dem Schutz der Privatsphäre der Nutzer höchste Priorität ein.

## Artikel 2 (Erfasste und gespeicherte Informationen)

Diese App verarbeitet ausschließlich die folgenden Informationen:

1.  **Ihre gesprochenen Inhalte (Audiodaten)** — Aufgenommene Audiodaten werden nur während der Transkription vorübergehend im lokalen Speicher des Geräts abgelegt und unmittelbar nach Abschluss der Verarbeitung gelöscht. Sie werden nicht an einen Server gesendet.
2.  **Transkriptions- und Organisationsergebnisse (Text)** — Werden gespeichert, damit Sie sie selbst einsehen können (iOS-Version: auf dem Gerät und in Ihrer privaten iCloud-Datenbank; Android-Version: nur auf dem Gerät. Details in Artikel 4).
3.  **App-Einstellungen** — Notwendige Einstellungswerte für den Betrieb der App wie Thema, Schriftgröße, Zustand des „Wasserpegels im Kopf“.

Diese App erfasst keine personenbezogenen Daten wie Name, E-Mail-Adresse, Telefonnummer, Standortinformationen, Kontakte, Kalender, Fotos oder Gerätekennungen.

## Artikel 3 (Spracherkennung und KI-Kategorisierung)

**Die Spracherkennung (Transkription)** erfolgt vollständig auf Ihrem iOS-Gerät.

-   Spracherkennung: Verwendet Apples Speech-Framework (on-device). Die Audiodaten selbst werden niemals außerhalb des Geräts gesendet.

**Die KI-Kategorisierung** verwendet eine externe KI.

-   Gesendet wird **nur der Inhalt des Gesprochenen (der transkribierte Text)**. Die Audiodaten werden nicht gesendet.
-   Der Empfänger ist eine externe KI, die über den Server des Entwicklers (über ein Backend zu Googles Gemini) weitergeleitet wird.
-   Die gesendeten Inhalte werden **ausschließlich zur Kategorisierung verwendet und nicht gespeichert**. Sie werden auch nicht zum Trainieren der KI verwendet.
-   **iOS-Version**: Sie können jederzeit in den Einstellungen unter „Auf dem Gerät“ zu einer **rein geräteinternen Kategorisierung** (Apples FoundationModels / geräteinterne Regeln) wechseln. In diesem Fall verlässt auch der Text das Gerät nicht.

**Zur Android-Version:** Die Android-Version bietet keine Organisationsmethode (Kategorisierung), die vollständig auf dem Gerät abläuft. Wenn Sie eine Organisation durchführen, wird der transkribierte Text **immer** an die externe KI (Googles Gemini über unser Backend) gesendet. Einen Wechsel zu „Auf dem Gerät“ wie in der iOS-Version gibt es nicht. Es wird nur der transkribierte Inhalt gesendet, nicht die Stimme selbst, und der gesendete Text wird ausschließlich zur Kategorisierung verwendet, nicht gespeichert und auch nicht zum Trainieren der KI genutzt. Die Transkription (Spracherkennung) selbst findet vollständig auf dem Gerät statt.

## Artikel 4 (Speicherung und Synchronisierung)

**iOS-Version:** Die Transkriptions- und Organisationsergebnisse werden ausschließlich in Ihrer **privaten iCloud-Datenbank** (CloudKit Private Database) gespeichert. Dies ist ein von Apple bereitgestellter Speicher, auf den nur Sie selbst zugreifen können. Der Entwickler dieser App kann die gespeicherten Inhalte weder einsehen noch abrufen. Für die Nutzung von iCloud gilt die Datenschutzrichtlinie von Apple.

**Android-Version:** Die Transkriptions- und Organisationsergebnisse werden **nur auf diesem Gerät** gespeichert. Eine automatische Cloud-Synchronisierung findet nicht statt. Bei einem Gerätewechsel können Sie die Daten über „Stimme & Daten“ in der App in eine Datei exportieren und auf dem neuen Gerät importieren. Den Speicherort der Exportdatei wählen Sie selbst (auf dem Gerät, in Ihrer Cloud-Speicher-App etc.). Der Entwickler hat keinen Zugriff auf diese Datei.

## Artikel 5 (Verwendungszweck)

Die verarbeiteten Informationen werden ausschließlich für die folgenden Zwecke verwendet:

1.  Erstellung von Transkriptionen aus Ihrer Stimme und deren Anzeige für Sie
2.  Kategorisierung der Transkriptionen in „Jetzt ansehen / Später bedenken / Ruhen lassen / Loslassen“ und deren Anzeige für Sie
3.  Speicherung und Anzeige Ihrer früher gesprochenen Inhalte, damit Sie sie selbst einsehen können
4.  Beibehaltung der für den Betrieb der App notwendigen Einstellungswerte

## Artikel 6 (Nutzung externer Dienste)

Diese App nutzt die folgenden externen Dienste zur Bereitstellung ihrer Funktionen. **Ihre Stimme selbst wird an keinen dieser Dienste gesendet.**

-   **iCloud / CloudKit** (nur iOS-Version. Von Apple bereitgestellt. Speicherung und Synchronisierung nur in Ihrer eigenen privaten Datenbank)
-   **Spracherkennung** (iOS-Version: Apples Speech-Framework; Android-Version: geräteinterne Spracherkennungs-Engine. Beide laufen auf dem Gerät; Ihre Stimme wird nicht nach außen gesendet)
-   **Externe KI (Cloud)** (KI-Kategorisierung. Nur der transkribierte Inhalt wird gesendet. Wird ausschließlich zur Kategorisierung verwendet, nicht gespeichert und nicht zum Trainieren der KI genutzt. In der iOS-Version kann dies über die Einstellung „Auf dem Gerät“ deaktiviert werden, aber **die Android-Version sendet immer an die externe KI**. Details in Artikel 3)
-   **FoundationModels** (nur iOS-Version. Von Apple bereitgestellt. Läuft vollständig auf dem Gerät. Wird bei aktivierter „Auf dem Gerät“-Einstellung und als Fallback verwendet, wenn die externe KI nicht verfügbar ist)
-   **Abrechnungsdienste** (iOS-Version: **Apple StoreKit**; Android-Version: **RevenueCat**. Kauf, Verlängerung, Kündigung und Verwaltung des KUU+-Abonnementstatus. Ihre gesprochenen Inhalte werden nicht gesendet. Zu RevenueCat siehe Artikel 7 und die [RevenueCat-Datenschutzrichtlinie](https://www.revenuecat.com/privacy))
-   **Play Integrity API (über Firebase App Check; nur Android-Version)** (Integritätsnachweis für Gerät und App, um zu bestätigen, dass Anfragen an die Klassifizierungs-API von einer legitimen App stammen. Enthält keine gesprochenen Inhalte oder benutzeridentifizierende Informationen)
-   **Google AdMob (Google Mobile Ads SDK)** (Nur wenn kein KUU+-Abonnement besteht, wird ein nativer Werbeplatz zwischen den Abschnitten auf dem „Was du gesagt hast“-Bildschirm angezeigt. Ihre gesprochenen Inhalte werden nicht gesendet. Details in Artikel 13)
-   **Firebase Analytics** (Von Google bereitgestellt. Zur Qualitätsverbesserung der App. In der iOS-Version **nur, wenn der Nutzer in den Einstellungen explizit zustimmt (Opt-in)**; in der Android-Version werden **standardmäßig** inhaltsfreie Nutzungsereignisse gesendet (in beiden Fällen werden keine gesprochenen Inhalte gesendet). Die iOS-Version nutzt bei Opt-in auch **Crashlytics**, aber **die Android-Version enthält kein Crashlytics**. Details in Artikel 14)

Der Server dieser App dient lediglich als Relay für die KI-Kategorisierung und speichert keinerlei Inhalte (zustandslos). Es werden keine Authentifizierungsdienste verwendet, die ein persönliches Konto erfordern.

## Artikel 7 (Weitergabe an Dritte)

Der Entwickler dieser App hat keine Möglichkeit, auf Ihre gesprochenen Inhalte, Transkriptionsergebnisse oder Organisationsergebnisse zuzugreifen und gibt diese nicht an Dritte weiter.

Zum Zweck der Auslieferung von Werbung an Nutzer ohne KUU+-Abonnement werden Informationen, die Google AdMob für die Werbeauslieferung benötigt, an Google gesendet. Dazu gehören Gerätekennungen, Werbe-ID, Gerätesprache, Region, grobe Standortinformationen und Informationen zu Werbeinteraktionen (Details in Artikel 13; es gilt die AdMob-Datenschutzrichtlinie von Google). Während Sie ein KUU+-Abonnement haben, findet diese Datenübertragung nicht statt.

Wenn Sie in der **Android-Version** ein KUU+-Abonnement abschließen, werden Kaufinformationen (Produkt-ID, Preis, Kaufdatum etc.) an RevenueCat, Inc. zur Abwicklung des Kaufs und zur Verwaltung Ihres Abonnementstatus (aktiv/inaktiv) gesendet. Ihre gesprochenen Inhalte werden nicht gesendet. Details zur Datenverarbeitung durch RevenueCat finden Sie in der [RevenueCat-Datenschutzrichtlinie](https://www.revenuecat.com/privacy).

Eine Offenlegung erfolgt nur, wenn dies gesetzlich vorgeschrieben ist und nach dem vorgeschriebenen Verfahren.

## Artikel 8 (Löschung von Daten)

Sie können jederzeit alle Daten über „Einstellungen → Stimme & Daten → Gespeicherte Inhalte löschen“ in der App löschen. Dadurch werden die Daten auf dem Gerät (bei der iOS-Version auch die Daten in der privaten iCloud-Datenbank) vollständig entfernt. Gelöschte Daten können nicht wiederhergestellt werden.

Bei der Deinstallation dieser App werden die Daten auf dem Gerät gelöscht. Die iCloud-Daten der iOS-Version können über die Apple-Einstellungen (Einstellungen → Apple-ID → iCloud → Speicher verwalten) gelöscht werden. Da die Android-Version Daten nur auf dem Gerät speichert, werden diese bei der Deinstallation entfernt.

## Artikel 9 (Sicherheitsmaßnahmen)

-   **iOS-Version**: Temporäre Audiodateien während der Aufnahme werden durch die Dateischutzfunktion von iOS (`FileProtectionType.complete`) verschlüsselt und sind bei gesperrtem Gerät unzugänglich. Die Kommunikation mit iCloud wird von Apple per SSL/TLS verschlüsselt.
-   **Android-Version**: Aufgenommene Audiodaten werden nicht einmal als temporäre Datei auf die Festplatte geschrieben, sondern nur im Speicher verarbeitet und sofort nach der Erkennung verworfen. Gespeicherte Transkriptions- und Organisationsergebnisse werden im app-spezifischen Bereich von Android gespeichert und sind für andere Apps unzugänglich. Sie sind zudem von der automatischen Cloud-Sicherung von Android ausgeschlossen.
-   Jegliche Kommunikation mit der externen KI wird verschlüsselt (HTTPS/TLS). Der Server des Entwicklers dient nur als Relay für die Kategorisierung und speichert keine Inhalte (zustandslos).

## Artikel 10 (Nutzung durch Minderjährige)

Diese App wird mit der Altersfreigabe 4+ angeboten, ist aber aufgrund ihres Charakters (Gedankenorganisation) für Nutzer gedacht, die lesen und schreiben können. Minderjährige sollten die App nur mit Zustimmung eines Erziehungsberechtigten nutzen.

## Artikel 11 (Änderungen dieser Richtlinie)

Diese Richtlinie kann aufgrund von Gesetzesänderungen, neuen Funktionen oder Änderungen in den Spezifikationen der Frameworks oder Richtlinien der jeweiligen Plattformen (Apple / Google) überarbeitet werden. Wesentliche Änderungen werden bei einem App-Update oder auf der öffentlichen Seite dieser Richtlinie bekannt gegeben.

## Artikel 12 (Kontakt)

Anfragen zu dieser Richtlinie richten Sie bitte über den Abschnitt „Entwickler“ auf der App-Seite im App Store oder bei Google Play oder über „Einstellungen → Kontakt“ in der App an uns.

## Artikel 13 (Werbung und App Tracking Transparency)

Solange Sie kein KUU+-Abonnement haben, zeigt diese App einen einzigen nativen Werbeplatz von Google AdMob auf dem „Was du gesagt hast“-Bildschirm an. Die Werbung selbst wird dezent zwischen den Abschnitten platziert, um die Atmosphäre von KUU zu wahren.

-   **Ihre gesprochenen Inhalte werden niemals für Werbung verwendet.** (Die Werbung greift nicht auf Transkriptionen, Organisationsergebnisse oder Themen zu.)
-   Für die Werbeauslieferung kann Google AdMob Gerätekennungen (einschließlich IDFA), Werbe-ID, grobe Standortinformationen (Coarse Location), Diagnosedaten und Produktinteraktionen (Interaktionen mit Werbung innerhalb der App) erfassen.
-   **iOS-Version**: Eine **App Tracking Transparency** (ATT)-Aufforderung wird einmalig direkt vor der ersten Werbeanzeige angezeigt. Auch wenn Sie ablehnen, wird Werbung angezeigt, aber die an Google gesendeten Informationen sind auf einen begrenzten Umfang (nicht personalisiert) beschränkt. Sie können die ATT-Berechtigung jederzeit in den iOS-Einstellungen unter „Datenschutz & Sicherheit“ → „Tracking“ ändern.
-   **Android-Version**: ATT ist ein reiner iOS-Mechanismus und existiert nicht auf Android. Stattdessen wird die **Werbe-ID (Advertising ID)** von Google für die Werbeauslieferung verwendet. Sie können die Personalisierung von Werbung in den Einstellungen Ihres Geräts unter „Einstellungen → Datenschutz → Anzeigen“ (die Formulierung kann je nach Gerät und Android-Version variieren) deaktivieren oder Ihre Werbe-ID zurücksetzen. Zusätzlich befolgt die Android-Version die in anwendbaren Regionen wie der EU angezeigte Einwilligungsverwaltung (UMP).
-   **Mit einem KUU+-Abonnement werden jegliche Werbung und die damit verbundene Datenübertragung gestoppt.**
-   Details zur Datenverarbeitung durch Google AdMob finden Sie in der [Google AdMob-Datenschutzrichtlinie](https://support.google.com/admob/answer/6128543).

## Artikel 14 (Nutzung von Firebase Analytics / Crashlytics)

**Das in diesem Artikel beschriebene Opt-in-Verfahren gilt für die iOS-Version. Für die Android-Version siehe den Abschnitt „Zur Android-Version“ am Ende dieses Artikels.**

**Die iOS-Version** kann zur Qualitätsverbesserung der App und zur sofortigen Erkennung von Produktionsproblemen Googles Firebase Analytics (aggregierte Nutzungsdaten) und Firebase Crashlytics (Absturzberichte) verwenden. **Diese Funktion ist standardmäßig AUS (keine Datenübertragung) und wird nur aktiviert, wenn Sie in „Einstellungen → Daten & Diagnose“ explizit zustimmen (Opt-in).**

-   **Gesendete Informationen**:
    -   Eine von Firebase automatisch ausgestellte anonymisierte Installations-ID (basiert auf IDFV; keine direkt persönlich identifizierbare Kennung).
    -   Aggregierte Signale zu In-App-Ereignissen (z. B. Abschluss von Aufnahmesitzungen, Anzeige/Konversion von Paywalls, Abschluss des Onboardings. Numerische Werte werden in groben, gebündelten Einheiten gesendet).
    -   Symbolisierte Stack-Traces bei abnormaler Beendigung der App.
-   **Nicht gesendete Informationen**: Ihre gesprochenen Inhalte (Audio), Transkriptionen, KI-Organisationsergebnisse und die von Ihnen festgelegten Themennamen sind **auf Typebene so konzipiert, dass sie nicht gesendet werden können** (die Implementierung der API verhindert die Übergabe von Zeichenkettenwerten an das Analyse-SDK).
-   **Solange kein Opt-in erfolgt ist, findet keinerlei Kommunikation mit Firebase statt** (einschließlich aller oben genannten Kategorien).
-   **Möglichkeit zum Beenden der Übertragung**: Sie können den Schalter in „Einstellungen → Daten & Diagnose“ jederzeit auf AUS stellen. Dadurch wird die bisherige Installations-ID verworfen und alle auf dem Gerät gespeicherten, noch nicht gesendeten Absturzprotokolle werden gelöscht.
-   Empfänger ist Google LLC (USA). Es gelten die [Firebase-Datenschutzinformationen](https://firebase.google.com/support/privacy) von Google.

**Zur Android-Version:** Die Android-Version verwendet Firebase Analytics und sendet zur Produktverbesserung **inhaltsfreie Nutzungsereignisse** (gebündelte Werte wie Bildschirmwechsel und Häufigkeit der Funktionsnutzung) sowie eine von Firebase ausgestellte anonyme App-Instanz-ID. **Im Gegensatz zur iOS-Version ist dies standardmäßig aktiviert.** Ihre gesprochenen Inhalte (Audio), Transkriptionen, Organisationsergebnisse und Themennamen **können nicht gesendet werden**, da die API des Analyse-SDKs so konzipiert ist, dass keine Zeichenkettenwerte übergeben werden können. **Die Android-Version enthält kein Crashlytics und sendet keine Absturzberichte.** Empfänger ist Google LLC (USA); es gelten die [Firebase-Datenschutzinformationen](https://firebase.google.com/support/privacy) von Google.
