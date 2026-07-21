> Detta är en referensöversättning för din bekvämlighet. Den japanska versionen är den officiella texten.

# Integritetspolicy för KUU

Senast uppdaterad: 21 juli 2026

**Kort sagt:** Det du säger är ditt. **Din röst skickas aldrig utanför din enhet.** Transkriberingen sker på din enhet. För organisering (AI-kategorisering) används en extern AI, men endast den transkriberade texten skickas. Den används enbart för organisering och sparas inte (i iOS-versionen kan du byta till organisering enbart på enheten via ”På enheten” i Inställningar; **Android-versionen skickar endast till den externa AI:n – det finns inget alternativ för organisering på enheten**). Det som sparas finns endast på din enhet och, i iOS-versionen, i din privata databas på iCloud (Android lagrar endast på enheten). Utvecklaren sparar inte ditt innehåll och kan inte se det som tas emot. Du kan när som helst radera all data inifrån appen. Appen gör endast **minimala nätverksanrop** för fakturering (StoreKit på iOS / RevenueCat på Android) och Google AdMob-annonser, och den informationen inkluderar aldrig det du har sagt (annonser försvinner med KUU+). Användningen mäts för att förbättra kvaliteten, men detta inkluderar inte heller det du har sagt (iOS är opt-in för användaren; Android skickar innehållsfri mätning som standard – se Artikel 14).

---

## Artikel 1 (Grundläggande policy)

Denna app, ”KUU” (hädanefter ”Appen”), är en applikation som hjälper dig att få ut tankar ur huvudet genom att säga dem högt och organisera dem. Den finns som **iOS- och Android-version**, och denna policy gäller för båda. Appen hanterar information endast i den minsta utsträckning som krävs för att tillhandahålla sina funktioner, med högsta prioritet på att skydda användarens integritet.

## Artikel 2 (Information som hanteras och sparas)

Den information som Appen hanterar är begränsad till följande:

1.  **Innehållet du talar in (ljuddata)** — Inspelat ljud sparas endast tillfälligt i ett lokalt utrymme på enheten under transkriberingsprocessen och raderas omedelbart efter att processen är klar. Det skickas inte till någon server.
2.  **Transkriberingsresultat och organiseringsresultat (text)** — Sparas så att du själv kan granska dem (iOS-versionen: på enheten och i din privata databas på iCloud; Android-versionen: endast på enheten. Se Artikel 4 för detaljer).
3.  **Appinställningar** — Inställningsvärden som krävs för appens funktion, såsom tema, textstorlek och tillståndet för vattennivån i huvudet.

Appen samlar inte in personuppgifter som namn, e-postadress, telefonnummer, platsinformation, kontakter, kalender, foton eller enhetsidentifierare.

## Artikel 3 (Om röstigenkänning och AI-organisering)

**Röstigenkänning (transkribering)** sker helt och hållet på din iOS-enhet.

-   Röstigenkänning: Använder Apples Speech-ramverk (på enheten). Ljudet i sig skickas aldrig utanför enheten.

**AI-organisering (kategorisering)** använder en extern AI.

-   Endast **det du sagt i textform (den transkriberade texten)** skickas. Din röst skickas inte.
-   Det skickas till en extern AI, via utvecklarens server (via en backend till Googles Gemini).
-   Den skickade texten **används endast för kategorisering och sparas inte**. Den används inte heller för att träna AI:n.
-   **I iOS-versionen** kan du när som helst byta till **organisering som sker enbart på enheten** (Apples FoundationModels / regler på enheten) via ”På enheten” i Inställningar. I så fall lämnar inte heller texten enheten.

**Om Android-versionen:** Android-versionen erbjuder inte en organiseringsmetod som sker helt och hållet på enheten. När du organiserar skickas den transkriberade texten **alltid** till den externa AI:n (Googles Gemini via vår backend). Det finns ingen möjlighet att byta till ”På enheten” som i iOS-versionen. Endast den transkriberade texten skickas – din röst skickas aldrig, och den skickade texten används enbart för kategorisering, sparas inte och används inte heller för att träna AI:n. Själva transkriberingen (röstigenkänningen) sker helt och hållet på enheten.

