> Esta es una traducción de referencia para su comodidad. La versión japonesa es el texto de referencia.

# Política de privacidad de KUU

Última actualización: 21 de julio de 2026

**En resumen:** Lo que usted dice es suyo. **Su voz nunca se envía fuera de su dispositivo**. La transcripción se realiza en su dispositivo. La organización (clasificación por IA) utiliza una IA externa, pero solo se envía el texto transcrito, se utiliza únicamente para la organización y no se almacena (en la versión para iOS, puede cambiar a la organización solo en el dispositivo a través de la opción «En el dispositivo» en los ajustes; **la versión para Android solo envía a la IA externa, no dispone de organización en el dispositivo**). Los datos se guardan en su dispositivo y, en la versión para iOS, también en su base de datos privada de iCloud (la versión para Android solo guarda en el dispositivo). El desarrollador no almacena su contenido ni puede ver lo que se recibe. Puede eliminar todos los datos desde la aplicación en cualquier momento. La aplicación realiza únicamente las **comunicaciones mínimas necesarias** para la facturación (StoreKit en iOS / RevenueCat en Android) y los anuncios de Google AdMob, y esa información nunca incluye lo que usted ha dicho (los anuncios se desactivan con la suscripción a KUU+). Se mide el uso para mejorar la calidad, pero esto tampoco incluye nunca lo que usted ha dicho (en iOS es con consentimiento explícito del usuario; en Android, la medición sin contenido se realiza por defecto; consulte el Artículo 14).

---

## Artículo 1 (Principios básicos)

Esta aplicación, «KUU» (en adelante, «esta Aplicación»), es una aplicación que le ayuda a sacar los pensamientos de su cabeza expresándolos en voz alta y organizándolos. Existen **versiones para iOS y Android**, y esta política se aplica a ambas. Esta Aplicación maneja la información únicamente en la medida mínima necesaria para proporcionar sus funciones, priorizando la protección de la privacidad del usuario.

## Artículo 2 (Información recopilada y almacenada)

La información que maneja esta Aplicación se limita a lo siguiente:

1.  **Contenido hablado por el usuario (datos de audio)** — El audio grabado se almacena temporalmente en un área local del dispositivo solo durante el proceso de transcripción y se elimina inmediatamente después de que finalice el procesamiento. No se envía a ningún servidor.
2.  **Resultados de la transcripción y organización (texto)** — Se guardan para que usted pueda revisarlos (en la versión para iOS, en el dispositivo y en su base de datos privada de iCloud; en la versión para Android, solo en el dispositivo; consulte el Artículo 4).
3.  **Ajustes de la aplicación** — Valores de configuración necesarios para el funcionamiento de la aplicación, como el tema, el tamaño del texto y el estado del nivel de agua en la cabeza.

Esta Aplicación no recopila información personal como nombre, dirección de correo electrónico, número de teléfono, información de ubicación, contactos, calendario, fotos o identificadores de dispositivo.

## Artículo 3 (Reconocimiento de voz y clasificación por IA)

El **reconocimiento de voz (transcripción)** se realiza íntegramente en su dispositivo iOS.

-   Reconocimiento de voz: Utiliza el framework Speech de Apple (en el dispositivo). El audio en sí nunca se envía fuera del dispositivo.

La **clasificación por IA (categorización)** utiliza una IA externa.

-   Solo se envía el **contenido textual (el texto transcrito)**. El audio no se envía.
-   El destino es una IA externa, a través del servidor del desarrollador (que a su vez se comunica con Gemini de Google a través de nuestro backend).
-   El contenido enviado se **utiliza únicamente para la clasificación y no se almacena**. Tampoco se utiliza para el entrenamiento de la IA.
-   En la **versión para iOS**, puede cambiar en cualquier momento a la **clasificación solo en el dispositivo** (FoundationModels de Apple / reglas en el dispositivo) desde la opción «En el dispositivo» en los ajustes. En este caso, el texto tampoco sale del dispositivo.

**Acerca de la versión para Android:** La versión para Android no ofrece un método de organización (clasificación) que se complete únicamente en el dispositivo. Al organizar, el texto transcrito se envía **siempre** a la IA externa (Gemini de Google a través de nuestro backend). No existe la opción de cambiar a «En el dispositivo» como en la versión para iOS. Solo se envía el contenido textual; el audio en sí no se envía, y el texto enviado se utiliza únicamente para la clasificación, no se almacena ni se usa para el entrenamiento de la IA. La transcripción (reconocimiento de voz) en sí se completa dentro del dispositivo.

