> Esta es una traducción de referencia para su comodidad. La versión en japonés es el texto autoritativo.

# Política de privacidad de KUU

Última actualización: 2 de agosto de 2026

**En resumen:** Lo que usted dice es suyo. **La aplicación nunca envía el audio de su voz al exterior**. En dispositivos iPhone y Android, la transcripción también se realiza en el propio dispositivo. **La versión de la aplicación para Apple Watch no realiza grabaciones**; solo recibe el texto producido por los métodos de entrada estándar de watchOS (dictado, escritura a mano o teclado). Cuando elige el dictado, el reconocimiento de voz lo realiza el sistema de Apple (consulte el Artículo 3). Para la organización se utiliza una IA externa, pero solo se envía el contenido transcrito en texto. Este se utiliza únicamente para la organización y no se almacena. El contenido se guarda en su dispositivo y, en la versión de iOS, también en su base de datos privada de iCloud (la versión de Android solo guarda en el dispositivo). El desarrollador no almacena su contenido ni puede ver lo que se recibe. Puede eliminar todos sus datos desde la aplicación en cualquier momento. La aplicación solo realiza las **comunicaciones mínimas necesarias** para la facturación (StoreKit en iOS / RevenueCat en Android) y los anuncios de Google AdMob. Dicha información nunca incluye lo que usted ha dicho (los anuncios se desactivan con la suscripción a KUU+). Se mide el uso para mejorar la calidad, pero esta medición tampoco incluye lo que usted ha dicho (en iOS es opcional para el usuario; en Android se realiza por defecto una medición sin contenido; consulte el Artículo 14).

---

## Artículo 1 (Principios básicos)

La aplicación «KUU» (en adelante, «la aplicación») está diseñada para ayudarle a exteriorizar y organizar sus pensamientos hablándolos en voz alta. Existen versiones para **iOS (iPhone y Apple Watch) y Android**, y esta política se aplica a todas ellas. La aplicación gestiona la información en la medida mínima necesaria para ofrecer sus funciones, dando la máxima prioridad a la protección de la privacidad del usuario.

## Artículo 2 (Información recopilada y almacenada)

La información que gestiona la aplicación se limita a lo siguiente:

1.  **El contenido de lo que usted dice (datos de audio)** — El audio grabado se almacena temporalmente en un área del dispositivo solo durante el proceso de transcripción, y se elimina inmediatamente después de finalizar dicho proceso. No se envía a ningún servidor. **La versión de la aplicación para Apple Watch no realiza grabaciones** (consulte el Artículo 3).
2.  **Resultados de la transcripción y organización (texto)** — Se guardan para que usted pueda consultarlos (en la versión de iOS, en el dispositivo y en su base de datos privada de iCloud; en la versión de Android, solo en el dispositivo. En un Apple Watch enlazado, solo se guardan los títulos recientes de cada categoría para su visualización; consulte el Artículo 4).
3.  **Ajustes de la aplicación** — El tema, el tamaño del texto, el estado del nivel de agua mental y otros valores de configuración necesarios para el funcionamiento de la aplicación.

La aplicación no recopila datos personales como nombre, dirección de correo electrónico, número de teléfono, ubicación, contactos, calendario, fotos o identificadores de dispositivo.

## Artículo 3 (Reconocimiento de voz y clasificación con IA)

En iPhone (versión de iOS) y en dispositivos Android, el **reconocimiento de voz (transcripción)** se realiza íntegramente en su propio dispositivo (para la versión de Apple Watch, consulte el final de este artículo).

-   Reconocimiento de voz: Se utiliza el framework Speech de Apple (en el dispositivo). El audio de su voz nunca se envía fuera del dispositivo.

La **clasificación con IA (categorización)** utiliza una IA externa.

