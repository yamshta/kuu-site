> Dette er en referenceoversættelse for nemheds skyld. Den japanske version er den autoritative tekst.

# Privatlivspolitik for KUU

Sidst opdateret: 21. juli 2026

**Kort sagt:** Det, du siger, er dit. **Selve din stemme bliver aldrig sendt uden for din enhed.** Transskribering sker på din enhed. Til organisering bruges en ekstern AI, men det er kun den transskriberede tekst, der sendes. Den bruges udelukkende til organisering og gemmes ikke (på iOS kan du skifte til organisering kun på enheden via "På enheden" i Indstillinger; **Android-versionen sender kun til den eksterne AI — der er ingen organisering på enheden**). Det, der gemmes, ligger kun på din enhed, og på iOS også i din private iCloud-database (Android gemmer kun på enheden). Udvikleren gemmer ikke dit indhold og kan ikke se, hvad der modtages. Du kan til enhver tid slette alle data indefra i appen. Appen foretager kun den **absolut nødvendige netværkskommunikation** til fakturering (StoreKit på iOS / RevenueCat på Android) og Google AdMob-reklamer, og disse oplysninger indeholder aldrig det, du har sagt (reklamer forsvinder med KUU+). Brugsdata måles for at forbedre kvaliteten, men dette indeholder heller aldrig det, du har sagt (iOS er bruger-opt-in; Android sender som standard målinger uden indhold — se Artikel 14).

---

## Artikel 1 (Grundlæggende politik)

KUU ("Appen") er en applikation (tilgængelig på **iOS og Android**), der hjælper dig med at få tanker ud af hovedet ved at sige dem højt og organisere dem. Denne politik gælder for begge versioner. Appen behandler kun oplysninger i det omfang, det er absolut nødvendigt for at levere dens funktioner, og prioriterer brugerens privatliv højest.

## Artikel 2 (Oplysninger, der indhentes og gemmes)

Appen håndterer udelukkende følgende oplysninger:

1.  **Brugerens indtalte indhold (lyddata)** — Den optagede lyd gemmes midlertidigt i en lokal buffer på enheden, kun mens transskriberingen foregår. Den slettes øjeblikkeligt efter behandlingen. Den sendes aldrig til nogen server.
2.  **Transskriberingsresultater og organiseringsresultater (tekst)** — Gemmes, så du selv kan gennemse dem (iOS: på din enhed og i din private iCloud-database; Android: kun på enheden — se Artikel 4).
3.  **Indstillinger i appen** — Tema, tekststørrelse, vandstand i hovedet og andre indstillingsværdier, der er nødvendige for appens funktion.

Appen indsamler ikke personlige oplysninger såsom navn, e-mailadresse, telefonnummer, lokation, kontakter, kalender, billeder eller enhedsidentifikatorer.

## Artikel 3 (Om talegenkendelse og AI-organisering)

**Talegenkendelse (transskribering)** udføres udelukkende på din iOS-enhed:

-   Talegenkendelse: Apples Speech-framework (på enheden). Selve din stemme sendes aldrig uden for enheden.

**AI-organisering (kategorisering)** bruger en ekstern AI:

-   Det er kun **teksten fra det, du har sagt (transskriptionen)**, der sendes. Din stemme sendes aldrig.
-   Den sendes til en ekstern cloud-AI (Googles Gemini via udviklerens backend), videresendt gennem udviklerens server.
-   Den sendte tekst bruges **udelukkende til kategorisering og gemmes aldrig**. Den bruges heller ikke til at træne AI'en.
-   **På iOS** kan du til enhver tid skifte til **organisering udelukkende på enheden** (Apples FoundationModels / regler på enheden) via "På enheden" i Indstillinger. I så fald forlader teksten heller aldrig enheden.

**Om Android-versionen:** Android-versionen tilbyder ikke en organiseringsmetode, der udelukkende foregår på enheden. Når du organiserer, bliver den transskriberede tekst **altid** sendt til den eksterne AI (Googles Gemini via vores backend). Der er ingen "På enheden"-kontakt som på iOS. Det er kun den transskriberede tekst, der sendes — selve din stemme sendes aldrig, og den sendte tekst bruges udelukkende til kategorisering og bliver hverken gemt eller brugt til at træne AI'en. Selve transskriberingen (talegenkendelsen) foregår udelukkende på enheden.

