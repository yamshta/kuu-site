> Questa è una traduzione di riferimento fornita per comodità. Il testo autorevole è la versione giapponese.

# Informativa sulla privacy di KUU

Ultimo aggiornamento: 2 agosto 2026

**In breve:** Ciò che dici è solo tuo. **L'App non invia mai la tua voce all'esterno**. Sui dispositivi iPhone e Android, anche la trascrizione avviene sul dispositivo. **La versione dell'App per Apple Watch non effettua alcuna registrazione**: riceve solo il testo prodotto tramite i metodi di input standard di watchOS (dettatura, scrittura a mano o tastiera) e quando scegli la dettatura, il riconoscimento vocale è gestito dal sistema di Apple (v. Articolo 3). Per l'organizzazione (classificazione AI) viene utilizzata un'IA esterna, ma viene inviato solo il testo trascritto. Tale testo è utilizzato unicamente per l'organizzazione e non viene conservato. I dati sono salvati solo sul tuo dispositivo e, su iOS, anche nel tuo database privato di iCloud (la versione Android salva i dati solo sul dispositivo). Lo sviluppatore non archivia i tuoi contenuti e non può visualizzarli. Puoi eliminare tutti i dati dall'interno dell'app in qualsiasi momento. L'app effettua solo le **comunicazioni di rete strettamente necessarie** per la fatturazione (StoreKit su iOS / RevenueCat su Android) e per gli annunci di Google AdMob; tali comunicazioni non includono mai ciò che hai detto (gli annunci vengono disattivati con l'iscrizione a KUU+). Viene effettuata una misurazione dell'utilizzo per migliorare la qualità, ma anche questa non include mai ciò che hai detto (su iOS è richiesta l'adesione esplicita dell'utente; su Android la misurazione, priva di contenuti, è attiva per impostazione predefinita — v. Articolo 14).

---

## Articolo 1 (Principi fondamentali)

KUU (di seguito "l'App") è un'applicazione che ti aiuta a esternare e organizzare i pensieri che hai in testa, esprimendoli a voce alta. È disponibile per **iOS (iPhone e Apple Watch) e Android** e la presente informativa si applica a tutte le versioni. L'App tratta le informazioni solo nella misura minima necessaria a fornire le proprie funzionalità, dando la massima priorità alla protezione della privacy dell'utente.

## Articolo 2 (Informazioni raccolte e conservate)

L'App tratta esclusivamente le seguenti informazioni:

1.  **Il contenuto di ciò che dici (dati audio)** — L'audio registrato viene salvato in un'area temporanea sul dispositivo solo durante il processo di trascrizione e viene eliminato subito dopo il suo completamento. Non viene inviato ad alcun server. **La versione dell'App per Apple Watch non effettua alcuna registrazione** (v. Articolo 3).
2.  **Trascrizioni e risultati dell'organizzazione (testo)** — Vengono salvati per consentirti di riesaminarli (su iOS: sul dispositivo e nel tuo database privato di iCloud; su Android: solo sul dispositivo. Su un Apple Watch abbinato, vengono salvati solo i titoli recenti di ciascuna categoria, a scopo di visualizzazione — v. Articolo 4).
3.  **Impostazioni dell'app** — Tema, dimensione del testo, stato del "livello dell'acqua" nella testa e altri valori necessari al funzionamento dell'App.

L'App non raccoglie dati personali quali nome, indirizzo e-mail, numero di telefono, posizione, contatti, calendario, foto o identificativi del dispositivo.

## Articolo 3 (Riconoscimento vocale e classificazione AI)

Il **riconoscimento vocale (trascrizione)**, su iPhone (versione iOS) e su dispositivi Android, viene eseguito interamente sul tuo dispositivo (per la versione Apple Watch, v. la fine di questo articolo).

-   Riconoscimento vocale: utilizza il framework Speech di Apple (on-device). La tua voce non viene mai inviata all'esterno del dispositivo.

La **classificazione AI (categorizzazione)** utilizza un'intelligenza artificiale esterna:

-   Viene inviato solo il **testo trascritto**. La tua voce non viene mai inviata.
-   Il destinatario è un'IA esterna (Gemini di Google), raggiunta tramite un server dello sviluppatore che funge da intermediario.
-   Il testo inviato viene **utilizzato solo per la classificazione e non viene mai conservato**. Non viene nemmeno utilizzato per l'addestramento dell'IA.
-   L'invio riguarda non solo il testo trascritto a voce, ma anche qualsiasi testo digitato o modificato manualmente. Se è attiva l'assegnazione automatica del tema (funzione di KUU+, opzionale), vengono inviati anche i titoli, i testi e i nomi dei temi degli elementi già salvati, al fine di effettuare l'assegnazione (in ogni caso, tutti i dati sono usati solo per la classificazione e non vengono conservati).
-   Nelle versioni dell'app per **iOS** precedenti alla 2.3.0, era possibile scegliere una classificazione esclusivamente locale tramite l'impostazione "Sul dispositivo" (questa opzione non è più disponibile dalla versione 2.3.0).

**Riguardo alla versione Android:** la versione Android non offre un metodo di organizzazione (classificazione) che si svolge interamente sul dispositivo. Quando si avvia l'organizzazione, il testo trascritto viene **sempre** inviato all'IA esterna (Gemini di Google tramite il nostro backend). Viene inviato solo il testo trascritto — la voce non viene mai inviata — e il testo inviato è utilizzato unicamente per la classificazione, non viene conservato né usato per l'addestramento dell'IA. La trascrizione (riconoscimento vocale) vera e propria si svolge interamente sul dispositivo.

**Riguardo alla versione Apple Watch:** la versione dell'App per Apple Watch non registra audio né esegue il riconoscimento vocale. Per l'inserimento del testo, utilizza l'input di testo standard di watchOS (a scelta dell'utente tra dettatura, scrittura a mano o tastiera) e l'App riceve solo il testo risultante. Quando si sceglie la dettatura, il riconoscimento vocale viene eseguito come funzionalità di Apple (watchOS); il modo in cui viene elaborato — inclusa la possibilità che avvenga sul dispositivo o sui server di Apple — dipende dal dispositivo, dalle impostazioni e dalla lingua, ed **è regolato dall'informativa sulla privacy di Apple**. L'App non può accedere a tali dati audio e non li riceve né li conserva. Il testo ricevuto viene gestito esattamente come il testo dettato su iPhone (classificazione AI secondo il presente articolo; archiviazione secondo l'Articolo 4).

## Articolo 4 (Archiviazione e sincronizzazione)

**Versione iOS:** l'App archivia le trascrizioni e i risultati dell'organizzazione unicamente nel tuo **database privato di iCloud** (CloudKit Private Database). Si tratta di uno spazio di archiviazione fornito da Apple a cui solo tu puoi accedere. Lo sviluppatore dell'App non può visualizzare né recuperare alcun contenuto archiviato. L'utilizzo di iCloud è soggetto all'informativa sulla privacy di Apple.

**Versione Android:** le trascrizioni e i risultati dell'organizzazione sono archiviati **solo su questo dispositivo**. Non è prevista una sincronizzazione automatica sul cloud. In caso di cambio di dispositivo, è possibile esportare i dati in un file da "Voce e dati" nell'app e importarli sul nuovo dispositivo. La destinazione del file viene scelta dall'utente (sul dispositivo, in un'app di archiviazione cloud, ecc.). Lo sviluppatore non può accedere a tale file.

**Versione Apple Watch:** a scopo di visualizzazione, una parte del testo organizzato (i titoli recenti di ciascuna categoria) viene trasferita all'Apple Watch abbinato tramite la comunicazione diretta tra dispositivi di Apple (Watch Connectivity) e viene **archiviata anche sull'orologio**. Il testo inserito sull'Apple Watch viene trasferito all'iPhone con lo stesso meccanismo. Nessun server dello sviluppatore è coinvolto in questo trasferimento o archiviazione.

## Articolo 5 (Finalità del trattamento)

Le informazioni trattate sono utilizzate esclusivamente per:

1.  Generare trascrizioni dalla voce dell'utente e mostrargliele
2.  Classificare le trascrizioni in "Da vedere ora / Da pensare dopo / Da lasciar decantare / Da lasciar andare" e mostrarle all'utente
3.  Archiviare e visualizzare i contenuti espressi in precedenza dall'utente, affinché possa riesaminarli
4.  Mantenere le impostazioni necessarie al funzionamento dell'app

