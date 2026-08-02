> Detta är en översättning som tillhandahålls som referens. Den japanska versionen är den juridiskt gällande texten.

# KUU Integritetspolicy

Senast uppdaterad: 2 augusti 2026

**Kort sagt:** Det du säger är ditt. **Appen skickar aldrig själva ljudinspelningen någonstans**. På iPhone- och Android-enheter sker även transkriberingen på själva enheten. **Apple Watch-versionen av appen spelar inte in ljud överhuvudtaget** – den tar endast emot text som skapats via klockans standardinmatning (diktering, handskrift eller tangentbord). När du väljer diktering hanteras röstigenkänningen av Apples system (se Artikel 3). För att organisera (AI-kategorisera) används en extern AI, men det är endast den transkriberade texten som skickas. Texten används enbart för organisering och sparas inte. Det som sparas lagras på din enhet och, för iOS-versionen, i din privata iCloud-databas (Android-versionen lagrar endast på enheten). Utvecklaren lagrar inte ditt innehåll och kan inte se vad som tas emot. Du kan när som helst radera all data inifrån appen. Appen gör endast **minimala nätverksanrop** för fakturering (iOS=StoreKit／Android=RevenueCat) och annonser från Google AdMob, och den informationen inkluderar aldrig det du har sagt (annonserna tas bort med KUU+). För kvalitetsförbättring mäts användningen, men inte heller detta inkluderar det du har sagt (iOS kräver aktivt samtycke från användaren, Android genomför en innehållsfri mätning som standard. Se Artikel 14 för detaljer).

---

## Artikel 1 (Grundpolicy)

Denna app, ”KUU” (hädanefter ”appen”), är utformad för att hjälpa dig att få ut tankar ur huvudet genom att säga dem högt och sedan organisera dem. Den finns för **iOS (iPhone och Apple Watch) och Android**, och denna policy gäller för samtliga versioner. Appen hanterar information endast i den minsta möjliga utsträckning som krävs för att tillhandahålla sina funktioner, med högsta prioritet på att skydda användarens integritet.

## Artikel 2 (Information som samlas in och sparas)

Appen hanterar endast följande information:

1.  **Inspelat ljud (ljuddata)** — Ljudet sparas tillfälligt i enhetens lokala minne endast under transkriberingsprocessen och raderas omedelbart efteråt. Det skickas aldrig till någon server. **Apple Watch-versionen av appen genomför ingen ljudinspelning överhuvudtaget** (se Artikel 3).
2.  **Transkriberad och organiserad text** — Sparas så att du själv kan gå tillbaka och se vad du har sagt (iOS-versionen: på enheten och i din privata iCloud-databas; Android-versionen: endast på enheten. På en parkopplad Apple Watch sparas endast de senaste titlarna i varje kategori för visningsändamål. Se Artikel 4 för detaljer).
3.  **Inställningar i appen** — Tema, textstorlek, vattennivån i huvudet och andra inställningsvärden som krävs för appens funktion.

Appen samlar inte in personuppgifter som namn, e-postadress, telefonnummer, platsinformation, kontakter, kalender, foton eller enhetsidentifierare.

## Artikel 3 (Om röstigenkänning och AI-kategorisering)

**Röstigenkänning (transkribering)** sker, på iPhone (iOS-versionen) och Android-enheter, helt och hållet på din egen enhet (för Apple Watch, se slutet av denna artikel).

-   Röstigenkänning: Apples Speech-ramverk (on-device) används. Själva ljudinspelningen skickas aldrig utanför enheten.

**AI-kategorisering (sortering)** använder en extern AI.

-   Endast den **transkriberade texten** skickas. Ljudet skickas inte.
-   Texten skickas till en extern AI, via utvecklarens server (backend) till Googles Gemini.
-   Den skickade texten **används endast för kategorisering och sparas inte**. Den används inte heller för att träna AI:n.
-   Det som skickas inkluderar, utöver den transkriberade texten, även text som du har skrivit in eller redigerat manuellt. Om automatisk tematilldelning (KUU+, valfri inställning) är aktiverad, skickas även sparade titlar, brödtexter och teman för befintliga anteckningar för att tilldelningen ska kunna ske (allt används endast för kategorisering och sparas inte).
-   I **iOS-versioner** av appen före 2.3.0 kunde man välja att kategoriseringen skulle ske endast på enheten via inställningen "På enheten" (denna inställning finns inte längre kvar från och med version 2.3.0).

**Om Android-versionen:** Android-versionen erbjuder inte en organiseringsmetod (kategorisering) som sker helt och hållet på enheten. När du organiserar skickas den transkriberade texten **alltid** till en extern AI (Googles Gemini via vår backend). Endast den transkriberade texten skickas; själva ljudinspelningen skickas inte, och den skickade texten används enbart för kategorisering, sparas inte och används inte för att träna AI:n. Själva transkriberingen (röstigenkänningen) sker helt och hållet på enheten.