## Artikel 4 (Lagring og synkronisering)

**iOS-versionen:** Appen gemmer transskriberede og organiserede tekster udelukkende i din **private iCloud-database** (CloudKit Private Database). Dette er et lager leveret af Apple, som kun du har adgang til. Appens udvikler kan hverken se eller hente det gemte indhold. Brugen af iCloud er underlagt Apples privatlivspolitik.

**Android-versionen:** Transskriberede og organiserede tekster gemmes **udelukkende på denne enhed**. Der er ingen automatisk synkronisering til skyen. Ved skift af enhed kan du eksportere til en fil fra "Stemmeføring & data" i appen og importere den på den nye enhed. Du vælger selv, hvor filen gemmes (på enheden, i din cloud-lagerapp osv.). Udvikleren har ikke adgang til denne fil.

## Artikel 5 (Formål med brugen)

De håndterede oplysninger bruges udelukkende til følgende formål:

1.  At generere transskriptioner fra brugerens stemme og vise dem.
2.  At kategorisere transskriptioner i "Se nu / Tænk over senere / Lad ligge / Giv slip" og vise dem for brugeren.
3.  At gemme og vise tidligere indtalt indhold, så brugeren selv kan gennemse det.
4.  At bevare de indstillingsværdier, der er nødvendige for appens funktion.

## Artikel 6 (Brug af eksterne tjenester)

Appen bruger følgende eksterne tjenester for at levere sine funktioner. **Selve din stemme sendes ikke til nogen af disse tjenester.**

