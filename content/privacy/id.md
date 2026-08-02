> Ini adalah terjemahan referensi untuk kemudahan Anda. Versi bahasa Jepang adalah teks yang berwenang.

# Kebijakan Privasi KUU

Terakhir diperbarui: 2 Agustus 2026

**Singkatnya:** Apa yang Anda ucapkan adalah milik Anda. **Aplikasi ini tidak pernah mengirimkan data suara Anda ke mana pun**. Di perangkat iPhone dan Android, transkripsi juga dilakukan di dalam perangkat. **Versi Apple Watch dari aplikasi ini tidak melakukan perekaman sama sekali**—ia hanya menerima teks yang dihasilkan oleh input standar watchOS (dikte, tulisan tangan, atau keyboard); saat Anda memilih dikte, proses mendengarkan ditangani oleh sistem Apple (lihat Pasal 3). Penataan (klasifikasi AI) menggunakan AI eksternal, tetapi hanya teks hasil transkripsi yang dikirim. Teks tersebut hanya digunakan untuk penataan dan tidak disimpan. Data disimpan hanya di perangkat Anda, dan untuk versi iOS juga di database pribadi iCloud Anda (versi Android hanya menyimpan di perangkat). Pengembang tidak menyimpan konten Anda dan tidak dapat melihat apa yang diterima. Anda dapat menghapus semua data dari dalam aplikasi kapan saja. Aplikasi hanya melakukan **komunikasi jaringan minimal** untuk penagihan (StoreKit di iOS / RevenueCat di Android) dan iklan Google AdMob, dan informasi tersebut tidak pernah menyertakan apa yang Anda ucapkan (iklan dapat dinonaktifkan dengan berlangganan KUU+). Kami mengukur penggunaan untuk meningkatkan kualitas, tetapi ini juga tidak pernah menyertakan apa yang Anda ucapkan (iOS memerlukan persetujuan pengguna (opt-in); Android mengirimkan pengukuran bebas-konten secara default — lihat Pasal 14).

---

## Pasal 1 (Prinsip Dasar)

Aplikasi "KUU" (selanjutnya disebut "Aplikasi") adalah aplikasi yang membantu Anda mengeluarkan dan menata pemikiran di kepala Anda dengan menyuarakannya. **Tersedia dalam versi iOS (iPhone dan Apple Watch) dan Android**, dan kebijakan ini berlaku untuk keduanya. Aplikasi ini hanya menangani informasi dalam lingkup minimum yang diperlukan untuk menyediakan fiturnya, dengan memprioritaskan perlindungan privasi pengguna.

## Pasal 2 (Informasi yang Diperoleh dan Disimpan)

Informasi yang ditangani oleh Aplikasi ini terbatas pada hal-hal berikut:

1.  **Konten yang Anda ucapkan (data audio)** — Audio yang direkam disimpan sementara di area lokal perangkat hanya selama proses transkripsi, dan segera dihapus setelah proses selesai. Data ini tidak dikirim ke server mana pun. **Versi Apple Watch dari aplikasi ini tidak melakukan perekaman sama sekali** (lihat Pasal 3).
2.  **Hasil transkripsi dan penataan (teks)** — Disimpan agar Anda dapat meninjaunya kembali (versi iOS: di perangkat dan database pribadi iCloud Anda; versi Android: hanya di perangkat. Di Apple Watch yang terhubung, hanya judul terbaru dari setiap kategori yang disimpan untuk keperluan tampilan. Lihat Pasal 4).
3.  **Pengaturan dalam aplikasi** — Nilai pengaturan yang diperlukan untuk pengoperasian aplikasi, seperti tema, ukuran teks, dan status ketinggian air di kepala.

Aplikasi ini tidak memperoleh informasi pribadi seperti nama, alamat email, nomor telepon, informasi lokasi, kontak, kalender, foto, atau pengidentifikasi perangkat.

## Pasal 3 (Tentang Pengenalan Suara dan Klasifikasi AI)

**Pengenalan suara (transkripsi)**, pada perangkat iPhone (versi iOS) dan Android, sepenuhnya diselesaikan di perangkat Anda (untuk versi Apple Watch, silakan lihat bagian akhir Pasal ini).

-   Pengenalan suara: Menggunakan kerangka kerja Speech dari Apple (di perangkat). Data suara Anda sendiri tidak pernah dikirim ke luar perangkat.

**Klasifikasi AI (kategorisasi)** menggunakan AI eksternal.

