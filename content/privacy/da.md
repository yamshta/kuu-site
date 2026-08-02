> Dette er en oversættelse til orientering. Den japanske version er den autoritative tekst.

# Privatlivspolitik for KUU

Senest opdateret: 2. august 2026

**Kort sagt:** Det, du har indtalt, er dit. **Appen sender aldrig selve din stemme noget sted hen**. På iPhone- og Android-enheder foregår transskribering også på selve enheden. **Apple Watch-versionen af appen optager slet ikke lyd** – den modtager kun den tekst, der er produceret via standard-input på uret (diktat, håndskrift eller tastatur). Når du vælger diktat, håndteres lytningen af Apples eget system (se Artikel 3). Til organisering (AI-kategorisering) anvendes en ekstern AI, men det er kun den transskriberede tekst, der sendes. Den bruges udelukkende til organisering og gemmes ikke. Lagring sker kun på din enhed, og for iOS-versionen også i din private iCloud-database (Android-versionen lagrer kun på enheden). Udvikleren gemmer ikke dit indhold og kan ikke se, hvad der modtages. Du kan til enhver tid slette alle data indefra i appen. Appen foretager kun den **absolut nødvendige netværkskommunikation** til fakturering (StoreKit på iOS / RevenueCat på Android) og Google AdMob-annoncer, og disse oplysninger indeholder aldrig det, du har sagt (annoncer deaktiveres med KUU+). Vi måler brugsdata for at forbedre kvaliteten, men dette indeholder heller aldrig det, du har sagt (iOS kræver brugerens samtykke (opt-in); Android sender som standard målinger uden indhold – se Artikel 14).

---

## Artikel 1 (Grundlæggende politik)

Appen "KUU" (herefter "appen") er en applikation, der hjælper dig med at få tanker ud af hovedet ved at sige dem højt og organisere dem. Der findes en **iOS-version (iPhone og Apple Watch) og en Android-version**, og denne politik gælder for begge. Appen behandler kun oplysninger i det omfang, det er absolut nødvendigt for at levere dens funktioner, og prioriterer beskyttelsen af brugerens privatliv højest.

## Artikel 2 (Oplysninger, der indsamles og gemmes)

De oplysninger, appen håndterer, er begrænset til følgende:

1.  **Indtalt indhold (lyddata)** — Den optagede lyd gemmes kun midlertidigt i et lokalt område på enheden under transskriberingsprocessen og slettes omgående, når behandlingen er afsluttet. Den sendes ikke til nogen server. **Apple Watch-versionen af appen foretager slet ikke lydoptagelser** (se Artikel 3).
2.  **Transskriberings- og organiseringsresultater (tekst)** — Gemmes, så du selv kan gennemse dem (iOS-versionen: på enheden og i din private iCloud-database; Android-versionen: kun på enheden. På et parret Apple Watch gemmes kun de seneste titler i hver kategori af hensyn til visning. Se Artikel 4 for detaljer).
3.  **Indstillinger i appen** — Værdier, der er nødvendige for appens funktion, såsom tema, tekststørrelse og vandstand i hovedet.

Appen indsamler ikke personlige oplysninger såsom navn, e-mailadresse, telefonnummer, lokalitet, kontakter, kalender, billeder eller enhedsidentifikatorer.

## Artikel 3 (Om talegenkendelse og AI-kategorisering)

**Talegenkendelse (transskribering)** foregår fuldstændigt på din egen enhed for iPhone (iOS-versionen) og Android-enheder (for Apple Watch-versionen, se slutningen af denne artikel).

-   Talegenkendelse: Anvender Apples Speech framework (på enheden). Selve lyden sendes aldrig ud af enheden.

**AI-organisering (kategorisering)** anvender en ekstern AI:

