> Tämä on viitteellinen käännös. Virallinen ja sitova teksti on japaninkielinen versio.

# KUU:n tietosuojakäytäntö

Päivitetty viimeksi: 21. heinäkuuta 2026

**Lyhyesti:** Se, mitä puhut, on sinun. **Itse puhetta ei lähetetä ulkopuolelle.** Puheentunnistus tapahtuu laitteesi sisällä. Järjestelyyn (tekoälyluokitteluun) käytetään ulkoista tekoälyä, mutta sinne lähetetään ainoastaan tekstimuotoinen sisältö. Sitä käytetään vain järjestelyyn, eikä sitä tallenneta (iOS-versiossa voit vaihtaa asetuksista laitteen sisäiseen järjestelyyn. **Android-versiossa käytetään ainoastaan ulkoista tekoälyä, eikä laitteen sisäistä järjestelyä ole saatavilla**). Tiedot tallennetaan laitteeseesi ja iOS-versiossa myös iCloudiin (yksityiseen tietokantaan). Android-versiossa tiedot tallennetaan vain laitteen sisälle. Kehittäjä ei tallenna sisältöäsi eikä näe vastaanotettuja tietoja. Voit poistaa kaikki tiedot milloin tahansa sovelluksen sisältä. Sovellus tekee ainoastaan **välttämättömät verkkopyynnöt** laskutusta (iOS=StoreKit／Android=RevenueCat) ja Google AdMob -mainoksia varten, eivätkä nämä tiedot sisällä puheesi sisältöä (mainokset poistuvat KUU+-tilauksella). Laadun parantamiseksi keräämme käyttötietoja, mutta nekään eivät sisällä puheesi sisältöä (iOS:ssä käyttäjän suostumuksella, Androidissa sisältöneutraali mittaus oletuksena. Lisätietoja artiklassa 14).

---

## Artikla 1 (Yleiset periaatteet)

Tämä sovellus, ”KUU” (jäljempänä ”sovellus”), on suunniteltu auttamaan sinua purkamaan ja järjestämään ajatuksiasi puhumalla ne ääneen. Sovelluksesta on saatavilla **iOS- ja Android-versiot**, ja tämä käytäntö koskee molempia. Sovellus käsittelee tietoja ainoastaan toimintojen tarjoamiseksi välttämättömässä laajuudessa ja asettaa käyttäjän yksityisyyden suojan etusijalle.

## Artikla 2 (Kerättävät ja tallennettavat tiedot)

Sovellus käsittelee ainoastaan seuraavia tietoja:

1.  **Käyttäjän puhuma sisältö (äänidata)** — Nauhoitettu ääni tallennetaan väliaikaisesti laitteen sisäiseen muistiin ainoastaan puheentunnistuksen ajaksi ja poistetaan välittömästi käsittelyn jälkeen. Äänidataa ei lähetetä palvelimille.
2.  **Puheentunnistuksen ja järjestelyn tulokset (teksti)** — Tallennetaan, jotta voit itse tarkastella niitä myöhemmin (iOS-versiossa laitteeseen ja iCloudin yksityiseen tietokantaan, Android-versiossa ainoastaan laitteen sisälle. Lisätietoja artiklassa 4).
3.  **Sovelluksen asetukset** — Teema, tekstikoko, pään vesitason tila ja muut sovelluksen toiminnan kannalta tarpeelliset asetusarvot.

Sovellus ei kerää henkilötietoja, kuten nimeä, sähköpostiosoitetta, puhelinnumeroa, sijaintitietoja, yhteystietoja, kalenteritietoja, valokuvia tai laitetunnisteita.

## Artikla 3 (Tietoa puheentunnistuksesta ja tekoälyluokittelusta)

**Puheentunnistus (tekstiksi muuntaminen)** tapahtuu kokonaisuudessaan käyttämässäsi iOS-laitteessa.

-   Puheentunnistus: Käytämme Applen Speech-kehystä (laitteen sisäinen). Itse puhetta ei koskaan lähetetä laitteen ulkopuolelle.

**Tekoälyluokittelu (kategorisointi)** käyttää ulkoista tekoälyä.