**Om Apple Watch-versionen:** Apple Watch-versionen av appen varken spelar in ljud eller utför röstigenkänning. För inmatning används watchOS standardfunktioner för textinmatning (användaren väljer mellan diktering, handskrift och tangentbord), och appen tar endast emot den resulterande texten. När diktering väljs utförs röstigenkänningen som en funktion i Apple (watchOS). Hur den processen hanteras (inklusive om den sker på enheten eller skickas till Apples servrar) beror på din enhetsmodell, dina inställningar och ditt språk, och **styrs av Apples integritetspolicy**. Appen har inte tillgång till denna ljuddata, tar inte emot den och lagrar den inte. Den resulterande texten hanteras på samma sätt som text du talat in på iPhone (AI-kategorisering enligt denna artikel, lagring enligt Artikel 4).

## Artikel 4 (Lagring och synkronisering)

**iOS-versionen:** Transkriberad och organiserad text sparas endast i din **privata iCloud-databas** (CloudKit Private Database). Detta är en lagringstjänst från Apple som endast du har tillgång till. Appens utvecklare kan varken se eller hämta det lagrade innehållet. Användningen av iCloud omfattas av Apples integritetspolicy.

**Android-versionen:** Transkriberad och organiserad text sparas **endast på denna enhet**. Det sker ingen automatisk synkronisering till molnet. Vid byte av enhet kan du exportera dina data till en fil via ”Röst och data” i appen och sedan importera den på den nya enheten. Du väljer själv var filen ska sparas (på enheten, i en molnlagringsapp etc.). Utvecklaren har inte tillgång till denna fil.

**Apple Watch-versionen:** För visningsändamål överförs en del av din organiserade text (de senaste titlarna i varje kategori) till din parkopplade Apple Watch via Apples kommunikationsprotokoll mellan enheter (Watch Connectivity) och **sparas även på klockan**. Text som du matar in på Apple Watch överförs till din iPhone på samma sätt. Ingen av utvecklarens servrar är inblandad i denna överföring eller lagring.

## Artikel 5 (Användningsändamål)

Hanterad information används endast för följande ändamål:

1.  Generera transkriberingar från röst och visa dem för användaren.
2.  Kategorisera transkriberingar i ”se nu / tänk senare / låt vila / släpp taget” och visa dem för användaren.
3.  Lagra och visa vad användaren tidigare har sagt, så att denne själv kan se det igen.
4.  Behålla de inställningsvärden som krävs för appens funktion.

## Artikel 6 (Användning av externa tjänster)

Appen använder följande externa tjänster för att tillhandahålla sina funktioner. **Själva ljudinspelningen skickas inte till någon av dessa tjänster.**

