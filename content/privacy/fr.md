> Cette traduction est fournie à titre indicatif. Seule la version japonaise fait foi.

# Politique de confidentialité de KUU

Dernière mise à jour : 21 juillet 2026

**En résumé :** Ce que vous dites vous appartient. **Votre voix elle-même n'est jamais envoyée à l'extérieur de votre appareil**. La transcription s'effectue sur votre appareil. L'organisation par IA utilise une IA externe, mais seul le texte transcrit est envoyé. Il est utilisé uniquement pour l'organisation et n'est pas conservé (sur iOS, vous pouvez opter pour une organisation exclusivement sur l'appareil via l'option « Sur l'appareil » dans les Réglages ; **la version Android envoie systématiquement les données à l'IA externe ; il n'y a pas d'option d'organisation sur l'appareil**). Les données sont stockées uniquement sur votre appareil, et sur iOS, également dans votre base de données privée iCloud (la version Android ne stocke les données que sur l'appareil). Le développeur ne stocke pas votre contenu et ne peut pas consulter ce qui est reçu. Vous pouvez supprimer toutes vos données à tout moment depuis l'application. L'application n'effectue que les **communications réseau minimales** nécessaires à la facturation (StoreKit sur iOS / RevenueCat sur Android) et aux publicités Google AdMob, et ces informations n'incluent jamais ce que vous avez dit (les publicités sont désactivées avec KUU+). Nous mesurons l'utilisation pour améliorer la qualité, mais cela n'inclut jamais non plus ce que vous avez dit (sur iOS, la participation est volontaire (opt-in) ; sur Android, une mesure sans contenu est effectuée par défaut – voir l'article 14).

---

## Article 1 (Principes de base)

L'application « KUU » (ci-après « l'Application ») vous aide à extérioriser et à organiser les pensées que vous avez en tête en les exprimant à voix haute. Elle est disponible en **versions iOS et Android**, et la présente politique s'applique aux deux. L'Application ne traite les informations que dans la mesure minimale nécessaire pour fournir ses fonctionnalités, en accordant la priorité absolue à la protection de la vie privée de l'utilisateur.

## Article 2 (Informations collectées et stockées)

Les informations traitées par l'Application se limitent à ce qui suit :

1.  **Contenu que vous énoncez (données audio)** — L'audio enregistré n'est stocké que temporairement dans une zone locale de l'appareil pendant le processus de transcription, puis est supprimé rapidement une fois le traitement terminé. Il n'est jamais envoyé à un serveur.
2.  **Résultats de la transcription et de l'organisation (texte)** — Sauvegardés pour que vous puissiez les consulter (sur iOS : sur votre appareil et dans votre base de données privée iCloud ; sur Android : uniquement sur l'appareil. Voir l'article 4 pour plus de détails).
3.  **Réglages de l'application** — Thème, taille du texte, état du niveau d'eau dans la tête et autres valeurs de configuration nécessaires au fonctionnement de l'Application.

L'Application ne collecte aucune information personnelle telle que votre nom, adresse e-mail, numéro de téléphone, localisation, contacts, calendrier, photos ou identifiants d'appareil.

## Article 3 (Reconnaissance vocale et classification par IA)

La **reconnaissance vocale (transcription)** s'effectue entièrement sur votre appareil iOS.

-   Reconnaissance vocale : utilise le framework Speech d'Apple (sur l'appareil). Votre voix elle-même n'est jamais envoyée à l'extérieur de l'appareil.

La **classification par IA (catégorisation)** utilise une IA externe.

-   Seul le **contenu textuel (le texte transcrit)** est envoyé. Votre voix n'est pas envoyée.
-   Le destinataire est une IA externe (Gemini de Google), via le serveur du développeur (backend).
-   Le contenu envoyé est **uniquement utilisé pour la classification et n'est pas stocké**. Il n'est pas non plus utilisé pour l'entraînement de l'IA.
-   Sur la **version iOS**, vous pouvez à tout moment passer à une **classification exclusivement sur l'appareil** (FoundationModels d'Apple / règles sur l'appareil) via l'option « Sur l'appareil » dans les Réglages. Dans ce cas, même le texte ne quitte pas votre appareil.

**Concernant la version Android :** La version Android ne propose pas de méthode d'organisation (classification) s'exécutant entièrement sur l'appareil. Lorsque vous effectuez une organisation, le texte transcrit est **systématiquement** envoyé à l'IA externe (Gemini de Google via notre backend). Il n'existe pas d'option « Sur l'appareil » comme sur la version iOS. Seul le contenu textuel est envoyé ; votre voix elle-même n'est pas transmise, et le texte envoyé est utilisé uniquement pour la classification. Il n'est ni stocké, ni utilisé pour l'entraînement de l'IA. La transcription (reconnaissance vocale) elle-même s'effectue entièrement sur l'appareil.

