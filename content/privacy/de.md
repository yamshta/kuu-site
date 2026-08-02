> Dies ist eine unverbindliche Übersetzung. Maßgeblich ist die japanische Fassung.

# KUU Datenschutzrichtlinie

Letzte Aktualisierung: 2. August 2026

**Kurz gesagt:** Was Sie sprechen, gehört Ihnen. **Die App sendet niemals Ihre Stimme selbst nach außen**. Auf iPhone- und Android-Geräten findet auch die Transkription auf dem Gerät statt. **Die Apple-Watch-Version dieser App führt keine Aufnahmen durch** und empfängt nur den Text, der über die Standardeingabe der Watch (Spracheingabe, Handschrift, Tastatur) erzeugt wird (bei Auswahl der Spracheingabe erfolgt die Erkennung durch Apples System; Details in Artikel 3). Für die Gliederung (KI-Kategorisierung) wird eine externe KI genutzt, an die jedoch nur der transkribierte Text gesendet wird. Dieser wird ausschließlich für die Gliederung verwendet und nicht gespeichert. Gespeichert wird auf Ihrem Gerät und bei der iOS-Version zusätzlich in Ihrer privaten iCloud-Datenbank (die Android-Version speichert nur auf dem Gerät). Der Entwickler speichert Ihre Inhalte nicht und kann die empfangenen Daten nicht einsehen. Sie können jederzeit alle Daten aus der App heraus löschen. Die App führt nur **absolut notwendige Netzwerkkommunikation** für die Abrechnung (iOS=StoreKit／Android=RevenueCat) und für Werbung von Google AdMob durch. Diese Kommunikation enthält niemals Ihre gesprochenen Inhalte (Werbung kann durch ein KUU+-Abonnement deaktiviert werden). Zur Qualitätsverbesserung wird die Nutzung gemessen, aber auch dies schließt Ihre gesprochenen Inhalte nicht ein (iOS erfordert ein Opt-in des Nutzers, Android führt eine inhaltsfreie Messung standardmäßig durch; Details in Artikel 14).

---

## Artikel 1 (Grundprinzipien)

Die App „KUU“ (im Folgenden „diese App“) ist eine Anwendung, die Sie dabei unterstützt, Ihre Gedanken laut auszusprechen und zu ordnen. Sie ist für **iOS (iPhone und Apple Watch) und Android** verfügbar, und diese Richtlinie gilt für beide Versionen. Diese App verarbeitet Informationen nur im für die Bereitstellung ihrer Funktionen minimal erforderlichen Umfang und räumt dem Schutz der Privatsphäre der Nutzer höchste Priorität ein.

## Artikel 2 (Erfasste und gespeicherte Informationen)

Diese App verarbeitet ausschließlich die folgenden Informationen:

1.  **Von Ihnen gesprochene Inhalte (Audiodaten)** — Aufgenommene Audiodaten werden nur während der Transkription temporär auf dem Gerät gespeichert und nach Abschluss der Verarbeitung umgehend gelöscht. Sie werden nicht an einen Server gesendet. **Die Apple-Watch-Version dieser App führt keine Aufnahmen durch** (Artikel 3).
2.  **Transkriptions- und Gliederungsergebnisse (Text)** — Werden gespeichert, damit Sie sie selbst einsehen können (iOS-Version: auf dem Gerät und in Ihrer privaten iCloud-Datenbank; Android-Version: nur auf dem Gerät. Auf einer gekoppelten Apple Watch werden zur Anzeige nur die letzten Titel jeder Kategorie gespeichert; Details in Artikel 4).
3.  **App-Einstellungen** — Design, Schriftgröße, Wasserstand-Status und andere für den Betrieb der App notwendige Einstellungswerte.

Diese App erfasst keine personenbezogenen Daten wie Namen, E-Mail-Adressen, Telefonnummern, Standortdaten, Kontakte, Kalender, Fotos oder Gerätekennungen.

## Artikel 3 (Über Spracherkennung und KI-Kategorisierung)