-   Det er **kun det transskriberede indhold (teksten)**, der sendes. Din stemme sendes ikke.
-   Det sendes til en ekstern AI (Googles Gemini) via udviklerens server (backend).
-   Den sendte tekst **bruges udelukkende til kategorisering og bliver aldrig gemt**. Den bruges heller ikke til at træne AI'en.
-   Dette omfatter ikke kun det indhold, du har indtalt og fået transskriberet, men også indhold, du har indtastet eller redigeret manuelt. Hvis automatisk tema-tildeling (KUU+, valgfri indstilling) er aktiveret, sendes gemte emners titler, brødtekst og temanavne også med henblik på tildeling (alt sammen bruges udelukkende til klassificering og gemmes ikke).
-   I **iOS-versioner** af appen før 2.3.0 kan du vælge kategorisering udelukkende på enheden via indstillingen "På enheden" (denne indstilling udgik fra og med version 2.3.0).

**Om Android-versionen:** Android-versionen tilbyder ikke en organiseringsmetode, der udelukkende foregår på enheden. Når du organiserer, bliver den transskriberede tekst **altid** sendt til den eksterne AI (Googles Gemini via vores backend). Det er kun den transskriberede tekst, der sendes – selve din stemme sendes ikke, og den sendte tekst bruges udelukkende til kategorisering og bliver hverken gemt eller brugt til at træne AI'en. Selve transskriberingen (talegenkendelsen) foregår fuldstændigt på enheden.

**Om Apple Watch-versionen:** Apple Watch-versionen af appen hverken optager lyd eller udfører talegenkendelse. Til input anvendes standard tekst-input i watchOS (brugeren vælger mellem diktat, håndskrift eller tastatur), og appen modtager kun den resulterende tekst. Når du vælger diktat, udføres talegenkendelsen som en funktion i Apple (watchOS), og behandlingen heraf (herunder om den sker på enheden eller sendes til Apples servere) afhænger af din enhed, indstillinger og sprog, og **er underlagt Apples privatlivspolitik**. Appen kan ikke tilgå disse lyddata og hverken modtager eller gemmer dem. Den modtagne tekst behandles på samme måde som tekst, du har indtalt på iPhone (AI-kategorisering under denne artikel, lagring under Artikel 4).

## Artikel 4 (Lagring og synkronisering)

**iOS-versionen:** Transskriberings- og organiseringsresultater gemmes udelukkende i din **private iCloud-database** (CloudKit Private Database). Dette er et lagringssystem leveret af Apple, hvor kun du har adgang til det gemte indhold. Appens udvikler kan hverken se eller hente det gemte indhold. Brugen af iCloud er underlagt Apples privatlivspolitik.

**Android-versionen:** Transskriberings- og organiseringsresultater gemmes **udelukkende på denne enhed**. Der sker ingen automatisk synkronisering til skyen. Ved skift af enhed kan du eksportere data til en fil via "Stemmme & data" i appen og importere den på den nye enhed. Du vælger selv, hvor filen skal gemmes (på enheden, i din cloud-lagringsapp osv.). Udvikleren har ikke adgang til denne fil.

**Apple Watch-versionen:** Af hensyn til visning overføres en del af de organiserede resultater (de seneste titler i hver kategori) til dit parrede Apple Watch via Apples enhed-til-enhed-kommunikation (Watch Connectivity) og **gemmes også på Apple Watch**. Tekst, du indtaster på Apple Watch, overføres til din iPhone via samme mekanisme. Udviklerens server er ikke involveret i denne overførsel eller lagring.

## Artikel 5 (Formål med brugen)

De behandlede oplysninger anvendes udelukkende til følgende formål:

1.  At generere en transskribering fra brugerens stemme og vise den til brugeren.
2.  At kategorisere transskriberingen i "Se nu / Tænk senere / Parker / Giv slip" og vise den til brugeren.
3.  At gemme og vise det, brugeren tidligere har indtalt, så brugeren selv kan gennemse det.
4.  At opbevare de indstillinger, der er nødvendige for appens funktion.

## Artikel 6 (Brug af eksterne tjenester)

Appen anvender følgende eksterne tjenester for at levere sine funktioner. **Selve din stemme sendes ikke til nogen af disse tjenester**.

