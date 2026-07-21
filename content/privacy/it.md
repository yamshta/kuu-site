> Questa è una traduzione di riferimento fornita per comodità. La versione giapponese costituisce il testo autorevole.

# Informativa sulla privacy di KUU

Ultimo aggiornamento: 21 luglio 2026

**In sintesi:** Ciò che dici è tuo. **L'audio stesso non viene mai inviato all'esterno del tuo dispositivo.** La trascrizione avviene sul tuo dispositivo. L'organizzazione tramite IA utilizza un'IA esterna, ma viene inviato solo il testo trascritto. Tale testo è utilizzato esclusivamente per l'organizzazione e non viene conservato dal fornitore dell'IA (su iOS è possibile passare all'organizzazione esclusivamente sul dispositivo tramite l'impostazione "Sul dispositivo"; **la versione Android invia i dati solo all'IA esterna e non dispone di un'opzione di organizzazione sul dispositivo**). I dati vengono salvati solo sul tuo dispositivo e, per la versione iOS, anche nel tuo database privato di iCloud (la versione Android salva i dati solo sul dispositivo). Lo sviluppatore non archivia i tuoi contenuti e non può visualizzare ciò che viene ricevuto. Puoi eliminare tutti i dati in qualsiasi momento dall'interno dell'app. L'app effettua solo le **comunicazioni di rete minime necessarie** per la fatturazione (StoreKit su iOS / RevenueCat su Android) e per gli annunci di Google AdMob; tali informazioni non includono mai ciò che hai detto (gli annunci vengono disattivati con KUU+). L'utilizzo viene misurato per migliorare la qualità, ma anche in questo caso non viene mai incluso ciò che hai detto (su iOS l'utente deve fornire il consenso esplicito (opt-in); su Android la misurazione senza contenuti è attiva per impostazione predefinita; vedi l'Articolo 14).

---

## Articolo 1 (Principi generali)

L'applicazione "KUU" (di seguito "l'App") è un'applicazione che ti aiuta a esternare e organizzare i pensieri che hai in testa, parlando a voce alta. È disponibile una **versione per iOS e una per Android** e la presente informativa si applica a entrambe. L'App tratta le informazioni solo nella misura minima necessaria per fornire le sue funzionalità, dando la massima priorità alla protezione della privacy dell'utente.

## Articolo 2 (Informazioni raccolte e conservate)

L'App tratta esclusivamente le seguenti informazioni:

1.  **Contenuto pronunciato dall'utente (dati audio)** — L'audio registrato viene salvato in un'area temporanea sul dispositivo solo durante il processo di trascrizione e viene eliminato immediatamente al termine dell'elaborazione. Non viene inviato a nessun server.
2.  **Risultati della trascrizione e dell'organizzazione (testo)** — Vengono salvati per consentirti di riesaminarli (versione iOS: sul dispositivo e nel database privato di iCloud; versione Android: solo sul dispositivo. Per i dettagli, vedi l'Articolo 4).
3.  **Impostazioni dell'app** — Valori di impostazione necessari per il funzionamento dell'app, come tema, dimensione del testo e stato del livello dell'acqua nella testa.

L'App non raccoglie dati personali come nome, indirizzo e-mail, numero di telefono, informazioni sulla posizione, contatti, calendario, foto o identificativi del dispositivo.

## Articolo 3 (Riconoscimento vocale e organizzazione tramite IA)

Il **riconoscimento vocale (trascrizione)** viene eseguito interamente sul tuo dispositivo iOS.

- Riconoscimento vocale: utilizza il framework Speech di Apple (on-device). L'audio stesso non viene mai inviato all'esterno del dispositivo.

L'**organizzazione tramite IA (categorizzazione)** utilizza un'IA esterna.

- Viene inviato **solo il contenuto testuale (il testo trascritto)**. L'audio non viene inviato.
- La destinazione è un'IA esterna, tramite il server dello sviluppatore (passando per il backend di Google Gemini).
- Il contenuto inviato viene **utilizzato solo per la categorizzazione e non viene conservato**. Non viene utilizzato neanche per l'addestramento dell'IA.
- **Sulla versione iOS**, è possibile passare in qualsiasi momento all'**organizzazione esclusivamente sul dispositivo** (FoundationModels di Apple / regole sul dispositivo) tramite l'impostazione "Sul dispositivo". In questo caso, neanche il testo lascia il dispositivo.

**Riguardo alla versione Android:** la versione Android non offre un metodo di organizzazione (categorizzazione) che si svolge interamente sul dispositivo. Quando si esegue l'organizzazione, il testo trascritto viene **sempre** inviato a un'IA esterna (Gemini di Google tramite il nostro backend). Non è presente un'opzione "Sul dispositivo" come nella versione iOS. Viene inviato solo il contenuto testuale, l'audio stesso non viene inviato, e il testo inviato viene utilizzato esclusivamente per la categorizzazione, non viene conservato né utilizzato per l'addestramento dell'IA. La trascrizione (riconoscimento vocale) stessa si svolge interamente sul dispositivo.