## Artículo 4 (Almacenamiento y sincronización)

**Versión para iOS:** Los resultados de la transcripción y organización se almacenan únicamente en su **base de datos privada de iCloud** (CloudKit Private Database). Este es un almacenamiento proporcionado por Apple al que solo usted puede acceder. El desarrollador de esta Aplicación no puede ver ni obtener el contenido almacenado. El uso de iCloud está sujeto a la política de privacidad de Apple.

**Versión para Android:** Los resultados de la transcripción y organización se almacenan **únicamente en este dispositivo**. No se realiza una sincronización automática en la nube. Al cambiar de dispositivo, puede exportar los datos a un archivo desde «Voz y datos» en la aplicación e importarlos en el nuevo dispositivo. Usted elige dónde guardar el archivo (en el dispositivo, en su aplicación de almacenamiento en la nube, etc.). El desarrollador no puede acceder a este archivo.

## Artículo 5 (Finalidad del uso)

La información manejada se utiliza únicamente para los siguientes fines:

1.  Generar transcripciones a partir de la voz y mostrárselas al usuario.
2.  Clasificar las transcripciones en «Ver ahora / Pensar después / Reposar / Soltar» y mostrárselas al usuario.
3.  Almacenar y mostrar el contenido hablado previamente por el usuario para que pueda revisarlo.
4.  Mantener los valores de configuración necesarios para el funcionamiento de la aplicación.

## Artículo 6 (Uso de servicios externos)

Esta Aplicación utiliza los siguientes servicios externos para proporcionar sus funciones. **El audio en sí no se envía a ninguno de estos servicios**.

