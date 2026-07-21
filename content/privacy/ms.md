> Terjemahan ini ialah rujukan untuk kemudahan. Versi Bahasa Jepun adalah teks yang berautoriti.

# Dasar Privasi KUU

Tarikh kemas kini terakhir: 21 Julai 2026

**Secara ringkas:** Apa yang anda tuturkan adalah milik anda. **Suara anda sendiri tidak akan dihantar ke luar peranti anda**. Transkripsi berlaku di dalam peranti anda. Penyusunan (klasifikasi AI) menggunakan AI luaran, tetapi hanya teks yang ditranskripsi dihantar. Ia digunakan semata-mata untuk penyusunan dan tidak disimpan (pada iOS, anda boleh beralih kepada penyusunan pada peranti sahaja melalui "Pada Peranti" dalam Tetapan; **versi Android hanya menghantar ke AI luaran — tiada pilihan penyusunan pada peranti**). Data disimpan hanya pada peranti anda, dan pada iOS juga dalam pangkalan data peribadi iCloud anda (Android menyimpan pada peranti sahaja). Pembangun tidak menyimpan kandungan anda dan tidak boleh melihat apa yang diterima. Anda boleh memadam semua data dari dalam aplikasi pada bila-bila masa. Aplikasi ini membuat **permintaan rangkaian yang minimum** hanya untuk pengebilan (StoreKit pada iOS / RevenueCat pada Android) dan iklan Google AdMob, dan maklumat itu tidak sekali-kali mengandungi apa yang anda katakan (iklan hilang dengan KUU+). Penggunaan diukur untuk meningkatkan kualiti, tetapi ini juga tidak sekali-kali mengandungi apa yang anda katakan (iOS memerlukan keikutsertaan pengguna; Android menghantar pengukuran bebas kandungan secara lalai — lihat Perkara 14).

---

## Perkara 1 (Dasar Asas)

Aplikasi ini, "KUU" (selepas ini "Aplikasi"), ialah sebuah aplikasi yang membantu anda meluahkan dan menyusun fikiran di dalam kepala anda dengan menuturkannya. Ia tersedia pada **iOS dan Android**, dan dasar ini terpakai untuk kedua-dua versi. Aplikasi ini memproses maklumat hanya setakat minimum yang diperlukan untuk menyediakan ciri-cirinya, dengan mengutamakan perlindungan privasi pengguna.

## Perkara 2 (Maklumat yang Diperoleh dan Disimpan)

Aplikasi ini mengendalikan maklumat berikut sahaja:

1.  **Kandungan yang anda tuturkan (data audio)** — Audio yang dirakam disimpan sementara dalam storan setempat peranti hanya semasa proses transkripsi, dan dipadam serta-merta selepas pemprosesan selesai. Ia tidak dihantar ke mana-mana pelayan.
2.  **Teks transkripsi dan hasil penyusunan** — Disimpan supaya anda boleh menyemaknya semula (iOS: pada peranti anda dan dalam pangkalan data peribadi iCloud anda; Android: pada peranti sahaja — lihat Perkara 4).
3.  **Tetapan dalam aplikasi** — Nilai tetapan yang diperlukan untuk operasi aplikasi seperti tema, saiz teks dan keadaan aras air di kepala.

Aplikasi ini tidak mengumpul maklumat peribadi seperti nama, alamat e-mel, nombor telefon, lokasi, kenalan, kalendar, foto, atau pengecam peranti.

## Perkara 3 (Mengenai Pengecaman Pertuturan dan Klasifikasi AI)

**Pengecaman pertuturan (transkripsi)** dilakukan sepenuhnya pada peranti iOS anda.

-   Pengecaman pertuturan: Menggunakan rangka kerja Speech Apple (pada peranti). Suara anda sendiri tidak sekali-kali dihantar ke luar peranti.

**Klasifikasi AI (pengkategorian)** menggunakan AI luaran.