## Articolo 4 (Archiviazione e sincronizzazione)

**Versione iOS:** I risultati della trascrizione e dell'organizzazione vengono salvati esclusivamente nel tuo **database privato di iCloud** (CloudKit Private Database). Si tratta di uno spazio di archiviazione fornito da Apple a cui solo tu puoi accedere. Lo sviluppatore dell'App non può visualizzare né recuperare i contenuti archiviati. L'utilizzo di iCloud è soggetto all'informativa sulla privacy di Apple.

**Versione Android:** I risultati della trascrizione e dell'organizzazione sono salvati **solo su questo dispositivo**. Non è prevista una sincronizzazione automatica su cloud. In caso di cambio di dispositivo, è possibile esportare i dati in un file da "Voce e dati" all'interno dell'app e importarli sul nuovo dispositivo. La destinazione dell'esportazione viene scelta dall'utente (sul dispositivo, nell'app di archiviazione cloud in uso, ecc.). Lo sviluppatore non può accedere a tale file.

## Articolo 5 (Finalità del trattamento)

Le informazioni trattate sono utilizzate esclusivamente per le seguenti finalità:

1.  Generare trascrizioni dall'audio e mostrarle all'utente.
2.  Categorizzare le trascrizioni in "Vedi ora / Pensa dopo / Metti in pausa / Lascia andare" e mostrarle all'utente.
3.  Archiviare e visualizzare i contenuti pronunciati in passato dall'utente, per consentirgli di riesaminarli.
4.  Mantenere i valori di impostazione necessari per il funzionamento dell'app.

## Articolo 6 (Utilizzo di servizi esterni)

L'App utilizza i seguenti servizi esterni per fornire le sue funzionalità. **L'audio stesso non viene inviato a nessuno di questi servizi.**