## Artikel 4 (Lagring och synkronisering)

**iOS-versionen:** Transkriberings- och organiseringsresultat sparas endast i din **privata databas på iCloud** (CloudKit Private Database). Detta är ett lagringsutrymme som tillhandahålls av Apple och som endast du har tillgång till. Appens utvecklare kan varken se eller hämta det sparade innehållet. Användningen av iCloud omfattas av Apples integritetspolicy.

**Android-versionen:** Transkriberings- och organiseringsresultat sparas **endast på denna enhet**. Automatisk molnsynkronisering sker inte. Vid byte av enhet kan du exportera data till en fil från ”Röst och data” i appen och importera den på den nya enheten. Du väljer själv var filen sparas (på enheten, i en molnlagringsapp, etc.). Utvecklaren har inte tillgång till denna fil.

## Artikel 5 (Syfte med användningen)

Den hanterade informationen används endast för följande syften:

1.  Att generera transkriptioner från din röst och visa dem för dig.
2.  Att kategorisera transkriptioner i ”Se nu / Tänk senare / Låt vila / Släpp taget” och visa dem för dig.
3.  Att spara och visa det du tidigare har sagt så att du själv kan granska det.
4.  Att lagra inställningsvärden som är nödvändiga för appens funktion.

## Artikel 6 (Användning av externa tjänster)

Appen använder följande externa tjänster för att tillhandahålla sina funktioner. **Din röst skickas aldrig till någon av dessa tjänster.**