-   Solo se envía **el contenido en texto (el texto transcrito)**. El audio de su voz no se envía.
-   El destino es una IA externa, a través del servidor del desarrollador (backend que se comunica con Gemini de Google).
-   El contenido enviado se **utiliza únicamente para la clasificación y no se almacena**. Tampoco se utiliza para el entrenamiento de la IA.
-   El contenido enviado incluye no solo lo que ha hablado y se ha transcrito, sino también lo que ha introducido o editado manualmente. Si la asignación automática de temas (KUU+, opcional) está activada, también se envían los títulos, el cuerpo del texto y los nombres de los temas de los elementos ya guardados para realizar la asignación (en todos los casos, se utilizan únicamente para la clasificación y no se almacenan).
-   En la **versión de iOS**, las versiones de la aplicación anteriores a la 2.3.0 permitían elegir una clasificación exclusiva en el dispositivo a través del ajuste «En el dispositivo» (este ajuste dejó de ofrecerse a partir de la versión 2.3.0).

**Acerca de la versión de Android:** La versión de Android no ofrece un método de organización (clasificación) que se complete únicamente en el dispositivo. Al organizar, el texto transcrito se envía **siempre** a la IA externa (Gemini de Google a través de nuestro backend). Únicamente se envía el contenido en texto; la voz en sí nunca se envía, y el texto enviado se utiliza exclusivamente para la clasificación, no se almacena ni se usa para el entrenamiento de la IA. La transcripción (reconocimiento de voz) sí se realiza íntegramente en el dispositivo.

**Acerca de la versión para Apple Watch:** La versión de la aplicación para Apple Watch no graba audio ni realiza el reconocimiento de voz por sí misma. Para la entrada de datos, utiliza la entrada de texto estándar de watchOS (a elección del usuario: dictado, escritura a mano o teclado), y la aplicación solo recibe el texto resultante. Si elige el dictado, el reconocimiento de voz lo realiza una función de Apple (watchOS); su procesamiento —incluyendo si se realiza en el dispositivo o si se envía a los servidores de Apple— depende de su modelo de dispositivo, su configuración y su idioma, y **se rige por la política de privacidad de Apple**. La aplicación no puede acceder a dicho audio y nunca lo recibe ni lo almacena. El texto resultante se trata de la misma manera que el texto hablado en el iPhone (clasificación con IA según este artículo; almacenamiento según el Artículo 4).

## Artículo 4 (Almacenamiento y sincronización)

**Versión de iOS:** Los resultados de la transcripción y la organización se almacenan únicamente en su **base de datos privada de iCloud** (CloudKit Private Database). Este es un servicio de almacenamiento proporcionado por Apple al que solo usted puede acceder. El desarrollador de la aplicación no puede ver ni obtener el contenido almacenado. Las condiciones de uso y la seguridad de iCloud se rigen por la política de privacidad de Apple.

**Versión de Android:** Los resultados de la transcripción y la organización se almacenan **únicamente en este dispositivo**. No se realiza una sincronización automática en la nube. Al cambiar de dispositivo, puede exportar los datos a un archivo desde «Voz y datos» en la aplicación e importarlos en el nuevo dispositivo. Usted elige dónde se guarda el archivo (en el dispositivo, en su aplicación de almacenamiento en la nube, etc.). El desarrollador no puede acceder a dicho archivo.

**Versión para Apple Watch:** Para su visualización, una parte de los resultados de la organización (los títulos recientes de cada categoría) se transfiere al Apple Watch enlazado mediante la comunicación entre dispositivos de Apple (Watch Connectivity) y **se almacena también en el Apple Watch**. El texto que introduce en el Apple Watch se transfiere al iPhone por el mismo mecanismo. El servidor del desarrollador no interviene en esta transferencia ni en este almacenamiento.

## Artículo 5 (Finalidad del uso)

La información gestionada se utiliza únicamente para las siguientes finalidades:

1.  Generar transcripciones a partir de su voz y mostrárselas.
2.  Clasificar las transcripciones en «Ver ahora / Pensar después / Aparcar / Soltar» y mostrárselas.
3.  Almacenar y mostrar el contenido que ha hablado previamente para que usted pueda consultarlo.
4.  Conservar los ajustes necesarios para el funcionamiento de la aplicación.

## Artículo 6 (Servicios externos utilizados)

La aplicación utiliza los siguientes servicios externos para ofrecer sus funciones. **El audio de su voz no se envía a ninguno de estos servicios**.

