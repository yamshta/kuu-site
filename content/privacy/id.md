> Ini adalah terjemahan referensi untuk kemudahan Anda. Versi bahasa Jepang adalah teks yang otoritatif.

# Kebijakan Privasi KUU

Terakhir diperbarui: 21 Juli 2026

**Singkatnya:** Apa yang Anda ucapkan adalah milik Anda. **Suara Anda sendiri tidak akan pernah dikirim ke luar**. Transkripsi terjadi di dalam perangkat Anda. Pengorganisasian (klasifikasi AI) menggunakan AI eksternal, tetapi yang dikirimkan hanyalah teks hasil transkripsi, yang hanya digunakan untuk pengorganisasian dan tidak disimpan (versi iOS dapat diubah ke pengorganisasian hanya di perangkat melalui "Di Perangkat" pada Pengaturan. **Versi Android hanya mengirim ke AI eksternal dan tidak memiliki opsi pengorganisasian di perangkat**). Data disimpan di perangkat Anda, dan untuk versi iOS, juga di iCloud Anda (database privat) (versi Android hanya menyimpan di perangkat). Pengembang tidak menyimpan konten Anda dan tidak dapat melihat apa yang diterima. Anda dapat menghapus semua data dari dalam aplikasi kapan saja. Aplikasi hanya melakukan **komunikasi minimal yang diperlukan** untuk penagihan (iOS=StoreKit/Android=RevenueCat) dan iklan Google AdMob, dan informasi tersebut tidak pernah menyertakan apa yang Anda ucapkan (iklan dapat dinonaktifkan dengan berlangganan KUU+). Kami mengukur penggunaan untuk meningkatkan kualitas, tetapi ini juga tidak pernah menyertakan apa yang Anda ucapkan (iOS memerlukan persetujuan pengguna (opt-in), Android mengirimkan pengukuran bebas-konten secara default. Lihat Pasal 14 untuk detailnya).

---

## Pasal 1 (Kebijakan Dasar)

Aplikasi ini, "KUU" ("Aplikasi ini"), adalah aplikasi yang membantu Anda menuangkan dan mengorganisasi pikiran di kepala Anda dengan mengucapkannya. Terdapat **versi iOS dan Android**, dan kebijakan ini berlaku untuk keduanya. Aplikasi ini hanya memproses informasi dalam lingkup minimal yang diperlukan untuk menyediakan fungsinya, dengan memprioritaskan perlindungan privasi pengguna.

## Pasal 2 (Informasi yang Diperoleh dan Disimpan)

Informasi yang ditangani oleh Aplikasi ini terbatas pada hal-hal berikut:

1.  **Konten yang Anda ucapkan (data audio)** — Audio yang direkam disimpan sementara di area temporer perangkat hanya selama proses transkripsi, dan segera dihapus setelah proses selesai. Data ini tidak dikirim ke server mana pun.
2.  **Hasil transkripsi dan pengorganisasian (teks)** — Disimpan agar Anda dapat meninjaunya kembali (versi iOS: di perangkat dan di database privat iCloud Anda; versi Android: hanya di dalam perangkat. Lihat Pasal 4 untuk detailnya).
3.  **Pengaturan dalam aplikasi** — Nilai pengaturan yang diperlukan untuk pengoperasian aplikasi, seperti tema, ukuran teks, dan status level air di kepala.

Aplikasi ini tidak memperoleh informasi pribadi seperti nama, alamat email, nomor telepon, informasi lokasi, kontak, kalender, foto, atau pengidentifikasi perangkat.

## Pasal 3 (Mengenai Pengenalan Suara dan Klasifikasi AI)

**Pengenalan suara (transkripsi)** sepenuhnya dilakukan di dalam perangkat iOS Anda.

-   Pengenalan suara: Menggunakan kerangka kerja Speech dari Apple (di perangkat). Suara Anda sendiri tidak pernah dikirim ke luar perangkat.

**Klasifikasi AI (pengorganisasian)** menggunakan AI eksternal.

