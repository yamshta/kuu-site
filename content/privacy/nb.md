> Dette er en referanseoversettelse for enkelhets skyld. Den japanske versjonen er den autoritative teksten.

# Personvernerklæring for KUU

Sist oppdatert: 21. juli 2026

**Kort fortalt:** Det du sier, er ditt. **Selve stemmen din sendes aldri ut fra enheten din**. Transkribering skjer på enheten din. Organisering (AI-kategorisering) bruker en ekstern KI, men det er kun den transkriberte teksten som sendes. Den brukes kun til organisering og lagres ikke (på iOS kan du bytte til organisering kun på enheten via «På enheten» i Innstillinger. **Android-versjonen sender kun til den eksterne KI-en – det finnes ikke noe alternativ for organisering på enheten**). Data lagres på enheten din, og for iOS-versjonen også i din private iCloud-database (Android-versjonen lagrer kun på enheten). Utvikleren lagrer ikke innholdet ditt og kan ikke se det som mottas. Du kan når som helst slette all data fra innsiden av appen. Appen utfører kun **absolutt nødvendige nettverksforespørsler** for fakturering (iOS=StoreKit／Android=RevenueCat) og Google AdMob-annonser, og denne informasjonen inneholder aldri det du har sagt (annonser deaktiveres med KUU+). Bruksmønstre måles for å forbedre kvaliteten, men dette inkluderer heller aldri det du har sagt (iOS krever aktivt samtykke fra brukeren, mens Android sender innholdsfrie målinger som standard – se Artikkel 14).

---

## Artikkel 1 (Grunnprinsipper)

Appen «KUU» (heretter «appen») er en app som hjelper deg med å få tanker ut av hodet ved å si dem høyt og organisere dem. Den finnes i en **iOS- og Android-versjon**, og denne erklæringen gjelder for begge. Appen behandler informasjon kun i den grad det er absolutt nødvendig for å levere funksjonalitet, med brukerens personvern som høyeste prioritet.

## Artikkel 2 (Informasjon som innhentes og lagres)

Appen behandler kun følgende informasjon:

1.  **Det du snakker inn (lyddata)** — Lydopptak lagres midlertidig i enhetens internminne kun under transkriberingsprosessen, og slettes umiddelbart etter at behandlingen er fullført. De sendes ikke til noen server.
2.  **Resultater fra transkribering og organisering (tekst)** — Lagres slik at du selv kan se gjennom dem (iOS-versjonen: på enheten og i din private iCloud-database; Android-versjonen: kun på enheten. Se Artikkel 4 for detaljer).
3.  **Innstillinger i appen** — Tema, tekststørrelse, vannivå-status i hodet og andre innstillingsverdier som er nødvendige for appens funksjon.

Appen samler ikke inn personopplysninger som navn, e-postadresse, telefonnummer, posisjonsdata, kontakter, kalender, bilder eller enhetsidentifikatorer.

## Artikkel 3 (Om stemmegjenkjenning og KI-kategorisering)

**Stemmegjenkjenning (transkribering)** utføres i sin helhet på din iOS-enhet.

-   Stemmegjenkjenning: Bruker Apples Speech-rammeverk (på enheten). Selve stemmen din sendes aldri ut fra enheten.

**KI-kategorisering (organisering)** bruker en ekstern KI.

-   Det er **kun den transkriberte teksten** som sendes. Selve stemmen sendes ikke.
-   Den sendes til en ekstern KI, via utviklerens server (backend som kobler til Googles Gemini).
-   Den innsendte teksten **brukes kun til kategorisering og lagres ikke**. Den brukes heller ikke til å trene KI-en.
-   **For iOS-versjonen** kan du når som helst bytte til **kategorisering kun på enheten** (ved hjelp av Apples FoundationModels / lokale regler) via «På enheten» i Innstillinger. I dette tilfellet forlater heller ikke teksten enheten din.

**Om Android-versjonen:** Android-versjonen tilbyr ikke en organiseringsmetode som kun kjører på enheten. Når du velger å organisere, vil den transkriberte teksten **alltid** bli sendt til den eksterne KI-en (Googles Gemini via vår backend). Det finnes ikke en «På enheten»-bryter som i iOS-versjonen. Det er kun den transkriberte teksten som sendes. Selve stemmen din sendes ikke, og den innsendte teksten brukes kun til kategorisering. Den blir verken lagret eller brukt til å trene KI-en. Selve transkriberingen (stemmegjenkjenningen) utføres i sin helhet på enheten.

