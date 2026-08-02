> Ini adalah terjemahan rujukan untuk kemudahan. Versi Jepun adalah teks yang berautoriti.

# Dasar Privasi KUU

Kemas kini terakhir: 2 Ogos 2026

**Ringkasnya:** Apa yang anda tuturkan adalah milik anda. **Aplikasi ini tidak sekali-kali menghantar audio suara anda ke mana-mana pihak luar**. Pada peranti iPhone dan Android, transkripsi juga berlaku di dalam peranti. **Versi Apple Watch aplikasi ini tidak melakukan sebarang rakaman** — ia hanya menerima teks yang dihasilkan oleh input standard jam tangan (imlak, tulisan tangan, atau papan kekunci); apabila anda memilih imlak, proses mendengar dikendalikan oleh sistem Apple sendiri (lihat Perkara 3). Penyusunan AI menggunakan AI luaran, tetapi hanya teks yang ditranskripsi dihantar. Ia digunakan semata-mata untuk penyusunan dan tidak disimpan oleh penyedia AI. Apa yang disimpan hanya berada pada peranti anda, dan pada iOS juga dalam pangkalan data peribadi iCloud anda (Android menyimpan pada peranti sahaja). Pembangun tidak menyimpan kandungan anda dan tidak boleh melihat apa yang diterima. Anda boleh memadam semua data dari dalam aplikasi pada bila-bila masa. Aplikasi ini hanya membuat **permintaan rangkaian yang minimum** untuk pengebilan (StoreKit pada iOS / RevenueCat pada Android) dan iklan Google AdMob, dan maklumat itu tidak sekali-kali merangkumi apa yang anda katakan (iklan hilang dengan KUU+). Penggunaan diukur untuk meningkatkan kualiti, tetapi ini juga tidak merangkumi apa yang anda katakan (iOS adalah ikut serta pengguna; Android menghantar pengukuran bebas kandungan secara lalai — lihat Perkara 14).

---

## Perkara 1 (Dasar Asas)

Aplikasi "KUU" ("Aplikasi ini") ialah sebuah aplikasi (tersedia pada **iOS — iPhone dan Apple Watch — dan Android**) yang membantu anda meluahkan fikiran dengan menuturkannya dan menyusunnya. Dasar ini terpakai kepada semua versi. Aplikasi ini memproses maklumat hanya pada tahap minimum yang diperlukan untuk menyediakan ciri-cirinya, dengan mengutamakan perlindungan privasi pengguna.

## Perkara 2 (Maklumat yang Dikumpul dan Disimpan)

Maklumat yang dikendalikan oleh Aplikasi ini terhad kepada yang berikut:

1.  **Audio yang anda rakam (data suara)** — Audio yang dirakam disimpan sementara dalam storan setempat peranti hanya semasa proses transkripsi, dan dipadamkan sebaik sahaja proses selesai. Ia tidak dihantar ke pelayan. **Versi Apple Watch aplikasi ini tidak melakukan sebarang rakaman** (lihat Perkara 3).
2.  **Hasil transkripsi dan penyusunan (teks)** — Disimpan supaya anda boleh menyemaknya semula (iOS: pada peranti anda dan dalam pangkalan data peribadi iCloud anda; Android: pada peranti sahaja. Pada Apple Watch yang dipasangkan, hanya tajuk terkini dalam setiap kategori disimpan, untuk paparan — lihat Perkara 4).
3.  **Tetapan dalam aplikasi** — Nilai tetapan yang diperlukan untuk operasi aplikasi seperti tema, saiz teks, dan keadaan paras air di kepala.

Aplikasi ini tidak mengumpul maklumat peribadi seperti nama, alamat e-mel, nombor telefon, maklumat lokasi, kenalan, kalendar, foto, atau pengecam peranti.

## Perkara 3 (Mengenai Pengecaman Pertuturan dan Pengkategorian AI)

Pada iPhone (iOS) dan peranti Android, **pengecaman pertuturan (transkripsi)** dilakukan sepenuhnya pada peranti anda sendiri (untuk Apple Watch, sila lihat di akhir Perkara ini):

-   Pengecaman pertuturan: Menggunakan kerangka Speech Apple (pada peranti). Audio suara anda sendiri tidak sekali-kali dihantar ke luar peranti.

**Pengkategorian AI (penyusunan)** menggunakan AI luaran:

-   Hanya **teks daripada apa yang dituturkan (teks transkripsi)** yang dihantar. Suara anda tidak dihantar.
-   Ia dihantar ke AI luaran, melalui pelayan pembangun (ke Gemini Google melalui backend kami).
-   Teks yang dihantar **hanya digunakan untuk pengkategorian dan tidak sekali-kali disimpan**. Ia juga tidak digunakan untuk melatih AI.
-   Data yang dihantar termasuk bukan sahaja apa yang anda tuturkan dan ditranskripsi, tetapi juga apa-apa yang anda taip atau sunting secara manual. Jika penetapan tema automatik (KUU+, pilihan) diaktifkan, tajuk, teks, dan nama tema item yang telah disimpan juga dihantar untuk tujuan penetapan (semuanya hanya digunakan untuk klasifikasi dan tidak disimpan).
-   **Pada iOS**, versi Aplikasi sebelum 2.3.0 membenarkan anda memilih klasifikasi di dalam peranti sahaja melalui "Pada Peranti" dalam Tetapan (tetapan ini tidak lagi ditawarkan mulai versi 2.3.0).

**Mengenai versi Android:** Versi Android tidak menawarkan kaedah penyusunan (pengkategorian) yang berfungsi di dalam peranti sahaja. Apabila anda menyusun, teks yang ditranskripsi **semestinya** akan dihantar ke AI luaran (Gemini Google melalui backend kami). Hanya teks yang ditranskripsi dihantar — audio suara anda sendiri tidak dihantar, dan teks yang dihantar digunakan semata-mata untuk pengkategorian dan tidak disimpan atau digunakan untuk melatih AI. Proses transkripsi (pengecaman pertuturan) itu sendiri berlaku sepenuhnya di dalam peranti.

**Mengenai versi Apple Watch:** Versi Apple Watch Aplikasi ini tidak merakam audio atau melakukan pengecaman pertuturan. Ia menggunakan input teks standard watchOS (pilihan pengguna antara imlak, tulisan tangan, atau papan kekunci), dan Aplikasi ini hanya menerima teks yang terhasil. Apabila anda memilih imlak, pengecaman pertuturan dilakukan sebagai ciri Apple (watchOS); cara ia diproses — termasuk sama ada ia berlaku di dalam peranti atau di pelayan Apple — bergantung pada peranti, tetapan dan bahasa anda, dan adalah **tertakluk pada dasar privasi Apple**. Aplikasi ini tidak boleh mengakses data audio tersebut, dan tidak sekali-kali menerimanya atau menyimpannya. Teks yang terhasil dikendalikan sama seperti teks yang anda tuturkan pada iPhone (pengkategorian AI di bawah Perkara ini; penyimpanan di bawah Perkara 4).

## Perkara 4 (Penyimpanan dan Penyegerakan)

**iOS:** Aplikasi ini menyimpan teks yang ditranskripsi dan disusun hanya dalam **Pangkalan Data Peribadi iCloud** anda (CloudKit Private Database). Ini adalah storan yang disediakan oleh Apple yang hanya anda boleh akses. Pembangun Aplikasi ini tidak boleh melihat atau mendapatkan semula sebarang kandungan yang disimpan. Penggunaan iCloud adalah tertakluk pada dasar privasi Apple.

**Android:** Teks yang ditranskripsi dan disusun disimpan **pada peranti ini sahaja**. Tiada penyegerakan awan automatik. Apabila menukar peranti, anda boleh mengeksport ke fail dari "Suara & Data" dalam Aplikasi dan mengimportnya pada peranti baharu. Anda memilih tempat fail itu disimpan (pada peranti, dalam aplikasi storan awan anda, dsb.). Pembangun tidak boleh mengakses fail tersebut.

**Apple Watch:** Untuk tujuan paparan, sebahagian daripada teks anda yang disusun (tajuk terkini dalam setiap kategori) dipindahkan ke Apple Watch anda yang dipasangkan melalui komunikasi antara peranti Apple (Watch Connectivity) dan **juga disimpan pada jam tangan tersebut**. Teks yang anda masukkan pada Apple Watch dipindahkan ke iPhone anda dengan cara yang sama. Tiada pelayan pembangun yang terlibat dalam pemindahan atau penyimpanan ini.

## Perkara 5 (Tujuan Penggunaan)

Maklumat yang dikendalikan hanya digunakan untuk tujuan berikut:

1.  Menjana transkripsi daripada suara anda dan memaparkannya kepada anda
2.  Mengkategorikan transkripsi kepada "Lihat Sekarang / Fikir Nanti / Simpan Dulu / Lepaskan" dan memaparkannya
3.  Menyimpan dan memaparkan apa yang telah anda tuturkan supaya anda boleh menyemaknya semula
4.  Mengekalkan tetapan yang diperlukan untuk operasi aplikasi

