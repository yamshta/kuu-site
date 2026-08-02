> Ceci est une traduction de référence fournie à titre indicatif. La version japonaise fait foi.

# Politique de confidentialité de KUU

Dernière mise à jour : 2 août 2026

**En résumé :** Ce que vous dites vous appartient. **L'application n'envoie jamais l'audio de votre voix à l'extérieur**. Sur les appareils iPhone et Android, la transcription s'effectue également au sein de l'appareil. **La version Apple Watch de l'application n'effectue aucun enregistrement** — elle ne reçoit que le texte produit par les méthodes de saisie standard de la montre (dictée, griffonnage ou clavier) ; lorsque vous choisissez la dictée, la reconnaissance vocale est gérée par le système d'Apple (voir l'article 3). L'organisation par IA utilise une IA externe, mais seul le texte transcrit est envoyé. Il est utilisé uniquement pour l'organisation et n'est pas conservé. Les données sont stockées uniquement sur votre appareil et, sur iOS, également dans votre base de données privée iCloud (sur Android, le stockage se fait uniquement sur l'appareil). Le développeur ne stocke pas votre contenu et ne peut pas visualiser ce qui est reçu. Vous pouvez supprimer toutes vos données à tout moment depuis l'application. L'application n'effectue que les **communications réseau minimales** nécessaires à la facturation (StoreKit sur iOS / RevenueCat sur Android) et aux publicités Google AdMob, et ces informations n'incluent jamais ce que vous avez dit (les publicités sont désactivées avec KUU+). L'utilisation est mesurée pour améliorer la qualité, mais cela n'inclut jamais non plus ce que vous avez dit (sur iOS, c'est l'utilisateur qui doit l'activer ; sur Android, des mesures sans contenu sont envoyées par défaut — voir l'article 14).

---

## Article 1 (Principes de base)

KUU (ci-après « l'Application ») est une application qui vous aide à externaliser et organiser vos pensées en les exprimant à voix haute. Elle est disponible sur **iOS (iPhone et Apple Watch) et Android**, et la présente politique s'applique à toutes ces versions. L'Application ne traite les informations que dans la mesure minimale nécessaire pour fournir ses fonctionnalités, en accordant la priorité à la protection de la vie privée de l'utilisateur.

## Article 2 (Informations collectées et stockées)

L'Application ne traite que les informations suivantes :

1.  **Contenu audio que vous enregistrez** — L'audio enregistré est stocké temporairement dans une zone locale de l'appareil, uniquement pendant le processus de transcription. Il est supprimé immédiatement après le traitement. Il n'est jamais envoyé à un serveur. **La version Apple Watch de l'application n'effectue aucun enregistrement** (voir l'article 3).
2.  **Texte transcrit et organisé** — Il est sauvegardé pour que vous puissiez le consulter (iOS : sur votre appareil et dans votre base de données privée iCloud ; Android : sur l'appareil uniquement. Sur une Apple Watch jumelée, seuls les titres récents de chaque catégorie sont stockés, à des fins d'affichage — voir l'article 4).
3.  **Paramètres de l'application** — Thème, taille du texte, état du niveau d'eau dans la tête, et autres valeurs nécessaires au fonctionnement de l'Application.

L'Application ne collecte pas de données personnelles telles que le nom, l'adresse e-mail, le numéro de téléphone, la localisation, les contacts, le calendrier, les photos ou les identifiants de l'appareil.

## Article 3 (Reconnaissance vocale et organisation par IA)

Sur iPhone (iOS) et sur les appareils Android, la **reconnaissance vocale (transcription)** est effectuée entièrement sur votre propre appareil (pour l'Apple Watch, voir la fin de cet article) :

-   Reconnaissance vocale : Utilise le framework Speech d'Apple (sur l'appareil). L'audio de votre voix n'est jamais envoyé hors de l'appareil.

L'**organisation par IA (catégorisation)** utilise une IA externe :

-   Seul le **texte de ce que vous avez dit (le transcript)** est envoyé. Votre voix n'est jamais envoyée.
-   Il est envoyé à une IA externe dans le cloud (Gemini de Google via le backend du développeur), relayé par le serveur du développeur.
-   Le texte envoyé est **uniquement utilisé pour la catégorisation et n'est jamais stocké**. Il n'est pas non plus utilisé pour entraîner l'IA.
-   Ce qui est envoyé inclut non seulement ce que vous avez dit et transcrit, mais aussi tout ce que vous avez tapé ou modifié à la main. Si l'attribution automatique de thèmes (KUU+, optionnelle) est activée, les titres, textes et noms de thèmes des éléments sauvegardés sont également envoyés à des fins d'attribution (tous sont uniquement utilisés pour la classification et ne sont pas stockés).
-   **Sur iOS**, les versions de l'Application antérieures à la 2.3.0 vous permettent de choisir une classification uniquement sur l'appareil via « Sur l'appareil » dans les Réglages (cette option n'est plus proposée à partir de la version 2.3.0).