-   Ainoastaan **tekstimuotoinen sisältö (puheentunnistuksen tulos)** lähetetään. Ääntä ei lähetetä.
-   Tiedot lähetetään ulkoiselle tekoälylle kehittäjän palvelimen kautta (taustajärjestelmän kautta Googlen Geminille).
-   Lähetettyä sisältöä käytetään **ainoastaan luokitteluun, eikä sitä tallenneta**. Sitä ei myöskään käytetä tekoälyn opettamiseen.
-   **iOS-versiossa** voit milloin tahansa vaihtaa **laitteen sisäiseen luokitteluun** (Applen FoundationModels / laitteen sisäiset säännöt) asetusten ”Laitteen sisäinen” -valinnalla. Tällöin myöskään tekstiä ei lähetetä laitteen ulkopuolelle.

**Tietoa Android-versiosta:** Android-versio ei tarjoa laitteen sisällä tapahtuvaa järjestelyä (luokittelua). Kun järjestät ajatuksia, tekstiksi muunnettu sisältö lähetetään **aina** ulkoiselle tekoälylle (Googlen Geminille taustajärjestelmämme kautta). iOS-version kaltaista ”Laitteen sisäinen” -valintaa ei ole. Ainoastaan tekstimuotoinen sisältö lähetetään – itse puhetta ei lähetetä, ja lähetettyä tekstiä käytetään vain luokitteluun, eikä sitä tallenneta tai käytetä tekoälyn opettamiseen. Itse puheentunnistus tapahtuu laitteen sisällä.

## Artikla 4 (Tallennus ja synkronointi)

**iOS-versio:** Puheentunnistuksen ja järjestelyn tulokset tallennetaan ainoastaan sinun **iCloudin yksityiseen tietokantaasi** (CloudKit Private Database). Tämä on Applen tarjoama tallennustila, johon vain sinulla on pääsy. Tämän sovelluksen kehittäjä ei voi tarkastella eikä hakea tallennettua sisältöä. iCloudin käyttöön sovelletaan Applen tietosuojakäytäntöä.

**Android-versio:** Puheentunnistuksen ja järjestelyn tulokset tallennetaan **ainoastaan tähän laitteeseen**. Automaattista pilvisynkronointia ei ole. Laitetta vaihtaessasi voit viedä tiedot tiedostoon sovelluksen ”Ääni ja data” -osiosta ja tuoda ne uuteen laitteeseen. Valitset itse vientikohteen (laitteen sisäinen muisti, käyttämäsi pilvitallennussovellus jne.). Kehittäjällä ei ole pääsyä tähän tiedostoon.

## Artikla 5 (Käyttötarkoitus)

Käsiteltäviä tietoja käytetään ainoastaan seuraaviin tarkoituksiin:

1.  Puheentunnistustulosten luomiseen äänestä ja niiden näyttämiseen käyttäjälle
2.  Puheentunnistustulosten luokitteluun kategorioihin ”Käsiteltävät”, ”Myöhemmin”, ”Haudottavat” ja ”Hylättävät” ja niiden näyttämiseen käyttäjälle
3.  Käyttäjän aiempien puheiden tallentamiseen ja näyttämiseen käyttäjän itsensä tarkasteltavaksi
4.  Sovelluksen toiminnan kannalta välttämättömien asetusten ylläpitämiseen

## Artikla 6 (Ulkopuolisten palveluiden käyttö)

Sovellus käyttää toimintojensa tarjoamiseen seuraavia ulkopuolisia palveluita. **Itse puhetta ei lähetetä mihinkään näistä palveluista.**