## Artikkel 4 (Lagring og synkronisering)

**iOS-versjonen:** Appen lagrer transkriberte og organiserte tekster kun i din **private iCloud-database** (CloudKit Private Database). Dette er en lagringstjeneste levert av Apple, hvor kun du har tilgang til innholdet. Utvikleren av denne appen kan verken se eller hente ut det lagrede innholdet. Apples personvernerklæring gjelder for bruk av iCloud.

**Android-versjonen:** Transkriberte og organiserte tekster lagres **kun på denne enheten**. Det utføres ingen automatisk nettsky-synkronisering. Ved bytte av enhet kan du eksportere data til en fil fra «Stemme og data» i appen, og deretter importere den på den nye enheten. Du velger selv hvor filen skal lagres (på enheten, i din foretrukne skylagringsapp, e.l.). Utvikleren har ikke tilgang til denne filen.

## Artikkel 5 (Formål med bruken)

Informasjonen som behandles, brukes kun til følgende formål:

1.  Å generere transkribering fra stemme og vise den til brukeren
2.  Å kategorisere transkriberingen i «se nå / tenk på senere / la ligge / gi slipp» og vise den til brukeren
3.  Å lagre og vise det brukeren tidligere har snakket inn, slik at brukeren selv kan se gjennom det
4.  Å opprettholde innstillingsverdier som er nødvendige for appens funksjon

## Artikkel 6 (Bruk av eksterne tjenester)

Appen benytter følgende eksterne tjenester for å levere funksjonalitet. **Selve stemmen din sendes ikke til noen av disse tjenestene**.