-   **iCloud / CloudKit** (solo en la versión para iOS. Proporcionado por Apple. Almacenamiento y sincronización solo en su propia base de datos privada).
-   **Reconocimiento de voz** (en la versión para iOS, el framework Speech de Apple; en la versión para Android, el motor de reconocimiento de voz del dispositivo. Ambos se ejecutan en el dispositivo y el audio no se envía fuera de él).
-   **IA externa (nube)** (Clasificación por IA. Solo se envía el contenido textual. Se utiliza únicamente para la clasificación, no se almacena ni se usa para el entrenamiento de la IA. En la versión para iOS se puede desactivar desde «En el dispositivo» en los ajustes, pero **la versión para Android solo envía a la IA externa**. Consulte el Artículo 3).
-   **FoundationModels** (solo en la versión para iOS. Proporcionado por Apple. Se ejecuta completamente en el dispositivo. Se utiliza cuando la opción «En el dispositivo» está activada o como alternativa cuando la IA externa no está disponible).
-   **Servicios de facturación** (en la versión para iOS, **Apple StoreKit**; en la versión para Android, **RevenueCat**. Para la compra, renovación, cancelación y gestión del estado de la suscripción a KUU+. No se envía el contenido hablado. Para RevenueCat, consulte el Artículo 7 y la [política de privacidad de RevenueCat](https://www.revenuecat.com/privacy)).
-   **Play Integrity API (a través de Firebase App Check. Solo en la versión para Android)** (Atestación de la integridad del dispositivo y la aplicación para confirmar que las solicitudes a la API de clasificación provienen de una aplicación legítima. No contiene el contenido hablado ni información que identifique al usuario).
-   **Google AdMob (SDK de Google Mobile Ads)** (Solo cuando no se está suscrito a KUU+, muestra un anuncio nativo en la pantalla «Lo que has dicho». No se envía el contenido hablado. Consulte el Artículo 13).
-   **Firebase Analytics** (Proporcionado por Google. Para la mejora de la calidad de la aplicación. En la versión para iOS, **solo si el usuario lo activa explícitamente en los Ajustes**; en la versión para Android, se envían eventos de uso sin contenido **por defecto** (en ningún caso se envía el contenido hablado). La versión para iOS también utiliza **Crashlytics** si el usuario lo activa, pero **la versión para Android no incluye Crashlytics**. Consulte el Artículo 14).

El servidor de esta Aplicación es mínimo y solo actúa como intermediario para la clasificación por IA, sin almacenar ningún contenido (es *stateless*). No se utilizan servicios de autenticación que requieran cuentas personales.

## Artículo 7 (Cesión a terceros)

El desarrollador de esta Aplicación no tiene medios para acceder al contenido hablado por el usuario, a los resultados de la transcripción o a los resultados de la organización, y no los cederá a terceros.

Con el fin de mostrar publicidad a los usuarios no suscritos a KUU+, se enviará a Google información que Google AdMob requiere para la publicación de anuncios, como identificadores de dispositivo, ID de publicidad, idioma y región del dispositivo, ubicación aproximada e información sobre la interacción con los anuncios (consulte el Artículo 13; se aplica la política de privacidad de AdMob de Google). Mientras esté suscrito a KUU+, este envío de información no se producirá.

Al suscribirse a KUU+ en la **versión para Android**, la información de la compra (ID del producto, precio, fecha de compra, etc.) se enviará a RevenueCat, Inc. para gestionar el proceso de compra y el estado de la suscripción (activa/inactiva). No se envía el contenido hablado. Para más detalles sobre el manejo de datos de RevenueCat, consulte la [política de privacidad de RevenueCat](https://www.revenuecat.com/privacy).

Solo se divulgará información si así lo exige la ley, siguiendo los procedimientos establecidos.

## Artículo 8 (Eliminación de datos)

El usuario puede eliminar todos los datos en cualquier momento desde «Ajustes → Voz y datos → Eliminar lo guardado» dentro de la aplicación. Esta acción borrará permanentemente los datos del dispositivo (y, en la versión para iOS, también los datos de la base de datos privada de iCloud). Los datos eliminados no se pueden recuperar.

Al desinstalar esta Aplicación, se eliminarán los datos del dispositivo. En la versión para iOS, los datos de iCloud se pueden eliminar desde los ajustes de Apple (Ajustes → ID de Apple → iCloud → Gestionar almacenamiento de la cuenta). En la versión para Android, como los datos solo se guardan en el dispositivo, se eliminan al desinstalar la aplicación.

## Artículo 9 (Medidas de seguridad)

-   **Versión para iOS**: Los archivos de audio temporales durante la grabación están cifrados por la protección de archivos de iOS (`FileProtectionType.complete`) y son inaccesibles mientras el dispositivo está bloqueado. La comunicación con iCloud es cifrada por Apple mediante SSL/TLS.
-   **Versión para Android**: El audio grabado no se escribe en el disco, ni siquiera como archivo temporal; se procesa únicamente en la memoria y se descarta inmediatamente después del reconocimiento. Los resultados de la transcripción y organización guardados se almacenan en el área privada de la aplicación en Android, inaccesible para otras aplicaciones, y se excluyen de la copia de seguridad automática en la nube de Android.
-   Toda la comunicación con la IA externa está cifrada (HTTPS/TLS). El servidor del desarrollador solo actúa como intermediario para la clasificación y no almacena contenido (es *stateless*).

## Artículo 10 (Uso por menores de edad)

Esta Aplicación tiene una clasificación de edad de 4+, pero debido a su naturaleza de organización de pensamientos, se asume que será utilizada por personas con capacidad de leer y escribir. Si un menor de edad utiliza la aplicación, debe hacerlo con el consentimiento de sus padres o tutores.

## Artículo 11 (Modificaciones de esta política de privacidad)

Esta política puede ser revisada debido a cambios en la legislación, adición de funciones o cambios en las especificaciones de los frameworks o políticas de cada plataforma (Apple / Google). En caso de cambios importantes, se notificará en la actualización de la aplicación o en la página pública de esta política.

## Artículo 12 (Contacto)

Para consultas sobre esta política, póngase en contacto con nosotros a través de la sección «Desarrollador» en la página de la aplicación en la App Store o Google Play, o a través de «Ajustes → Contacto» dentro de la aplicación.

## Artículo 13 (Publicidad y Transparencia en el Seguimiento de Apps)

Esta Aplicación muestra un único anuncio nativo servido por Google AdMob en la pantalla «Lo que has dicho» solo durante el período en que no se está suscrito a KUU+. El anuncio en sí se muestra de forma discreta entre las secciones de la pantalla para mantener la estética de KUU.

-   **El contenido que usted habla nunca se utiliza para la publicidad** (los anuncios no consultan sus transcripciones, resultados de clasificación o temas).
-   Para la publicación de anuncios, Google AdMob puede recopilar identificadores de dispositivo (incluido el IDFA), ID de publicidad, ubicación aproximada (Coarse Location), datos de diagnóstico e interacciones con el producto (información sobre la interacción con los anuncios dentro de la aplicación).
-   **Versión para iOS**: Se mostrará una única vez un aviso de **Transparencia en el Seguimiento de Apps** (ATT) justo antes de que aparezca el primer anuncio. Los anuncios se seguirán mostrando aunque el usuario no dé su consentimiento, pero la información enviada a Google será limitada (sin personalización). El estado del consentimiento de ATT se puede cambiar en cualquier momento en «Ajustes» → «Privacidad y seguridad» → «Seguimiento» de iOS.
-   **Versión para Android**: ATT es un mecanismo exclusivo de iOS y no existe en Android. En su lugar, se utiliza el **ID de publicidad** de Google para la publicación de anuncios. Puede optar por no recibir anuncios personalizados o restablecer su ID de publicidad desde los «Ajustes → Privacidad → Anuncios» de su dispositivo (la redacción puede variar según el dispositivo y la versión de Android). Además, la versión para Android cumple con la gestión de consentimiento (UMP) que se muestra en las regiones aplicables, como la UE.
-   **Al suscribirse a KUU+, se detienen todos los anuncios y el envío de datos relacionado con ellos**.
-   Para más detalles sobre el manejo de datos por parte de Google AdMob, consulte la [política de privacidad de Google AdMob](https://support.google.com/admob/answer/6128543).

## Artículo 14 (Uso de Firebase Analytics / Crashlytics)

**El modelo de consentimiento explícito (opt-in) de este artículo se aplica a la versión para iOS. Para la versión para Android, consulte la sección «Acerca de la versión para Android» al final de este artículo.**

La **versión para iOS** puede utilizar Firebase Analytics de Google (para agregar datos de uso) y Firebase Crashlytics (para informes de fallos) con el fin de mejorar la calidad de la aplicación y detectar incidentes en producción de inmediato. **Esta función está DESACTIVADA por defecto (no se envían datos) y solo se activa si el usuario da su consentimiento explícito en «Ajustes → Datos y diagnóstico».**

-   **Información enviada**:
    -   Un ID de instalación anonimizado emitido automáticamente por Firebase (basado en el IDFV; no es un identificador que identifique personalmente al usuario de forma directa).
    -   Señales agregadas de eventos de interacción dentro de la aplicación (eventos para agregar datos como la finalización de sesiones de grabación, visualizaciones y conversiones de la pantalla de pago, finalización del onboarding, etc. Los valores numéricos se envían con una granularidad aproximada y agrupada).
    -   Trazas de la pila de llamadas (*stack traces*) simbolizadas cuando la aplicación se cierra de forma inesperada.
-   **Información que no se envía**: El contenido hablado (audio), los resultados de la transcripción, el texto de los resultados de la clasificación por IA y los nombres de los temas configurados por el usuario están **diseñados a nivel de tipo para que no puedan ser enviados** (la implementación de la API impide pasar valores de tipo cadena de texto al SDK de análisis).
-   **Mientras el consentimiento no esté activado, no se produce ninguna comunicación con Firebase en absoluto**, incluyendo toda la información mencionada anteriormente.
-   **Cómo detener el envío**: Puede desactivar el interruptor en «Ajustes → Datos y diagnóstico» en cualquier momento. Al desactivarlo, se descartan los ID de instalación anteriores y se eliminan los informes de fallos no enviados que estuvieran guardados localmente en el dispositivo.
-   El destinatario es Google LLC (Estados Unidos). Se aplica la [Información de privacidad de Firebase](https://firebase.google.com/support/privacy) de Google.

**Acerca de la versión para Android:** La versión para Android utiliza Firebase Analytics para enviar **eventos de uso sin contenido** para la mejora del producto (valores agrupados como transiciones de pantalla y recuentos de uso de funciones) y un ID de instancia de la aplicación anónimo emitido por Firebase. **A diferencia de la versión para iOS, esta función está activada por defecto.** El contenido hablado (audio), las transcripciones, el texto de los resultados de la organización y los nombres de los temas **no pueden ser enviados**, ya que la API del SDK de análisis está diseñada para no poder pasar valores de tipo cadena de texto. **La versión para Android no incluye Crashlytics y no envía informes de fallos.** El destinatario es Google LLC (Estados Unidos); se aplica la [Información de privacidad de Firebase](https://firebase.google.com/support/privacy) de Google.