-   Yang dikirim hanyalah **konten dalam bentuk teks (teks transkripsi)**. Data suara tidak dikirim.
-   Tujuan pengiriman adalah AI eksternal, melalui server pengembang (melalui backend ke Gemini milik Google).
-   Konten yang dikirim **hanya digunakan untuk klasifikasi dan tidak disimpan**. Konten tersebut juga tidak digunakan untuk melatih AI.
-   Yang dikirim mencakup tidak hanya konten yang diucapkan dan ditranskripsi, tetapi juga konten yang Anda ketik atau edit secara manual. Jika penetapan tema otomatis (KUU+, pengaturan opsional) diaktifkan, judul, isi, dan nama tema dari item yang sudah tersimpan juga akan dikirim untuk tujuan penetapan (semua ini hanya digunakan untuk klasifikasi dan tidak disimpan).
-   Pada **versi iOS** aplikasi sebelum 2.3.0, Anda dapat memilih klasifikasi yang hanya berjalan di perangkat melalui pengaturan "Di Perangkat" (pengaturan ini tidak lagi ditawarkan sejak versi 2.3.0).

**Tentang versi Android:** Versi Android tidak menawarkan metode penataan (klasifikasi) yang sepenuhnya berjalan di perangkat. Saat Anda melakukan penataan, teks hasil transkripsi **selalu** dikirim ke AI eksternal (Gemini milik Google melalui backend kami). Hanya konten dalam bentuk teks yang dikirim—data suara Anda sendiri tidak pernah dikirim, dan teks yang dikirim hanya digunakan untuk klasifikasi, tidak disimpan, dan tidak digunakan untuk melatih AI. Proses transkripsi (pengenalan suara) itu sendiri sepenuhnya berjalan di perangkat.

**Tentang versi Apple Watch:** Versi Apple Watch dari aplikasi ini tidak melakukan perekaman audio maupun pengenalan suara. Input menggunakan input teks standar watchOS (pengguna memilih antara dikte, tulisan tangan, atau keyboard), dan Aplikasi ini hanya menerima teks hasilnya. Saat Anda memilih dikte, pengenalan suara dijalankan sebagai fitur Apple (watchOS); prosesnya—termasuk apakah terjadi di perangkat atau dikirim ke server Apple—tergantung pada perangkat, pengaturan, dan bahasa Anda, serta **diatur oleh kebijakan privasi Apple**. Aplikasi ini tidak dapat mengakses data audio tersebut, dan tidak pernah menerimanya atau menyimpannya. Teks yang diterima akan ditangani sama seperti teks yang Anda ucapkan di iPhone (klasifikasi AI berdasarkan Pasal ini; penyimpanan berdasarkan Pasal 4).

## Pasal 4 (Penyimpanan dan Sinkronisasi)

**Versi iOS:** Hasil transkripsi dan penataan disimpan secara eksklusif di **database pribadi iCloud** Anda (CloudKit Private Database). Ini adalah penyimpanan yang disediakan Apple yang hanya dapat diakses oleh Anda sendiri. Pengembang Aplikasi ini tidak dapat melihat maupun mengambil konten yang tersimpan. Penggunaan iCloud tunduk pada kebijakan privasi Apple.

**Versi Android:** Hasil transkripsi dan penataan disimpan **hanya di perangkat ini**. Tidak ada sinkronisasi cloud otomatis. Saat berganti perangkat, Anda dapat mengekspor data ke file dari menu "Suara & Data" di dalam aplikasi dan mengimpornya di perangkat baru. Anda sendiri yang memilih tujuan ekspor file tersebut (di perangkat, di aplikasi penyimpanan cloud Anda, dll.). Pengembang tidak dapat mengakses file tersebut.

**Versi Apple Watch:** Untuk keperluan tampilan, sebagian hasil penataan Anda (judul terbaru dari setiap kategori) ditransfer ke Apple Watch Anda yang terhubung melalui komunikasi antar-perangkat dari Apple (Watch Connectivity) dan **juga disimpan di dalam Apple Watch**. Teks yang Anda masukkan di Apple Watch juga ditransfer ke iPhone Anda dengan mekanisme yang sama. Server pengembang tidak terlibat dalam proses transfer atau penyimpanan ini.

## Pasal 5 (Tujuan Penggunaan)

Informasi yang ditangani hanya digunakan untuk tujuan berikut:

1.  Menghasilkan transkripsi dari suara Anda dan menampilkannya kepada Anda
2.  Mengklasifikasikan transkripsi ke dalam kategori "Lihat Sekarang / Pikirkan Nanti / Simpan Dulu / Lepaskan" dan menampilkannya kepada Anda
3.  Menyimpan dan menampilkan konten yang pernah Anda ucapkan agar Anda dapat meninjaunya kembali
4.  Mempertahankan nilai pengaturan yang diperlukan untuk pengoperasian aplikasi