**Concernant la version Android :** La version Android ne propose pas d'organisation s'effectuant uniquement sur l'appareil. Lorsque vous organisez, le texte transcrit est **toujours** envoyé à l'IA externe (Gemini de Google via notre backend). Seul le texte transcrit est envoyé — votre voix elle-même n'est jamais envoyée, et le texte envoyé est utilisé uniquement pour la catégorisation, n'est ni stocké ni utilisé pour entraîner l'IA. La transcription (reconnaissance vocale) elle-même s'exécute entièrement sur l'appareil.

**Concernant la version Apple Watch :** La version Apple Watch de l'Application n'effectue ni enregistrement audio ni reconnaissance vocale elle-même. Pour la saisie, elle utilise l'entrée de texte standard de watchOS (au choix de l'utilisateur : dictée, griffonnage ou clavier), et l'Application ne reçoit que le texte qui en résulte. Lorsque vous choisissez la dictée, la reconnaissance vocale est effectuée en tant que fonctionnalité d'Apple (watchOS) ; son traitement — y compris si cela se produit sur l'appareil ou sur les serveurs d'Apple — dépend de votre appareil, de vos réglages et de votre langue, et est **régi par la politique de confidentialité d'Apple**. L'Application ne peut pas accéder à cet audio, ne le reçoit jamais et ne le stocke jamais. Le texte résultant est traité exactement comme le texte que vous auriez dicté sur iPhone (organisation par IA selon cet article ; stockage selon l'article 4).

## Article 4 (Stockage et synchronisation)

**iOS :** L'Application stocke le texte transcrit et organisé dans votre **base de données privée iCloud** (CloudKit Private Database). Il s'agit d'un stockage fourni par Apple auquel vous seul pouvez accéder. Le développeur ne peut ni visualiser ni récupérer aucun contenu stocké. L'utilisation d'iCloud est soumise à la politique de confidentialité d'Apple.

**Android :** Le texte transcrit et organisé est stocké **sur cet appareil uniquement**. Il n'y a pas de synchronisation automatique dans le cloud. Lors d'un changement d'appareil, vous pouvez exporter les données dans un fichier depuis « Voix et données » dans l'Application et l'importer sur le nouvel appareil. Vous choisissez où le fichier est sauvegardé (sur l'appareil, dans votre application de stockage cloud, etc.). Le développeur ne peut pas accéder à ce fichier.

**Apple Watch :** À des fins d'affichage, une partie de votre texte organisé (les titres récents de chaque catégorie) est transférée à votre Apple Watch jumelée via la communication d'appareil à appareil d'Apple (Watch Connectivity) et est **également stockée sur la montre**. Le texte que vous saisissez sur l'Apple Watch est transféré à votre iPhone de la même manière. Aucun serveur du développeur n'est impliqué dans ce transfert ou ce stockage.

## Article 5 (Finalité de l'utilisation)

Les informations traitées sont utilisées uniquement pour :

1.  Générer des transcriptions à partir de votre voix et vous les afficher
2.  Catégoriser les transcriptions en « À voir maintenant / À voir plus tard / À laisser reposer / À lâcher » et les afficher
3.  Stocker et afficher ce que vous avez dit pour que vous puissiez le consulter
4.  Conserver les paramètres nécessaires au fonctionnement de l'application

## Article 6 (Utilisation de services externes)