-   **iCloud / CloudKit** (endast iOS-versionen. Tillhandahålls av Apple. Spara och synkronisera endast till din egen privata databas).
-   **Röstigenkänning** (iOS-versionen använder Apples Speech-ramverk, Android-versionen använder enhetens inbyggda röstigenkänningsmotor. Båda körs på enheten och rösten skickas inte utanför den).
-   **Extern AI (molnbaserad)** (AI-organisering. Endast den transkriberade texten skickas. Används enbart för kategorisering, sparas inte och används inte för att träna AI:n. I iOS-versionen kan detta stängas av via ”På enheten” i Inställningar, men **Android-versionen skickar endast till den externa AI:n**. Se Artikel 3 för detaljer).
-   **FoundationModels** (endast iOS-versionen. Tillhandahålls av Apple. Körs helt på enheten. Används när ”På enheten” är aktiverat eller som reserv när den externa AI:n inte är tillgänglig).
-   **Faktureringstjänster** (iOS-versionen: **Apple StoreKit**; Android-versionen: **RevenueCat**. Hantering av köp, förnyelse, avslutande och status för KUU+-prenumerationer. Inget av det du sagt skickas. För RevenueCat, se Artikel 7 och [RevenueCats integritetspolicy](https://www.revenuecat.com/privacy)).
-   **Play Integrity API (via Firebase App Check; endast Android-versionen)** (Verifierar att anrop till kategoriserings-API:et kommer från en legitim app genom att intyga enhetens/appens integritet. Innehåller inte det du sagt eller information som identifierar användaren).
-   **Google AdMob (Google Mobile Ads SDK)** (Endast när KUU+ inte är aktivt: en plats för en inbyggd annons mellan avsnitten på skärmen ”Det du sagt”. Inget av det du sagt skickas. Se Artikel 13 för detaljer).
-   **Firebase Analytics** (Tillhandahålls av Google. För att förbättra appens kvalitet. I iOS-versionen **används det endast om användaren uttryckligen väljer det (opt-in) i Inställningar**; i Android-versionen skickas innehållsfria användningshändelser **som standard** (i båda fallen skickas inget av det du sagt). iOS-versionen använder också **Crashlytics** vid opt-in, men **Android-versionen inkluderar inte Crashlytics**. Se Artikel 14 för detaljer).

Appens server är minimal och fungerar endast som en mellanhand för AI-organisering, och sparar inget innehåll (statslös). Autentiseringstjänster som kräver personliga konton används inte.

## Artikel 7 (Utlämnande till tredje part)

Appens utvecklare har ingen möjlighet att komma åt det du har sagt, dina transkriptioner eller dina organiseringsresultat, och lämnar inte ut dessa till tredje part.

För att leverera annonser till användare som inte prenumererar på KUU+ skickas information som krävs av Google AdMob för annonsleverans till Google, inklusive enhetsidentifierare, annons-ID, enhetens språk och region, ungefärlig platsinformation och information om annonsinteraktioner (se Artikel 13; Googles AdMob-integritetspolicy gäller). När KUU+ är aktivt sker inte denna informationsöverföring.

När du prenumererar på KUU+ i **Android-versionen** skickas köpinformation (produkt-ID, pris, köpdatum etc.) till RevenueCat, Inc. för att hantera köpet och din behörighet (aktiv/inaktiv status). Inget av det du sagt skickas. För detaljer om RevenueCats datahantering, se [RevenueCats integritetspolicy](https://www.revenuecat.com/privacy).

Information lämnas endast ut om det krävs enligt lag, i enlighet med föreskrivna förfaranden.

## Artikel 8 (Radering av data)

Du kan när som helst radera all data från ”Inställningar → Röst och data → Radera det som sparats” inuti appen. Detta raderar permanent all data på enheten (och, i iOS-versionen, även data i den privata databasen på iCloud). Raderad data kan inte återställas.

Om du avinstallerar appen raderas data på enheten. I iOS-versionen kan data på iCloud tas bort via Inställningar → Apple-ID → iCloud → Hantera lagring. Android-versionen lagrar endast data på enheten, så den raderas vid avinstallation.

## Artikel 9 (Säkerhetsåtgärder)

-   **iOS-versionen**: Tillfälliga ljudfiler under inspelning krypteras med iOS filskydd (`FileProtectionType.complete`) och är oåtkomliga när enheten är låst. Kommunikation med iCloud krypteras av Apple via SSL/TLS.
-   **Android-versionen**: Inspelat ljud skrivs aldrig till disken, inte ens som en temporär fil; det bearbetas endast i minnet och raderas omedelbart efter igenkänning. Sparade transkriptioner och organiseringsresultat lagras i appens privata utrymme, oåtkomligt för andra appar, och exkluderas från Androids automatiska molnsäkerhetskopiering.
-   All kommunikation med den externa AI:n är krypterad (HTTPS/TLS). Utvecklarens server fungerar endast som mellanhand för organiseringsanrop och sparar inget innehåll (statslös).

## Artikel 10 (Användning av minderåriga)

Appen har åldersgränsen 4+, men med tanke på dess syfte (att organisera tankar) förutsätts användning av personer som kan läsa och skriva. Minderåriga bör använda appen med en vårdnadshavares samtycke.

## Artikel 11 (Ändringar i denna policy)

Denna policy kan komma att uppdateras på grund av lagändringar, nya funktioner eller ändringar i specifikationer för respektive plattforms (Apple / Google) ramverk eller policyer. Vid väsentliga ändringar kommer detta att meddelas i samband med en appuppdatering eller på den publika sidan för denna policy.

## Artikel 12 (Kontakt)

För frågor gällande denna policy, vänligen kontakta oss via avsnittet ”Utvecklare” på appens sida i App Store eller Google Play, eller via ”Inställningar → Kontakt” inuti appen.

## Artikel 13 (Om annonser och App Tracking Transparency)

När du inte prenumererar på KUU+ visar appen en plats för en inbyggd annons från Google AdMob mellan avsnitten på skärmen ”Det du sagt”. Annonsen visas diskret för att passa KUU:s visuella stil.

-   **Det du har sagt används aldrig för annonsering.** Annonserna tar inte hänsyn till dina transkriptioner, organiseringsresultat eller teman.
-   För annonsleverans kan Google AdMob samla in enhetsidentifierare (inklusive IDFA), annons-ID, ungefärlig platsinformation (Coarse Location), diagnostik och produktinteraktioner (interaktioner med annonser i appen).
-   **iOS-versionen**: En **App Tracking Transparency** (ATT)-förfrågan visas en gång, precis före den första annonsen. Annonser visas även om du nekar, men informationen som skickas till Google begränsas (icke-personanpassad). Du kan när som helst ändra ATT-tillståndet i iOS under ”Inställningar” → ”Integritet och säkerhet” → ”Spårning”.
-   **Android-versionen**: ATT är ett system exklusivt för iOS och finns inte på Android. Istället används Googles **annons-ID (Advertising ID)** för annonsleverans. Du kan välja bort personanpassade annonser eller återställa ditt annons-ID från enhetens ”Inställningar → Integritet → Annonser” (formuleringen kan variera beroende på enhet och Android-version). Android-versionen följer också den samtyckeshantering (UMP) som visas i tillämpliga regioner som EU.
-   **En prenumeration på KUU+ stoppar all annonsering och relaterad dataöverföring.**
-   För detaljer om AdMobs datahantering, se [Google AdMobs integritetspolicy](https://support.google.com/admob/answer/6128543).

## Artikel 14 (Om användning av Firebase Analytics / Crashlytics)

**Opt-in-modellen i denna artikel gäller för iOS-versionen. För Android-versionen, se ”Om Android-versionen” i slutet av denna artikel.**

**iOS-versionen** kan, för att förbättra appens kvalitet och snabbt upptäcka driftproblem, använda Googles Firebase Analytics (aggregerad användningsstatistik) och Firebase Crashlytics (kraschrapporter). **Denna funktion är som standard AV (ingen data skickas) och aktiveras endast om du uttryckligen väljer det (opt-in) via ”Inställningar → Data och diagnostik”.**

-   **Information som skickas**:
    -   Ett anonymiserat installations-ID som utfärdas automatiskt av Firebase (baserat på IDFV; inte en direkt personlig identifierare).
    -   Aggregerade signaler om händelser i appen (t.ex. slutförda inspelningssessioner, visning/konvertering av betalvägg, slutförd introduktion. Numeriska värden skickas med grov granularitet).
    -   Symboliserade stackspårningar vid onormal avslutning av appen (krasch).
-   **Information som inte skickas**: Det du har sagt (ljud), transkriptionsresultat, text från AI-organisering och teman du har angett är **omöjligt att skicka på grund av appens tekniska design** (implementeringen har ett API som förhindrar att strängvärden skickas till analys-SDK:et).
-   **När opt-in inte är aktivt sker ingen som helst kommunikation med Firebase** (inklusive all ovan nämnd information).
-   **Hur man slutar skicka data**: Du kan när som helst stänga av detta via reglaget i ”Inställningar → Data och diagnostik”. När det stängs av raderas tidigare installations-ID, och eventuella osända kraschloggar som lagrats lokalt på enheten tas också bort.
-   Mottagaren är Google LLC (USA). Googles [Integritetsinformation för Firebase](https://firebase.google.com/support/privacy) gäller.

**Om Android-versionen:** Android-versionen använder Firebase Analytics för att skicka **innehållsfria användningshändelser** för produktförbättring (aggregerade värden som skärmövergångar och antal gånger en funktion används) samt ett anonymt App Instance ID som utfärdas av Firebase. **Till skillnad från iOS-versionen är detta aktiverat som standard.** Det du har sagt (ljud), transkriptioner, organiseringsresultat och teman **kan inte skickas** – analys-SDK:ets API är utformat så att strängvärden inte kan skickas till det. **Android-versionen inkluderar inte Crashlytics och skickar inga kraschrapporter.** Mottagaren är Google LLC (USA); Googles [Integritetsinformation för Firebase](https://firebase.google.com/support/privacy) gäller.
