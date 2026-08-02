> Dette er en referanseoversettelse for enkelhets skyld. Den japanske versjonen er den autoritative teksten.

# Personvernerklæring for KUU

Sist oppdatert: 2. august 2026

**Kort fortalt:** Det du har sagt, er ditt. **Appen sender aldri selve lydopptaket ditt noe sted.** På iPhone- og Android-enheter skjer også transkriberingen på enheten. **Apple Watch-versjonen av appen gjør ingen lydopptak i det hele tatt** – den mottar kun teksten som er produsert av standardinndata på klokken (diktering, håndskrift eller tastatur). Når du velger diktering, håndteres talegjenkjenningen av Apples eget system (se artikkel 3). For organisering (KI-kategorisering) brukes en ekstern KI, men kun den transkriberte teksten sendes. Den brukes utelukkende til organisering og lagres ikke. Det som lagres, ligger kun på enheten din, og for iOS også i din private iCloud-database (Android lagrer kun på enheten). Utvikleren lagrer ikke innholdet ditt og kan ikke se det som mottas. Du kan slette all data fra innsiden av appen når som helst. Appen utfører kun **minimalt med nettverkskommunikasjon** for fakturering (StoreKit på iOS / RevenueCat på Android) og Google AdMob-annonser, og denne informasjonen inkluderer aldri det du har sagt (annonser deaktiveres med KUU+). Bruksmønstre måles for å forbedre kvaliteten, men dette inkluderer heller aldri det du har sagt (iOS krever aktiv påmelding fra brukeren; Android sender innholdsfri måling som standard – se artikkel 14).

---

## Artikkel 1 (Grunnprinsipper)

Appen «KUU» (heretter «appen») er en applikasjon som hjelper deg med å få tanker ut av hodet ved å si dem høyt og organisere dem. Den er tilgjengelig for **iOS (iPhone og Apple Watch) og Android**, og denne erklæringen gjelder for alle versjoner. Appen behandler informasjon kun i den grad det er nødvendig for å levere funksjonalitet, og prioriterer brukernes personvern.

## Artikkel 2 (Informasjon som innhentes og lagres)

Appen håndterer kun følgende informasjon:

1.  **Lyd du tar opp** — Lydopptak lagres midlertidig i et lokalt buffer på enheten kun under transkribering, og slettes umiddelbart etterpå. Det sendes aldri til noen server. **Apple Watch-versjonen av appen gjør ingen lydopptak i det hele tatt** (se artikkel 3).
2.  **Transkribert og organisert tekst** — Lagres slik at du selv kan se gjennom det (iOS: på enheten din og i din private iCloud-database; Android: kun på enheten. På en tilkoblet Apple Watch lagres kun de nyeste titlene i hver kategori, for visningsformål. Se artikkel 4).
3.  **Innstillinger i appen** — Tema, tekststørrelse, vannstand i hodet og andre verdier som er nødvendige for appens funksjon.

Appen samler ikke inn personopplysninger som navn, e-postadresse, telefonnummer, posisjonsdata, kontakter, kalender, bilder eller enhetsidentifikatorer.

## Artikkel 3 (Om talegjenkjenning og KI-kategorisering)

**Talegjenkjenning (transkribering)** foregår i sin helhet på din egen enhet for iPhone (iOS) og Android-enheter (for Apple Watch, se slutten av denne artikkelen).

-   Talegjenkjenning: Bruker Apples Speech-rammeverk (på enheten). Selve stemmen din sendes aldri ut av enheten.

**KI-kategorisering (sortering)** bruker en ekstern KI:

-   Kun **teksten av det du sa (transkripsjonen)** sendes. Stemmen din sendes aldri.
-   Den sendes til en ekstern KI, via utviklerens tjener (backend via Googles Gemini).
-   Teksten som sendes, brukes **kun til kategorisering og blir aldri lagret**. Den brukes heller ikke til å trene KI-en.
-   Dette omfatter ikke bare det du har sagt og transkribert, men også alt du har skrevet eller redigert manuelt. Hvis automatisk tematisering er aktivert (KUU+, valgfritt), sendes også lagrede titler, tekster og temanavn for å kunne tildele tema (alt brukes kun til klassifisering og lagres ikke).
-   **For iOS-versjonen** før 2.3.0 kan du velge klassifisering kun på enheten via «På enheten» i Innstillinger (denne innstillingen tilbys ikke lenger fra og med versjon 2.3.0).

**Om Android-versjonen:** Android-versjonen tilbyr ikke en organiseringsmetode som kun foregår på enheten. Når du organiserer, blir den transkriberte teksten **alltid** sendt til den eksterne KI-en (Googles Gemini via vår backend). Kun den transkriberte teksten sendes – selve stemmen din sendes aldri, og den sendte teksten brukes utelukkende til kategorisering og blir verken lagret eller brukt til å trene KI-en. Selve transkriberingen (talegjenkjenningen) kjører i sin helhet på enheten.