L'Application utilise les services externes suivants pour fournir ses fonctionnalités. **L'audio de votre voix n'est envoyé à aucun d'entre eux.**

-   **iCloud / CloudKit** (iOS uniquement. Fourni par Apple. Stockage et synchronisation uniquement dans votre propre base de données privée)
-   **Reconnaissance vocale** (iOS : framework Speech d'Apple ; Android : moteur de reconnaissance vocale de l'appareil. Les deux s'exécutent sur l'appareil ; votre voix n'est jamais envoyée hors de l'appareil. **La version Apple Watch n'effectue pas de reconnaissance vocale au sein de l'application et utilise la saisie standard de watchOS** — voir l'article 3.)
-   **Saisie de texte standard de watchOS** (Apple Watch uniquement. Fourni par Apple. Votre choix de dictée, griffonnage ou clavier. Lorsque vous choisissez la dictée, la reconnaissance vocale est effectuée en tant que fonctionnalité d'Apple et est régie par la politique de confidentialité d'Apple. L'Application ne peut pas accéder à cet audio. Voir l'article 3.)
-   **Watch Connectivity** (Apple Watch uniquement. Fourni par Apple. Transfère directement le texte d'affichage entre votre iPhone et votre Apple Watch. Aucun serveur du développeur n'est impliqué. Voir l'article 4.)
-   **Une IA externe dans le cloud** (Organisation par IA. Seul le texte de ce que vous avez dit est envoyé ; utilisé uniquement pour la catégorisation, jamais stocké, jamais utilisé pour l'entraînement de l'IA. Voir l'article 3.)
-   **Services de facturation** (iOS : **Apple StoreKit** ; Android : **RevenueCat**. Achat, renouvellement, annulation et gestion des droits de l'abonnement KUU+. Aucun contenu parlé n'est envoyé. Pour RevenueCat, voir l'article 7 et la [politique de confidentialité de RevenueCat](https://www.revenuecat.com/privacy).)
-   **API Play Integrity (via Firebase App Check ; Android uniquement)** (Vérifie que les requêtes à l'API de classification proviennent d'une application légitime — une attestation d'intégrité de l'appareil/application. Ne contient aucun contenu parlé ni aucune information identifiant l'utilisateur.)
-   **Google AdMob (SDK Google Mobile Ads)** (Uniquement lorsque KUU+ n'est pas actif : un emplacement publicitaire natif entre les sections de l'écran « Ce que vous avez dit ». Aucun contenu parlé n'est envoyé. Voir l'article 13.)
-   **Firebase Analytics** (Fourni par Google. Pour l'amélioration de la qualité de l'application. Sur iOS, **utilisé uniquement si vous l'activez explicitement via les Réglages** ; sur Android, des événements d'utilisation sans contenu sont envoyés **par défaut** (dans les deux cas, aucun contenu parlé n'est envoyé). iOS utilise également **Crashlytics** sur activation, mais **la version Android n'inclut pas Crashlytics**. Voir l'article 14.)

L'Application exploite un serveur minimal et sans état (stateless) uniquement pour relayer les requêtes d'organisation par IA (aucun contenu n'est stocké). Elle n'utilise pas de services d'authentification nécessitant des comptes personnels.

## Article 7 (Divulgation à des tiers)

Le développeur n'a aucun moyen d'accéder à votre contenu parlé, à vos transcriptions ou à vos résultats organisés, et ne les divulgue à aucun tiers.

Pour diffuser des publicités aux utilisateurs non abonnés à KUU+, l'Application envoie à Google les informations requises par Google AdMob pour la diffusion publicitaire — y compris les identifiants de l'appareil, l'identifiant publicitaire, la langue et la région de l'appareil, la localisation approximative et les données d'interaction avec la publicité (voir l'article 13 ; la politique de confidentialité de Google AdMob s'applique). Lorsque KUU+ est actif, cette transmission n'a pas lieu.

Lorsque vous vous abonnez à KUU+ sur la version **Android**, les informations d'achat (ID du produit, prix, date d'achat, etc.) sont envoyées à RevenueCat, Inc. pour gérer l'achat et votre droit d'accès (actif/inactif). Aucun contenu parlé n'est envoyé. Pour plus de détails sur le traitement des données par RevenueCat, consultez la [politique de confidentialité de RevenueCat](https://www.revenuecat.com/privacy).

Les informations ne seront divulguées que dans les cas où la loi l'exige, conformément aux procédures légales établies.

## Article 8 (Suppression des données)

Vous pouvez supprimer toutes vos données à tout moment depuis « Réglages → Voix et données → Supprimer ce qui est stocké » à l'intérieur de l'Application. Cette action supprime de manière permanente les données sur l'appareil (et, sur iOS, également dans la base de données privée iCloud). Les données supprimées ne peuvent pas être récupérées.

La désinstallation de l'Application supprime les données locales. Sur iOS, les données iCloud peuvent être supprimées via Réglages → Identifiant Apple → iCloud → Gérer le stockage. La version Android ne stockant les données que sur l'appareil, celles-ci sont supprimées lors de la désinstallation.

**Apple Watch :** Lorsque vous supprimez toutes les données, les données d'affichage déjà transférées sur votre Apple Watch sont remplacées par un contenu vide lors de la prochaine connexion de la montre. La suppression de l'application de votre Apple Watch supprime également les données d'affichage qui y sont stockées.

## Article 9 (Mesures de sécurité)

-   **iOS :** Les fichiers audio temporaires pendant l'enregistrement sont chiffrés par la protection des fichiers d'iOS (`FileProtectionType.complete`) et sont inaccessibles lorsque l'appareil est verrouillé. La communication avec iCloud est chiffrée par Apple via SSL/TLS.
-   **Android :** L'audio enregistré n'est jamais écrit sur le disque, même en tant que fichier temporaire ; il est traité uniquement en mémoire et supprimé immédiatement après la reconnaissance. Les transcriptions et résultats organisés stockés se trouvent dans l'espace de stockage privé de l'application, inaccessible aux autres applications, et sont exclus de la sauvegarde automatique dans le cloud d'Android.
-   **Apple Watch :** Le transfert entre votre iPhone et votre Apple Watch est géré par Watch Connectivity d'Apple et ne transite par aucun serveur du développeur. Ce qui est stocké sur l'Apple Watch est limité au texte d'affichage (les titres récents de chaque catégorie) ; aucun audio n'est stocké.
-   Toute communication avec l'IA externe est chiffrée (HTTPS/TLS). Le serveur du développeur ne fait que relayer les requêtes d'organisation et ne stocke aucun contenu (sans état).

## Article 10 (Utilisation par des mineurs)

L'Application est classée 4+, mais sa nature (organisation de pensées) suppose que l'utilisateur sache lire et écrire. Les mineurs doivent utiliser l'Application avec le consentement de leur tuteur légal.

## Article 11 (Modifications de cette politique)

Cette politique peut être mise à jour en raison de changements législatifs, de l'ajout de fonctionnalités, ou de modifications des spécifications des frameworks ou politiques de chaque plateforme (Apple / Google). Les changements importants seront annoncés via une mise à jour de l'application ou sur la page publique de cette politique.

## Article 12 (Contact)

Pour toute question concernant cette politique, veuillez nous contacter via la section « Développeur » sur la page de l'Application dans l'App Store ou Google Play, ou via « Réglages → Contact » à l'intérieur de l'Application.

## Article 13 (Publicités et App Tracking Transparency)

Lorsque vous n'êtes pas abonné à KUU+, l'Application affiche un seul emplacement publicitaire natif, fourni par Google AdMob, entre les sections de l'écran « Ce que vous avez dit ». Les publicités sont présentées de manière discrète pour s'intégrer à l'univers de KUU.

-   **Votre contenu parlé n'est jamais utilisé à des fins publicitaires.** Les publicités ne consultent pas vos transcriptions, vos résultats organisés ou vos thèmes.
-   Pour la diffusion des publicités, Google AdMob peut collecter des identifiants d'appareil (y compris l'IDFA), un identifiant publicitaire, une localisation approximative, des diagnostics et des données d'interaction avec le produit (interactions avec les publicités au sein de l'Application).
-   **iOS :** Une demande d'**App Tracking Transparency** (ATT) est affichée une seule fois, juste avant la première publicité. Les publicités seront toujours affichées si vous refusez, mais les informations envoyées à Google seront limitées (non personnalisées). Vous pouvez modifier l'autorisation ATT à tout moment dans « Réglages → Confidentialité et sécurité → Suivi » sur iOS.
-   **Android :** L'ATT est un mécanisme exclusif à iOS et n'existe pas sur Android. C'est l'**identifiant publicitaire** de Google qui est utilisé pour la diffusion des publicités. Vous pouvez désactiver la personnalisation des publicités ou réinitialiser votre identifiant publicitaire depuis les « Paramètres → Confidentialité → Annonces » de votre appareil (la formulation varie selon l'appareil et la version d'Android). La version Android se conforme également à la gestion du consentement (UMP) affichée dans les régions concernées, comme l'UE.
-   **L'abonnement à KUU+ arrête toutes les publicités et la transmission de données qui y est liée.**
-   Pour plus de détails sur le traitement des données par AdMob, consultez la [politique de confidentialité de Google AdMob](https://support.google.com/admob/answer/6128543).

## Article 14 (Utilisation de Firebase Analytics / Crashlytics)

**Le modèle d'activation volontaire (opt-in) décrit dans cet article s'applique à la version iOS. Pour la version Android, veuillez consulter la section « Concernant la version Android » à la fin de cet article.**

**Sur iOS**, pour l'amélioration de la qualité de l'application et la détection immédiate des incidents en production, l'Application peut utiliser Firebase Analytics de Google (agrégation de l'utilisation) et Firebase Crashlytics (rapports de plantage). **Cette fonctionnalité est DÉSACTIVÉE par défaut (aucune donnée envoyée) et ne fonctionne que si vous l'activez explicitement via « Réglages → Données et diagnostics ».**

-   **Informations envoyées** :
    -   Un ID d'installation anonymisé émis automatiquement par Firebase (dérivé de l'IDFV ; ce n'est pas un identifiant personnel direct)
    -   Des signaux agrégés d'événements dans l'application (achèvement d'une session d'enregistrement, affichage/conversion du paywall, fin de l'onboarding, etc. Les valeurs numériques sont regroupées avec une granularité grossière.)
    -   Les traces de pile de plantage (symbolisées) lorsque l'Application se termine anormalement
-   **Informations qui ne sont pas envoyées** : Le contenu que vous avez dit (audio), les transcriptions, le texte des résultats organisés par l'IA et les noms de thèmes que vous définissez sont rendus **inenyoyables au niveau du type de donnée** (l'API de l'implémentation empêche de passer des valeurs de type chaîne de caractères au SDK d'analyse).
-   **Tant que la fonctionnalité n'est pas activée, aucune communication avec Firebase n'a lieu** (y compris pour toutes les catégories ci-dessus).
-   **Comment arrêter l'envoi** : Vous pouvez désactiver le bouton dans « Réglages → Données et diagnostics » à tout moment. Une fois désactivé, les ID d'installation passés sont supprimés et tous les journaux de plantage non envoyés et stockés sur l'appareil sont également supprimés.
-   Le destinataire est Google LLC (États-Unis). La [politique de confidentialité de Firebase de Google](https://firebase.google.com/support/privacy) s'applique.

**Concernant la version Android :** La version Android utilise Firebase Analytics pour envoyer des **événements d'utilisation sans contenu** à des fins d'amélioration du produit (valeurs groupées telles que les transitions d'écran et le nombre d'utilisations de fonctionnalités) ainsi qu'un ID d'instance d'application anonyme émis par Firebase. **Contrairement à iOS, cette fonction est activée par défaut.** Le contenu que vous avez dit (audio), les transcriptions, le texte des résultats organisés et les noms de thèmes **ne peuvent pas être envoyés** — l'API du SDK d'analyse est conçue de manière à ce que des valeurs de type chaîne de caractères ne puissent pas lui être transmises. **La version Android n'inclut pas Crashlytics et n'envoie aucun rapport de plantage.** Le destinataire est Google LLC (États-Unis) ; la [politique de confidentialité de Firebase de Google](https://firebase.google.com/support/privacy) s'applique.