**Spracherkennung (Transkription)**: Auf dem iPhone (iOS-Version) und auf Android-Geräten erfolgt die Spracherkennung vollständig auf Ihrem Gerät (zur Apple-Watch-Version siehe Ende dieses Artikels).

-   Spracherkennung: Apple Speech Framework (on-device). Die Audiodaten selbst werden nicht vom Gerät gesendet.

**KI-Kategorisierung** nutzt eine externe KI.

-   Es wird **nur der transkribierte Text** gesendet. Die Audiodaten werden nicht gesendet.
-   Die Übertragung erfolgt an eine externe KI (Googles Gemini) über den Server des Entwicklers (Backend).
-   Die gesendeten Inhalte werden **ausschließlich zur Kategorisierung verwendet und nicht gespeichert**. Sie werden auch nicht für das Training der KI verwendet.
-   Gesendet werden nicht nur die gesprochenen und transkribierten Inhalte, sondern auch manuell eingegebene oder bearbeitete Texte. Wenn die automatische Themenzuweisung (KUU+, optionale Einstellung) aktiviert ist, werden zur Zuweisung auch Titel, Text und Themennamen bereits gespeicherter Einträge gesendet (alle diese Daten werden ebenfalls nur zur Kategorisierung verwendet und nicht gespeichert).
-   **iOS-Version**: In App-Versionen vor 2.3.0 konnten Sie unter „Einstellungen“ eine rein geräteinterne Kategorisierung wählen (diese Option wird ab Version 2.3.0 nicht mehr angeboten).

**Über die Android-Version:** Die Android-Version bietet keine Möglichkeit zur rein geräteinternen Organisation (Kategorisierung). Bei der Organisation wird der transkribierte Text **immer** an eine externe KI (Googles Gemini über unser Backend) gesendet. Es wird nur der Text gesendet, nicht die Audiodaten selbst. Der gesendete Text wird ausschließlich zur Kategorisierung verwendet, nicht gespeichert und nicht für das KI-Training genutzt. Die Transkription (Spracherkennung) selbst findet vollständig auf dem Gerät statt.

**Über die Apple-Watch-Version:** Die Apple-Watch-Version dieser App führt weder Aufnahmen noch Spracherkennung durch. Für die Eingabe wird die Standard-Texteingabe von watchOS verwendet (Spracheingabe, Handschrift oder Tastatur, nach Wahl des Nutzers), und diese App empfängt nur den daraus resultierenden Text. Wenn die Spracheingabe gewählt wird, erfolgt die Spracherkennung als Funktion von Apple (watchOS). Deren Verarbeitung – einschließlich der Frage, ob sie auf dem Gerät oder auf Apples Servern stattfindet – hängt von Ihrem Gerätemodell, Ihren Einstellungen und Ihrer Sprache ab, und es gilt die **Datenschutzrichtlinie von Apple**. Diese App hat keinen Zugriff auf die Audiodaten und empfängt oder speichert sie nicht. Der empfangene Text wird genauso behandelt wie auf dem iPhone gesprochener Text (KI-Kategorisierung gemäß diesem Artikel, Speicherung gemäß Artikel 4).

## Artikel 4 (Speicherung und Synchronisierung)

**iOS-Version:** Transkriptions- und Gliederungsergebnisse werden ausschließlich in Ihrer **privaten iCloud-Datenbank** (CloudKit Private Database) gespeichert. Dies ist ein von Apple bereitgestellter Speicher, auf den nur Sie selbst zugreifen können. Der Entwickler dieser App kann die gespeicherten Inhalte weder einsehen noch abrufen. Für die Nutzung von iCloud gelten die Nutzungs- und Sicherheitsbestimmungen der Datenschutzrichtlinie von Apple.