**Om Apple Watch-versjonen:** Apple Watch-versjonen av appen verken tar opp lyd eller utfører talegjenkjenning selv. For inndata brukes standard tekstinntasting i watchOS (du velger mellom diktering, håndskrift eller tastatur), og appen mottar kun den resulterende teksten. Når du velger diktering, utføres talegjenkjenningen som en funksjon fra Apple (watchOS). Hvordan den behandles – inkludert om det skjer på enheten eller på Apples servere – avhenger av enheten, innstillingene og språket ditt, og er **underlagt Apples personvernerklæring**. Appen har ikke tilgang til lyden, og mottar eller lagrer den aldri. Den resulterende teksten behandles nøyaktig som tekst du har snakket inn på iPhone (KI-kategorisering under denne artikkelen; lagring under artikkel 4).

## Artikkel 4 (Lagring og synkronisering)

**iOS-versjonen:** Transkribert og organisert tekst lagres kun i din **private iCloud-database** (CloudKit Private Database). Dette er en lagringstjeneste levert av Apple som kun du har tilgang til. Appens utvikler kan verken se eller hente ut lagret innhold. Bruken av iCloud er underlagt Apples personvernerklæring.

**Android-versjonen:** Transkribert og organisert tekst lagres **kun på denne enheten**. Det utføres ingen automatisk skysynkronisering. Ved bytte av enhet kan du eksportere dataene til en fil fra «Stemme og data» i appen og importere den på den nye enheten. Du velger selv hvor filen lagres (på enheten, i din skylagringsapp osv.). Utvikleren har ikke tilgang til denne filen.

**Apple Watch-versjonen:** For visningsformål overføres en del av den organiserte teksten (de nyeste titlene i hver kategori) til din tilkoblede Apple Watch via Apples enhet-til-enhet-kommunikasjon (Watch Connectivity) og **lagres også på klokken**. Tekst du skriver inn på Apple Watch, overføres til iPhone på samme måte. Utviklerens server er ikke involvert i denne overføringen eller lagringen.

## Artikkel 5 (Formål med bruken)

Informasjonen som håndteres, brukes kun til følgende formål:

1.  Å generere transkripsjoner fra stemmen din og vise dem til deg
2.  Å kategorisere transkripsjoner i «Se nå / Tenk på senere / La ligge / Gi slipp» og vise dem til deg
3.  Å lagre og vise det du har sagt, slik at du selv kan se gjennom det
4.  Å opprettholde innstillinger som er nødvendige for appens funksjon

## Artikkel 6 (Bruk av eksterne tjenester)

Appen bruker følgende eksterne tjenester for å levere funksjonalitet. **Selve stemmen din sendes ikke til noen av disse tjenestene.**