-   Hanya **teks daripada apa yang anda tuturkan (transkrip)** dihantar. Suara anda tidak dihantar.
-   Ia dihantar ke AI luaran melalui pelayan pembangun (melalui bahagian belakang ke Gemini milik Google).
-   Teks yang dihantar **digunakan hanya untuk pengkategorian dan tidak sekali-kali disimpan**. Ia juga tidak digunakan untuk melatih AI.
-   **Pada iOS**, anda boleh beralih kepada **penyusunan pada peranti sahaja** (FoundationModels milik Apple / peraturan pada peranti) pada bila-bila masa melalui "Pada Peranti" dalam Tetapan. Dalam kes itu, teks juga tidak akan meninggalkan peranti.

**Mengenai versi Android:** Versi Android tidak menawarkan kaedah penyusunan (pengkategorian) yang berlaku sepenuhnya pada peranti. Apabila anda menyusun, teks yang ditranskripsi **sentiasa** dihantar ke AI luaran (Gemini milik Google melalui bahagian belakang kami). Tiada pilihan untuk beralih kepada "Pada Peranti" seperti pada iOS. Hanya teks yang ditranskripsi dihantar — suara anda sendiri tidak dihantar, dan teks yang dihantar digunakan semata-mata untuk pengkategorian dan tidak disimpan atau digunakan untuk melatih AI. Transkripsi (pengecaman pertuturan) itu sendiri berjalan sepenuhnya pada peranti.

## Perkara 4 (Penyimpanan dan Penyegerakan)

**Versi iOS:** Hasil transkripsi dan penyusunan disimpan hanya dalam **Pangkalan Data Peribadi iCloud** anda (CloudKit Private Database). Ini ialah storan yang disediakan oleh Apple yang hanya anda boleh akses. Pembangun aplikasi ini tidak boleh melihat atau mendapatkan kandungan yang disimpan. Penggunaan iCloud tertakluk pada dasar privasi Apple.

**Versi Android:** Hasil transkripsi dan penyusunan disimpan **pada peranti ini sahaja**. Tiada penyegerakan awan automatik. Apabila menukar peranti, anda boleh mengeksport data ke fail dari "Suara & Data" dalam aplikasi dan mengimportnya pada peranti baharu. Anda memilih destinasi eksport (pada peranti, dalam aplikasi storan awan anda, dsb.). Pembangun tidak boleh mengakses fail ini.

## Perkara 5 (Tujuan Penggunaan)

Maklumat yang dikendalikan digunakan hanya untuk tujuan berikut:

1.  Menjana transkripsi daripada suara anda dan memaparkannya kepada anda
2.  Mengklasifikasikan transkripsi kepada "Lihat Sekarang / Fikir Kemudian / Simpan Dulu / Lepaskan" dan memaparkannya kepada anda
3.  Menyimpan dan memaparkan kandungan yang pernah anda tuturkan supaya anda boleh menyemaknya semula
4.  Mengekalkan nilai tetapan yang diperlukan untuk operasi aplikasi

## Perkara 6 (Penggunaan Perkhidmatan Luaran)

Aplikasi ini menggunakan perkhidmatan luaran berikut untuk menyediakan fungsinya. **Suara anda sendiri tidak dihantar ke mana-mana perkhidmatan ini**.