-   Yang dikirimkan **hanyalah konten dalam bentuk tulisan (teks transkripsi)**. Suara Anda tidak dikirimkan.
-   Tujuan pengiriman adalah AI eksternal, melalui server pengembang (melalui backend ke Gemini dari Google).
-   Konten yang dikirim **hanya digunakan untuk klasifikasi dan tidak disimpan**. Konten tersebut juga tidak digunakan untuk melatih AI.
-   **Versi iOS** dapat diubah kapan saja ke **klasifikasi hanya di perangkat** (FoundationModels dari Apple / aturan di perangkat) melalui "Di Perangkat" pada Pengaturan. Dalam kasus ini, teks juga tidak akan keluar dari perangkat.

**Tentang versi Android:** Versi Android tidak menyediakan metode pengorganisasian (klasifikasi) yang sepenuhnya berjalan di perangkat. Saat Anda melakukan pengorganisasian, teks hasil transkripsi **selalu** dikirim ke AI eksternal (Gemini dari Google melalui backend kami). Tidak ada opsi "Di Perangkat" seperti pada versi iOS. Yang dikirimkan hanyalah konten dalam bentuk tulisan, suara Anda sendiri tidak dikirimkan, dan teks yang dikirim hanya digunakan untuk klasifikasi, tidak disimpan, dan tidak digunakan untuk melatih AI. Proses transkripsi (pengenalan suara) itu sendiri sepenuhnya berjalan di perangkat.

## Pasal 4 (Penyimpanan dan Sinkronisasi)

**Versi iOS:** Hasil transkripsi dan pengorganisasian hanya disimpan di **database privat iCloud Anda** (CloudKit Private Database). Ini adalah penyimpanan yang disediakan oleh Apple, dan hanya Anda yang dapat mengakses konten yang tersimpan. Pengembang Aplikasi ini tidak dapat melihat atau mengambil konten yang tersimpan. Penggunaan iCloud tunduk pada kebijakan privasi Apple.

**Versi Android:** Hasil transkripsi dan pengorganisasian disimpan **hanya di perangkat ini**. Tidak ada sinkronisasi cloud otomatis. Saat berganti perangkat, Anda dapat mengekspor data ke file dari "Suara & Data" di dalam aplikasi, lalu mengimpornya di perangkat baru. Anda sendiri yang memilih tujuan ekspor (di dalam perangkat, aplikasi penyimpanan cloud yang Anda gunakan, dll.). Pengembang tidak dapat mengakses file ini.

## Pasal 5 (Tujuan Penggunaan)

Informasi yang ditangani hanya akan digunakan untuk tujuan berikut:

1.  Menghasilkan transkripsi dari suara dan menampilkannya kepada pengguna
2.  Mengklasifikasikan transkripsi ke dalam "Lihat Sekarang / Pikirkan Nanti / Simpan Dulu / Lepaskan" dan menampilkannya kepada pengguna
3.  Menyimpan dan menampilkan konten yang telah diucapkan pengguna di masa lalu agar dapat ditinjau kembali oleh pengguna
4.  Menyimpan nilai pengaturan yang diperlukan untuk pengoperasian aplikasi

## Pasal 6 (Penggunaan Layanan Eksternal)

Aplikasi ini menggunakan layanan eksternal berikut untuk menyediakan fungsinya. **Suara Anda sendiri tidak dikirim ke layanan mana pun.**