-   **iCloud / CloudKit** (kun iOS. Levert av Apple. Lagring og synkronisering kun til din egen private database)
-   **Talegjenkjenning** (iOS: Apples Speech-rammeverk; Android: enhetens innebygde talegjenkjenningsmotor. Begge kjører på enheten; stemmen din sendes aldri ut av enheten. **Apple Watch-versjonen utfører ikke talegjenkjenning i appen og bruker standard watchOS-inndata**. Se artikkel 3.)
-   **Standard tekstinntasting i watchOS** (kun Apple Watch. Levert av Apple. Du velger mellom diktering, håndskrift eller tastatur. Ved diktering utføres talegjenkjenning som en Apple-funksjon og er underlagt Apples personvernerklæring. Appen har ikke tilgang til lyden. Se artikkel 3.)
-   **Watch Connectivity** (kun Apple Watch. Levert av Apple. Overfører visningstekst direkte mellom din iPhone og Apple Watch. Utviklerens server er ikke involvert. Se artikkel 4.)
-   **En ekstern KI (skybasert)** (KI-kategorisering. Kun teksten av det du sa sendes; brukes utelukkende til kategorisering, lagres aldri, og brukes aldri til KI-trening. Se artikkel 3.)
-   **Faktureringstjenester** (iOS: **Apple StoreKit**; Android: **RevenueCat**. For kjøp, fornyelse, kansellering og statusadministrasjon av KUU+-abonnement. Innholdet du har sagt, sendes ikke. For RevenueCat, se artikkel 7 og [RevenueCats personvernerklæring](https://www.revenuecat.com/privacy).)
-   **Play Integrity API (via Firebase App Check; kun Android)** (Verifiserer at forespørsler til klassifiserings-API-et kommer fra en legitim app – en attestering av enhetens/appens integritet. Inneholder ikke det du har sagt eller brukeridentifiserende informasjon.)
-   **Google AdMob (Google Mobile Ads SDK)** (Kun når KUU+ ikke er aktivt: én enkelt annonseplass mellom seksjoner på «Det du har sagt»-skjermen. Innholdet du har sagt, sendes ikke. Se artikkel 13.)
-   **Firebase Analytics** (Levert av Google. For kvalitetsforbedring av appen. På iOS, **brukes kun når du eksplisitt melder deg på via Innstillinger**; på Android sendes innholdsfrie brukshendelser **som standard** (i begge tilfeller sendes ikke det du har sagt). iOS bruker også **Crashlytics** ved påmelding, men **Android-versjonen inkluderer ikke Crashlytics**. Se artikkel 14.)

Appens server er minimal og fungerer kun som en mellomstasjon for KI-kategorisering, uten å lagre noe innhold (stateless). Appen bruker ikke autentiseringstjenester som krever personlige kontoer.

## Artikkel 7 (Utlevering til tredjeparter)

Appens utvikler har ingen mulighet til å få tilgang til innholdet du har sagt, transkripsjoner eller organiserte resultater, og utleverer ikke dette til noen tredjepart.

For å levere annonser til brukere som ikke abonnerer på KUU+, sendes informasjon som Google AdMob krever for annonselevering – inkludert enhetsidentifikatorer, annonse-ID, enhetens språk og region, omtrentlig posisjon og interaksjonsdata med annonser – til Google (se artikkel 13; Googles personvernerklæring for AdMob gjelder). Mens KUU+ er aktivt, skjer ikke denne overføringen.

Når du abonnerer på KUU+ på **Android-versjonen**, sendes kjøpsinformasjon (produkt-ID, pris, kjøpsdato osv.) til RevenueCat, Inc. for å håndtere kjøpet og dine rettigheter (aktiv/inaktiv). Innholdet du har sagt, sendes ikke. Se [RevenueCats personvernerklæring](https://www.revenuecat.com/privacy) for detaljer.

Informasjon vil kun bli utlevert når det er påkrevd ved lov, i henhold til gjeldende prosedyrer.

## Artikkel 8 (Sletting av data)

Du kan slette all data når som helst fra «Innstillinger → Stemme og data → Slett det som er lagret» inne i appen. Dette fjerner permanent data på enheten (og, for iOS, også i den private iCloud-databasen). Slettede data kan ikke gjenopprettes.

Avinstallering av appen sletter lokale data. På iOS kan iCloud-data fjernes via Innstillinger → Apple ID → iCloud → Administrer lagring. Android-versjonen lagrer kun data på enheten, så de fjernes ved avinstallering.

**Apple Watch:** Når du sletter all data, vil visningsdataene som allerede er overført til din Apple Watch, bli erstattet med tomt innhold neste gang klokken kobles til. Sletting av appen fra din Apple Watch fjerner også visningsdataene som er lagret på den.

## Artikkel 9 (Sikkerhetstiltak)

-   **iOS-versjonen**: Midlertidige lydfiler under opptak krypteres av iOS' filbeskyttelse (`FileProtectionType.complete`) og er utilgjengelige når enheten er låst. Kommunikasjon med iCloud krypteres av Apple via SSL/TLS.
-   **Android-versjonen**: Lydopptak skrives aldri til disk, selv ikke som en midlertidig fil; det behandles kun i minnet og forkastes umiddelbart etter gjenkjenning. Lagrede transkripsjoner og organiserte resultater ligger i appens private lagringsområde, utilgjengelig for andre apper, og er ekskludert fra Androids automatiske skysikkerhetskopiering.
-   **Apple Watch-versjonen**: Overføringen mellom din iPhone og Apple Watch håndteres av Apples Watch Connectivity og går ikke via noen av utviklerens servere. Det som lagres på Apple Watch, er begrenset til visningstekst (de nyeste titlene i hver kategori); ingen lyd lagres.
-   All kommunikasjon med den eksterne KI-en er kryptert (HTTPS/TLS). Utviklerens server videresender kun organiseringsforespørsler og lagrer ikke noe innhold (stateless).

## Artikkel 10 (Bruk av mindreårige)

Appen er vurdert til 4+, men dens natur (organisering av tanker) forutsetter lese- og skriveferdigheter. Mindreårige bør bruke appen med samtykke fra en foresatt.

## Artikkel 11 (Endringer i denne personvernerklæringen)

Denne erklæringen kan bli oppdatert som følge av lovendringer, nye funksjoner eller endringer i spesifikasjonene for hver plattforms (Apple / Google) rammeverk eller retningslinjer. Vesentlige endringer vil bli varslet via en appoppdatering eller på den offentlige siden for denne erklæringen.

## Artikkel 12 (Kontakt)

For henvendelser angående denne erklæringen, vennligst kontakt oss via «Utvikler»-seksjonen på appens side i App Store eller Google Play, eller via «Innstillinger → Kontakt» inne i appen.

## Artikkel 13 (Om annonser og App Tracking Transparency)

Når du ikke abonnerer på KUU+, viser appen én enkelt annonseplass mellom seksjonene på «Det du har sagt»-skjermen, levert av Google AdMob. Annonsene vises diskret for å passe inn i KUUs visuelle uttrykk.

-   **Innholdet du har sagt, brukes aldri til annonsering.** Annonser tar ikke hensyn til dine transkripsjoner, organiserte resultater eller temaer.
-   For å levere annonser kan Google AdMob samle inn enhetsidentifikatorer (inkludert IDFA), annonse-ID, omtrentlig posisjon (Coarse Location), diagnostikk og produktinteraksjoner (interaksjoner med annonser i appen).
-   **iOS-versjonen:** En forespørsel om **App Tracking Transparency** (ATT) vises én gang, rett før den første annonsen. Annonser vil fortsatt vises hvis du avslår, men informasjonen som sendes til Google vil være begrenset (ikke-personlig tilpasset). Du kan endre ATT-tillatelsen når som helst i iOS under «Innstillinger → Personvern og sikkerhet → Sporing».
-   **Android-versjonen:** ATT er en funksjon kun for iOS og finnes ikke på Android. I stedet brukes Googles **annonse-ID (Advertising ID)** for annonselevering. Du kan velge bort personlig tilpassede annonser eller tilbakestille annonse-ID-en fra enhetens «Innstillinger → Personvern → Annonser» (ordlyden kan variere etter enhet og Android-versjon). Android-versjonen følger også samtykkehåndteringen (UMP) som vises i aktuelle regioner som EU.
-   **Et abonnement på KUU+ stopper alle annonser og tilhørende dataoverføring.**
-   For detaljer om AdMobs databehandling, se [Google AdMobs personvernerklæring](https://support.google.com/admob/answer/6128543).

## Artikkel 14 (Om bruk av Firebase Analytics / Crashlytics)

**Påmeldingsmodellen i denne artikkelen gjelder for iOS-versjonen. For Android-versjonen, se «Om Android-versjonen» på slutten av denne artikkelen.**

**På iOS** kan appen bruke Googles Firebase Analytics (aggregerte bruksdata) og Firebase Crashlytics (krasjrapportering) for kvalitetsforbedring og umiddelbar varsling om produksjonsfeil. **Denne funksjonen er AV som standard (ingen data sendes) og aktiveres kun når du eksplisitt melder deg på via «Innstillinger → Data og diagnostikk».**

-   **Informasjon som sendes**:
    -   En anonymisert installasjons-ID automatisk utstedt av Firebase (basert på IDFV; ikke en direkte personlig identifikator)
    -   Aggregerte signaler om hendelser i appen (fullføring av opptak, visning/konvertering av betalingsmur, fullføring av introduksjon osv. Numeriske verdier grupperes i grove intervaller.)
    -   Symboliserte stakkspor (crash stack traces) når appen avsluttes unormalt
-   **Informasjon som ikke sendes**: Ditt talte innhold (lyd), transkripsjoner, KI-organiserte resultater og temanavn du angir, er **designet slik at de ikke kan sendes på typenivå** (implementeringens API forhindrer at strengverdier kan sendes til analyseverktøyet).
-   **Så lenge du ikke har meldt deg på, forekommer ingen kommunikasjon med Firebase i det hele tatt** (inkludert alle kategoriene ovenfor).
-   **Slik stopper du sendingen**: Slå av bryteren i «Innstillinger → Data og diagnostikk» når som helst. Når den slås av, forkastes tidligere installasjons-ID-er, og eventuelle usendte krasjlogger som er lagret lokalt på enheten, slettes.
-   Mottakeren er Google LLC (USA). Googles [personverninformasjon for Firebase](https://firebase.google.com/support/privacy) gjelder.

**Om Android-versjonen:** Android-versjonen bruker Firebase Analytics til å sende **innholdsfrie brukshendelser** for produktforbedring (grupperte verdier som skjermoverganger og antall ganger en funksjon brukes) pluss en anonym App Instance ID utstedt av Firebase. **I motsetning til iOS, er dette aktivert som standard.** Ditt talte innhold (lyd), transkripsjoner, organiserte resultater og temanavn **kan ikke sendes** – analyseverktøyets API er designet slik at strengverdier ikke kan overføres til det. **Android-versjonen inkluderer ikke Crashlytics og sender ingen krasjrapporter.** Mottakeren er Google LLC (USA); Googles [personverninformasjon for Firebase](https://firebase.google.com/support/privacy) gjelder.