-   **iCloud / CloudKit** (kun iOS-versjonen. Levert av Apple. Lagring og synkronisering kun til din egen private database)
-   **Stemmegjenkjenning** (iOS-versjonen: Apples Speech-rammeverk, Android-versjonen: enhetens innebygde stemmegjenkjenningsmotor. Begge kjøres på enheten, og stemmen sendes ikke ut fra enheten)
-   **En ekstern KI (nettsky)** (KI-kategorisering. Kun transkribert tekst sendes. Brukes kun til kategorisering, lagres ikke og brukes ikke til å trene KI-en. Kan deaktiveres i iOS-versjonen via «På enheten», men **Android-versjonen sender kun til den eksterne KI-en**. Se Artikkel 3 for detaljer)
-   **FoundationModels** (kun iOS-versjonen. Levert av Apple. Kjøres i sin helhet på enheten. Brukes når «På enheten» er aktivert, og som reserve når den eksterne KI-en ikke er tilgjengelig)
-   **Faktureringstjenester** (iOS-versjonen: **Apple StoreKit**, Android-versjonen: **RevenueCat**. For kjøp, fornyelse, kansellering og rettighetsstyring av KUU+-abonnementet. Det du har sagt, sendes ikke. For RevenueCat, se Artikkel 7 og [RevenueCats personvernerklæring](https://www.revenuecat.com/privacy))
-   **Play Integrity API (via Firebase App Check. Kun Android-versjonen)** (For å bekrefte at forespørsler til kategoriserings-API-et kommer fra en legitim app, gjennom en attestasjon av enhetens og appens integritet. Inneholder ikke det du har sagt eller informasjon som kan identifisere deg)
-   **Google AdMob (Google Mobile Ads SDK)** (Kun når du ikke abonnerer på KUU+. Viser én enkelt, integrert annonseplass mellom seksjoner på «Det du har sagt»-skjermen. Det du har sagt, sendes ikke. Se Artikkel 13 for detaljer)
-   **Firebase Analytics** (Levert av Google. For kvalitetsforbedring av appen. For iOS-versjonen: **kun hvis brukeren aktivt samtykker (opt-in) i Innstillinger**. For Android-versjonen: sender **innholdsfrie brukshendelser som standard** (i begge tilfeller sendes ikke det du har sagt). iOS-versjonen bruker også **Crashlytics** ved aktivt samtykke, men **Android-versjonen inkluderer ikke Crashlytics**. Se Artikkel 14 for detaljer)

Appens server er minimal og fungerer kun som en mellomstasjon for KI-kategorisering, uten å lagre noe innhold (state-less). Det benyttes ingen autentiseringstjenester som krever personlige kontoer.

## Artikkel 7 (Utlevering til tredjeparter)

Utvikleren av appen har ingen mulighet til å få tilgang til det du har snakket inn, transkriberte tekster eller organiserte resultater, og vil ikke utlevere dette til tredjeparter.

For å levere annonser til brukere som ikke abonnerer på KUU+, sendes informasjon som Google AdMob trenger for annonselevering, til Google. Dette kan inkludere enhetsidentifikatorer, annonse-ID, enhetens språk og region, omtrentlig posisjon og informasjon om klikk på annonser (se Artikkel 13, Googles personvernerklæring for AdMob gjelder). Denne dataoverføringen skjer ikke så lenge du abonnerer på KUU+.

Når du abonnerer på KUU+ i **Android-versjonen**, sendes kjøpsinformasjon (produkt-ID, pris, kjøpsdato osv.) til RevenueCat, Inc. for å håndtere kjøpet og dine rettigheter (gyldig/ugyldig). Det du har sagt, sendes ikke. For detaljer om RevenueCats databehandling, se [RevenueCats personvernerklæring](https://www.revenuecat.com/privacy).

Informasjon vil kun bli utlevert dersom det er påkrevd ved lov, i henhold til gjeldende prosedyrer.

## Artikkel 8 (Sletting av data)

Du kan når som helst slette all data via «Innstillinger → Stemme og data → Slett lagret innhold» i appen. Dette sletter permanent dataene på enheten (og for iOS-versjonen, også data i din private iCloud-database). Slettede data kan ikke gjenopprettes.

Når du avinstallerer appen, slettes dataene på enheten. For iOS-versjonen kan data i iCloud slettes via Apples innstillinger (Innstillinger → Apple ID → iCloud → Administrer lagring). Siden Android-versjonen kun lagrer lokalt på enheten, slettes dataene ved avinstallering.

## Artikkel 9 (Sikkerhetstiltak)

-   **iOS-versjonen**: Midlertidige lydfiler under opptak krypteres av iOS' filbeskyttelse (`FileProtectionType.complete`) og er utilgjengelige når enheten er låst. Kommunikasjon med iCloud krypteres av Apple med SSL/TLS.
-   **Android-versjonen**: Lydopptak skrives aldri til disk, selv ikke som midlertidige filer. De behandles kun i minnet og forkastes umiddelbart etter gjenkjenning. Lagrede transkriberinger og organiserte resultater lagres i appens private område og er utilgjengelige for andre apper. De er også ekskludert fra Androids automatiske sikkerhetskopiering til nettskyen.
-   All kommunikasjon med den eksterne KI-en krypteres (HTTPS/TLS). Utviklerens server fungerer kun som en mellomstasjon for kategorisering og lagrer ikke innhold (state-less).

## Artikkel 10 (Bruk av mindreårige)

Appen har aldersgrense 4+, men på grunn av sin natur som et verktøy for tankeorganisering, forutsettes det at brukeren kan lese og skrive. Mindreårige bør bruke appen med samtykke fra en foresatt.

## Artikkel 11 (Endringer i personvernerklæringen)

Denne erklæringen kan bli revidert som følge av lovendringer, nye funksjoner, eller endringer i rammeverk eller retningslinjer fra plattformene (Apple / Google). Ved vesentlige endringer vil dette bli varslet i forbindelse med en app-oppdatering eller på den offentlige siden for denne erklæringen.

## Artikkel 12 (Kontakt)

For spørsmål angående denne erklæringen, vennligst ta kontakt via «Utvikler»-seksjonen på appens side i App Store eller Google Play, eller via «Innstillinger → Kontakt» i appen.

## Artikkel 13 (Om annonser og App Tracking Transparency)

Når du ikke abonnerer på KUU+, viser appen én enkelt, integrert annonseplass fra Google AdMob på «Det du har sagt»-skjermen. Annonsen vises på en diskré måte mellom seksjonene for å bevare KUUs visuelle uttrykk.

-   **Det du har sagt, brukes aldri til annonsering** (annonsene tar ikke hensyn til transkriberinger, kategoriseringsresultater eller temaer).
-   For å levere annonser kan Google AdMob samle inn informasjon som enhetsidentifikatorer (inkludert IDFA), annonse-ID, omtrentlig posisjon (Coarse Location), diagnostikk og produktinteraksjon (interaksjon med annonser i appen).
-   **iOS-versjonen**: En forespørsel om **App Tracking Transparency** (ATT) vises én gang, rett før den første annonsen vises. Selv om du avviser forespørselen, vil annonser fortsatt vises, men informasjonen som sendes til Google, vil være begrenset (ikke-personlig tilpasset). Du kan når som helst endre ATT-tillatelsen i iOS under «Innstillinger» → «Personvern og sikkerhet» → «Sporing».
-   **Android-versjonen**: ATT er en mekanisme spesifikk for iOS og finnes ikke på Android. I stedet brukes Googles **annonse-ID (Advertising ID)** for annonselevering. Du kan reservere deg mot personlig tilpasset annonsering eller tilbakestille annonse-ID-en din fra enhetens «Innstillinger → Personvern → Annonser» (ordlyden kan variere avhengig av enhet og Android-versjon). Android-versjonen følger også samtykkestyring (UMP) som vises i relevante regioner, som EU.
-   **Når du abonnerer på KUU+, stanses all annonsevisning og tilhørende dataoverføring**.
-   For detaljer om Google AdMobs databehandling, se [Google AdMobs personvernerklæring](https://support.google.com/admob/answer/6128543).

## Artikkel 14 (Om bruk av Firebase Analytics / Crashlytics)

**Samtykkemodellen (opt-in) i denne artikkelen gjelder for iOS-versjonen. For Android-versjonen, se avsnittet «Om Android-versjonen» nederst i artikkelen.**

**iOS-versjonen** kan benytte Googles Firebase Analytics (samlet bruksstatistikk) og Firebase Crashlytics (krasjrapportering) for å forbedre appens kvalitet og raskt oppdage feil i produksjon. **Denne funksjonen er avslått som standard (ingen data sendes) og aktiveres kun dersom du eksplisitt gir ditt samtykke (opt-in) via «Innstillinger → Data og diagnostikk».**

-   **Informasjon som sendes**:
    -   En anonymisert installasjons-ID utstedt automatisk av Firebase (basert på IDFV, ikke en direkte personlig identifikator).
    -   Aggregerte signaler om hendelser i appen (fullførte opptakssesjoner, visning/konvertering på betalingsmur, fullført introduksjon, o.l. for statistikk. Numeriske verdier sendes med grov granularitet).
    -   Stack trace (symbolisert) ved uventet avslutning av appen.
-   **Informasjon som ikke sendes**: Det du har sagt (lyd), transkriberte tekster, resultater fra KI-kategorisering og tema-navn du har angitt, **er gjort umulig å sende på typenivå i koden** (implementasjonen er slik at API-et til analyseverktøyet ikke kan motta tekstverdier).
-   **Så lenge du ikke har gitt ditt samtykke, vil ingen kommunikasjon, inkludert informasjonen nevnt over, skje med Firebase**.
-   **Hvordan stanse sendingen**: Du kan når som helst slå av bryteren i «Innstillinger → Data og diagnostikk». Når du slår den av, forkastes den tidligere installasjons-ID-en, og eventuelle usendte krasjlogger som er lagret lokalt på enheten, slettes.
-   Mottakeren er Google LLC (USA). Googles [personverninformasjon for Firebase](https://firebase.google.com/support/privacy) gjelder.

**Om Android-versjonen:** Android-versjonen bruker Firebase Analytics og sender **innholdsfrie brukshendelser** for produktforbedring (aggregerte verdier som skjermoverganger og antall ganger en funksjon brukes) samt en anonym App Instance ID utstedt av Firebase. **I motsetning til iOS-versjonen, er dette aktivert som standard.** Det du har sagt (lyd), transkriberinger, organiserte resultater og tema-navn **kan ikke sendes**. Dette skyldes at API-et til analyseverktøyet er designet slik at tekstverdier ikke kan overføres. **Android-versjonen inkluderer ikke Crashlytics og sender ingen krasjrapporter.** Mottakeren er Google LLC (USA), og Googles [personverninformasjon for Firebase](https://firebase.google.com/support/privacy) gjelder.