## Article 4 (Stockage et synchronisation)

**Version iOS :** Les résultats de la transcription et de l'organisation sont stockés uniquement dans votre **base de données privée iCloud** (CloudKit Private Database). Il s'agit d'un espace de stockage fourni par Apple auquel vous seul pouvez accéder. Le développeur de l'Application ne peut ni consulter, ni récupérer le contenu qui y est stocké. Les conditions d'utilisation et la sécurité d'iCloud sont soumises à la politique de confidentialité d'Apple.

**Version Android :** Les résultats de la transcription et de l'organisation sont stockés **uniquement sur cet appareil**. Il n'y a pas de synchronisation automatique avec le cloud. Lors d'un changement d'appareil, vous pouvez exporter vos données vers un fichier depuis « Voix et données » dans l'application, puis l'importer sur le nouvel appareil. C'est vous qui choisissez l'emplacement de l'exportation (sur l'appareil, dans votre application de stockage cloud, etc.). Le développeur ne peut pas accéder à ce fichier.

## Article 5 (Finalité de l'utilisation)

Les informations traitées sont utilisées uniquement aux fins suivantes :

1.  Générer des transcriptions à partir de votre voix et vous les afficher
2.  Classifier les transcriptions en « Maintenant », « Plus tard », « En attente » et « Relâcher » et vous les afficher
3.  Stocker et afficher le contenu que vous avez énoncé par le passé pour que vous puissiez le consulter
4.  Conserver les valeurs de configuration nécessaires au fonctionnement de l'Application

## Article 6 (Utilisation de services externes)

Pour fournir ses fonctionnalités, l'Application a recours aux services externes suivants. **Votre voix elle-même n'est envoyée à aucun de ces services.**

