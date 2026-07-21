> Dit is een referentievertaling voor uw gemak. De Japanse versie is de gezaghebbende tekst.

# Privacybeleid voor KUU

Laatst bijgewerkt: 21 juli 2026

**In het kort:** Wat u zegt, is van u. **Uw stem zelf wordt nooit naar buiten verzonden**. Transcriptie vindt plaats op uw apparaat. Voor de organisatie (AI-classificatie) wordt een externe AI gebruikt, maar alleen de getranscribeerde tekst wordt verzonden. Deze wordt uitsluitend gebruikt voor de organisatie en wordt niet bewaard (in de iOS-versie kunt u via "Op apparaat" in de instellingen overschakelen naar organisatie die uitsluitend op het apparaat plaatsvindt; **de Android-versie verzendt altijd naar de externe AI; er is geen optie voor organisatie op het apparaat**). De gegevens worden opgeslagen op uw apparaat en, in de iOS-versie, ook in uw privédatabase van iCloud (de Android-versie slaat alleen op het apparaat op). De ontwikkelaar slaat uw inhoud niet op en kan deze niet inzien. U kunt op elk moment alle gegevens verwijderen vanuit de app. De app voert alleen **minimale netwerkcommunicatie** uit voor facturering (StoreKit op iOS / RevenueCat op Android) en advertenties van Google AdMob. Deze communicatie bevat nooit wat u hebt gezegd (advertenties kunnen worden uitgeschakeld met een KUU+-abonnement). Om de kwaliteit te verbeteren, meten we het gebruik, maar ook dit omvat nooit wat u hebt gezegd (op iOS is dit opt-in voor de gebruiker; op Android wordt standaard inhoudsvrije meting uitgevoerd - zie Artikel 14).

---

## Artikel 1 (Algemeen Beleid)

Deze app, "KUU" (hierna "de App"), is een applicatie die u helpt uw gedachten te ordenen door ze hardop uit te spreken. De app is beschikbaar voor **iOS en Android**, en dit beleid is op beide versies van toepassing. De App verwerkt informatie uitsluitend voor zover dit minimaal noodzakelijk is om de functies aan te bieden, waarbij de bescherming van de privacy van de gebruiker de hoogste prioriteit heeft.

## Artikel 2 (Informatie die wordt verzameld en opgeslagen)

De App verwerkt uitsluitend de volgende informatie:

1.  **Audio die u opneemt (spraakgegevens)** — De opgenomen audio wordt alleen tijdens de transcriptieverwerking tijdelijk op uw apparaat opgeslagen en onmiddellijk na voltooiing verwijderd. Deze wordt niet naar een server verzonden.
2.  **Getranscribeerde en georganiseerde tekst** — Opgeslagen zodat u kunt teruglezen wat u hebt gezegd (iOS: op uw apparaat en in uw privédatabase van iCloud; Android: uitsluitend op het apparaat - zie Artikel 4).
3.  **App-instellingen** — Thema, tekstgrootte, de waterstand van het hoofd en andere waarden die nodig zijn voor de werking van de app.

De App verzamelt geen persoonlijke informatie zoals naam, e-mailadres, telefoonnummer, locatiegegevens, contacten, agenda, foto's of apparaat-ID's.

## Artikel 3 (Over spraakherkenning en AI-classificatie)

**Spraakherkenning (transcriptie)** wordt volledig op uw iOS-apparaat uitgevoerd.

-   Spraakherkenning: Maakt gebruik van Apple's Speech-framework (op het apparaat). Uw stem zelf wordt nooit buiten het apparaat verzonden.

**AI-classificatie (categorisatie)** maakt gebruik van een externe AI.