-   **iCloud / CloudKit** (vain iOS-versio. Applen tarjoama. Tallennus ja synkronointi ainoastaan omaan yksityiseen tietokantaasi)
-   **Puheentunnistus** (iOS-versiossa Applen Speech-kehys, Android-versiossa laitteen sisäinen puheentunnistusmoottori. Molemmat suoritetaan laitteessa, eikä ääntä lähetetä laitteen ulkopuolelle)
-   **Ulkoinen tekoäly (pilvipalvelu)** (Tekoälyluokittelu. Vain tekstimuotoinen sisältö lähetetään. Käytetään ainoastaan luokitteluun, ei tallenneta eikä käytetä tekoälyn opettamiseen. iOS-versiossa tämän voi kytkeä pois päältä asetuksella ”Laitteen sisäinen”, mutta **Android-versiossa käytetään ainoastaan ulkoista tekoälyä**. Lisätietoja artiklassa 3)
-   **FoundationModels** (vain iOS-versio. Applen tarjoama. Toimii täysin laitteen sisällä. Käytetään, kun ”Laitteen sisäinen” -asetus on päällä tai vararatkaisuna, jos ulkoinen tekoäly ei ole käytettävissä)
-   **Laskutuspalvelut** (iOS-versiossa **Apple StoreKit**, Android-versiossa **RevenueCat**. KUU+-tilauksen ostaminen, uusiminen, peruuttaminen ja käyttöoikeuksien hallinta. Puheen sisältöä ei lähetetä. Lisätietoja RevenueCatista artiklassa 7 ja [RevenueCatin tietosuojakäytännössä](https://www.revenuecat.com/privacy))
-   **Play Integrity API (Firebase App Checkin kautta, vain Android-versio)** (Laitteen ja sovelluksen eheyden varmentaminen sen varmistamiseksi, että luokittelu-API:lle tehdyt pyynnöt tulevat laillisesta sovelluksesta. Ei sisällä puheen sisältöä tai käyttäjää yksilöiviä tietoja)
-   **Google AdMob (Google Mobile Ads SDK)** (Vain kun KUU+-tilaus ei ole aktiivinen. Näyttää yhden natiivimainoksen osioiden välissä ”Puhutut asiat” -näkymässä. Puheen sisältöä ei lähetetä. Lisätietoja artiklassa 13)
-   **Firebase Analytics** (Googlen tarjoama. Sovelluksen laadun parantamiseen. iOS-versiossa **vain, jos käyttäjä antaa siihen nimenomaisen suostumuksensa asetuksissa**, Android-versiossa sisältöneutraaleja käyttötapahtumia lähetetään **oletusarvoisesti** (kummassakaan tapauksessa puheen sisältöä ei lähetetä). iOS-versio käyttää suostumuksella myös **Crashlytics**-palvelua, mutta **Android-versio ei sisällä Crashlyticsiä**. Lisätietoja artiklassa 14)

Sovelluksen palvelin on minimalistinen ja toimii ainoastaan tekoälyluokittelun välittäjänä, eikä se tallenna mitään sisältöä (tilaton). Emme käytä henkilökohtaista tiliä vaativia todennuspalveluita.

## Artikla 7 (Tietojen luovuttaminen kolmansille osapuolille)

Sovelluksen kehittäjällä ei ole keinoja päästä käsiksi käyttäjän puhumaan sisältöön, puheentunnistuksen tuloksiin tai järjestelyn tuloksiin, eikä hän luovuta niitä kolmansille osapuolille.

Mainosten näyttämiseksi käyttäjille, jotka eivät ole tilanneet KUU+:aa, Google AdMobille lähetetään sen mainonnan tarjoamiseen tarvitsemia tietoja, kuten laitetunnisteita, mainostunnisteita, laitteen kieltä ja aluetta, karkeita sijaintitietoja ja mainosvuorovaikutustietoja (lisätietoja artiklassa 13, sovelletaan Googlen AdMobin tietosuojakäytäntöä). Kun KUU+-tilaus on aktiivinen, näitä tietoja ei lähetetä.

Kun tilaat KUU+:n **Android-versiossa**, ostotiedot (tuotetunnus, hinta, ostopäivämäärä jne.) lähetetään RevenueCat, Inc. -yhtiölle oston käsittelyä ja käyttöoikeuden (voimassa/ei voimassa) hallintaa varten. Puheen sisältöä ei lähetetä. Lisätietoja RevenueCatin tietojenkäsittelystä löydät [RevenueCatin tietosuojakäytännöstä](https://www.revenuecat.com/privacy).

Tietoja luovutetaan ainoastaan lain niin vaatiessa ja säädettyjä menettelytapoja noudattaen.

## Artikla 8 (Tietojen poistaminen)

Käyttäjä voi poistaa kaikki tiedot milloin tahansa sovelluksen sisältä kohdasta ”Asetukset → Ääni ja data → Poista tallennetut asiat”. Poistaminen hävittää pysyvästi laitteella olevat tiedot (ja iOS-versiossa myös iCloudin yksityisessä tietokannassa olevat tiedot). Poistettuja tietoja ei voi palauttaa.

Sovelluksen asennuksen poistaminen poistaa laitteella olevat tiedot. iOS-versiossa iCloudissa olevat tiedot voi poistaa Applen asetuksista (Asetukset → Apple ID → iCloud → Hallitse tallennustilaa). Android-versio tallentaa tiedot vain laitteen sisälle, joten ne poistuvat asennuksen poiston yhteydessä.

## Artikla 9 (Turvatoimet)

-   **iOS-versio**: Nauhoituksen aikaiset väliaikaiset äänitiedostot salataan iOS:n tiedostosuojaustoiminnolla (`FileProtectionType.complete`), eikä niihin pääse käsiksi laitteen ollessa lukittuna. Yhteys iCloudiin on Applen SSL/TLS-salaama.
-   **Android-versio**: Nauhoitettua ääntä ei kirjoiteta levylle edes väliaikaisesti; se käsitellään ainoastaan muistissa ja hävitetään välittömästi tunnistuksen jälkeen. Tallennetut puheentunnistus- ja järjestelytulokset säilytetään sovelluksen yksityisellä tallennusalueella, johon muilla sovelluksilla ei ole pääsyä. Ne on myös suljettu Androidin automaattisen pilvivarmuuskopioinnin ulkopuolelle.
-   Kaikki tiedonsiirto ulkoiselle tekoälylle on salattua (HTTPS/TLS). Kehittäjän palvelin ainoastaan välittää järjestelypyyntöjä eikä tallenna mitään sisältöä (tilaton).

## Artikla 10 (Alaikäisten käyttö)

Sovelluksen ikäraja on 4+, mutta sen luonteen (ajatusten järjestely) vuoksi sen oletetaan olevan tarkoitettu luku- ja kirjoitustaitoisille käyttäjille. Alaikäisten tulee käyttää sovellusta huoltajan suostumuksella.

## Artikla 11 (Muutokset tähän tietosuojakäytäntöön)

Tätä käytäntöä voidaan päivittää lakimuutosten, uusien ominaisuuksien tai alustojen (Apple / Google) kehysten tai käytäntöjen muutosten vuoksi. Merkittävistä muutoksista ilmoitetaan sovelluspäivityksen yhteydessä tai tämän käytännön julkisella sivulla.

## Artikla 12 (Yhteydenotot)

Tähän käytäntöön liittyvissä kysymyksissä voit ottaa yhteyttä App Storen tai Google Playn sovellussivun ”Kehittäjä”-osion kautta tai sovelluksen sisältä kohdasta ”Asetukset → Ota yhteyttä”.

## Artikla 13 (Tietoa mainoksista ja App Tracking Transparency -kehyksestä)

Kun et ole tilannut KUU+:aa, sovellus näyttää yhden Google AdMobin tarjoaman natiivimainoksen ”Puhutut asiat” -näkymän osioiden välissä. Mainokset on muotoiltu hienovaraisesti KUU:n visuaalisen ilmeen säilyttämiseksi.

-   **Puhumaasi sisältöä ei koskaan käytetä mainontaan.** Mainokset eivät hyödynnä puheentunnistustuloksiasi, järjestelytuloksiasi tai teemojasi.
-   Mainonnan tarjoamiseksi Google AdMob saattaa kerätä laitetunnisteita (mukaan lukien IDFA), mainostunnisteen, karkean sijainnin, diagnostiikkatietoja ja tuoteinteraktiotietoja (mainoksiin liittyvä vuorovaikutus sovelluksessa).
-   **iOS-versio**: **App Tracking Transparency** (ATT) -suostumuspyyntö näytetään kerran, juuri ennen ensimmäistä mainosta. Mainoksia näytetään, vaikka kieltäytyisit, mutta Googlelle lähetettävät tiedot ovat rajallisia (ei-personoituja). Voit muuttaa ATT-lupaa milloin tahansa iOS:n asetuksista: ”Asetukset → Tietosuoja ja suojaus → Seuranta”.
-   **Android-versio**: ATT on vain iOS-ominaisuus, eikä sitä ole Androidissa. Sen sijaan mainonnan tarjoamiseen käytetään Googlen **mainostunnistetta (Advertising ID)**. Voit kieltäytyä mainosten personoinnista tai nollata mainostunnisteesi laitteen asetuksista: ”Asetukset → Tietosuoja → Mainokset” (sanat voivat vaihdella laitteen ja Android-version mukaan). Lisäksi Android-versio noudattaa sovellettavilla alueilla, kuten EU:ssa, näytettävää suostumustenhallintaa (UMP).
-   **KUU+-tilaus lopettaa kaikki mainokset ja niihin liittyvän tiedonsiirron.**
-   Lisätietoja AdMobin tietojenkäsittelystä löydät [Google AdMobin tietosuojakäytännöstä](https://support.google.com/admob/answer/6128543).

## Artikla 14 (Tietoa Firebase Analyticsin ja Crashlyticsin käytöstä)

**Tämän artiklan suostumukseen perustuva malli koskee iOS-versiota. Android-version osalta katso tämän artiklan lopussa oleva kohta ”Tietoa Android-versiosta”.**

**iOS-versio** saattaa käyttää sovelluksen laadun parantamiseen ja tuotantovirheiden nopeaan havaitsemiseen Googlen Firebase Analyticsia (koostetut käyttötiedot) ja Firebase Crashlyticsia (kaatumisraportit). **Tämä toiminto on oletusarvoisesti POIS PÄÄLTÄ (tietoja ei lähetetä) ja aktivoituu vain, jos käyttäjä antaa siihen nimenomaisen suostumuksensa kohdassa ”Asetukset → Data ja diagnostiikka”.**

-   **Lähetettävät tiedot**:
    -   Firebasen automaattisesti luoma anonymisoitu asennustunniste (perustuu IDFV:hen; ei suoraan henkilöön yhdistettävä tunniste).
    -   Koostetut signaalit sovelluksen sisäisistä tapahtumista (esim. nauhoitussession onnistuminen, maksumuurin näyttäminen/konversio, perehdytyksen suorittaminen. Numeeriset arvot lähetetään karkealla, ryhmitellyllä tarkkuudella).
    -   Symboloitu kaatumisraportti (stack trace), kun sovellus sulkeutuu odottamatta.
-   **Ei-lähetettävät tiedot**: Puhumasi sisältö (ääni), puheentunnistuksen tulokset, tekoälyn luokittelutulokset ja asettamasi teemojen nimet on **suunniteltu niin, ettei niitä voi teknisesti lähettää** (toteutuksen rajapinta estää merkkijonoarvojen välittämisen analytiikka-SDK:lle).
-   **Kun suostumusta ei ole annettu, mitään yhteydenpitoa Firebaseen ei tapahdu.**
-   **Lähettämisen lopettaminen**: Voit kytkeä asetuksen pois päältä milloin tahansa kohdassa ”Asetukset → Data ja diagnostiikka”. Kun asetus kytketään pois, aiempi asennustunniste hylätään ja laitteelle tallennetut lähettämättömät kaatumisraportit poistetaan.
-   Tietojen vastaanottaja on Google LLC (Yhdysvallat). Sovelletaan Googlen [Firebase Privacy Information](https://firebase.google.com/support/privacy) -tietoja.

**Tietoa Android-versiosta:** Android-versio käyttää Firebase Analyticsia ja lähettää tuotekehitystä varten **sisältöneutraaleja käyttötapahtumia** (ryhmiteltyjä arvoja, kuten näkymien välillä siirtymisiä ja toimintojen käyttökertoja) sekä Firebasen luoman anonyymin sovellusesiintymän tunnisteen (App Instance ID). **Toisin kuin iOS-versiossa, tämä on oletusarvoisesti käytössä.** Puhumaasi sisältöä (ääntä), puheentunnistuksen tuloksia, järjestelytuloksia tai teemojen nimiä **ei voida lähettää**, sillä analytiikka-SDK:n rajapinta on suunniteltu niin, ettei sille voi välittää merkkijonoarvoja. **Android-versio ei sisällä Crashlyticsiä, eikä se lähetä kaatumisraportteja.** Tietojen vastaanottaja on Google LLC (Yhdysvallat), ja sovelletaan Googlen [Firebase Privacy Information](https://firebase.google.com/support/privacy) -tietoja.