-   **iCloud / CloudKit** (version iOS uniquement. Fourni par Apple. Stockage et synchronisation uniquement dans votre propre base de données privée)
-   **Reconnaissance vocale** (version iOS : framework Speech d'Apple ; version Android : moteur de reconnaissance vocale sur l'appareil. Les deux s'exécutent sur l'appareil ; votre voix n'est pas envoyée à l'extérieur.)
-   **IA externe (cloud)** (Classification par IA. Seul le contenu textuel est envoyé. Il est utilisé uniquement pour la classification, n'est pas stocké et n'est pas utilisé pour l'entraînement de l'IA. Désactivable sur iOS via l'option « Sur l'appareil », mais **la version Android envoie systématiquement les données à l'IA externe**. Voir l'article 3.)
-   **FoundationModels** (version iOS uniquement. Fourni par Apple. S'exécute entièrement sur l'appareil. Utilisé lorsque l'option « Sur l'appareil » est activée ou en solution de repli si l'IA externe est indisponible.)
-   **Services de facturation** (version iOS : **Apple StoreKit** ; version Android : **RevenueCat**. Gestion de l'achat, du renouvellement, de l'annulation et des droits de l'abonnement KUU+. Aucun contenu énoncé n'est envoyé. Concernant RevenueCat, voir l'article 7 et la [politique de confidentialité de RevenueCat](https://www.revenuecat.com/privacy).)
-   **Play Integrity API (via Firebase App Check ; version Android uniquement)** (Vérifie que les requêtes à l'API de classification proviennent d'une application légitime via une attestation d'intégrité de l'appareil et de l'application. Ne contient ni le contenu énoncé, ni d'informations permettant de vous identifier.)
-   **Google AdMob (SDK Google Mobile Ads)** (Uniquement si vous n'êtes pas abonné à KUU+ : affiche un encart publicitaire natif entre les sections de l'écran « Ce que vous avez dit ». Aucun contenu énoncé n'est envoyé. Voir l'article 13.)
-   **Firebase Analytics** (Fourni par Google. Pour l'amélioration de la qualité de l'application. Sur la version iOS, **utilisé uniquement si l'utilisateur y consent explicitement (opt-in) dans les Réglages** ; sur la version Android, des événements d'utilisation sans contenu sont envoyés **par défaut** (dans les deux cas, aucun contenu énoncé n'est envoyé). La version iOS utilise également **Crashlytics** sur opt-in, mais **la version Android n'intègre pas Crashlytics**. Voir l'article 14.)

Le serveur de l'Application est minimaliste et ne sert qu'à relayer les requêtes de classification par IA ; il ne stocke aucun contenu (il est sans état ou *stateless*). L'Application n'utilise aucun service d'authentification nécessitant un compte personnel.

## Article 7 (Communication à des tiers)

Le développeur de l'Application n'a aucun moyen d'accéder au contenu que vous énoncez, à ses transcriptions ou aux résultats de l'organisation, et ne communique aucune de ces informations à des tiers.

Afin de diffuser des publicités aux utilisateurs non abonnés à KUU+, des informations requises par Google AdMob pour la diffusion publicitaire sont envoyées à Google, telles que les identifiants de l'appareil, l'identifiant publicitaire, la langue et la région de l'appareil, la localisation approximative et les informations sur les clics publicitaires (voir l'article 13, la politique de confidentialité d'AdMob de Google s'applique). Cette transmission d'informations n'a pas lieu tant que vous êtes abonné à KUU+.

Lorsque vous vous abonnez à KUU+ sur la **version Android**, les informations d'achat (ID du produit, prix, date d'achat, etc.) sont envoyées à RevenueCat, Inc. pour la gestion du processus d'achat et de vos droits (détermination du statut actif/inactif). Aucun contenu énoncé n'est envoyé. Pour plus de détails sur le traitement des données par RevenueCat, veuillez consulter la [politique de confidentialité de RevenueCat](https://www.revenuecat.com/privacy).

Nous ne communiquerons des informations que si la loi l'exige, en suivant les procédures établies.

## Article 8 (Suppression des données)

Vous pouvez à tout moment supprimer l'intégralité de vos données depuis « Réglages → Voix et données → Supprimer les données stockées » dans l'application. Cette action effacera de manière permanente les données sur l'appareil (et, sur la version iOS, également les données de votre base de données privée iCloud). Les données supprimées ne peuvent pas être récupérées.

La désinstallation de l'Application supprime les données sur l'appareil. Sur iOS, les données iCloud peuvent être supprimées via les réglages d'Apple (Réglages → Identifiant Apple → iCloud → Gérer le stockage). La version Android ne stockant les données que sur l'appareil, celles-ci sont supprimées lors de la désinstallation.

## Article 9 (Mesures de sécurité)

-   **Version iOS** : Les fichiers audio temporaires créés pendant l'enregistrement sont chiffrés par la fonctionnalité de protection des fichiers d'iOS (`FileProtectionType.complete`) et sont inaccessibles lorsque l'appareil est verrouillé. Les communications avec iCloud sont chiffrées par Apple via SSL/TLS.
-   **Version Android** : L'audio enregistré n'est jamais écrit sur le disque, même en tant que fichier temporaire ; il est traité uniquement en mémoire et immédiatement supprimé après la reconnaissance. Les transcriptions et résultats de l'organisation sont stockés dans l'espace de stockage privé de l'application sur Android, inaccessible aux autres applications. Ils sont également exclus de la sauvegarde automatique sur le cloud d'Android.
-   Toutes les communications avec l'IA externe sont chiffrées (HTTPS/TLS). Le serveur du développeur ne fait que relayer les requêtes de classification et ne stocke aucun contenu (il est sans état ou *stateless*).

## Article 10 (Utilisation par les mineurs)

L'Application est classée 4+, mais sa nature (organisation de la pensée) suppose une utilisation par des personnes en âge de lire et d'écrire. Les mineurs doivent utiliser l'Application avec le consentement de leur tuteur légal.

## Article 11 (Modification de la présente politique)

La présente politique peut être révisée en raison de modifications de la législation, de l'ajout de fonctionnalités ou de changements dans les spécifications des frameworks ou politiques des plateformes (Apple / Google). En cas de modification importante, nous vous en informerons lors d'une mise à jour de l'application ou sur la page publique de cette politique.

## Article 12 (Contact)

Pour toute question concernant cette politique, veuillez nous contacter via la section « Développeur » sur la page de l'application dans l'App Store ou Google Play, ou via « Réglages → Contact » dans l'application.

## Article 13 (Publicités et App Tracking Transparency)

Uniquement lorsque vous n'êtes pas abonné à KUU+, l'Application affiche un seul encart publicitaire natif fourni par Google AdMob dans l'écran « Ce que vous avez dit ». Pour préserver l'univers de KUU, la publicité est affichée de manière discrète entre les sections de l'écran.

-   **Le contenu que vous énoncez n'est jamais utilisé à des fins publicitaires** (les publicités ne consultent ni vos transcriptions, ni les résultats de la classification, ni vos thèmes).
-   Pour la diffusion publicitaire, Google AdMob peut collecter des informations telles que des identifiants d'appareil (y compris l'IDFA), l'identifiant publicitaire, la localisation approximative, des diagnostics et des données d'interaction avec le produit (interactions avec les publicités dans l'application).
-   **Version iOS** : une invite **App Tracking Transparency** (ATT) s'affiche une seule fois, juste avant la première publicité. Si vous refusez, des publicités seront tout de même affichées, mais les informations envoyées à Google seront limitées (non personnalisées). Vous pouvez modifier votre autorisation ATT à tout moment dans les « Réglages » d'iOS → « Confidentialité et sécurité » → « Suivi ».
-   **Version Android** : ATT est un mécanisme propre à iOS et n'existe pas sur Android. C'est l'**identifiant publicitaire** de Google (Advertising ID) qui est utilisé pour la diffusion des publicités. Vous pouvez désactiver la personnalisation des annonces ou réinitialiser votre identifiant publicitaire depuis les « Paramètres » de votre appareil → « Confidentialité » → « Annonces » (le libellé peut varier selon l'appareil et la version d'Android). La version Android se conforme également à la gestion du consentement (UMP) affichée dans les régions concernées, comme l'UE.
-   **L'abonnement à KUU+ interrompt toutes les publicités et les transmissions d'informations associées.**
-   Pour plus de détails sur le traitement des données par Google AdMob, veuillez consulter la [politique de confidentialité de Google AdMob](https://support.google.com/admob/answer/6128543).

## Article 14 (Utilisation de Firebase Analytics / Crashlytics)

**Le modèle de consentement explicite (opt-in) décrit dans cet article s'applique à la version iOS. Pour la version Android, veuillez consulter la section « Concernant la version Android » à la fin de cet article.**

La **version iOS** peut utiliser Firebase Analytics (agrégation des données d'utilisation) et Firebase Crashlytics (rapports de plantage) de Google pour améliorer la qualité de l'application et être informée rapidement des incidents en production. **Cette fonctionnalité est désactivée par défaut (aucune donnée n'est envoyée) et ne s'active que si vous y consentez explicitement (opt-in) via « Réglages → Données et diagnostics ».**

-   **Informations envoyées** :
    -   Un identifiant d'installation anonymisé émis automatiquement par Firebase (basé sur l'IDFV ; ce n'est pas un identifiant qui permet de vous identifier personnellement).
    -   Des signaux agrégés sur les événements d'interaction dans l'application (ex. : achèvement ou non d'une session d'enregistrement, affichage du mur de paiement et conversion, finalisation de l'intégration). Les valeurs numériques sont envoyées avec une granularité grossière (par tranches).
    -   Les traces de pile (*stack traces*) symbolisées lorsque l'application se termine de manière anormale.
-   **Informations qui ne sont pas envoyées** : le contenu que vous énoncez (audio), les textes des transcriptions, les résultats de la classification par IA et les noms de thèmes que vous définissez sont **conçus pour ne pas pouvoir être envoyés au niveau du typage des données** (l'implémentation utilise une API qui ne permet pas de transmettre des valeurs textuelles au SDK d'analyse).
-   **Tant que vous n'avez pas donné votre consentement (opt-in), aucune communication, y compris pour les informations ci-dessus, n'est effectuée avec Firebase.**
-   **Comment arrêter l'envoi** : vous pouvez désactiver le bouton à tout moment dans « Réglages → Données et diagnostics ». Une fois désactivé, l'identifiant d'installation passé est abandonné et tous les journaux de plantage non envoyés qui étaient stockés localement sur l'appareil sont supprimés.
-   Le destinataire est Google LLC (États-Unis). Les [informations sur la confidentialité de Firebase](https://firebase.google.com/support/privacy) de Google s'appliquent.

**Concernant la version Android :** La version Android utilise Firebase Analytics pour envoyer des **événements d'utilisation sans contenu** (valeurs agrégées comme les transitions d'écran ou le nombre d'utilisations d'une fonctionnalité) à des fins d'amélioration du produit, ainsi qu'un identifiant d'instance d'application (App Instance ID) anonyme émis par Firebase. **Contrairement à la version iOS, cette fonction est activée par défaut.** Le contenu que vous énoncez (audio), les textes des transcriptions et de l'organisation, ainsi que les noms des thèmes, **ne peuvent pas être envoyés** en raison d'une conception qui empêche de transmettre des valeurs textuelles au SDK d'analyse. **La version Android n'intègre pas Crashlytics et n'envoie donc aucun rapport de plantage.** Le destinataire est Google LLC (États-Unis), et les [informations sur la confidentialité de Firebase](https://firebase.google.com/support/privacy) de Google s'appliquent.