-   Alleen de **getranscribeerde tekst** wordt verzonden. Uw stem wordt niet verzonden.
-   De tekst wordt via de server van de ontwikkelaar (backend) doorgestuurd naar een externe AI (Google's Gemini).
-   De verzonden tekst wordt **uitsluitend gebruikt voor classificatie en wordt niet opgeslagen**. Deze wordt ook niet gebruikt om de AI te trainen.
-   **In de iOS-versie** kunt u op elk moment overschakelen naar **classificatie die uitsluitend op het apparaat plaatsvindt** (via Apple's FoundationModels / lokale regels) door "Op apparaat" te kiezen in de instellingen. In dat geval verlaat ook de tekst uw apparaat niet.

**Over de Android-versie:** De Android-versie biedt geen methode voor organisatie (classificatie) die volledig op het apparaat plaatsvindt. Wanneer u uw gedachten organiseert, wordt de getranscribeerde tekst **altijd** verzonden naar de externe AI (Google's Gemini via onze backend). Er is geen optie om over te schakelen naar "Op apparaat", zoals in de iOS-versie. Alleen de getranscribeerde tekst wordt verzonden – uw stem zelf wordt niet verzonden, en de verzonden tekst wordt uitsluitend gebruikt voor classificatie, wordt niet opgeslagen en wordt niet gebruikt om de AI te trainen. De transcriptie (spraakherkenning) zelf vindt volledig op het apparaat plaats.

## Artikel 4 (Opslag en synchronisatie)

**iOS-versie:** Getranscribeerde en georganiseerde tekst wordt uitsluitend opgeslagen in uw **privédatabase van iCloud** (CloudKit Private Database). Dit is een opslagdienst van Apple waar alleen u toegang toe hebt. De ontwikkelaar van deze app kan de opgeslagen inhoud niet inzien of ophalen. Het privacybeleid van Apple is van toepassing op het gebruik van iCloud.

**Android-versie:** Getranscribeerde en georganiseerde tekst wordt **uitsluitend op dit apparaat opgeslagen**. Er vindt geen automatische cloudsynchronisatie plaats. Bij het wisselen van apparaat kunt u uw gegevens exporteren naar een bestand via "Stem & Gegevens" in de app en dit importeren op het nieuwe apparaat. U kiest zelf waar het bestand wordt opgeslagen (op het apparaat, in uw cloudopslag-app, etc.). De ontwikkelaar heeft geen toegang tot dit bestand.

## Artikel 5 (Doeleinden van gebruik)

De verwerkte informatie wordt uitsluitend voor de volgende doeleinden gebruikt:

1.  Het genereren van transcripties van uw stem en deze aan u tonen
2.  Het classificeren van transcripties in "Nu bekijken / Later over nadenken / Laten rusten / Loslaten" en deze aan u tonen
3.  Het opslaan en weergeven van wat u in het verleden hebt gezegd, zodat u dit zelf kunt teruglezen
4.  Het bewaren van instellingen die nodig zijn voor de werking van de app

## Artikel 6 (Gebruik van externe diensten)

De App maakt gebruik van de volgende externe diensten om haar functies te kunnen aanbieden. **Uw stem zelf wordt naar geen van deze diensten verzonden.**

-   **iCloud / CloudKit** (alleen iOS-versie. Aangeboden door Apple. Opslag en synchronisatie uitsluitend in uw eigen privédatabase)
-   **Spraakherkenning** (iOS-versie: Apple's Speech-framework; Android-versie: de spraakherkenningsengine op het apparaat. Beide worden op het apparaat uitgevoerd; uw stem wordt niet buiten het apparaat verzonden)
-   **Een externe AI (cloud)** (AI-classificatie. Alleen de getranscribeerde tekst wordt verzonden; uitsluitend gebruikt voor classificatie, niet opgeslagen, niet gebruikt voor AI-training. In de iOS-versie kan dit worden uitgeschakeld via "Op apparaat" in de instellingen, maar **de Android-versie verzendt uitsluitend naar de externe AI**. Zie Artikel 3 voor details.)
-   **FoundationModels** (alleen iOS-versie. Aangeboden door Apple. Volledig op het apparaat uitgevoerd. Gebruikt wanneer "Op apparaat" is ingeschakeld of als fallback wanneer de externe AI niet beschikbaar is)
-   **Factureringsdiensten** (iOS-versie: **Apple StoreKit**; Android-versie: **RevenueCat**. Voor het beheren van de aankoop, verlenging, annulering en status van het KUU+-abonnement. Uw gesproken inhoud wordt niet verzonden. Zie Artikel 7 en het [privacybeleid van RevenueCat](https://www.revenuecat.com/privacy) voor meer informatie over RevenueCat)
-   **Play Integrity API (via Firebase App Check; alleen Android-versie)** (Verificatie van de integriteit van het apparaat en de app om te bevestigen dat verzoeken naar de classificatie-API afkomstig zijn van een legitieme app. Bevat geen gesproken inhoud of informatie die de gebruiker identificeert)
-   **Google AdMob (Google Mobile Ads SDK)** (Alleen wanneer u geen KUU+-abonnement hebt: toont één native advertentie tussen de secties op het "Wat u zei"-scherm. Uw gesproken inhoud wordt niet verzonden. Zie Artikel 13 voor details)
-   **Firebase Analytics** (Aangeboden door Google. Voor kwaliteitsverbetering van de app. In de iOS-versie **alleen gebruikt als u expliciet opt-in geeft via de instellingen**; in de Android-versie worden inhoudsvrije gebruiksgebeurtenissen **standaard** verzonden (in beide gevallen wordt uw gesproken inhoud niet verzonden). De iOS-versie maakt ook gebruik van **Crashlytics** na opt-in, maar **de Android-versie bevat geen Crashlytics**. Zie Artikel 14 voor details)

De server van de app is minimaal en dient alleen als doorgeefluik voor de AI-classificatie; er wordt geen inhoud opgeslagen (stateless). De app maakt geen gebruik van authenticatiediensten die een persoonlijk account vereisen.

## Artikel 7 (Openbaarmaking aan derden)

De ontwikkelaar van de app heeft geen middelen om toegang te krijgen tot uw gesproken inhoud, transcripties of georganiseerde resultaten, en zal deze niet aan derden verstrekken.

Om advertenties te tonen aan gebruikers zonder KUU+-abonnement, wordt informatie die Google AdMob nodig heeft voor advertentieweergave – zoals apparaat-ID's, advertentie-ID, de taal en regio van het apparaat, globale locatiegegevens en informatie over interacties met advertenties – naar Google verzonden (zie Artikel 13; het privacybeleid van Google AdMob is van toepassing). Zolang u een KUU+-abonnement hebt, vindt deze gegevensoverdracht niet plaats.

Wanneer u zich abonneert op KUU+ in de **Android-versie**, wordt aankoopinformatie (product-ID, prijs, aankoopdatum, etc.) naar RevenueCat, Inc. verzonden voor het verwerken van de aankoop en het beheren van uw abonnementsstatus (actief/inactief). Uw gesproken inhoud wordt niet verzonden. Raadpleeg het [privacybeleid van RevenueCat](https://www.revenuecat.com/privacy) voor details over hoe RevenueCat gegevens verwerkt.

Informatie wordt alleen openbaar gemaakt indien dit wettelijk verplicht is en volgens de voorgeschreven procedures.

## Artikel 8 (Verwijdering van gegevens)

U kunt op elk moment alle gegevens verwijderen via "Instellingen → Stem & Gegevens → Opgeslagen gegevens verwijderen" in de app. Hiermee worden alle gegevens op het apparaat (en in de iOS-versie ook de gegevens in uw privédatabase van iCloud) permanent verwijderd. Verwijderde gegevens kunnen niet worden hersteld.

Als u de app verwijdert, worden de lokale gegevens gewist. In de iOS-versie kunnen de gegevens in iCloud worden verwijderd via de instellingen van Apple (Instellingen → Apple ID → iCloud → Beheer opslag). Omdat de Android-versie gegevens alleen op het apparaat opslaat, worden deze verwijderd wanneer u de app de-installeert.

## Artikel 9 (Beveiligingsmaatregelen)

-   **iOS-versie**: Tijdelijke audiobestanden tijdens het opnemen worden versleuteld door de bestandsbescherming van iOS (`FileProtectionType.complete`) en zijn niet toegankelijk wanneer het apparaat is vergrendeld. Communicatie met iCloud wordt door Apple versleuteld via SSL/TLS.
-   **Android-versie**: Opgenomen audio wordt nooit naar de schijf geschreven, zelfs niet als tijdelijk bestand; deze wordt uitsluitend in het geheugen verwerkt en onmiddellijk na de herkenning verwijderd. Opgeslagen transcripties en georganiseerde resultaten worden bewaard in de privéopslagruimte van de app, die niet toegankelijk is voor andere apps, en zijn uitgesloten van de automatische cloudback-up van Android.
-   Alle communicatie met de externe AI wordt versleuteld (HTTPS/TLS). De server van de ontwikkelaar dient alleen als doorgeefluik voor de classificatieverzoeken en slaat geen inhoud op (stateless).

## Artikel 10 (Gebruik door minderjarigen)

De app heeft een leeftijdsclassificatie van 4+, maar vanwege de aard van de app (het ordenen van gedachten) is deze bedoeld voor gebruikers die kunnen lezen en schrijven. Minderjarigen dienen de app te gebruiken met toestemming van een ouder of voogd.

## Artikel 11 (Wijzigingen in dit beleid)

Dit beleid kan worden bijgewerkt als gevolg van wetswijzigingen, de toevoeging van nieuwe functies, of wijzigingen in de specificaties van de frameworks of het beleid van de platforms (Apple/Google). Belangrijke wijzigingen zullen worden aangekondigd via een app-update of op de openbare pagina van dit beleid.

## Artikel 12 (Contact)

Voor vragen over dit beleid kunt u contact met ons opnemen via de sectie "Ontwikkelaar" op de App Store- of Google Play-pagina van de app, of via "Instellingen → Contact" in de app.

## Artikel 13 (Over advertenties en App Tracking Transparency)

Wanneer u geen KUU+-abonnement hebt, toont de app één native advertentie, aangeboden door Google AdMob, tussen de secties op het "Wat u zei"-scherm. De advertenties worden discreet weergegeven om de sfeer van KUU te behouden.

-   **Uw gesproken inhoud wordt nooit gebruikt voor advertenties.** Advertenties raadplegen uw transcripties, georganiseerde resultaten of thema's niet.
-   Voor het tonen van advertenties kan Google AdMob apparaat-ID's (inclusief IDFA), advertentie-ID, globale locatie, diagnostische gegevens en productinteracties (interacties met advertenties in de app) verzamelen.
-   **iOS-versie**: Er wordt eenmalig een **App Tracking Transparency** (ATT)-verzoek getoond, vlak voor de eerste advertentie. Advertenties worden ook getoond als u geen toestemming geeft, maar de informatie die naar Google wordt verzonden, is dan beperkt (niet-gepersonaliseerd). U kunt uw ATT-toestemming op elk moment wijzigen in de iOS-instellingen via "Instellingen → Privacy en beveiliging → Tracking".
-   **Android-versie**: ATT is een mechanisme specifiek voor iOS en bestaat niet op Android. In plaats daarvan wordt Google's **Advertentie-ID (Advertising ID)** gebruikt voor het tonen van advertenties. U kunt zich afmelden voor gepersonaliseerde advertenties of uw advertentie-ID resetten via de instellingen van uw apparaat onder "Instellingen → Privacy → Advertenties" (de bewoording kan verschillen per apparaat en Android-versie). De Android-versie volgt ook het toestemmingsbeheer (UMP) dat wordt getoond in relevante regio's zoals de EU.
-   **Een abonnement op KUU+ stopt alle advertenties en de bijbehorende gegevensoverdracht.**
-   Raadpleeg het [privacybeleid van Google AdMob](https://support.google.com/admob/answer/6128543) voor details over de gegevensverwerking door AdMob.

## Artikel 14 (Over het gebruik van Firebase Analytics / Crashlytics)

**Het opt-in-model in dit artikel is van toepassing op de iOS-versie. Voor de Android-versie, zie "Over de Android-versie" aan het einde van dit artikel.**

**De iOS-versie** kan voor kwaliteitsverbetering en het onmiddellijk detecteren van incidenten gebruikmaken van Google's Firebase Analytics (geaggregeerde gebruiksgegevens) en Firebase Crashlytics (crashrapporten). **Deze functie is standaard UIT (geen gegevens verzonden) en wordt alleen geactiveerd als u expliciet toestemming geeft (opt-in) via "Instellingen → Gegevens & Diagnostiek".**

-   **Informatie die wordt verzonden**:
    -   Een geanonimiseerde installatie-ID die automatisch wordt uitgegeven door Firebase (gebaseerd op IDFV; dit is geen direct persoonlijk identificeerbare code)
    -   Geaggregeerde signalen van gebeurtenissen in de app (zoals het voltooien van een opnamesessie, weergave/conversie van de betaalmuur, voltooien van de onboarding. Numerieke waarden worden verzonden met een grove, gebundelde granulariteit.)
    -   Gesymboliseerde crash stack traces wanneer de app abnormaal afsluit
-   **Informatie die niet wordt verzonden**: Uw gesproken inhoud (audio), transcripties, de tekst van AI-classificatieresultaten en de themanamen die u instelt, zijn **op type-niveau onverzendbaar gemaakt in het ontwerp** (de API van de implementatie staat niet toe dat tekenreekswaarden worden doorgegeven aan de analyse-SDK).
-   **Zolang u geen opt-in hebt gegeven, vindt er geen enkele communicatie met Firebase plaats** (inclusief alle bovengenoemde categorieën).
-   **Hoe het verzenden te stoppen**: U kunt de schakelaar bij "Instellingen → Gegevens & Diagnostiek" op elk moment UIT zetten. Wanneer u dit doet, worden eerdere installatie-ID's verwijderd en worden alle lokaal opgeslagen, nog niet verzonden crashlogs gewist.
-   De ontvanger is Google LLC (Verenigde Staten). De [Privacy-informatie van Firebase](https://firebase.google.com/support/privacy) van Google is van toepassing.

**Over de Android-versie:** De Android-versie gebruikt Firebase Analytics en verzendt **inhoudsvrije gebruiksgebeurtenissen** voor productverbetering (geaggregeerde waarden zoals schermovergangen en het aantal keren dat functies worden gebruikt) plus een anonieme App Instance ID die door Firebase wordt uitgegeven. **In tegenstelling tot de iOS-versie is dit standaard ingeschakeld.** Uw gesproken inhoud (audio), transcripties, de tekst van georganiseerde resultaten en themanamen **kunnen niet worden verzonden** vanwege een ontwerp waarbij de API van de analyse-SDK geen tekenreekswaarden kan accepteren. **De Android-versie bevat geen Crashlytics en verzendt geen crashrapporten.** De ontvanger is Google LLC (Verenigde Staten); de [Privacy-informatie van Firebase](https://firebase.google.com/support/privacy) van Google is van toepassing.