-   **iCloud / CloudKit** (kun iOS-versionen. Leveret af Apple. Gemmer og synkroniserer kun i din egen private database)
-   **Talegenkendelse** (iOS-versionen bruger Apples Speech-framework, Android-versionen bruger enhedens interne talegenkendelsesmotor. Begge kører på enheden, og lyden sendes ikke uden for enheden)
-   **Ekstern AI (cloud)** (AI-organisering. Kun den transskriberede tekst sendes. Bruges udelukkende til kategorisering, gemmes ikke og bruges ikke til AI-træning. På iOS kan dette slås fra via "På enheden" i Indstillinger, men **Android-versionen sender kun til den eksterne AI**. Se detaljer i Artikel 3)
-   **FoundationModels** (kun iOS-versionen. Leveret af Apple. Kører udelukkende på enheden. Bruges, når "På enheden" er aktiveret, og som fallback, når den eksterne AI ikke er tilgængelig)
-   **Faktureringstjenester** (iOS-versionen bruger **Apple StoreKit**, Android-versionen bruger **RevenueCat**. Til køb, fornyelse, opsigelse og rettighedsstyring af KUU+-abonnementet. Indtalt indhold sendes ikke. For RevenueCat, se Artikel 7 og [RevenueCats privatlivspolitik](https://www.revenuecat.com/privacy))
-   **Play Integrity API (via Firebase App Check. Kun Android-versionen)** (For at bekræfte, at anmodninger til klassificerings-API'en kommer fra en legitim app, via en attestering af enhedens og appens integritet. Indeholder ikke indtalt indhold eller brugeridentificerende oplysninger)
-   **Google AdMob (Google Mobile Ads SDK)** (Kun når KUU+ ikke er aktivt, vises én enkelt native annonce mellem sektioner på skærmen "Det du har sagt". Indtalt indhold sendes ikke. Se detaljer i Artikel 13)
-   **Firebase Analytics** (Leveret af Google. Til forbedring af appens kvalitet. På iOS-versionen **kun hvis brugeren eksplicit tilmelder sig (opt-in) i Indstillinger**; på Android-versionen sendes brugsdatahændelser uden indhold **som standard** (i begge tilfælde sendes indtalt indhold ikke). iOS-versionen bruger også **Crashlytics** ved tilmelding, men **Android-versionen inkluderer ikke Crashlytics**. Se detaljer i Artikel 14)

Appens server fungerer udelukkende som et minimalt relæ for AI-organisering og gemmer intet indhold (er stateless). Der bruges ingen autentificeringstjenester, der kræver en personlig konto.

## Artikel 7 (Videregivelse til tredjepart)

Appens udvikler har ingen mulighed for at tilgå brugerens indtalte indhold, transskriberingsresultater eller organiseringsresultater og videregiver ikke disse til nogen tredjepart.

For at levere reklamer til brugere, der ikke abonnerer på KUU+, sendes oplysninger, som Google AdMob kræver til reklamelevering – herunder enhedsidentifikatorer, reklame-ID, enhedens sprog og region, omtrentlig placering og oplysninger om interaktion med reklamer – til Google (se Artikel 13; Googles AdMob-privatlivspolitik gælder). Mens KUU+ er aktivt, sker denne informationsoverførsel ikke.

Når du abonnerer på KUU+ på **Android-versionen**, sendes købsoplysninger (produkt-ID, pris, købsdato osv.) til RevenueCat, Inc. for at håndtere købet og dine rettigheder (aktiv/inaktiv). Indtalt indhold sendes ikke. Se detaljer om RevenueCats datahåndtering i [RevenueCats privatlivspolitik](https://www.revenuecat.com/privacy).

Oplysninger vil kun blive videregivet, hvis det er påkrævet ved lov, og i overensstemmelse med de gældende procedurer.

## Artikel 8 (Sletning af data)

Brugeren kan til enhver tid slette alle data fra "Indstillinger → Stemmeføring & data → Slet det, der er gemt" inde i appen. Dette fjerner permanent data på enheden (og på iOS-versionen også data i den private iCloud-database). Slettede data kan ikke gendannes.

Hvis du afinstallerer appen, slettes data på enheden. På iOS-versionen kan data i iCloud fjernes via Apples indstillinger (Indstillinger → Apple-id → iCloud → Administrer lagringsplads). Da Android-versionen kun gemmer data på enheden, slettes de ved afinstallation.

## Artikel 9 (Sikkerhedsforanstaltninger)

-   **iOS-versionen**: Midlertidige lydfiler under optagelse krypteres af iOS' filbeskyttelse (`FileProtectionType.complete`) og er utilgængelige, når enheden er låst. Kommunikation med iCloud krypteres af Apple via SSL/TLS.
-   **Android-versionen**: Optaget lyd skrives aldrig til disken, heller ikke som en midlertidig fil; den behandles udelukkende i hukommelsen og kasseres umiddelbart efter genkendelse. Gemte transskriptioner og organiseringsresultater ligger i appens private lagerområde, utilgængeligt for andre apps, og er udelukket fra Androids automatiske backup til skyen.
-   Al kommunikation med den eksterne AI er krypteret (HTTPS/TLS). Udviklerens server videresender kun anmodninger om organisering og gemmer intet indhold (er stateless).

## Artikel 10 (Brug af mindreårige)

Appen har en aldersgrænse på 4+, men dens natur (organisering af tanker) forudsætter, at brugeren kan læse og skrive. Hvis mindreårige bruger appen, skal de have samtykke fra en værge.

## Artikel 11 (Ændringer i denne politik)

Denne politik kan blive opdateret som følge af lovændringer, tilføjelse af funktioner eller ændringer i specifikationerne for hver platforms (Apple / Google) frameworks eller politikker. Væsentlige ændringer vil blive annonceret via en app-opdatering eller på den offentlige side for denne politik.

## Artikel 12 (Kontakt)

For henvendelser vedrørende denne politik, bedes du kontakte os via "Udvikler"-sektionen på appens side i App Store eller Google Play, eller via "Indstillinger → Kontakt" inde i appen.

## Artikel 13 (Om reklamer og App Tracking Transparency)

Når du ikke abonnerer på KUU+, viser appen én enkelt native annonce fra Google AdMob mellem sektionerne på skærmen "Det du har sagt". Selve reklamen vises diskret for at bevare KUU's visuelle ro.

-   **Dit indtalte indhold bruges aldrig til reklamer.** (Reklamer konsulterer ikke dine transskriptioner, organiseringsresultater eller temaer).
-   For at levere reklamer kan Google AdMob indsamle enhedsidentifikatorer (inklusive IDFA), reklame-ID, Coarse Location (omtrentlig placering), Diagnostics og Product Interaction (oplysninger om interaktion med reklamer i appen).
-   **iOS-versionen**: En **App Tracking Transparency** (ATT) prompt vises én gang, lige før den første reklame. Reklamer vil stadig blive vist, hvis du afviser, men de oplysninger, der sendes til Google, vil være begrænsede (ikke-personaliserede). Du kan til enhver tid ændre ATT-tilladelsen i iOS under "Indstillinger" → "Anonymitet & sikkerhed" → "Tracking".
-   **Android-versionen**: ATT er en funktion, der er specifik for iOS, og findes ikke på Android. I stedet bruges Googles **Reklame-id (Advertising ID)** til reklamelevering. Du kan fravælge personaliserede reklamer eller nulstille dit reklame-id fra din enheds "Indstillinger → Privatliv → Annoncer" (ordlyden kan variere afhængigt af enhed og Android-version). Android-versionen overholder også den samtykkestyring (UMP), der vises i relevante regioner som f.eks. EU.
-   **Når du abonnerer på KUU+, stopper alle reklamer og den relaterede dataoverførsel.**
-   For detaljer om AdMobs datahåndtering, se venligst [Google AdMobs privatlivspolitik](https://support.google.com/admob/answer/6128543).

## Artikel 14 (Om brug af Firebase Analytics / Crashlytics)

**Tilvalgsmodellen (opt-in) i denne artikel gælder for iOS-versionen. For Android-versionen, se "Om Android-versionen" i slutningen af denne artikel.**

**På iOS** kan appen, med henblik på kvalitetsforbedring og øjeblikkelig varsling om produktionsfejl, bruge Googles Firebase Analytics (aggregeret brugsdata) og Firebase Crashlytics (nedbrudsrapportering). **Denne funktion er som standard SLÅET FRA (ingen data sendes) og aktiveres kun, hvis du eksplicit tilmelder dig (opt-in) via "Indstillinger → Data & diagnostik".**

-   **Oplysninger, der sendes**:
    -   Et anonymiseret installations-ID, som Firebase automatisk udsteder (baseret på IDFV; det er ikke en direkte personlig identifikator)
    -   Aggregerede signaler om hændelser i appen (fuldførelse af optagelsessession, visning/konvertering på betalingsmur, gennemførelse af onboarding osv. Numeriske værdier sendes i grupperede, grove intervaller.)
    -   Symboliserede crash stack traces, når appen lukker unormalt
-   **Oplysninger, der ikke sendes**: Dit indtalte indhold (lyd), transskriptioner, AI-organiserede resultater (tekst) og de temanavne, du indstiller, er **designet til at være umulige at sende på typeniveau** (implementeringens API forhindrer, at strengværdier kan sendes til analyse-SDK'et).
-   **I perioder, hvor du ikke er tilmeldt, forekommer der ingen kommunikation med Firebase overhovedet** (herunder alle ovenstående kategorier).
-   **Sådan stopper du afsendelse**: Du kan til enhver tid slå kontakten i "Indstillinger → Data & diagnostik" FRA. Når den slås fra, kasseres tidligere installations-ID'er, og eventuelle usendte nedbrudslogfiler, der er gemt lokalt på enheden, slettes.
-   Modtageren er Google LLC (USA). Googles [Firebase Privacy Information](https://firebase.google.com/support/privacy) gælder.

**Om Android-versionen:** Android-versionen bruger Firebase Analytics til at sende **brugsdatahændelser uden indhold** til produktforbedring (grupperede værdier som skærmskift og antal gange en funktion er brugt) samt et anonymt App Instance ID udstedt af Firebase. **I modsætning til iOS er dette aktiveret som standard.** Dit indtalte indhold (lyd), transskriptioner, organiserede resultater (tekst) og temanavne **kan ikke sendes** — analyse-SDK'ets API er designet, så strengværdier ikke kan videregives til det. **Android-versionen inkluderer ikke Crashlytics og sender ingen nedbrudsrapporter.** Modtageren er Google LLC (USA); Googles [Firebase Privacy Information](https://firebase.google.com/support/privacy) gælder.