-   **iCloud / CloudKit** (iOS sahaja. Disediakan oleh Apple. Disimpan dan disegerakkan hanya ke pangkalan data peribadi anda sendiri)
-   **Pengecaman pertuturan** (iOS: rangka kerja Speech Apple; Android: enjin pengecaman pertuturan pada peranti. Kedua-duanya berjalan pada peranti; suara tidak dihantar ke luar peranti)
-   **AI luaran (awan)** (Klasifikasi AI. Hanya teks yang ditranskripsi dihantar. Digunakan semata-mata untuk pengkategorian, tidak disimpan, dan tidak digunakan untuk melatih AI. Pada iOS, ia boleh dimatikan melalui "Pada Peranti" dalam Tetapan, tetapi **versi Android hanya menghantar ke AI luaran**. Lihat Perkara 3)
-   **FoundationModels** (iOS sahaja. Disediakan oleh Apple. Berjalan sepenuhnya pada peranti. Digunakan apabila tetapan "Pada Peranti" didayakan, atau sebagai sandaran apabila AI luaran tidak tersedia)
-   **Perkhidmatan pengebilan** (iOS: **Apple StoreKit**; Android: **RevenueCat**. Untuk pengurusan pembelian, pembaharuan, pembatalan, dan status kelayakan langganan KUU+. Kandungan tuturan tidak dihantar. Mengenai RevenueCat, lihat Perkara 7 dan [Dasar Privasi RevenueCat](https://www.revenuecat.com/privacy))
-   **Play Integrity API (melalui Firebase App Check. Android sahaja)** (Pengesahan integriti peranti/aplikasi untuk memastikan permintaan kepada API klasifikasi datang daripada aplikasi yang sah. Tidak mengandungi kandungan tuturan atau maklumat yang mengenal pasti pengguna)
-   **Google AdMob (Google Mobile Ads SDK)** (Hanya apabila tidak melanggan KUU+: satu slot iklan natif dipaparkan di antara bahagian dalam skrin "Perkara Dituturkan". Kandungan tuturan tidak dihantar. Lihat Perkara 13)
-   **Firebase Analytics** (Disediakan oleh Google. Untuk penambahbaikan kualiti aplikasi. Pada iOS, **digunakan hanya apabila pengguna secara jelas memilih untuk ikut serta melalui Tetapan**; pada Android, peristiwa penggunaan bebas kandungan dihantar **secara lalai** (dalam kedua-dua kes, kandungan tuturan tidak dihantar). iOS juga menggunakan **Crashlytics** melalui keikutsertaan, tetapi **versi Android tidak menyertakan Crashlytics**. Lihat Perkara 14)

Pelayan aplikasi ini adalah minimum dan hanya berfungsi sebagai perantara untuk klasifikasi AI, dan tidak menyimpan sebarang kandungan (tanpa keadaan atau *stateless*). Aplikasi ini tidak menggunakan perkhidmatan pengesahan yang memerlukan akaun peribadi.

## Perkara 7 (Pendedahan kepada Pihak Ketiga)

Pembangun aplikasi ini tidak mempunyai cara untuk mengakses kandungan tuturan, transkripsi, atau hasil penyusunan anda, dan tidak akan mendedahkannya kepada mana-mana pihak ketiga.

Untuk tujuan menyampaikan iklan kepada pengguna yang tidak melanggan KUU+, maklumat yang diperlukan oleh Google AdMob untuk penghantaran iklan—termasuk pengecam peranti, ID pengiklanan, bahasa dan rantau peranti, lokasi kasar, dan data interaksi iklan—dihantar kepada Google (lihat Perkara 13; dasar privasi AdMob Google terpakai). Semasa langganan KUU+ aktif, penghantaran maklumat ini tidak berlaku.

Apabila anda melanggan KUU+ pada versi **Android**, maklumat pembelian (ID produk, harga, tarikh pembelian, dsb.) dihantar kepada RevenueCat, Inc. untuk menguruskan proses pembelian dan kelayakan anda (aktif/tidak aktif). Kandungan tuturan tidak dihantar. Untuk butiran pengendalian data oleh RevenueCat, sila semak [Dasar Privasi RevenueCat](https://www.revenuecat.com/privacy).

Maklumat akan didedahkan hanya apabila diwajibkan oleh undang-undang, mengikut prosedur yang ditetapkan.

## Perkara 8 (Pemadaman Data)

Anda boleh memadam semua data pada bila-bila masa dari "Tetapan → Suara & Data → Padam perkara yang disimpan" di dalam aplikasi. Tindakan ini akan memadam secara kekal data pada peranti (dan, pada iOS, juga data dalam Pangkalan Data Peribadi iCloud). Data yang telah dipadam tidak boleh dipulihkan.

Menyahpasang aplikasi akan memadam data pada peranti. Pada iOS, data iCloud boleh dipadam melalui Tetapan Apple (Tetapan → Apple ID → iCloud → Urus Storan). Versi Android hanya menyimpan data pada peranti, jadi data akan dipadam apabila aplikasi dinyahpasang.

## Perkara 9 (Langkah-langkah Keselamatan)

-   **Versi iOS**: Fail audio sementara semasa rakaman disulitkan oleh perlindungan fail iOS (`FileProtectionType.complete`) dan tidak boleh diakses semasa peranti dikunci. Komunikasi dengan iCloud disulitkan oleh Apple melalui SSL/TLS.
-   **Versi Android**: Audio yang dirakam tidak ditulis ke cakera walaupun sebagai fail sementara; ia diproses hanya dalam memori dan dibuang serta-merta selepas pengecaman. Transkripsi dan hasil penyusunan yang disimpan berada dalam storan khusus aplikasi Android, tidak boleh diakses oleh aplikasi lain, dan dikecualikan daripada sandaran awan automatik Android.
-   Semua komunikasi dengan AI luaran disulitkan (HTTPS/TLS). Pelayan pembangun hanya bertindak sebagai perantara untuk permintaan penyusunan dan tidak menyimpan sebarang kandungan (tanpa keadaan atau *stateless*).

## Perkara 10 (Penggunaan oleh Pengguna Bawah Umur)

Aplikasi ini dinilai 4+, tetapi sifatnya (penyusunan fikiran) mengandaikan pengguna boleh membaca dan menulis. Pengguna bawah umur hendaklah menggunakan aplikasi ini dengan kebenaran penjaga mereka.

## Perkara 11 (Perubahan pada Dasar Privasi Ini)

Dasar ini mungkin dikemas kini disebabkan oleh perubahan dalam undang-undang, penambahan ciri, atau perubahan pada spesifikasi rangka kerja atau dasar setiap platform (Apple / Google). Perubahan penting akan diumumkan melalui kemas kini aplikasi atau pada halaman awam dasar ini.

## Perkara 12 (Hubungi Kami)

Untuk pertanyaan mengenai dasar ini, sila hubungi kami melalui bahagian "Pembangun" di halaman App Store atau Google Play aplikasi, atau melalui "Tetapan → Hubungi Kami" di dalam aplikasi.

## Perkara 13 (Mengenai Iklan dan App Tracking Transparency)

Apabila anda tidak melanggan KUU+, aplikasi ini memaparkan satu slot iklan natif di antara bahagian dalam skrin "Perkara Dituturkan", yang disampaikan oleh Google AdMob. Iklan itu sendiri dipaparkan secara sederhana agar selaras dengan suasana KUU.

-   **Kandungan tuturan anda tidak sekali-kali digunakan untuk iklan.** Iklan tidak merujuk kepada transkripsi, hasil penyusunan, atau tema anda.
-   Untuk penghantaran iklan, Google AdMob mungkin mengumpul pengecam peranti (termasuk IDFA), ID pengiklanan, Lokasi Kasar (lokasi anggaran), Diagnostik, dan Interaksi Produk (interaksi berkaitan iklan dalam aplikasi).
-   **Versi iOS**: Gesaan **App Tracking Transparency** (ATT) dipaparkan sekali sahaja, sejurus sebelum iklan pertama. Iklan masih akan dipaparkan jika anda menolak, tetapi maklumat yang dihantar kepada Google adalah terhad (tidak diperibadikan). Anda boleh menukar kebenaran ATT pada bila-bila masa dalam "Tetapan → Privasi & Keselamatan → Penjejakan" iOS.
-   **Versi Android**: ATT adalah mekanisme khusus iOS dan tidak wujud pada Android. Sebaliknya, **ID Pengiklanan (Advertising ID)** Google digunakan untuk penghantaran iklan. Anda boleh menarik diri daripada pemperibadian iklan atau menetapkan semula ID Pengiklanan anda dari "Tetapan → Privasi → Iklan" peranti anda (perkataan mungkin berbeza mengikut peranti dan versi Android). Versi Android juga mematuhi pengurusan persetujuan (UMP) yang dipaparkan di rantau berkenaan seperti EU.
-   **Melanggan KUU+ akan menghentikan semua iklan dan penghantaran data yang berkaitan.**
-   Untuk butiran mengenai pengendalian data oleh AdMob, sila rujuk [Dasar Privasi Google AdMob](https://support.google.com/admob/answer/6128543).

## Perkara 14 (Mengenai Penggunaan Firebase Analytics / Crashlytics)

**Kaedah keikutsertaan dalam Perkara ini terpakai untuk versi iOS. Untuk versi Android, sila lihat 'Mengenai versi Android' di akhir Perkara ini.**

**Pada iOS**, untuk penambahbaikan kualiti aplikasi dan kesedaran segera mengenai insiden pengeluaran, aplikasi ini mungkin menggunakan Firebase Analytics Google (agregat penggunaan) dan Firebase Crashlytics (laporan pepijat). **Ciri ini DIMATIKAN secara lalai (tiada data dihantar) dan beroperasi hanya apabila anda secara jelas memilih untuk ikut serta melalui "Tetapan → Data & Diagnostik".**

-   **Maklumat yang dihantar**:
    -   ID pemasangan tanpa nama yang dikeluarkan secara automatik oleh Firebase (berdasarkan IDFV; bukan pengecam peribadi secara langsung)
    -   Isyarat peristiwa agregat dalam aplikasi (penyelesaian sesi rakaman, paparan/penukaran Paywall, penyiapan Onboarding, dsb. Nilai berangka dihantar dalam granulariti kasar yang dikelompokkan).
    -   Jejak tindanan pepijat yang disimbolkan apabila aplikasi ditamatkan secara tidak normal.
-   **Maklumat yang tidak dihantar**: Kandungan tuturan (audio), teks transkripsi, teks hasil klasifikasi AI, dan nama tema yang anda tetapkan **direka bentuk agar tidak boleh dihantar pada peringkat jenis (type level)** (API pelaksanaan menghalang nilai rentetan daripada diserahkan kepada SDK analitik).
-   **Semasa keikutsertaan DIMATIKAN, tiada sebarang komunikasi dengan Firebase berlaku** (termasuk semua kategori di atas).
-   **Cara untuk berhenti menghantar**: Togol "Tetapan → Data & Diagnostik" kepada MATI pada bila-bila masa. Apabila dimatikan, ID pemasangan lalu akan dibuang dan sebarang log pepijat yang belum dihantar yang disimpan pada peranti akan dipadam.
-   Penerima ialah Google LLC (Amerika Syarikat). [Maklumat Privasi Firebase](https://firebase.google.com/support/privacy) Google terpakai.

**Mengenai versi Android:** Versi Android menggunakan Firebase Analytics untuk menghantar **peristiwa penggunaan bebas kandungan (content-free)** untuk penambahbaikan produk (nilai yang dikelompokkan seperti peralihan skrin dan kiraan penggunaan ciri) serta ID Instans Aplikasi tanpa nama yang dikeluarkan oleh Firebase. **Tidak seperti iOS, ciri ini didayakan secara lalai.** Kandungan tuturan (audio), transkripsi, teks hasil penyusunan, dan nama tema anda **tidak boleh dihantar** — reka bentuk API SDK analitik menghalang nilai rentetan daripada diserahkan kepadanya. **Versi Android tidak menyertakan Crashlytics dan tidak menghantar sebarang laporan pepijat.** Penerima ialah Google LLC (Amerika Syarikat); [Maklumat Privasi Firebase](https://firebase.google.com/support/privacy) Google terpakai.