## Perkara 6 (Penggunaan Perkhidmatan Luaran)

Aplikasi ini menggunakan perkhidmatan luaran berikut untuk menyediakan ciri-cirinya. **Audio suara anda sendiri tidak dihantar ke mana-mana perkhidmatan ini.**

-   **iCloud / CloudKit** (iOS sahaja. Disediakan oleh Apple. Hanya menyimpan dan menyegerak ke pangkalan data peribadi anda sendiri)
-   **Pengecaman Pertuturan** (iOS: kerangka Speech Apple; Android: enjin pengecaman pertuturan pada peranti. Kedua-duanya berjalan pada peranti; suara anda tidak dihantar ke luar peranti. **Versi Apple Watch tidak melakukan pengecaman pertuturan dalam aplikasi dan menggunakan input standard watchOS**. Lihat Perkara 3)
-   **Input teks standard watchOS** (Apple Watch sahaja. Disediakan oleh Apple. Pilihan pengguna antara imlak, tulisan tangan, atau papan kekunci. Apabila anda memilih imlak, pengecaman pertuturan dilakukan sebagai ciri Apple dan tertakluk pada dasar privasi Apple. Aplikasi ini tidak boleh mengakses audio tersebut. Lihat Perkara 3)
-   **Watch Connectivity** (Apple Watch sahaja. Disediakan oleh Apple. Menghantar teks paparan secara terus antara iPhone dan Apple Watch anda. Tiada pelayan pembangun yang terlibat. Lihat Perkara 4)
-   **AI luaran (awan)** (Pengkategorian AI. Hanya teks yang dihantar. Digunakan semata-mata untuk pengkategorian, tidak disimpan, dan tidak digunakan untuk latihan AI. Lihat Perkara 3)
-   **Perkhidmatan Pengebilan** (iOS: **Apple StoreKit**; Android: **RevenueCat**. Pengurusan pembelian, pembaharuan, pembatalan, dan status langganan KUU+. Tiada kandungan tuturan dihantar. Untuk RevenueCat, lihat Perkara 7 dan [dasar privasi RevenueCat](https://www.revenuecat.com/privacy))
-   **Play Integrity API (melalui Firebase App Check; Android sahaja)** (Pengesahan integriti peranti/aplikasi untuk memastikan permintaan kepada API klasifikasi datang daripada aplikasi yang sah. Tidak mengandungi kandungan tuturan atau maklumat yang mengenal pasti pengguna)
-   **Google AdMob (Google Mobile Ads SDK)** (Hanya apabila KUU+ tidak aktif: satu slot iklan natif antara bahagian dalam skrin "Apa yang dituturkan". Tiada kandungan tuturan dihantar. Lihat Perkara 13)
-   **Firebase Analytics** (Disediakan oleh Google. Untuk penambahbaikan kualiti aplikasi. Pada iOS, **digunakan hanya apabila anda secara eksplisit memilih ikut serta melalui Tetapan**; pada Android, peristiwa penggunaan bebas kandungan dihantar **secara lalai** (dalam kedua-dua kes tiada kandungan tuturan dihantar). iOS juga menggunakan **Crashlytics** secara ikut serta, tetapi **versi Android tidak menyertakan Crashlytics**. Lihat Perkara 14)

Pelayan Aplikasi ini adalah minimal dan tanpa keadaan (stateless), hanya berfungsi sebagai perantara untuk permintaan pengkategorian AI (tiada kandungan disimpan). Ia tidak menggunakan perkhidmatan pengesahan yang memerlukan akaun peribadi.

## Perkara 7 (Pendedahan kepada Pihak Ketiga)

Pembangun Aplikasi ini tidak mempunyai cara untuk mengakses kandungan tuturan, transkripsi, atau hasil penyusunan anda, dan tidak akan mendedahkannya kepada mana-mana pihak ketiga.

Untuk menyampaikan iklan kepada pengguna yang tidak melanggan KUU+, Aplikasi ini menghantar maklumat yang diperlukan oleh Google AdMob untuk penyampaian iklan — termasuk pengecam peranti, ID pengiklanan, bahasa dan rantau peranti, lokasi kasar, dan data interaksi iklan — kepada Google (lihat Perkara 13; dasar privasi AdMob Google terpakai). Semasa KUU+ aktif, penghantaran maklumat ini tidak berlaku.

Apabila anda melanggan KUU+ pada versi **Android**, maklumat pembelian (ID produk, harga, tarikh pembelian, dll.) dihantar kepada RevenueCat, Inc. untuk menguruskan pembelian dan kelayakan anda (aktif/tidak aktif). Tiada kandungan tuturan dihantar. Sila lihat [dasar privasi RevenueCat](https://www.revenuecat.com/privacy) untuk butiran.

Maklumat hanya akan didedahkan apabila dikehendaki oleh undang-undang.

## Perkara 8 (Pemadaman Data)

Anda boleh memadam semua data pada bila-bila masa dari "Tetapan → Suara & Data → Padam apa yang disimpan" di dalam Aplikasi. Ini akan memadam secara kekal data pada peranti (dan, pada iOS, juga dalam Pangkalan Data Peribadi iCloud). Data yang dipadam tidak boleh dipulihkan.

Menyahpasang Aplikasi akan memadam data setempat. Pada iOS, data iCloud boleh dialih keluar melalui Tetapan → Apple ID → iCloud → Urus Storan. Versi Android menyimpan data pada peranti sahaja, jadi ia akan dipadam semasa penyahpasangan.

**Apple Watch:** Apabila anda memadam semua data, data paparan yang telah dipindahkan ke Apple Watch anda akan digantikan dengan kandungan kosong pada kali seterusnya jam tangan bersambung. Memadam aplikasi dari Apple Watch anda juga akan memadam data paparan yang disimpan padanya.

## Perkara 9 (Langkah-langkah Keselamatan)

-   **iOS**: Fail audio sementara semasa rakaman disulitkan oleh perlindungan fail iOS (`FileProtectionType.complete`) dan tidak boleh diakses semasa peranti dikunci. Komunikasi dengan iCloud disulitkan oleh Apple melalui SSL/TLS.
-   **Android**: Audio yang dirakam tidak pernah ditulis ke cakera walaupun sebagai fail sementara; ia diproses dalam ingatan sahaja dan dibuang serta-merta selepas pengecaman. Transkripsi dan hasil penyusunan yang disimpan berada dalam storan peribadi aplikasi, tidak boleh diakses oleh aplikasi lain, dan dikecualikan daripada sandaran awan automatik Android.
-   **Apple Watch**: Pemindahan antara iPhone dan Apple Watch anda dikendalikan oleh Watch Connectivity Apple dan tidak melalui mana-mana pelayan pembangun. Apa yang disimpan pada Apple Watch terhad kepada teks paparan (tajuk terkini dalam setiap kategori); tiada audio disimpan.
-   Semua komunikasi dengan AI luaran disulitkan (HTTPS/TLS). Pelayan pembangun hanya menjadi perantara untuk permintaan penyusunan dan tidak menyimpan kandungan (tanpa keadaan/stateless).

## Perkara 10 (Penggunaan oleh Pengguna Bawah Umur)

Aplikasi ini dinilai 4+, tetapi sifatnya (penyusunan fikiran) mengandaikan kebolehan membaca dan menulis. Pengguna bawah umur harus menggunakannya dengan kebenaran penjaga mereka.

## Perkara 11 (Perubahan pada Dasar Privasi Ini)

Dasar ini mungkin dikemas kini disebabkan oleh perubahan dalam undang-undang, penambahan ciri, atau perubahan pada kerangka atau spesifikasi dasar setiap platform (Apple / Google). Perubahan penting akan diumumkan melalui kemas kini aplikasi atau di halaman awam dasar ini.

## Perkara 12 (Hubungi Kami)

Untuk pertanyaan mengenai dasar ini, sila hubungi kami melalui bahagian "Pembangun" di halaman App Store atau Google Play Aplikasi, atau melalui "Tetapan → Hubungi Kami" di dalam Aplikasi.

## Perkara 13 (Mengenai Iklan dan App Tracking Transparency)

Apabila anda tidak melanggan KUU+, Aplikasi ini memaparkan satu slot iklan natif antara bahagian dalam skrin "Apa yang dituturkan", yang disampaikan oleh Google AdMob. Iklan dipaparkan secara sederhana agar selaras dengan suasana KUU.

-   **Kandungan tuturan anda tidak sekali-kali digunakan untuk iklan.** Iklan tidak merujuk kepada transkripsi, hasil penyusunan, atau tema anda.
-   Untuk penyampaian iklan, Google AdMob mungkin mengumpul pengecam peranti (termasuk IDFA), ID pengiklanan, lokasi kasar, diagnostik, dan interaksi produk (interaksi berkaitan iklan dalam Aplikasi).
-   **iOS**: Gesaan **App Tracking Transparency** (ATT) dipaparkan sekali, sejurus sebelum iklan pertama. Iklan masih akan ditunjukkan jika anda menolak, tetapi maklumat yang dihantar kepada Google adalah terhad (tidak diperibadikan). Anda boleh menukar kebenaran ATT pada bila-bila masa dalam "Tetapan → Privasi & Keselamatan → Penjejakan" di iOS.
-   **Android**: ATT adalah ciri khusus iOS dan tidak wujud pada Android. Sebaliknya, **ID Pengiklanan** Google digunakan untuk penyampaian iklan. Anda boleh menarik diri daripada pemperibadian iklan atau menetapkan semula ID Pengiklanan anda dari "Tetapan → Privasi → Iklan" peranti anda (ayat mungkin berbeza mengikut peranti dan versi Android). Versi Android juga mematuhi pengurusan persetujuan (UMP) yang ditunjukkan di rantau yang berkenaan seperti EU.
-   **Melanggan KUU+ akan menghentikan semua iklan dan penghantaran data yang berkaitan dengannya.**
-   Untuk butiran mengenai pengendalian data oleh AdMob, sila lihat [dasar privasi Google AdMob](https://support.google.com/admob/answer/6128543).

## Perkara 14 (Mengenai Penggunaan Firebase Analytics / Crashlytics)

**Model ikut serta dalam Perkara ini terpakai pada versi iOS. Untuk versi Android, sila lihat "Mengenai versi Android" di akhir Perkara ini.**

**Pada iOS**, untuk penambahbaikan kualiti aplikasi dan kesedaran segera mengenai insiden pengeluaran, Aplikasi ini mungkin menggunakan Firebase Analytics Google (isyarat penggunaan agregat) dan Firebase Crashlytics (laporan kerosakan). **Ciri ini MATI secara lalai (tiada data dihantar) dan hanya beroperasi apabila anda secara eksplisit memilih ikut serta melalui "Tetapan → Data & Diagnostik".**

-   **Maklumat yang dihantar**:
    -   ID pemasangan tanpa nama yang dikeluarkan secara automatik oleh Firebase (berdasarkan IDFV; bukan pengecam peribadi secara langsung)
    -   Isyarat peristiwa dalam aplikasi agregat (penyelesaian sesi rakaman, paparan / penukaran paywall, penyelesaian Onboarding dsb. Nilai berangka dikelompokkan ke dalam granulariti kasar.)
    -   Jejak tindanan kerosakan (symbolicated crash stack traces) apabila Aplikasi ditamatkan secara tidak normal
-   **Maklumat yang tidak dihantar**: Kandungan tuturan anda (audio), transkripsi, teks hasil penyusunan AI, dan nama tema yang anda tetapkan **direka bentuk pada peringkat teknikal untuk tidak boleh dihantar** (API pelaksanaan menghalang penghantaran nilai rentetan kepada SDK analitik).
-   **Semasa ikut serta MATI, tiada sebarang komunikasi dengan Firebase berlaku sama sekali** (termasuk semua kategori di atas).
-   **Cara menghentikan penghantaran**: Tukar togol "Tetapan → Data & Diagnostik" kepada MATI pada bila-bila masa. Apabila dimatikan, ID pemasangan yang lalu akan dibuang dan sebarang log kerosakan yang belum dihantar yang disimpan pada peranti akan dipadam.
-   Penerima ialah Google LLC (Amerika Syarikat). [Maklumat Privasi Firebase](https://firebase.google.com/support/privacy) Google terpakai.

**Mengenai versi Android:** Versi Android menggunakan Firebase Analytics untuk menghantar **peristiwa penggunaan bebas kandungan** bagi penambahbaikan produk (nilai terkelompok seperti peralihan skrin dan kiraan penggunaan ciri) serta ID Instans Aplikasi tanpa nama yang dikeluarkan oleh Firebase. **Tidak seperti iOS, ini diaktifkan secara lalai.** Kandungan tuturan anda (audio), transkripsi, teks hasil penyusunan, dan nama tema **tidak boleh dihantar** — API SDK analitik direka bentuk supaya nilai rentetan tidak boleh dihantar kepadanya. **Versi Android tidak menyertakan Crashlytics dan tidak menghantar sebarang laporan kerosakan.** Penerima ialah Google LLC (Amerika Syarikat); [Maklumat Privasi Firebase](https://firebase.google.com/support/privacy) Google terpakai.