- **iCloud / CloudKit** (solo versione iOS. Fornito da Apple. Archiviazione e sincronizzazione solo nel tuo database privato).
- **Riconoscimento vocale** (versione iOS: framework Speech di Apple; versione Android: motore di riconoscimento vocale del dispositivo. Entrambi vengono eseguiti sul dispositivo e l'audio non viene inviato all'esterno).
- **IA esterna (cloud)** (Organizzazione tramite IA. Viene inviato solo il contenuto testuale. Utilizzato solo per la categorizzazione, non viene conservato né utilizzato per l'addestramento dell'IA. Sulla versione iOS può essere disattivato tramite l'impostazione "Sul dispositivo", ma **la versione Android invia i dati solo all'IA esterna**. Vedi l'Articolo 3).
- **FoundationModels** (solo versione iOS. Fornito da Apple. Eseguito interamente sul dispositivo. Utilizzato quando è attiva l'impostazione "Sul dispositivo" o come fallback quando l'IA esterna non è disponibile).
- **Servizi di fatturazione** (versione iOS: **Apple StoreKit**; versione Android: **RevenueCat**. Gestione dell'acquisto, rinnovo, cancellazione e stato dei diritti dell'abbonamento KUU+. Nessun contenuto vocale viene inviato. Per RevenueCat, vedi l'Articolo 7 e l'[informativa sulla privacy di RevenueCat](https://www.revenuecat.com/privacy)).
- **Play Integrity API (tramite Firebase App Check. Solo versione Android)** (Certificazione dell'integrità del dispositivo e dell'app per verificare che le richieste all'API di classificazione provengano da un'app legittima. Non contiene contenuti vocali né informazioni che identificano l'utente).
- **Google AdMob (Google Mobile Ads SDK)** (Solo quando l'abbonamento KUU+ non è attivo, viene visualizzato un singolo spazio pubblicitario nativo tra le sezioni nella schermata "Cose dette". Nessun contenuto vocale viene inviato. Per i dettagli, vedi l'Articolo 13).
- **Firebase Analytics** (Fornito da Google. Per il miglioramento della qualità dell'app. Sulla versione iOS, **utilizzato solo se l'utente fornisce esplicitamente il consenso (opt-in) nelle Impostazioni**; sulla versione Android, gli eventi di utilizzo senza contenuto vengono inviati **per impostazione predefinita** (in entrambi i casi, nessun contenuto vocale viene inviato). La versione iOS utilizza anche **Crashlytics** su base opt-in, ma **la versione Android non include Crashlytics**. Per i dettagli, vedi l'Articolo 14).

Il server dell'App è minimo e funge solo da intermediario per l'organizzazione tramite IA, senza conservare alcun contenuto (stateless). Non vengono utilizzati servizi di autenticazione che richiedono un account personale.

## Articolo 7 (Comunicazione a terzi)

Lo sviluppatore dell'App non ha modo di accedere ai contenuti pronunciati dall'utente, ai risultati della trascrizione o dell'organizzazione e non li fornisce a terzi.

Al fine di mostrare annunci pubblicitari agli utenti non abbonati a KUU+, informazioni richieste da Google AdMob per l'erogazione degli annunci, quali identificativi del dispositivo, ID pubblicitario, lingua e regione del dispositivo, posizione approssimativa e informazioni sulle interazioni con gli annunci, vengono inviate a Google (per i dettagli, vedi l'Articolo 13; si applica l'informativa sulla privacy di Google AdMob). Finché l'abbonamento a KUU+ è attivo, questa trasmissione di informazioni non avviene.

Quando ci si abbona a KUU+ sulla **versione Android**, le informazioni sull'acquisto (ID prodotto, prezzo, data di acquisto, ecc.) vengono inviate a RevenueCat, Inc. per la gestione della transazione e dei diritti (determinazione dello stato attivo/inattivo). Nessun contenuto vocale viene inviato. Per i dettagli sul trattamento dei dati da parte di RevenueCat, si prega di consultare l'[informativa sulla privacy di RevenueCat](https://www.revenuecat.com/privacy).

Le informazioni saranno divulgate solo nei casi in cui sia richiesto dalla legge, seguendo le procedure prescritte.

## Articolo 8 (Cancellazione dei dati)

L'utente può cancellare tutti i dati in qualsiasi momento dall'app, andando su "Impostazioni → Voce e dati → Cancella i contenuti salvati". La cancellazione rimuove permanentemente i dati sul dispositivo (e, sulla versione iOS, anche i dati nel database privato di iCloud). I dati cancellati non possono essere recuperati.

Disinstallando l'App, i dati presenti sul dispositivo vengono eliminati. Sulla versione iOS, i dati su iCloud possono essere rimossi dalle impostazioni di Apple (Impostazioni → ID Apple → iCloud → Gestisci spazio). La versione Android salva i dati solo sul dispositivo, quindi vengono eliminati con la disinstallazione.

## Articolo 9 (Misure di sicurezza)

- **Versione iOS**: I file audio temporanei durante la registrazione sono crittografati dalla funzione di protezione dei file di iOS (`FileProtectionType.complete`) e sono inaccessibili quando il dispositivo è bloccato. Le comunicazioni con iCloud sono crittografate da Apple tramite SSL/TLS.
- **Versione Android**: L'audio registrato non viene scritto su disco, neanche come file temporaneo; viene elaborato solo in memoria e scartato immediatamente dopo il riconoscimento. I risultati della trascrizione e dell'organizzazione salvati risiedono nell'area di archiviazione privata dell'app, inaccessibile ad altre app, e sono esclusi dal backup automatico su cloud di Android.
- Tutte le comunicazioni con l'IA esterna sono crittografate (HTTPS/TLS). Il server dello sviluppatore funge solo da intermediario per le richieste di organizzazione e non conserva alcun contenuto (stateless).

## Articolo 10 (Utilizzo da parte di minori)

L'App ha una classificazione di età 4+, ma data la sua natura (organizzazione del pensiero), si presume un utilizzo da parte di utenti in età di letto-scrittura. Se un minore utilizza l'app, deve farlo con il consenso di un genitore o tutore.

## Articolo 11 (Modifiche alla presente informativa)

La presente informativa può essere aggiornata a seguito di modifiche legislative, aggiunta di funzionalità o cambiamenti nelle specifiche dei framework o delle policy di ciascuna piattaforma (Apple / Google). In caso di modifiche significative, verrà data comunicazione al momento dell'aggiornamento dell'app o sulla pagina pubblica di questa informativa.

## Articolo 12 (Contatti)

Per domande relative alla presente informativa, si prega di contattarci tramite la sezione "Sviluppatore" sulla pagina dell'app nell'App Store o su Google Play, oppure tramite "Impostazioni → Contatti" all'interno dell'app.

## Articolo 13 (Pubblicità e Trasparenza nel tracciamento da parte delle app)

L'App mostra un singolo spazio pubblicitario nativo, fornito da Google AdMob, nella schermata "Cose dette" solo durante il periodo in cui non si è abbonati a KUU+. L'annuncio stesso viene visualizzato in modo discreto tra le sezioni dello schermo per mantenere l'atmosfera di KUU.

- **I tuoi contenuti vocali non vengono mai utilizzati per la pubblicità** (gli annunci non consultano le trascrizioni, i risultati dell'organizzazione o i temi).
- Per l'erogazione degli annunci, Google AdMob può raccogliere identificativi del dispositivo (incluso IDFA), ID pubblicitario, posizione approssimativa (Coarse Location), dati di diagnostica e interazioni con il prodotto (informazioni sul contatto con gli annunci all'interno dell'app).
- **Versione iOS**: Una richiesta di **Trasparenza nel tracciamento da parte delle app** (ATT) viene mostrata una sola volta, subito prima della visualizzazione del primo annuncio. Gli annunci verranno mostrati anche in caso di rifiuto, ma le informazioni inviate a Google saranno limitate (non personalizzate). È possibile modificare l'autorizzazione ATT in qualsiasi momento da "Impostazioni" → "Privacy e sicurezza" → "Tracciamento" su iOS.
- **Versione Android**: L'ATT è un meccanismo esclusivo di iOS e non esiste su Android. Al suo posto, viene utilizzato l'**ID pubblicitario** di Google per l'erogazione degli annunci. È possibile disattivare la personalizzazione degli annunci o reimpostare il proprio ID pubblicitario da "Impostazioni → Privacy → Annunci" del dispositivo (la dicitura può variare a seconda del dispositivo e della versione di Android). Inoltre, la versione Android si conforma alla gestione del consenso (UMP) mostrata nelle regioni applicabili come l'UE.
- **Abbonandosi a KUU+ si interrompono tutti gli annunci e la relativa trasmissione di dati.**
- Per i dettagli sul trattamento dei dati da parte di Google AdMob, si prega di consultare l'[informativa sulla privacy di Google AdMob](https://support.google.com/admob/answer/6128543).

## Articolo 14 (Utilizzo di Firebase Analytics / Crashlytics)

**Il modello di consenso esplicito (opt-in) descritto in questo articolo si applica alla versione iOS. Per la versione Android, si prega di consultare la sezione "Riguardo alla versione Android" alla fine di questo articolo.**

**Sulla versione iOS**, per il miglioramento della qualità dell'app e la notifica immediata di incidenti in produzione, l'App può utilizzare Firebase Analytics di Google (aggregazione dei dati di utilizzo) e Firebase Crashlytics (report di crash). **Questa funzionalità è DISATTIVATA per impostazione predefinita (nessun dato inviato) e si attiva solo se l'utente fornisce esplicitamente il consenso (opt-in) tramite "Impostazioni → Dati e diagnostica".**

- **Informazioni inviate**:
  - Un ID di installazione anonimizzato generato automaticamente da Firebase (basato su IDFV; non è un identificatore che permette di risalire direttamente alla persona).
  - Segnali aggregati di eventi di interazione all'interno dell'app (completamento di una sessione di registrazione, visualizzazione del paywall / conversione, completamento dell'onboarding, ecc. I valori numerici vengono inviati con una granularità grossolana e raggruppata).
  - Stack trace del crash (simbolizzati) in caso di chiusura anomala dell'app.
- **Informazioni non inviate**: Il contenuto pronunciato (audio), i risultati della trascrizione, il testo dei risultati dell'organizzazione tramite IA e i nomi dei temi impostati dall'utente sono **resi non inviabili a livello di tipo di dato** (l'implementazione dell'API impedisce di passare valori di tipo stringa all'SDK di analisi).
- **Durante il periodo in cui non è stato dato il consenso (opt-in), non si verifica alcuna comunicazione verso Firebase** (incluse tutte le categorie di cui sopra).
- **Come interrompere l'invio**: È possibile disattivare l'interruttore in "Impostazioni → Dati e diagnostica" in qualsiasi momento. Una volta disattivato, gli ID di installazione passati vengono scartati e tutti i log di crash non inviati e salvati localmente sul dispositivo vengono eliminati.
- Il destinatario è Google LLC (Stati Uniti). Si applicano le [Informazioni sulla privacy di Firebase](https://firebase.google.com/support/privacy) di Google.

**Riguardo alla versione Android:** La versione Android utilizza Firebase Analytics per inviare **eventi di utilizzo senza contenuto (content-free)** per il miglioramento del prodotto (valori raggruppati come transizioni tra schermate e conteggi di utilizzo delle funzionalità) e un App Instance ID anonimo emesso da Firebase. **A differenza di iOS, questa funzione è abilitata per impostazione predefinita.** Il contenuto pronunciato (audio), le trascrizioni, il testo dei risultati dell'organizzazione e i nomi dei temi **non possono essere inviati**, poiché la progettazione dell'API dell'SDK di analisi impedisce di passare valori di tipo stringa. **La versione Android non include Crashlytics e non invia report di crash.** Il destinatario è Google LLC (Stati Uniti); si applicano le [Informazioni sulla privacy di Firebase](https://firebase.google.com/support/privacy) di Google.