-   **iCloud / CloudKit** (hanya versi iOS. Disediakan oleh Apple. Hanya disimpan dan disinkronkan ke database privat Anda sendiri)
-   **Pengenalan suara** (versi iOS: kerangka kerja Speech dari Apple, versi Android: mesin pengenalan suara di perangkat. Keduanya berjalan di perangkat, suara tidak dikirim ke luar perangkat)
-   **AI eksternal (cloud)** (Klasifikasi AI. Hanya konten dalam bentuk tulisan yang dikirim. Hanya digunakan untuk klasifikasi, tidak disimpan, dan tidak digunakan untuk melatih AI. Pada versi iOS dapat dinonaktifkan melalui "Di Perangkat" pada Pengaturan, tetapi **versi Android hanya mengirim ke AI eksternal**. Lihat Pasal 3)
-   **FoundationModels** (hanya versi iOS. Disediakan oleh Apple. Berjalan sepenuhnya di perangkat. Digunakan saat pengaturan "Di Perangkat" aktif, atau sebagai cadangan saat AI eksternal tidak tersedia)
-   **Layanan penagihan** (versi iOS: **Apple StoreKit**, versi Android: **RevenueCat**. Untuk pembelian, perpanjangan, pembatalan, dan pengelolaan status langganan KUU+. Konten yang Anda ucapkan tidak dikirim. Mengenai RevenueCat, lihat Pasal 7 dan [Kebijakan Privasi RevenueCat](https://www.revenuecat.com/privacy))
-   **Play Integrity API (melalui Firebase App Check. Hanya versi Android)** (Atestasi integritas perangkat/aplikasi untuk memastikan permintaan ke API klasifikasi berasal dari aplikasi yang sah. Tidak mengandung konten yang Anda ucapkan atau informasi yang mengidentifikasi pengguna)
-   **Google AdMob (Google Mobile Ads SDK)** (Hanya saat tidak berlangganan KUU+, menampilkan 1 slot iklan native di antara bagian-bagian pada layar "Yang Telah Diucapkan". Konten yang Anda ucapkan tidak dikirim. Lihat Pasal 13 untuk detailnya)
-   **Firebase Analytics** (Disediakan oleh Google. Untuk peningkatan kualitas aplikasi. Pada versi iOS, **hanya jika pengguna secara eksplisit memilih ikut (opt-in) di Pengaturan**; pada versi Android, event penggunaan bebas-konten dikirim **secara default** (keduanya tidak mengirimkan konten yang Anda ucapkan). Versi iOS juga menggunakan **Crashlytics** dengan sistem opt-in, tetapi **versi Android tidak menyertakan Crashlytics**. Lihat Pasal 14 untuk detailnya)

Server Aplikasi ini bersifat minimal dan hanya berfungsi sebagai perantara untuk klasifikasi AI, serta tidak menyimpan konten apa pun (stateless). Kami tidak menggunakan layanan autentikasi yang memerlukan akun pribadi.

## Pasal 7 (Pemberian kepada Pihak Ketiga)

Pengembang Aplikasi ini tidak memiliki cara untuk mengakses konten yang Anda ucapkan, hasil transkripsi, atau hasil pengorganisasian, dan tidak akan memberikannya kepada pihak ketiga.

Untuk tujuan menayangkan iklan kepada pengguna yang tidak berlangganan KUU+, informasi yang diperlukan oleh Google AdMob untuk penayangan iklan akan dikirim ke Google. Informasi ini dapat mencakup pengidentifikasi perangkat, ID iklan, bahasa dan wilayah perangkat, perkiraan lokasi, dan informasi interaksi dengan iklan (lihat Pasal 13; kebijakan privasi AdMob dari Google berlaku). Selama Anda berlangganan KUU+, pengiriman informasi ini tidak akan terjadi.

Saat Anda berlangganan KUU+ pada **versi Android**, informasi pembelian (ID produk, harga, tanggal pembelian, dll.) akan dikirim ke RevenueCat, Inc. untuk memproses pembelian dan mengelola status langganan (aktif/tidak aktif). Konten yang Anda ucapkan tidak dikirim. Untuk detail penanganan data oleh RevenueCat, silakan tinjau [Kebijakan Privasi RevenueCat](https://www.revenuecat.com/privacy).

Kami hanya akan mengungkapkan informasi sesuai dengan prosedur yang ditetapkan jika diwajibkan oleh hukum.

## Pasal 8 (Penghapusan Data)

Pengguna dapat menghapus semua data kapan saja dari "Pengaturan → Suara & Data → Hapus yang tersimpan" di dalam aplikasi. Tindakan ini akan menghapus secara permanen data di perangkat (dan, pada versi iOS, juga data di database privat iCloud). Data yang telah dihapus tidak dapat dipulihkan.

Saat Anda menghapus instalan Aplikasi ini, data di perangkat akan dihapus. Untuk versi iOS, data di iCloud dapat dihapus melalui Pengaturan Apple (Pengaturan → Apple ID → iCloud → Kelola Penyimpanan). Karena versi Android hanya menyimpan data di perangkat, data akan terhapus saat aplikasi dihapus instalannya.

## Pasal 9 (Tindakan Pengamanan)

-   **Versi iOS**: File audio sementara selama perekaman dienkripsi oleh fitur perlindungan file iOS (`FileProtectionType.complete`) dan tidak dapat diakses saat perangkat terkunci. Komunikasi dengan iCloud dienkripsi oleh Apple menggunakan SSL/TLS.
-   **Versi Android**: Audio yang direkam tidak ditulis ke disk, bahkan sebagai file sementara; audio hanya diproses di memori dan langsung dibuang setelah proses pengenalan selesai. Hasil transkripsi dan pengorganisasian yang disimpan berada di area penyimpanan khusus aplikasi Android dan tidak dapat diakses oleh aplikasi lain. Data ini juga dikecualikan dari cadangan cloud otomatis Android.
-   Semua komunikasi dengan AI eksternal dienkripsi (HTTPS/TLS). Server pengembang hanya berfungsi sebagai perantara untuk klasifikasi dan tidak menyimpan konten (stateless).

## Pasal 10 (Penggunaan oleh Anak di Bawah Umur)

Aplikasi ini memiliki peringkat usia 4+, tetapi karena sifatnya untuk mengorganisasi pikiran, aplikasi ini ditujukan untuk pengguna yang sudah dapat membaca dan menulis. Jika digunakan oleh anak di bawah umur, harap gunakan dengan persetujuan dari orang tua atau wali.

## Pasal 11 (Perubahan Kebijakan Privasi)

Kebijakan ini dapat direvisi karena perubahan undang-undang, penambahan fitur, atau perubahan spesifikasi kerangka kerja atau kebijakan dari setiap platform (Apple / Google). Jika ada perubahan penting, kami akan memberitahukannya saat pembaruan aplikasi atau di halaman publikasi kebijakan ini.

## Pasal 12 (Kontak)

Untuk pertanyaan mengenai kebijakan ini, silakan hubungi kami melalui bagian "Pengembang" di halaman aplikasi di App Store atau Google Play, atau melalui "Pengaturan → Kontak" di dalam aplikasi.

## Pasal 13 (Mengenai Iklan dan App Tracking Transparency)

Selama Anda tidak berlangganan KUU+, Aplikasi ini hanya akan menampilkan satu slot iklan native dari Google AdMob di antara bagian-bagian pada layar "Yang Telah Diucapkan". Iklan itu sendiri ditampilkan secara halus di antara bagian layar untuk menjaga suasana KUU.

-   **Konten yang Anda ucapkan tidak akan pernah digunakan untuk iklan** (iklan tidak mengacu pada hasil transkripsi, klasifikasi, atau tema).
-   Untuk menayangkan iklan, Google AdMob dapat mengumpulkan pengidentifikasi perangkat (termasuk IDFA), ID iklan, Coarse Location (perkiraan lokasi), Diagnostics, dan Product Interaction (informasi interaksi dengan iklan di dalam aplikasi).
-   **Versi iOS**: Permintaan **App Tracking Transparency** (ATT) akan ditampilkan satu kali, tepat sebelum iklan pertama muncul. Iklan akan tetap ditampilkan meskipun Anda menolak, tetapi informasi yang dikirim ke Google akan terbatas (tanpa personalisasi). Status izin ATT dapat diubah kapan saja di "Pengaturan" → "Privasi & Keamanan" → "Pelacakan" pada iOS.
-   **Versi Android**: ATT adalah mekanisme khusus iOS dan tidak ada di Android. Sebagai gantinya, **ID Iklan (Advertising ID)** dari Google digunakan untuk penayangan iklan. Anda dapat memilih untuk tidak menerima personalisasi iklan atau mengatur ulang ID iklan Anda dari "Pengaturan → Privasi → Iklan" di perangkat Anda (istilah dapat bervariasi tergantung pada perangkat dan versi Android). Selain itu, versi Android mematuhi manajemen persetujuan (UMP) yang ditampilkan di wilayah yang berlaku seperti Uni Eropa.
-   **Berlangganan KUU+ akan menghentikan semua iklan dan pengiriman data terkait.**
-   Untuk detail mengenai penanganan data oleh Google AdMob, silakan tinjau [Kebijakan privasi Google AdMob](https://support.google.com/admob/answer/6128543).

## Pasal 14 (Mengenai Penggunaan Firebase Analytics / Crashlytics)

**Sistem opt-in pada pasal ini berlaku untuk versi iOS. Untuk versi Android, silakan lihat "Tentang versi Android" di akhir pasal ini.**

**Versi iOS**, untuk meningkatkan kualitas aplikasi dan mengetahui insiden produksi secara langsung, dapat menggunakan Firebase Analytics (agregasi penggunaan) dan Firebase Crashlytics (laporan kerusakan) dari Google. **Fitur ini secara default NONAKTIF (tidak ada data yang dikirim) dan hanya berfungsi jika pengguna secara eksplisit memilih ikut (opt-in) melalui "Pengaturan → Data & Diagnostik".**

-   **Informasi yang dikirim**:
    -   ID instalasi anonim yang diterbitkan secara otomatis oleh Firebase (berdasarkan IDFV; bukan pengidentifikasi yang secara langsung mengidentifikasi individu).
    -   Sinyal agregat dari event tindakan dalam aplikasi (misalnya, penyelesaian sesi rekaman, tampilan/konversi Paywall, penyelesaian Onboarding. Nilai numerik dikirim dalam granularitas kasar yang dikelompokkan).
    -   Jejak tumpukan (stack trace) kerusakan yang telah disimbolkan saat aplikasi berhenti secara tidak normal.
-   **Informasi yang tidak dikirim**: Konten yang Anda ucapkan (audio), hasil transkripsi, teks hasil klasifikasi AI, dan nama tema yang Anda atur **dirancang agar tidak dapat dikirim pada level tipe data** (secara implementasi, API-nya tidak memungkinkan nilai string diteruskan ke SDK pengukuran).
-   **Selama tidak diaktifkan (opt-in), tidak ada komunikasi apa pun dengan Firebase yang terjadi**, termasuk semua informasi di atas.
-   **Cara menghentikan pengiriman**: Anda dapat menonaktifkannya kapan saja dengan mematikan tombol di "Pengaturan → Data & Diagnostik". Saat dinonaktifkan, ID instalasi sebelumnya akan dibuang, dan log kerusakan yang belum terkirim yang tersimpan di perangkat lokal juga akan dihapus.
-   Penerima data adalah Google LLC (Amerika Serikat). [Informasi Privasi Firebase](https://firebase.google.com/support/privacy) dari Google berlaku.

**Tentang versi Android:** Versi Android menggunakan Firebase Analytics dan mengirimkan **event penggunaan bebas-konten** untuk peningkatan produk (nilai yang dikelompokkan seperti transisi layar dan jumlah penggunaan fitur) beserta App Instance ID anonim yang diterbitkan oleh Firebase. **Berbeda dengan iOS, fitur ini aktif secara default.** Konten yang Anda ucapkan (audio), hasil transkripsi, teks hasil pengorganisasian, dan nama tema **tidak dapat dikirim** karena desain SDK pengukuran yang tidak memungkinkan nilai string diteruskan. **Versi Android tidak menyertakan Crashlytics dan tidak mengirimkan laporan kerusakan.** Penerima data adalah Google LLC (Amerika Serikat); [Informasi Privasi Firebase](https://firebase.google.com/support/privacy) dari Google berlaku.