**Android-Version:** Transkriptions- und Gliederungsergebnisse werden **nur auf diesem Gerät** gespeichert. Eine automatische Cloud-Synchronisierung findet nicht statt. Bei einem Gerätewechsel können Sie die Daten in der App unter „Stimme & Daten“ in eine Datei exportieren und auf dem neuen Gerät importieren. Den Speicherort der Exportdatei wählen Sie selbst (z. B. auf dem Gerät oder in einer von Ihnen genutzten Cloud-Speicher-App). Der Entwickler hat keinen Zugriff auf diese Datei.

**Apple-Watch-Version:** Zu Anzeigezwecken wird ein Teil Ihrer Gliederungsergebnisse (die letzten Titel jeder Kategorie) über Apples geräteinterne Kommunikation (Watch Connectivity) an die gekoppelte Apple Watch übertragen und **auch auf der Apple Watch gespeichert**. Auf der Apple Watch eingegebener Text wird über den gleichen Mechanismus an das iPhone übertragen. An dieser Übertragung und Speicherung ist kein Server des Entwicklers beteiligt.

## Artikel 5 (Verwendungszweck)

Die verarbeiteten Informationen werden ausschließlich für die folgenden Zwecke verwendet:

1.  Erstellung von Transkriptionen aus Ihrer Stimme und deren Anzeige für Sie
2.  Kategorisierung von Transkriptionen in „Jetzt ansehen / Später ansehen / Ruhen lassen / Loslassen“ und deren Anzeige für Sie
3.  Speicherung und Anzeige Ihrer gesprochenen Inhalte, damit Sie sie selbst einsehen können
4.  Speicherung von für den Betrieb der App notwendigen Einstellungswerten

## Artikel 6 (Nutzung externer Dienste)

Diese App nutzt für die Bereitstellung ihrer Funktionen die folgenden externen Dienste. **Ihre Audiodaten selbst werden an keinen dieser Dienste gesendet.**