-   **iCloud / CloudKit** (solo en la versión de iOS; proporcionado por Apple; almacenamiento y sincronización únicamente en su propia base de datos privada).
-   **Reconocimiento de voz** (en la versión de iOS, el framework Speech de Apple; en la versión de Android, el motor de reconocimiento de voz del dispositivo; ambos se ejecutan en el dispositivo y el audio no se envía al exterior. **La versión para Apple Watch no realiza reconocimiento de voz propio, sino que utiliza la entrada estándar de watchOS**; consulte el Artículo 3).
-   **Entrada de texto estándar de watchOS** (solo en la versión para Apple Watch; proporcionado por Apple; el usuario elige entre dictado, escritura a mano o teclado. El reconocimiento de voz del dictado lo realiza una función de Apple y se rige por su política de privacidad. La aplicación no puede acceder a dicho audio; consulte el Artículo 3).
-   **Watch Connectivity** (solo en la versión para Apple Watch; proporcionado por Apple; transfiere directamente el texto para visualización entre el iPhone y el Apple Watch. El servidor del desarrollador no interviene; consulte el Artículo 4).
-   **IA externa (en la nube)** (para la clasificación con IA; solo se envía el contenido en texto; se utiliza únicamente para la clasificación, no se almacena ni se usa para el entrenamiento de la IA; consulte el Artículo 3).
-   **Servicios de facturación** (en la versión de iOS, **Apple StoreKit**; en la versión de Android, **RevenueCat**; para la compra, renovación, cancelación y gestión del estado de la suscripción a KUU+. No se envía el contenido de lo que dice. Para RevenueCat, consulte el Artículo 7 y la [política de privacidad de RevenueCat](https://www.revenuecat.com/privacy)).
-   **API Play Integrity (a través de Firebase App Check; solo en la versión de Android)** (para verificar que las solicitudes a la API de clasificación provienen de una aplicación legítima, mediante una certificación de integridad del dispositivo y la aplicación. No contiene el contenido de lo que dice ni información que identifique al usuario).
-   **Google AdMob (SDK de Google Mobile Ads)** (solo si no tiene una suscripción a KUU+; muestra un anuncio nativo entre secciones en la pantalla «Lo que has dicho». No se envía el contenido de lo que dice; consulte el Artículo 13).
-   **Firebase Analytics** (proporcionado por Google; para la mejora de la calidad de la aplicación. En la versión de iOS, **solo se utiliza si el usuario lo acepta explícitamente en los Ajustes**; en la versión de Android, se envían por **defecto** eventos de uso sin contenido (en ambos casos, no se envía el contenido de lo que dice). La versión de iOS también utiliza **Crashlytics** con aceptación explícita, pero **la versión de Android no incluye Crashlytics**. Consulte el Artículo 14).

El servidor de la aplicación es mínimo y sin estado (stateless), y solo actúa como intermediario para la clasificación con IA (no almacena contenido). No utiliza servicios de autenticación que requieran una cuenta personal.

## Artículo 7 (Comunicación a terceros)

El desarrollador de la aplicación no tiene medios para acceder al contenido de lo que usted dice, a las transcripciones ni a los resultados de la organización, y no los comunica a terceros.

Con el fin de mostrar anuncios a los usuarios no suscritos a KUU+, se envía a Google la información que Google AdMob requiere para la publicación de anuncios, como identificadores de dispositivo, ID de publicidad, idioma y región del dispositivo, ubicación aproximada e información sobre la interacción con los anuncios (consulte el Artículo 13; se aplica la política de privacidad de AdMob de Google). Mientras la suscripción a KUU+ esté activa, esta transmisión de información no se produce.

En la versión de **Android**, al suscribirse a KUU+, la información de la compra (ID del producto, precio, fecha de compra, etc.) se envía a RevenueCat, Inc. para gestionar la compra y sus derechos (activos/inactivos). No se envía el contenido de lo que dice. Para más detalles sobre el tratamiento de datos de RevenueCat, consulte su [política de privacidad](https://www.revenuecat.com/privacy).

La información solo se comunicará cuando la ley exija su divulgación, siguiendo los procedimientos establecidos.

## Artículo 8 (Eliminación de datos)

Usted puede eliminar todos sus datos en cualquier momento desde «Ajustes → Voz y datos → Eliminar lo guardado» dentro de la aplicación. Esta acción borrará permanentemente los datos del dispositivo (y, en la versión de iOS, también los de la base de datos privada de iCloud). Los datos eliminados no se pueden recuperar.

Al desinstalar la aplicación, se eliminan los datos del dispositivo. En la versión de iOS, los datos de iCloud se pueden eliminar desde los Ajustes de Apple (Ajustes → ID de Apple → iCloud → Gestionar almacenamiento). En la versión de Android, como los datos solo se guardan en el dispositivo, se eliminan al desinstalar la aplicación.

**Versión para Apple Watch:** Al eliminar todos los datos, los datos de visualización ya transferidos al Apple Watch se reemplazarán por contenido vacío la próxima vez que el reloj se conecte. Si elimina la aplicación de su Apple Watch, los datos de visualización guardados en él también se eliminarán.

## Artículo 9 (Medidas de seguridad)

-   **Versión de iOS**: Los archivos de audio temporales durante la grabación se cifran mediante la protección de archivos de iOS (`FileProtectionType.complete`) y son inaccesibles mientras el dispositivo está bloqueado. La comunicación con iCloud es cifrada por Apple mediante SSL/TLS.
-   **Versión de Android**: El audio grabado no se escribe en el disco, ni siquiera como archivo temporal; se procesa únicamente en la memoria y se descarta inmediatamente después del reconocimiento. Las transcripciones y los resultados de la organización guardados se almacenan en el área privada de la aplicación en Android, inaccesible para otras aplicaciones, y se excluyen de la copia de seguridad automática en la nube de Android.
-   **Versión para Apple Watch**: La transferencia entre el iPhone y el Apple Watch se realiza mediante Watch Connectivity de Apple y no pasa por ningún servidor del desarrollador. Lo que se almacena en el Apple Watch se limita al texto para visualización (los títulos recientes de cada categoría); no se almacena audio.
-   Toda la comunicación con la IA externa está cifrada (HTTPS/TLS). El servidor del desarrollador solo actúa como intermediario para la clasificación y no almacena contenido (es sin estado o stateless).

## Artículo 10 (Uso por parte de menores)

La aplicación tiene una clasificación de edad de 4+, pero por su naturaleza (organización de pensamientos), se asume que será utilizada por personas con capacidad de leer y escribir. Los menores de edad deben utilizar la aplicación con el consentimiento de sus padres o tutores.

## Artículo 11 (Modificaciones de esta política de privacidad)

Esta política puede ser modificada debido a cambios en la legislación, la adición de nuevas funciones o cambios en las especificaciones de los frameworks o políticas de cada plataforma (Apple / Google). En caso de cambios importantes, se notificará al actualizar la aplicación o en la página pública de esta política.

## Artículo 12 (Contacto)

Para consultas sobre esta política, póngase en contacto con nosotros a través de la sección «Desarrollador» en la página de la aplicación en la App Store o Google Play, o mediante «Ajustes → Contacto» dentro de la aplicación.

## Artículo 13 (Publicidad y Transparencia en el Seguimiento de Apps)

Cuando no tiene una suscripción a KUU+, la aplicación muestra un anuncio nativo de Google AdMob entre las secciones de la pantalla «Lo que has dicho». Los anuncios se presentan de forma discreta para mantener la estética de KUU.

-   **El contenido de lo que dice nunca se utiliza para fines publicitarios** (los anuncios no consultan sus transcripciones, resultados de organización ni temas).
-   Para la publicación de anuncios, Google AdMob puede recopilar identificadores de dispositivo (incluido el IDFA), ID de publicidad, ubicación aproximada (Coarse Location), datos de diagnóstico e interacciones con el producto (interacciones con los anuncios dentro de la aplicación).
-   **Versión de iOS**: Se muestra una solicitud de **Transparencia en el Seguimiento de Apps** (ATT) una única vez, justo antes de mostrar el primer anuncio. Los anuncios se seguirán mostrando aunque rechace la solicitud, pero la información enviada a Google será limitada (no personalizada). Puede cambiar el permiso de ATT en cualquier momento en «Ajustes → Privacidad y seguridad → Rastreo» de iOS.
-   **Versión de Android**: ATT es un mecanismo exclusivo de iOS y no existe en Android. En su lugar, se utiliza el **ID de publicidad** de Google para la publicación de anuncios. Puede optar por no recibir publicidad personalizada o restablecer su ID de publicidad desde los «Ajustes → Privacidad → Anuncios» de su dispositivo (la redacción puede variar según el dispositivo y la versión de Android). Además, la versión de Android cumple con la gestión del consentimiento (UMP) que se muestra en las regiones aplicables, como la UE.
-   **La suscripción a KUU+ detiene toda la publicidad y la transmisión de datos asociada**.
-   Para más detalles sobre el tratamiento de datos de AdMob, consulte la [política de privacidad de Google AdMob](https://support.google.com/admob/answer/6128543).

## Artículo 14 (Uso de Firebase Analytics / Crashlytics)

**Este artículo, en lo que respecta al método de aceptación voluntaria (opt-in), se aplica a la versión de iOS. Para la versión de Android, consulte el apartado «Acerca de la versión de Android» al final de este artículo.**

La **versión de iOS**, para mejorar la calidad de la aplicación y detectar inmediatamente incidentes en producción, puede utilizar Firebase Analytics de Google (para agregar datos de uso) y Firebase Crashlytics (para informes de fallos). **Esta función está DESACTIVADA por defecto (no se envía ningún dato) y solo se activa si el usuario la acepta explícitamente en «Ajustes → Datos y diagnóstico».**

-   **Información que se envía**:
    -   Un ID de instalación anonimizado emitido automáticamente por Firebase (basado en el IDFV; no es un identificador personal directo).
    -   Señales agregadas de eventos dentro de la aplicación (eventos agregados como la finalización de sesiones de grabación, la visualización/conversión de la pantalla de pago, la finalización del tutorial, etc. Los valores numéricos se envían con una granularidad aproximada y agrupada).
    -   Trazas de la pila de llamadas (stack traces) simbolizadas cuando la aplicación se cierra de forma inesperada.
-   **Información que no se envía**: El contenido de lo que dice (audio), las transcripciones, el texto de los resultados de la clasificación con IA y los nombres de los temas que usted establece están diseñados para que **no puedan enviarse a nivel de tipo** (la implementación de la API impide pasar valores de tipo cadena de texto al SDK de análisis).
-   **Mientras la función no esté aceptada, no se produce ninguna comunicación con Firebase** (incluidas todas las categorías anteriores).
-   **Cómo dejar de enviar datos**: Puede desactivar el interruptor en «Ajustes → Datos y diagnóstico» en cualquier momento. Al desactivarlo, los ID de instalación anteriores se descartan y los registros de fallos no enviados que estuvieran guardados en el dispositivo se eliminan.
-   El destinatario es Google LLC (Estados Unidos). Se aplica la [Información de privacidad de Firebase](https://firebase.google.com/support/privacy) de Google.

**Acerca de la versión de Android:** La versión de Android utiliza Firebase Analytics para enviar **eventos de uso sin contenido** con el fin de mejorar el producto (valores agrupados como transiciones de pantalla y recuentos de uso de funciones), además de un ID de instancia de la aplicación anónimo emitido por Firebase. **A diferencia de iOS, esta función está habilitada por defecto.** El contenido de lo que dice (audio), las transcripciones, el texto de los resultados de la organización y los nombres de los temas **no se pueden enviar**, ya que la API del SDK de análisis está diseñada para no poder pasar valores de tipo cadena de texto. **La versión de Android no incluye Crashlytics y no envía informes de fallos.** El destinatario es Google LLC (Estados Unidos); se aplica la [Información de privacidad de Firebase](https://firebase.google.com/support/privacy) de Google.