## Pasal 6 (Penggunaan Layanan Eksternal)

Aplikasi ini menggunakan layanan eksternal berikut untuk menyediakan fiturnya. **Data suara Anda sendiri tidak dikirim ke layanan mana pun.**

-   **iCloud / CloudKit** (Hanya versi iOS. Disediakan oleh Apple. Menyimpan dan menyinkronkan hanya ke database pribadi Anda)
-   **Pengenalan Suara** (versi iOS: kerangka kerja Speech dari Apple; versi Android: mesin pengenalan suara di perangkat. Keduanya berjalan di perangkat; data suara Anda tidak pernah dikirim ke luar perangkat. **Versi Apple Watch tidak melakukan pengenalan suara sendiri dan menggunakan input standar watchOS**. Lihat Pasal 3)
-   **Input teks standar watchOS** (Hanya versi Apple Watch. Disediakan oleh Apple. Pengguna memilih antara dikte, tulisan tangan, atau keyboard. Saat dikte dipilih, pengenalan suara dijalankan sebagai fitur Apple dan diatur oleh kebijakan privasi Apple. Aplikasi ini tidak dapat mengakses audio tersebut. Lihat Pasal 3)
-   **Watch Connectivity** (Hanya versi Apple Watch. Disediakan oleh Apple. Mengirimkan teks untuk keperluan tampilan secara langsung antara iPhone dan Apple Watch Anda. Server pengembang tidak terlibat. Lihat Pasal 4)
-   **AI eksternal (cloud)** (Klasifikasi AI. Hanya konten dalam bentuk teks yang dikirim; hanya digunakan untuk klasifikasi, tidak pernah disimpan, dan tidak pernah digunakan untuk melatih AI. Lihat Pasal 3)
-   **Layanan penagihan** (versi iOS: **Apple StoreKit**; versi Android: **RevenueCat**. Untuk mengelola pembelian, perpanjangan, pembatalan, dan status langganan KUU+. Konten yang diucapkan tidak dikirim. Untuk RevenueCat, lihat Pasal 7 dan [Kebijakan Privasi RevenueCat](https://www.revenuecat.com/privacy))
-   **Play Integrity API (melalui Firebase App Check; hanya versi Android)** (Untuk memverifikasi bahwa permintaan ke API klasifikasi berasal dari aplikasi yang sah—sebuah atestasi integritas perangkat/aplikasi. Tidak berisi konten yang diucapkan maupun informasi yang mengidentifikasi pengguna)
-   **Google AdMob (Google Mobile Ads SDK)** (Hanya saat langganan KUU+ tidak aktif: menampilkan satu slot iklan native di antara bagian-bagian pada layar "Yang Telah Diucapkan". Konten yang diucapkan tidak dikirim. Lihat Pasal 13)
-   **Firebase Analytics** (Disediakan oleh Google. Untuk peningkatan kualitas aplikasi. Pada iOS, **hanya digunakan jika Anda secara eksplisit menyetujuinya (opt-in) melalui Pengaturan**; pada Android, event penggunaan bebas-konten dikirim **secara default** (dalam kedua kasus, konten yang diucapkan tidak dikirim). iOS juga menggunakan **Crashlytics** dengan basis opt-in, tetapi **versi Android tidak menyertakan Crashlytics**. Lihat Pasal 14)

Server Aplikasi ini bersifat minimal dan stateless, hanya berfungsi sebagai perantara untuk permintaan klasifikasi AI (tidak ada konten yang disimpan). Aplikasi ini tidak menggunakan layanan otentikasi yang memerlukan akun pribadi.

## Pasal 7 (Pengungkapan kepada Pihak Ketiga)

Pengembang Aplikasi ini tidak memiliki sarana untuk mengakses konten yang Anda ucapkan, hasil transkripsi, atau hasil penataan Anda, dan tidak akan mengungkapkannya kepada pihak ketiga mana pun.

Untuk tujuan menayangkan iklan kepada pengguna yang tidak berlangganan KUU+, informasi yang diperlukan oleh Google AdMob untuk penayangan iklan—termasuk pengidentifikasi perangkat, ID iklan, bahasa dan wilayah perangkat, lokasi kasar, dan data interaksi iklan—dikirim ke Google (lihat Pasal 13; kebijakan privasi AdMob dari Google berlaku). Selama KUU+ aktif, transmisi informasi ini tidak terjadi.

Saat Anda berlangganan KUU+ pada **versi Android**, informasi pembelian (ID produk, harga, tanggal pembelian, dll.) dikirim ke RevenueCat, Inc. untuk mengelola pembelian dan hak langganan Anda (aktif/tidak aktif). Konten yang diucapkan tidak dikirim. Silakan lihat [Kebijakan Privasi RevenueCat](https://www.revenuecat.com/privacy) untuk detailnya.

Informasi hanya akan diungkapkan jika diwajibkan oleh hukum, sesuai dengan prosedur yang ditetapkan.

## Pasal 8 (Penghapusan Data)

Anda dapat menghapus semua data kapan saja dari menu "Pengaturan → Suara & Data → Hapus apa yang tersimpan" di dalam aplikasi. Tindakan ini akan menghapus secara permanen data di perangkat (dan, pada versi iOS, juga data di Database Pribadi iCloud). Data yang telah dihapus tidak dapat dipulihkan.

Mencopot pemasangan (uninstall) Aplikasi akan menghapus data lokal. Pada iOS, data iCloud dapat dihapus melalui Pengaturan → ID Apple → iCloud → Kelola Penyimpanan. Versi Android hanya menyimpan data di perangkat, sehingga data akan terhapus saat aplikasi dicopot.

**Versi Apple Watch:** Saat Anda menghapus semua data, data tampilan yang telah ditransfer ke Apple Watch Anda akan diganti dengan konten kosong saat jam terhubung kembali. Menghapus aplikasi dari Apple Watch Anda juga akan menghapus data tampilan yang tersimpan di dalamnya.

## Pasal 9 (Tindakan Keamanan)

-   **Versi iOS**: File audio sementara selama perekaman dienkripsi oleh perlindungan file iOS (`FileProtectionType.complete`) dan tidak dapat diakses saat perangkat terkunci. Komunikasi dengan iCloud dienkripsi oleh Apple melalui SSL/TLS.
-   **Versi Android**: Audio yang direkam tidak pernah ditulis ke disk, bahkan sebagai file sementara; audio diproses hanya di dalam memori dan langsung dibuang setelah pengenalan selesai. Hasil transkripsi dan penataan yang tersimpan berada di area penyimpanan pribadi aplikasi, tidak dapat diakses oleh aplikasi lain, dan dikecualikan dari cadangan cloud otomatis Android.
-   **Versi Apple Watch**: Penyerahan data antara iPhone dan Apple Watch Anda ditangani oleh Watch Connectivity dari Apple dan tidak melalui server pengembang mana pun. Apa yang disimpan di Apple Watch terbatas pada teks untuk tampilan (judul terbaru dari setiap kategori); tidak ada audio yang disimpan.
-   Semua komunikasi dengan AI eksternal dienkripsi (HTTPS/TLS). Server pengembang hanya meneruskan permintaan penataan dan tidak menyimpan konten apa pun (stateless).

## Pasal 10 (Penggunaan oleh Anak di Bawah Umur)

Aplikasi ini diberi peringkat usia 4+, tetapi karena sifatnya (penataan pemikiran), aplikasi ini ditujukan untuk pengguna yang sudah dapat membaca dan menulis. Anak di bawah umur harus menggunakan aplikasi ini dengan persetujuan dari orang tua atau wali mereka.

## Pasal 11 (Perubahan pada Kebijakan Ini)

Kebijakan ini dapat diperbarui karena adanya perubahan undang-undang, penambahan fitur, atau perubahan pada kerangka kerja atau spesifikasi kebijakan setiap platform (Apple / Google). Perubahan signifikan akan diumumkan melalui pembaruan aplikasi atau di halaman publik kebijakan ini.

## Pasal 12 (Kontak)

Untuk pertanyaan mengenai kebijakan ini, silakan hubungi kami melalui bagian "Pengembang" di halaman aplikasi di App Store atau Google Play, atau melalui "Pengaturan → Kontak" di dalam aplikasi.

## Pasal 13 (Tentang Iklan dan App Tracking Transparency)

Saat Anda tidak berlangganan KUU+, Aplikasi ini menampilkan satu slot iklan native di antara bagian-bagian pada layar "Yang Telah Diucapkan", yang ditayangkan oleh Google AdMob. Iklan ditampilkan secara minimalis agar sesuai dengan nuansa KUU.

-   **Konten yang Anda ucapkan tidak pernah digunakan untuk iklan.** Iklan tidak mengacu pada hasil transkripsi, hasil penataan, atau tema Anda.
-   Untuk penayangan iklan, Google AdMob dapat mengumpulkan pengidentifikasi perangkat (termasuk IDFA), ID iklan, lokasi kasar (Coarse Location), data diagnostik, dan interaksi produk (interaksi terkait iklan di dalam Aplikasi).
-   **Versi iOS**: Permintaan **App Tracking Transparency** (ATT) akan ditampilkan satu kali, tepat sebelum iklan pertama. Iklan akan tetap ditampilkan jika Anda menolak, tetapi informasi yang dikirim ke Google akan dibatasi (non-personalisasi). Anda dapat mengubah izin ATT kapan saja di "Pengaturan → Privasi & Keamanan → Pelacakan" pada iOS.
-   **Versi Android**: ATT adalah mekanisme khusus iOS dan tidak ada di Android. Sebagai gantinya, **ID Iklan (Advertising ID)** dari Google digunakan untuk penayangan iklan. Anda dapat memilih untuk tidak menerima personalisasi iklan atau mengatur ulang ID Iklan Anda dari "Setelan → Privasi → Iklan" di perangkat Anda (istilah dapat bervariasi tergantung perangkat dan versi Android). Versi Android juga mematuhi manajemen persetujuan (UMP) yang ditampilkan di wilayah yang berlaku seperti Uni Eropa.
-   **Berlangganan KUU+ akan menghentikan semua iklan dan transmisi data terkait.**
-   Untuk detail tentang penanganan data oleh AdMob, silakan lihat [kebijakan privasi Google AdMob](https://support.google.com/admob/answer/6128543).

## Pasal 14 (Tentang Penggunaan Firebase Analytics / Crashlytics)

**Model persetujuan (opt-in) dalam Pasal ini berlaku untuk versi iOS. Untuk versi Android, silakan lihat "Tentang versi Android" di akhir Pasal ini.**

**Pada iOS**, untuk peningkatan kualitas aplikasi dan kesadaran langsung atas insiden produksi, Aplikasi ini dapat menggunakan Firebase Analytics dari Google (sinyal penggunaan agregat) dan Firebase Crashlytics (pelaporan kerusakan). **Fitur ini NONAKTIF secara default (tidak ada data yang dikirim) dan hanya beroperasi jika Anda secara eksplisit menyetujuinya (opt-in) melalui "Pengaturan → Data & Diagnostik".**

-   **Informasi yang dikirim**:
    -   ID instalasi anonim yang diterbitkan secara otomatis oleh Firebase (berdasarkan IDFV; bukan pengidentifikasi pribadi langsung)
    -   Sinyal event dalam aplikasi yang diagregasi (penyelesaian sesi perekaman, penayangan/konversi paywall, penyelesaian orientasi, dll. Nilai numerik dikelompokkan ke dalam granularitas kasar.)
    -   Jejak tumpukan (stack trace) kerusakan yang telah disimbolkan saat Aplikasi berhenti secara tidak normal
-   **Informasi yang tidak dikirim**: Konten yang Anda ucapkan (audio), hasil transkripsi, teks hasil klasifikasi AI, dan nama tema yang Anda atur **dibuat tidak dapat dikirim pada tingkat tipe data** (API implementasi mencegah penerusan nilai string ke SDK analitik).
-   **Selama persetujuan (opt-in) TIDAK diberikan, tidak ada komunikasi apa pun dengan Firebase yang terjadi** (termasuk semua kategori di atas).
-   **Cara menghentikan pengiriman**: Alihkan tombol di "Pengaturan → Data & Diagnostik" ke posisi OFF kapan saja. Saat dimatikan, ID instalasi sebelumnya akan dibuang dan semua log kerusakan yang belum terkirim yang tersimpan di perangkat akan dihapus.
-   Penerima data adalah Google LLC (Amerika Serikat). [Informasi Privasi Firebase](https://firebase.google.com/support/privacy) dari Google berlaku.

**Tentang versi Android:** Versi Android menggunakan Firebase Analytics untuk mengirim **event penggunaan bebas-konten** demi peningkatan produk (nilai yang dikelompokkan seperti transisi layar dan jumlah penggunaan fitur) beserta ID Instans Aplikasi anonim yang diterbitkan oleh Firebase. **Berbeda dengan iOS, fitur ini diaktifkan secara default.** Konten yang Anda ucapkan (audio), hasil transkripsi, teks hasil penataan, dan nama tema **tidak dapat dikirim**—API SDK analitik dirancang agar nilai string tidak dapat diteruskan ke dalamnya. **Versi Android tidak menyertakan Crashlytics dan tidak mengirimkan laporan kerusakan.** Penerima data adalah Google LLC (Amerika Serikat); [Informasi Privasi Firebase](https://firebase.google.com/support/privacy) dari Google berlaku.