-   **iCloud / CloudKit** (nur iOS-Version; Apple; Speicherung und Synchronisierung nur in Ihrer eigenen privaten Datenbank)
-   **Spracherkennung** (iOS-Version: Apple Speech Framework; Android-Version: geräteinterne Spracherkennungs-Engine. Beide werden auf dem Gerät ausgeführt, Audiodaten werden nicht vom Gerät gesendet. **Die Apple-Watch-Version führt keine eigene Spracherkennung durch und verwendet die Standardeingabe von watchOS.** Siehe Artikel 3).
-   **Standard-Texteingabe von watchOS** (nur Apple-Watch-Version; Apple; Nutzer wählt zwischen Spracheingabe, Handschrift und Tastatur. Bei Spracheingabe erfolgt die Erkennung als Funktion von Apple und es gilt Apples Datenschutzrichtlinie. Diese App hat keinen Zugriff auf die Audiodaten. Details in Artikel 3).
-   **Watch Connectivity** (nur Apple-Watch-Version; Apple; Direkter Austausch von Anzeigetexten zwischen iPhone und Apple Watch. Kein Server des Entwicklers beteiligt. Details in Artikel 4).
-   **Externe KI (Cloud)** (KI-Kategorisierung; nur der Text wird gesendet; wird ausschließlich zur Kategorisierung verwendet, nicht gespeichert und nicht für das KI-Training genutzt. Details in Artikel 3).
-   **Abrechnungsdienste** (iOS-Version: **Apple StoreKit**, Android-Version: **RevenueCat**. Kauf, Verlängerung, Kündigung und Verwaltung des KUU+-Abonnements. Gesprochene Inhalte werden nicht gesendet. Zu RevenueCat siehe Artikel 7 und die [RevenueCat-Datenschutzrichtlinie](https://www.revenuecat.com/privacy)).
-   **Play Integrity API (über Firebase App Check; nur Android-Version)** (Integritätsprüfung von Gerät und App, um sicherzustellen, dass Anfragen an die Klassifizierungs-API von einer legitimen App stammen. Enthält keine gesprochenen Inhalte oder nutzeridentifizierende Informationen).
-   **Google AdMob (Google Mobile Ads SDK)** (Nur für Nutzer ohne KUU+-Abonnement: Anzeige eines nativen Werbeplatzes zwischen den Abschnitten auf dem „Gesprochenes“-Bildschirm. Gesprochene Inhalte werden nicht gesendet. Details in Artikel 13).
-   **Firebase Analytics** (Google; zur Qualitätsverbesserung der App. iOS-Version: **nur bei explizitem Opt-in des Nutzers in den Einstellungen**; Android-Version: sendet **standardmäßig** inhaltsfreie Nutzungsereignisse (in beiden Fällen werden keine gesprochenen Inhalte gesendet). iOS-Version nutzt bei Opt-in auch **Crashlytics**, aber **die Android-Version enthält kein Crashlytics**. Details in Artikel 14).

Der Server dieser App dient lediglich als zustandslose (stateless) Vermittlungsstelle für die KI-Kategorisierung und speichert keinerlei Inhalte. Es werden keine Authentifizierungsdienste genutzt, die ein persönliches Konto erfordern.

## Artikel 7 (Weitergabe an Dritte)

Der Entwickler dieser App hat keine Möglichkeit, auf Ihre gesprochenen Inhalte, Transkriptionen oder Gliederungsergebnisse zuzugreifen, und gibt diese nicht an Dritte weiter.

Zum Zweck der Auslieferung von Werbung an Nutzer ohne KUU+-Abonnement werden an Google AdMob Informationen gesendet, die für die Werbeauslieferung erforderlich sind, darunter Gerätekennungen, Werbe-IDs, Sprache und Region des Geräts, grobe Standortdaten sowie Informationen zur Interaktion mit der Werbung. (Details in Artikel 13; es gilt die AdMob-Datenschutzrichtlinie von Google). Während Ihr KUU+-Abonnement aktiv ist, findet diese Datenübertragung nicht statt.

Bei Abschluss eines KUU+-Abonnements über die **Android-Version** werden Kaufinformationen (Produkt-ID, Preis, Kaufdatum etc.) an RevenueCat, Inc. gesendet, um den Kauf abzuwickeln und Ihren Abonnementstatus (aktiv/inaktiv) zu verwalten. Gesprochene Inhalte werden nicht gesendet. Details zur Datenverarbeitung durch RevenueCat finden Sie in der [RevenueCat-Datenschutzrichtlinie](https://www.revenuecat.com/privacy).

Eine Offenlegung erfolgt nur dann, wenn dies gesetzlich vorgeschrieben ist, und nur im Einklang mit den vorgeschriebenen Verfahren.

## Artikel 8 (Löschen von Daten)

Sie können jederzeit alle Daten über „Einstellungen → Stimme & Daten → Gespeicherte Daten löschen“ in der App löschen. Dadurch werden die Daten auf dem Gerät (bei der iOS-Version auch die Daten in der privaten iCloud-Datenbank) dauerhaft entfernt. Gelöschte Daten können nicht wiederhergestellt werden.

Bei Deinstallation der App werden die auf dem Gerät gespeicherten Daten gelöscht. Die iCloud-Daten der iOS-Version können über die Apple-Einstellungen (Einstellungen → Apple-ID → iCloud → Speicher verwalten) gelöscht werden. Da die Android-Version nur auf dem Gerät speichert, werden die Daten bei der Deinstallation entfernt.

**Apple-Watch-Version:** Wenn Sie alle Daten löschen, werden auch die zur Anzeige auf die Apple Watch übertragenen Daten bei der nächsten Verbindung mit der Apple Watch durch leere Inhalte ersetzt. Wenn Sie die App von der Apple Watch entfernen, werden die auf der Watch gespeicherten Anzeigedaten ebenfalls gelöscht.

## Artikel 9 (Sicherheitsmaßnahmen)

-   **iOS-Version**: Temporäre Audiodateien während der Aufnahme werden durch die iOS-Dateischutzfunktion (`FileProtectionType.complete`) verschlüsselt und sind bei gesperrtem Gerät unzugänglich. Die Kommunikation mit iCloud wird von Apple mittels SSL/TLS verschlüsselt.
-   **Android-Version**: Aufgenommene Audiodaten werden nicht einmal als temporäre Datei auf die Festplatte geschrieben, sondern nur im Arbeitsspeicher verarbeitet und nach der Erkennung sofort verworfen. Gespeicherte Transkriptions- und Gliederungsergebnisse werden im app-spezifischen Speicherbereich von Android abgelegt, auf den andere Apps nicht zugreifen können. Sie sind zudem von der automatischen Cloud-Sicherung von Android ausgeschlossen.
-   **Apple-Watch-Version**: Der Datenaustausch zwischen iPhone und Apple Watch erfolgt über Apples Watch Connectivity und nicht über einen Server des Entwicklers. Auf der Apple Watch werden nur Anzeigetexte (die letzten Titel jeder Kategorie) gespeichert, keine Audiodaten.
-   Die gesamte Kommunikation mit der externen KI ist verschlüsselt (HTTPS/TLS). Der Server des Entwicklers dient nur als Vermittlungsstelle für die Gliederung und speichert keine Inhalte (zustandslos).

## Artikel 10 (Nutzung durch Minderjährige)

Die App hat die Altersfreigabe 4+, ist aber aufgrund ihres Zwecks (Gedanken ordnen) für Nutzer gedacht, die lesen und schreiben können. Minderjährige sollten die App nur mit Zustimmung eines Erziehungsberechtigten nutzen.

## Artikel 11 (Änderungen dieser Datenschutzrichtlinie)

Diese Richtlinie kann aufgrund von Gesetzesänderungen, neuen Funktionen oder Änderungen in den Spezifikationen der jeweiligen Plattform-Frameworks oder -Richtlinien (Apple / Google) aktualisiert werden. Wesentliche Änderungen werden bei einem App-Update oder auf der Veröffentlichungsseite dieser Richtlinie bekannt gegeben.

## Artikel 12 (Kontakt)

Bei Fragen zu dieser Richtlinie kontaktieren Sie uns bitte über den Abschnitt „Entwickler“ auf der App-Seite im App Store oder bei Google Play oder über „Einstellungen → Kontakt“ in der App.

## Artikel 13 (Über Werbung und App-Tracking-Transparenz)

Solange Sie kein KUU+-Abonnement haben, zeigt diese App einen von Google AdMob bereitgestellten nativen Werbeplatz auf dem „Gesprochenes“-Bildschirm an. Die Werbung selbst wird dezent zwischen den Abschnitten platziert, um die Atmosphäre von KUU zu wahren.

-   **Ihre gesprochenen Inhalte werden niemals für Werbezwecke verwendet** (die Werbung greift nicht auf Ihre Transkriptionen, Gliederungsergebnisse oder Themen zu).
-   Für die Werbeauslieferung kann Google AdMob Gerätekennungen (einschließlich IDFA), Werbe-IDs, grobe Standortdaten (Coarse Location), Diagnosedaten und Produktinteraktionen (Interaktionen mit Werbung innerhalb der App) erfassen.
-   **iOS-Version**: Eine **App Tracking Transparency (ATT)**-Abfrage wird einmalig direkt vor der ersten Werbeanzeige angezeigt. Auch wenn Sie ablehnen, wird Werbung angezeigt, aber die an Google gesendeten Informationen sind dann auf einen eingeschränkten (nicht-personalisierten) Umfang begrenzt. Die ATT-Zustimmung können Sie jederzeit in den iOS-Einstellungen unter „Einstellungen → Datenschutz & Sicherheit → Tracking“ ändern.
-   **Android-Version**: ATT ist ein reines iOS-System und existiert nicht auf Android. Stattdessen wird die **Werbe-ID (Advertising ID)** von Google für die Werbeauslieferung verwendet. Sie können die Personalisierung von Werbung deaktivieren oder Ihre Werbe-ID in den Einstellungen Ihres Geräts unter „Einstellungen → Datenschutz → Werbung“ (Wortlaut kann je nach Gerät und Android-Version variieren) zurücksetzen. Die Android-Version befolgt zudem die in anwendbaren Regionen wie der EU angezeigte Einwilligungsverwaltung (UMP).
-   **Mit einem KUU+-Abonnement werden die gesamte Werbung und die damit verbundene Datenübertragung deaktiviert.**
-   Details zur Datenverarbeitung durch Google AdMob finden Sie in der [Google AdMob-Datenschutzrichtlinie](https://support.google.com/admob/answer/6128543).

## Artikel 14 (Über die Nutzung von Firebase Analytics / Crashlytics)

**Das in diesem Artikel beschriebene Opt-in-Verfahren gilt für die iOS-Version. Für die Android-Version siehe den Abschnitt „Über die Android-Version“ am Ende dieses Artikels.**

Die **iOS-Version** kann zur Qualitätsverbesserung der App und zur sofortigen Erkennung von Problemen im Live-Betrieb Googles Firebase Analytics (aggregierte Nutzungsstatistiken) und Firebase Crashlytics (Absturzberichte) verwenden. **Diese Funktion ist standardmäßig DEAKTIVIERT (keine Datenübertragung) und wird nur aktiv, wenn Sie in „Einstellungen → Daten & Diagnose“ explizit zustimmen (Opt-in).**

-   **Gesendete Informationen**:
    -   Eine von Firebase automatisch erstellte, anonymisierte Installations-ID (basiert auf IDFV; keine direkt personenbezogene Kennung).
    -   Aggregierte Signale zu In-App-Ereignissen (z. B. Abschluss von Aufnahme-Sitzungen, Anzeige/Konversion der Paywall, Abschluss des Onboardings; numerische Werte werden in groben Rastern (Buckets) gesendet).
    -   Symbolisierte Stack-Traces bei abnormaler Beendigung der App.
-   **Nicht gesendete Informationen**: Ihre gesprochenen Inhalte (Audio), Transkriptionen, KI-Gliederungsergebnisse und von Ihnen festgelegte Themennamen sind **auf Typebene so konzipiert, dass sie nicht gesendet werden können** (die Implementierung der API verhindert die Übergabe von Zeichenkettenwerten an das Analytics-SDK).
-   **Solange keine Zustimmung (Opt-in) vorliegt, findet keinerlei Kommunikation mit Firebase statt**, einschließlich aller oben genannten Datenkategorien.
-   **Möglichkeit zur Deaktivierung**: Sie können den Schalter unter „Einstellungen → Daten & Diagnose“ jederzeit auf AUS stellen. Dadurch wird die bisherige Installations-ID verworfen und alle lokal auf dem Gerät gespeicherten, noch nicht gesendeten Absturzprotokolle werden gelöscht.
-   Empfänger ist Google LLC (USA). Es gelten die [Datenschutzinformationen von Firebase](https://firebase.google.com/support/privacy) von Google.

**Über die Android-Version:** Die Android-Version nutzt Firebase Analytics und sendet zur Produktverbesserung **inhaltsfreie Nutzungsereignisse** (Bucket-Werte wie Bildschirmwechsel oder die Nutzungshäufigkeit von Funktionen) sowie eine von Firebase erstellte anonyme App-Instanz-ID. **Im Gegensatz zur iOS-Version ist diese Funktion standardmäßig aktiviert.** Ihre gesprochenen Inhalte (Audio), Transkriptionen, Gliederungsergebnisse und Themennamen können aufgrund des Designs, das die Übergabe von Zeichenkettenwerten an das Analytics-SDK verhindert, **nicht gesendet werden**. **Die Android-Version enthält kein Crashlytics und sendet keine Absturzberichte.** Empfänger ist Google LLC (USA); es gelten die [Datenschutzinformationen von Firebase](https://firebase.google.com/support/privacy) von Google.