## Articolo 6 (Utilizzo di servizi esterni)

Per fornire le proprie funzionalità, l'App si avvale dei seguenti servizi esterni. **La tua voce non viene inviata a nessuno di questi servizi.**

-   **iCloud / CloudKit** (solo versione iOS. Fornito da Apple. Archiviazione e sincronizzazione solo nel tuo database privato)
-   **Riconoscimento vocale** (versione iOS: framework Speech di Apple; versione Android: motore di riconoscimento vocale integrato nel dispositivo. Entrambi vengono eseguiti sul dispositivo; la voce non viene inviata all'esterno. **La versione per Apple Watch non esegue un proprio riconoscimento vocale ma utilizza l'input standard di watchOS**. V. Articolo 3)
-   **Input di testo standard di watchOS** (solo versione Apple Watch. Fornito da Apple. L'utente sceglie tra dettatura, scrittura a mano o tastiera. In caso di dettatura, il riconoscimento vocale è eseguito come funzione di Apple ed è soggetto all'informativa sulla privacy di Apple. L'App non può accedere a tali dati audio. V. Articolo 3)
-   **Watch Connectivity** (solo versione Apple Watch. Fornito da Apple. Scambia direttamente il testo per la visualizzazione tra iPhone e Apple Watch. Nessun server dello sviluppatore è coinvolto. V. Articolo 4)
-   **IA esterna (cloud)** (classificazione AI. Viene inviato solo il testo; utilizzato unicamente per la classificazione, mai conservato, mai usato per l'addestramento dell'IA. V. Articolo 3)
-   **Servizi di fatturazione** (versione iOS: **Apple StoreKit**; versione Android: **RevenueCat**. Gestione dell'acquisto, rinnovo, annullamento e stato dell'abbonamento KUU+. Nessun contenuto vocale viene inviato. Per RevenueCat, v. Articolo 7 e l'[Informativa sulla privacy di RevenueCat](https://www.revenuecat.com/privacy))
-   **Play Integrity API (tramite Firebase App Check; solo versione Android)** (Verifica che le richieste all'API di classificazione provengano da un'app legittima — attestazione di integrità del dispositivo/app. Non contiene contenuti vocali né informazioni che identificano l'utente)
-   **Google AdMob (SDK Google Mobile Ads)** (solo quando l'iscrizione a KUU+ non è attiva: visualizza un annuncio nativo tra le sezioni della schermata "Le cose che hai detto". Nessun contenuto vocale viene inviato. V. Articolo 13)
-   **Firebase Analytics** (fornito da Google. Per il miglioramento della qualità dell'app. Sulla versione iOS, **utilizzato solo se l'utente acconsente esplicitamente nelle Impostazioni**; sulla versione Android, invia eventi di utilizzo privi di contenuto **per impostazione predefinita** (in entrambi i casi, nessun contenuto vocale viene inviato). La versione iOS utilizza anche **Crashlytics** su base volontaria, ma **la versione Android non include Crashlytics**. V. Articolo 14)

Il server dell'App è minimo e stateless, funge solo da intermediario per la classificazione AI (non archivia alcun contenuto). Non utilizza servizi di autenticazione che richiedono un account personale.

## Articolo 7 (Comunicazione a terzi)

Lo sviluppatore dell'App non ha modo di accedere ai contenuti vocali, alle trascrizioni o ai risultati dell'organizzazione dell'utente e non li comunica a terzi.

Per mostrare annunci agli utenti non iscritti a KUU+, l'App invia a Google le informazioni richieste da Google AdMob per la pubblicazione degli annunci, tra cui identificativi del dispositivo, ID pubblicitario, lingua e regione del dispositivo, posizione approssimativa e dati di interazione con gli annunci (v. Articolo 13; si applica l'informativa sulla privacy di AdMob di Google). Finché l'iscrizione a KUU+ è attiva, questa trasmissione di informazioni non avviene.

Quando ci si iscrive a KUU+ sulla versione **Android**, le informazioni sull'acquisto (ID prodotto, prezzo, data di acquisto, ecc.) vengono inviate a RevenueCat, Inc. per gestire l'acquisto e i relativi diritti (stato attivo/inattivo). Nessun contenuto vocale viene inviato. Per i dettagli sul trattamento dei dati da parte di RevenueCat, consultare l'[Informativa sulla privacy di RevenueCat](https://www.revenuecat.com/privacy).

Le informazioni verranno comunicate solo se richiesto dalla legge, in conformità con le procedure prescritte.

## Articolo 8 (Cancellazione dei dati)

L'utente può cancellare tutti i dati in qualsiasi momento da "Impostazioni → Voce e dati → Cancella i dati salvati" all'interno dell'App. Questa operazione rimuove permanentemente i dati sul dispositivo (e, su iOS, anche dal database privato di iCloud). I dati cancellati non possono essere recuperati.

Disinstallando l'App, i dati locali vengono eliminati. Su iOS, i dati di iCloud possono essere rimossi da Impostazioni → ID Apple → iCloud → Gestisci spazio. La versione Android archivia i dati solo sul dispositivo, quindi vengono eliminati con la disinstallazione.

**Versione Apple Watch:** quando si cancellano tutti i dati, anche i dati di visualizzazione già trasferiti all'Apple Watch vengono sostituiti con contenuti vuoti alla successiva connessione. Eliminando l'app dall'Apple Watch, vengono cancellati anche i dati di visualizzazione archiviati su di esso.

## Articolo 9 (Misure di sicurezza)

-   **Versione iOS**: i file audio temporanei durante la registrazione sono crittografati dalla protezione file di iOS (`FileProtectionType.complete`) e inaccessibili quando il dispositivo è bloccato. Le comunicazioni con iCloud sono crittografate da Apple tramite SSL/TLS.
-   **Versione Android**: l'audio registrato non viene scritto su disco, neanche come file temporaneo; viene elaborato solo in memoria e scartato immediatamente dopo il riconoscimento. Le trascrizioni e i risultati dell'organizzazione sono salvati nell'area di archiviazione privata dell'app, inaccessibile ad altre app, e sono esclusi dal backup automatico sul cloud di Android.
-   **Versione Apple Watch**: il trasferimento tra iPhone e Apple Watch è gestito da Watch Connectivity di Apple e non passa attraverso alcun server dello sviluppatore. I dati archiviati sull'Apple Watch sono limitati al testo di visualizzazione (i titoli recenti di ciascuna categoria); non viene archiviato alcun audio.
-   Tutte le comunicazioni con l'IA esterna sono crittografate (HTTPS/TLS). Il server dello sviluppatore funge solo da intermediario per la classificazione e non archivia alcun contenuto (stateless).

## Articolo 10 (Utilizzo da parte di minori)

L'App è classificata per età 4+, ma data la sua natura (organizzazione dei pensieri), si presume un utilizzo da parte di persone in grado di leggere e scrivere. I minori dovrebbero utilizzarla con il consenso di un genitore o tutore.

## Articolo 11 (Modifiche all'informativa sulla privacy)

La presente informativa può essere aggiornata a seguito di modifiche legislative, aggiunta di funzionalità o cambiamenti nelle specifiche dei framework o delle policy delle piattaforme (Apple/Google). Le modifiche significative saranno comunicate al momento dell'aggiornamento dell'app o sulla pagina pubblica di questa informativa.

## Articolo 12 (Contatti)

Per domande relative a questa informativa, si prega di contattarci tramite la sezione "Sviluppatore" sulla pagina dell'app nell'App Store o su Google Play, oppure tramite "Impostazioni → Contatti" all'interno dell'App.

## Articolo 13 (Annunci e App Tracking Transparency)

Quando non si è iscritti a KUU+, l'App mostra un solo annuncio nativo, fornito da Google AdMob, tra le sezioni della schermata "Le cose che hai detto". L'annuncio viene visualizzato in modo discreto per preservare l'atmosfera di KUU.

-   **I tuoi contenuti vocali non vengono mai utilizzati per la pubblicità.** (Gli annunci non consultano le tue trascrizioni, i risultati dell'organizzazione o i temi).
-   Per la pubblicazione degli annunci, Google AdMob può raccogliere identificativi del dispositivo (incluso IDFA), ID pubblicitario, posizione approssimativa (Coarse Location), dati di diagnostica e interazioni con il prodotto (interazioni con gli annunci all'interno dell'App).
-   **Versione iOS**: una richiesta di **App Tracking Transparency** (ATT) viene mostrata una sola volta, subito prima del primo annuncio. Gli annunci verranno comunque mostrati anche in caso di rifiuto, ma le informazioni inviate a Google saranno limitate (non personalizzate). È possibile modificare l'autorizzazione ATT in qualsiasi momento in "Impostazioni → Privacy e sicurezza → Tracciamento" di iOS.
-   **Versione Android**: l'ATT è un meccanismo esclusivo di iOS e non esiste su Android. Viene invece utilizzato l'**ID pubblicitario** di Google per la pubblicazione degli annunci. È possibile disattivare la personalizzazione degli annunci o reimpostare l'ID pubblicitario dalle "Impostazioni → Privacy → Annunci" del dispositivo (la dicitura può variare a seconda del dispositivo e della versione di Android). La versione Android si attiene inoltre alla gestione del consenso (UMP) mostrata nelle regioni applicabili, come l'UE.
-   **Iscrivendosi a KUU+, tutti gli annunci e la relativa trasmissione di dati vengono interrotti.**
-   Per i dettagli sul trattamento dei dati da parte di AdMob, consultare l'[Informativa sulla privacy di Google AdMob](https://support.google.com/admob/answer/6128543).

## Articolo 14 (Utilizzo di Firebase Analytics / Crashlytics)

**Il modello di consenso esplicito (opt-in) descritto in questo articolo si applica alla versione iOS. Per la versione Android, consultare la sezione "Riguardo alla versione Android" alla fine di questo articolo.**

La **versione iOS**, per migliorare la qualità dell'app e venire a conoscenza tempestivamente di eventuali incidenti, può utilizzare Firebase Analytics (per dati aggregati sull'utilizzo) e Firebase Crashlytics (per i rapporti sugli arresti anomali) di Google. **Questa funzione è DISATTIVATA per impostazione predefinita (nessun dato inviato) e si attiva solo se l'utente acconsente esplicitamente tramite "Impostazioni → Dati e diagnostica".**

-   **Informazioni inviate**:
    -   Un ID di installazione anonimo emesso automaticamente da Firebase (derivato dall'IDFV; non è un identificatore personale diretto).
    -   Dati aggregati sugli eventi in-app (completamento di una sessione di registrazione, visualizzazione/conversione del paywall, completamento dell'onboarding, ecc. I valori numerici vengono raggruppati con una granularità approssimativa).
    -   Lo stack trace (simbolizzato) degli arresti anomali dell'app.
-   **Informazioni non inviate**: i tuoi contenuti vocali (audio), le trascrizioni, il testo dei risultati della classificazione AI e i nomi dei temi che imposti sono **resi non inviabili a livello di codice** (l'implementazione dell'API impedisce di passare valori di tipo stringa all'SDK di analisi).
-   **Finché non si fornisce il consenso, non avviene alcuna comunicazione con Firebase** (incluse tutte le categorie di cui sopra).
-   **Come interrompere l'invio**: è possibile disattivare l'opzione in "Impostazioni → Dati e diagnostica" in qualsiasi momento. Una volta disattivata, gli ID di installazione passati vengono scartati e tutti i log di arresto anomalo non inviati e salvati sul dispositivo vengono eliminati.
-   Il destinatario è Google LLC (Stati Uniti). Si applica l'[Informativa sulla privacy di Firebase](https://firebase.google.com/support/privacy) di Google.

**Riguardo alla versione Android:** la versione Android utilizza Firebase Analytics per inviare **eventi di utilizzo privi di contenuto** per il miglioramento del prodotto (valori aggregati come le transizioni tra schermate e il numero di utilizzi delle funzioni) oltre a un ID istanza app anonimo emesso da Firebase. **A differenza della versione iOS, questa funzione è abilitata per impostazione predefinita.** I tuoi contenuti vocali (audio), le trascrizioni, il testo dei risultati dell'organizzazione e i nomi dei temi **non possono essere inviati** — l'API dell'SDK di analisi è progettata in modo da non poter passare valori di tipo stringa. **La versione Android non include Crashlytics e non invia rapporti sugli arresti anomali.** Il destinatario è Google LLC (Stati Uniti); si applica l'l'[Informativa sulla privacy di Firebase](https://firebase.google.com/support/privacy) di Google.