-   **iCloud / CloudKit** (kun iOS-versionen. Leveret af Apple. Gemmer og synkroniserer kun til din egen private database).
-   **Talegenkendelse** (iOS-versionen bruger Apples Speech framework, Android-versionen bruger enhedens indbyggede talegenkendelsesmotor. Begge kører på enheden, og lyden sendes ikke ud af enheden. **Apple Watch-versionen udfører ikke talegenkendelse i appen, men bruger standard watchOS-input**. Se Artikel 3).
-   **Standard tekst-input i watchOS** (kun Apple Watch-versionen. Leveret af Apple. Brugeren vælger mellem diktat, håndskrift eller tastatur. Ved valg af diktat udføres talegenkendelsen som en funktion af Apple og er underlagt Apples privatlivspolitik. Appen har ikke adgang til lyden. Se Artikel 3 for detaljer).
-   **Watch Connectivity** (kun Apple Watch-versionen. Leveret af Apple. Overfører tekst til visning direkte mellem iPhone og Apple Watch. Udviklerens server er ikke involveret. Se Artikel 4 for detaljer).
-   **Ekstern AI (cloud)** (AI-kategorisering. Kun den transskriberede tekst sendes. Bruges udelukkende til kategorisering, gemmes ikke og bruges ikke til at træne AI'en. Se Artikel 3 for detaljer).
-   **Faktureringstjenester** (iOS-versionen bruger **Apple StoreKit**, Android-versionen bruger **RevenueCat**. Til køb, fornyelse, opsigelse og rettighedsstyring af KUU+ abonnementer. Indtalt indhold sendes ikke. For RevenueCat, se Artikel 7 og [RevenueCats privatlivspolitik](https://www.revenuecat.com/privacy)).
-   **Play Integrity API (via Firebase App Check. Kun Android-versionen)** (Bekræfter, at anmodninger til klassificerings-API'en stammer fra en legitim app, ved at attestere enhedens/appens integritet. Indeholder hverken indtalt indhold eller brugeridentificerende oplysninger).
-   **Google AdMob (Google Mobile Ads SDK)** (Kun når KUU+ ikke er aktivt: viser én enkelt native annonce mellem sektionerne på "Det du har sagt"-skærmen. Indtalt indhold sendes ikke. Se Artikel 13 for detaljer).
-   **Firebase Analytics** (Leveret af Google. Til forbedring af appens kvalitet. På iOS-versionen **kun hvis brugeren eksplicit giver samtykke (opt-in) i Indstillinger**; på Android-versionen sendes **som standard** hændelser om brug uden indhold (i begge tilfælde sendes intet indtalt indhold). iOS-versionen bruger også **Crashlytics** ved samtykke, men **Android-versionen indeholder ikke Crashlytics**. Se Artikel 14 for detaljer).

Appens server fungerer kun som en minimal, tilstandsløs (stateless) mellemmand for AI-kategorisering og gemmer intet indhold. Appen bruger ikke autentificeringstjenester, der kræver en personlig konto.

## Artikel 7 (Videregivelse til tredjepart)

Appens udvikler har ingen mulighed for at tilgå brugerens indtalte indhold, transskriberinger eller organiseringsresultater og videregiver dem ikke til tredjepart.

Med det formål at levere annoncer til brugere, der ikke abonnerer på KUU+, sendes oplysninger, som Google AdMob kræver til annoncelevering – herunder enhedsidentifikatorer, annonce-ID, enhedens sprog og region, omtrentlig placering og data om interaktion med annoncer – til Google (se Artikel 13; Googles AdMob-privatlivspolitik er gældende). Denne dataoverførsel finder ikke sted, så længe KUU+ er aktivt.

Når du abonnerer på KUU+ i **Android-versionen**, sendes købsoplysninger (produkt-ID, pris, købsdato osv.) til RevenueCat, Inc. for at håndtere købsprocessen og dine rettigheder (aktiv/inaktiv-status). Intet indtalt indhold sendes. For detaljer om RevenueCats databehandling, se venligst [RevenueCats privatlivspolitik](https://www.revenuecat.com/privacy).

Oplysninger vil kun blive videregivet i henhold til gældende procedurer, hvis loven kræver det.

## Artikel 8 (Sletning af data)

Brugeren kan til enhver tid slette alle data via "Indstillinger → Stemme & data → Slet det, der er gemt" i appen. Dette sletter permanent alle data på enheden (og for iOS-versionen også data i den private iCloud-database). Slettede data kan ikke gendannes.

Hvis appen afinstalleres, slettes data på enheden. For iOS-versionen kan data i iCloud slettes via Indstillinger → Apple ID → iCloud → Administrer lagringsplads. Da Android-versionen kun gemmer data på enheden, slettes de ved afinstallation.

**Apple Watch-versionen:** Når du sletter alle data, vil de visningsdata, der allerede er overført til Apple Watch, blive erstattet med tomt indhold, næste gang uret opretter forbindelse. Hvis du sletter appen fra dit Apple Watch, slettes de gemte visningsdata på uret også.

## Artikel 9 (Sikkerhedsforanstaltninger)

-   **iOS-versionen**: Midlertidige lydfiler under optagelse krypteres af iOS' filbeskyttelse (`FileProtectionType.complete`) og er utilgængelige, når enheden er låst. Kommunikation med iCloud krypteres af Apple via SSL/TLS.
-   **Android-versionen**: Optaget lyd skrives aldrig til disken, heller ikke som en midlertidig fil; den behandles udelukkende i hukommelsen og kasseres umiddelbart efter genkendelse. Gemte transskriberinger og organiseringsresultater ligger i appens private lagerområde, utilgængeligt for andre apps, og er undtaget fra Androids automatiske cloud-backup.
-   **Apple Watch-versionen**: Overførsel mellem iPhone og Apple Watch håndteres af Apples Watch Connectivity og passerer ikke gennem udviklerens server. Det, der gemmes på Apple Watch, er begrænset til tekst til visning (de seneste titler i hver kategori); ingen lyd gemmes.
-   Al kommunikation med den eksterne AI er krypteret (HTTPS/TLS). Udviklerens server fungerer kun som en mellemmand for organisering og gemmer intet indhold (stateless).

## Artikel 10 (Brug af mindreårige)

Appen har en aldersgrænse på 4+, men dens natur (organisering af tanker) forudsætter, at brugeren kan læse og skrive. Mindreårige bør bruge appen med samtykke fra en værge.

## Artikel 11 (Ændringer i denne privatlivspolitik)

Denne politik kan blive revideret som følge af ændringer i lovgivningen, tilføjelse af nye funktioner eller ændringer i specifikationerne for de enkelte platformes (Apple / Google) frameworks eller politikker. Ved væsentlige ændringer vil det blive annonceret i forbindelse med en app-opdatering eller på den offentlige side for denne politik.

## Artikel 12 (Kontakt)

For henvendelser vedrørende denne politik, bedes du kontakte os via "Udvikler"-sektionen på appens side i App Store eller Google Play, eller via "Indstillinger → Kontakt" inde i appen.

## Artikel 13 (Om annoncer og App Tracking Transparency)

Når du ikke abonnerer på KUU+, viser appen én enkelt native annonce fra Google AdMob mellem sektionerne på "Det du har sagt"-skærmen. Selve annoncen vises diskret for at bevare KUU's visuelle udtryk.

-   **Dit indtalte indhold bruges aldrig til annoncering** (annoncerne har ikke adgang til dine transskriberinger, organiseringsresultater eller temaer).
-   Til annoncelevering kan Google AdMob indsamle enhedsidentifikatorer (herunder IDFA), annonce-ID, omtrentlig placering (Coarse Location), diagnostik og produktinteraktioner (interaktioner med annoncer i appen).
-   **iOS-versionen**: En **App Tracking Transparency** (ATT) anmodning vises én gang, umiddelbart før den første annonce. Annoncer vil stadig blive vist, hvis du afviser, men de oplysninger, der sendes til Google, vil være begrænsede (ikke-personaliserede). Du kan til enhver tid ændre din ATT-tilladelse i iOS under "Indstillinger" → "Anonymitet & sikkerhed" → "Sporing".
-   **Android-versionen**: ATT er en funktion, der er specifik for iOS, og findes ikke på Android. I stedet bruges Googles **Annonce-id (Advertising ID)** til annoncelevering. Du kan fravælge personaliserede annoncer eller nulstille dit annonce-id fra din enheds "Indstillinger → Anonymitet → Annoncer" (formuleringen kan variere afhængigt af enhed og Android-version). Android-versionen følger desuden den samtykkestyring (UMP), der vises i relevante regioner såsom EU.
-   **Et abonnement på KUU+ stopper alle annoncer og den tilhørende dataoverførsel**.
-   For detaljer om Google AdMobs databehandling, se [Google AdMobs privatlivspolitik](https://support.google.com/admob/answer/6128543).

## Artikel 14 (Om brug af Firebase Analytics / Crashlytics)

**Samtykkemodellen (opt-in) i denne artikel gælder for iOS-versionen. For Android-versionen, se afsnittet "Om Android-versionen" i slutningen af denne artikel.**

**iOS-versionen** kan, for at forbedre appens kvalitet og hurtigt opdage fejl i produktion, anvende Googles Firebase Analytics (aggregeret brugsstatistik) og Firebase Crashlytics (nedbrudsrapportering). **Denne funktion er som standard DEAKTIVERET (ingen data sendes) og aktiveres kun, hvis brugeren eksplicit giver samtykke (opt-in) via "Indstillinger → Data & diagnostik".**

-   **Oplysninger, der sendes**:
    -   Et anonymiseret installations-ID, som Firebase automatisk udsteder (baseret på IDFV; det er ikke en direkte personlig identifikator).
    -   Aggregerede signaler om hændelser i appen (fuldførelse af optagelsessession, visning/konvertering af betalingsmur, gennemførelse af onboarding osv. Numeriske værdier sendes i grupperet, grov granularitet).
    -   Symboliserede stack traces ved nedbrud, når appen lukker unormalt.
-   **Oplysninger, der ikke sendes**: Dit indtalte indhold (lyd), transskriberinger, AI-organiserede resultater og de temanavne, du har angivet, er **designet til at være umulige at sende på typeniveau** (implementeringens API forhindrer, at strengværdier kan sendes til analyse-SDK'et).
-   **Så længe der ikke er givet samtykke, finder ingen kommunikation med Firebase sted overhovedet** (inklusive alle ovenstående kategorier).
-   **Sådan stopper du afsendelse**: Du kan til enhver tid slå kontakten i "Indstillinger → Data & diagnostik" FRA. Når den slås fra, kasseres tidligere installations-ID'er, og eventuelle usendte nedbrudslogfiler, der er gemt lokalt på enheden, slettes.
-   Modtageren er Google LLC (USA). Googles [Firebase Privacy Information](https://firebase.google.com/support/privacy) er gældende.

**Om Android-versionen:** Android-versionen bruger Firebase Analytics til at sende **brugshændelser uden indhold** til produktforbedring (grupperede værdier såsom skærmskift og antal brug af funktioner) samt et anonymt App Instance ID udstedt af Firebase. **I modsætning til iOS er dette aktiveret som standard.** Dit indtalte indhold (lyd), transskriberinger, organiserede resultater og temanavne **kan ikke sendes** – analyse-SDK'ets API er designet, så strengværdier ikke kan overføres til det. **Android-versionen indeholder ikke Crashlytics og sender ingen nedbrudsrapporter.** Modtageren er Google LLC (USA); Googles [Firebase Privacy Information](https://firebase.google.com/support/privacy) er gældende.