-   **iCloud / CloudKit** (endast iOS-versionen. Tillhandahålls av Apple. Sparar och synkroniserar endast till din egen privata databas)
-   **Röstigenkänning** (iOS-versionen använder Apples Speech-ramverk, Android-versionen använder enhetens inbyggda röstigenkänningsmotor. Båda körs på enheten och ljudet skickas inte utanför enheten. **Apple Watch-versionen utför ingen egen röstigenkänning utan använder watchOS standardinmatning**. Se Artikel 3)
-   **watchOS standardfunktioner för textinmatning** (endast Apple Watch-versionen. Tillhandahålls av Apple. Användaren väljer mellan diktering, handskrift och tangentbord. Vid diktering utförs röstigenkänningen som en funktion från Apple och omfattas av Apples integritetspolicy. Appen har inte tillgång till ljudet. Se Artikel 3 för detaljer)
-   **Watch Connectivity** (endast Apple Watch-versionen. Tillhandahålls av Apple. Skickar text för visningsändamål direkt mellan iPhone och Apple Watch. Utvecklarens server är inte inblandad. Se Artikel 4 för detaljer)
-   **Extern AI (molnbaserad)** (AI-kategorisering. Endast textinnehåll skickas. Används enbart för kategorisering, sparas inte och används inte för att träna AI:n. Se Artikel 3 för detaljer)
-   **Faktureringstjänster** (iOS-versionen: **Apple StoreKit**, Android-versionen: **RevenueCat**. Hantering av köp, förnyelse, uppsägning och status för KUU+-prenumerationer. Inget av det du sagt skickas. För RevenueCat, se Artikel 7 och [RevenueCats integritetspolicy](https://www.revenuecat.com/privacy))
-   **Play Integrity API (via Firebase App Check. Endast Android-versionen)** (Verifiering av att anrop till kategoriserings-API:et kommer från en legitim app, genom att intyga enhetens och appens integritet. Innehåller inte det du sagt eller information som kan identifiera användaren)
-   **Google AdMob (Google Mobile Ads SDK)** (Endast för användare utan KUU+. Visar en annonsplats för en inbyggd annons mellan avsnitten på skärmen ”Det du sagt”. Inget av det du sagt skickas. Se Artikel 13 för detaljer)
-   **Firebase Analytics** (Tillhandahålls av Google. För kvalitetsförbättring av appen. I iOS-versionen **endast om användaren uttryckligen väljer det** i Inställningar. I Android-versionen skickas händelser om **innehållsfri användning som standard** (i båda fallen skickas inget av det du sagt). iOS-versionen använder även **Crashlytics** om användaren väljer det, men **Android-versionen inkluderar inte Crashlytics**. Se Artikel 14 för detaljer)

Appens server är minimal och används endast som en mellanhand (stateless) för AI-kategorisering och lagrar inget innehåll. Inga autentiseringstjänster som kräver personliga konton används.

## Artikel 7 (Utlämnande till tredje part)

Appens utvecklare har ingen möjlighet att komma åt det du har sagt, dina transkriberingar eller dina organiserade resultat, och lämnar inte ut något av detta till tredje part.

I syfte att visa annonser för användare som inte prenumererar på KUU+ skickas information som Google AdMob behöver för annonsvisning till Google. Detta kan inkludera enhetsidentifierare, annons-ID, enhetens språk och region, ungefärlig platsinformation och information om interaktion med annonser (se Artikel 13, Googles integritetspolicy för AdMob gäller). När KUU+ är aktivt sker ingen sådan informationsöverföring.

När du prenumererar på KUU+ i **Android-versionen** skickas köpinformation (produkt-ID, pris, köpdatum etc.) till RevenueCat, Inc. för att hantera köpet och din behörighet (aktiv/inaktiv). Inget av det du sagt skickas. För detaljer om RevenueCats datahantering, se deras [integritetspolicy](https://www.revenuecat.com/privacy).

Information kan komma att lämnas ut om det krävs enligt lag, i enlighet med föreskrivna procedurer.

## Artikel 8 (Radering av data)

Du kan när som helst radera all data via ”Inställningar → Röst och data → Radera sparat innehåll” i appen. Detta raderar permanent all data på enheten (och för iOS-versionen, även data i din privata iCloud-databas). Raderad data kan inte återskapas.

När du avinstallerar appen raderas data som är lagrad på enheten. För iOS-versionen kan data i iCloud raderas via Inställningar → Apple-ID → iCloud → Hantera lagring. Eftersom Android-versionen endast lagrar data lokalt, raderas den vid avinstallation.

**Apple Watch-versionen:** När du raderar all data, ersätts den visningsdata som redan överförts till din Apple Watch med tomt innehåll nästa gång klockan ansluter. Om du raderar appen från din Apple Watch raderas också den visningsdata som lagrats på den.

## Artikel 9 (Säkerhetsåtgärder)

-   **iOS-versionen**: Tillfälliga ljudfiler under inspelning krypteras med iOS filskyddsfunktion (`FileProtectionType.complete`) och är oåtkomliga när enheten är låst. Kommunikation med iCloud krypteras av Apple med SSL/TLS.
-   **Android-versionen**: Inspelat ljud skrivs inte till disken, inte ens som en tillfällig fil, utan bearbetas endast i minnet och kasseras omedelbart efter igenkänning. Sparade transkriberingar och organiserade resultat lagras i appens privata utrymme, oåtkomligt för andra appar, och är undantagna från Androids automatiska säkerhetskopiering till molnet.
-   **Apple Watch-versionen**: Överföringen mellan iPhone och Apple Watch hanteras av Apples Watch Connectivity och passerar inte via utvecklarens servrar. Det som lagras på Apple Watch är begränsat till text för visning (de senaste titlarna i varje kategori); inget ljud sparas.
-   Kommunikation med extern AI krypteras alltid (HTTPS/TLS). Utvecklarens server agerar endast som en mellanhand (stateless) för kategorisering och lagrar inget innehåll.

## Artikel 10 (Användning av minderåriga)

Appen har åldersgränsen 4+, men med tanke på dess syfte (att organisera tankar) förutsätts läs- och skrivkunnighet. Minderåriga bör använda appen med målsmans tillstånd.

## Artikel 11 (Ändringar i denna policy)

Denna policy kan komma att ändras på grund av lagändringar, nya funktioner, eller ändringar i specifikationerna för respektive plattforms (Apple / Google) ramverk eller policyer. Vid väsentliga ändringar kommer detta att meddelas i samband med en appuppdatering eller på den publika sidan för denna policy.

## Artikel 12 (Kontakt)

För frågor gällande denna policy, vänligen kontakta oss via ”Utvecklare”-sektionen på appens sida i App Store eller Google Play, eller via ”Inställningar → Kontakta oss” inuti appen.

## Artikel 13 (Om annonser och App Tracking Transparency)

Under perioder då du inte prenumererar på KUU+ visar appen en enda inbyggd annonsplats från Google AdMob, placerad mellan avsnitten på skärmen ”Det du sagt”. Annonsen visas på ett diskret sätt för att bevara KUU:s känsla.

-   **Innehållet i det du säger används aldrig för annonsering**. Annonserna tar inte hänsyn till dina transkriberingar, organiserade resultat eller teman.
-   För att kunna visa annonser kan Google AdMob samla in enhetsidentifierare (inklusive IDFA), annons-ID, ungefärlig platsinformation (Coarse Location), diagnostik och produktinteraktioner (interaktioner med annonser i appen).
-   **iOS-versionen**: En förfrågan om **App Tracking Transparency** (ATT) visas en gång, precis före den första annonsen. Annonser visas även om du nekar, men informationen som skickas till Google blir då begränsad (icke-personanpassad). Du kan när som helst ändra ditt ATT-medgivande via iOS ”Inställningar” → ”Integritet och säkerhet” → ”Spårning”.
-   **Android-versionen**: ATT är en funktion specifik för iOS och finns inte på Android. Istället används Googles **annons-ID (Advertising ID)** för annonsvisning. Du kan välja bort personanpassade annonser eller återställa ditt annons-ID via enhetens ”Inställningar → Integritet → Annonser” (ordalydelsen kan variera beroende på enhet och Android-version). Android-versionen följer även den hantering av samtycke (UMP) som visas i tillämpliga regioner som EU.
-   **Om du prenumererar på KUU+ upphör all annonsering och relaterad informationsöverföring.**
-   För detaljer om Google AdMobs datahantering, se [Google AdMobs integritetspolicy](https://support.google.com/admob/answer/6128543).

## Artikel 14 (Om användning av Firebase Analytics / Crashlytics)

**Modellen med aktivt samtycke (opt-in) i denna artikel gäller för iOS-versionen. För Android-versionen, se avsnittet ”Om Android-versionen” i slutet av denna artikel.**

**iOS-versionen** kan, för att förbättra appens kvalitet och snabbt upptäcka driftsproblem, använda Googles Firebase Analytics (för insamling av användningsstatistik) och Firebase Crashlytics (för kraschrapporter). **Denna funktion är inaktiverad (skickar ingen data) som standard och aktiveras endast om du uttryckligen väljer det via ”Inställningar → Data och diagnostik”.**

-   **Information som skickas**:
    -   Anonymiserat installations-ID som utfärdas automatiskt av Firebase (baserat på IDFV; en identifierare som inte direkt kan kopplas till en person).
    -   Aggregerade signaler om händelser i appen (sammanställda händelser som slutförda inspelningssessioner, visningar/konverteringar av betalvägg, slutförd onboarding. Numeriska värden skickas med grov granularitet).
    -   Kraschrapporter (symbolicated stack trace) när appen avslutas oväntat.
-   **Information som inte skickas**: Innehållet i det du säger (ljud), transkriberingar, AI-kategoriserade texter och de teman du skapar är **utformade på kodnivå för att inte kunna skickas** (implementeringen använder ett API som förhindrar att textvärden skickas till analys-SDK:et).
-   **Så länge funktionen inte är aktiverad sker ingen som helst kommunikation med Firebase** (inklusive all ovan nämnd information).
-   **Hur du slutar skicka**: Du kan när som helst stänga av funktionen via ”Inställningar → Data och diagnostik”. När den stängs av raderas tidigare installations-ID och eventuella osända kraschloggar som lagrats lokalt på enheten tas bort.
-   Mottagaren är Google LLC (USA). Googles [information om integritet i Firebase](https://firebase.google.com/support/privacy) gäller.

**Om Android-versionen:** Android-versionen använder Firebase Analytics och skickar **händelser om innehållsfri användning** för produktförbättring (aggregerade värden såsom skärmövergångar och antal gånger en funktion används) samt ett anonymt appinstans-ID som utfärdas av Firebase. **Till skillnad från iOS-versionen är detta aktiverat som standard.** Innehållet i det du säger (ljud), transkriberingar, organiserade texter och teman **kan inte skickas**, då analys-SDK:ets API är utformat för att inte kunna ta emot textvärden. **Android-versionen inkluderar inte Crashlytics och skickar inga kraschrapporter.** Mottagaren är Google LLC (USA); Googles [information om integritet i Firebase](https://firebase.google.com/support/privacy) gäller.
