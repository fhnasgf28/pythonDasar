Dokumentasi Fungsi: Kalkulasi Stok Minimum Otomatis
(_onchange_run_rate_type)
1. Gambaran Umum (Non-Teknis)
Bayangkan Anda mengelola stok susu di kulkas. Anda tentu tidak menunggu sampai susu habis total baru membeli lagi, bukan? Anda mungkin akan membeli lagi ketika susu tersisa 1 kotak. "1 kotak" inilah yang kita sebut Stok Minimum.

Fungsi kode ini adalah kalkulator otomatis untuk menentukan "Stok Minimum" (product_min_qty) tersebut di Odoo.

Setiap kali Anda mengubah Metode Perhitungan (misalnya, "Berdasarkan data Tahun Lalu" atau "Berdasarkan data 30 Hari Terakhir"), kalkulator ini akan langsung menghitung ulang berapa stok minimum yang ideal untuk produk tersebut.

2. Konsep Perhitungan: "Stok Minimum"
Secara konseptual, kode ini menghitung Stok Minimum menggunakan rumus sederhana:

Stok Minimum = (Kebutuhan Stok Pemesanan) + (Stok Pengaman)

Mari kita bedah masing-masing bagian:

Stok Pengaman (Safety Stock) Ini adalah stok "cadangan" Anda untuk berjaga-jaga jika ada keterlambatan pengiriman atau lonjakan permintaan. Anda bisa menentukannya dengan dua cara:

Jumlah Tetap (fix_qty): Misal, Anda selalu ingin ada cadangan 20 unit.

Persentase (percentage): Misal, Anda ingin cadangan 50% dari rata-rata penjualan harian.

Kebutuhan Stok Pemesanan (Replenishment Demand) Ini adalah jumlah stok yang akan Anda gunakan selama menunggu pesanan baru datang. Kode ini menghitungnya dengan rumus:

Rata-rata Penjualan Harian * (Waktu Tunggu + 1 Hari)

Rata-rata Penjualan Harian (run_rate_qty): Berapa unit produk yang terjual setiap hari (berdasarkan data tahun lalu atau beberapa hari terakhir).

Waktu Tunggu (lead_days): Berapa hari yang dibutuhkan sejak Anda memesan barang sampai barang itu tiba di gudang.

+ 1 Hari: Kode ini menambahkan 1 hari ekstra ke waktu tunggu. Ini bisa dianggap sebagai buffer tambahan untuk hari pemrosesan pesanan atau sebagai bagian dari strategi inventori.

3. Skenario dan Contoh Perhitungan
Mari kita gunakan data contoh yang konsisten:

Waktu Tunggu (lead_days): 5 hari (Butuh 5 hari dari PO sampai barang datang)

Rata-rata Penjualan (Tahun Lalu): 10 unit / hari

Rata-rata Penjualan (30 Hari Terakhir): 12 unit / hari

Skenario A: Data TAHUN LALU + Stok Pengaman JUMLAH TETAP
Anda memilih run_rate_type = 'get_last_year' dan safety_stock_select = 'fix_qty'.

Stok Pengaman (safety_stock): Anda isi 20 unit.

Perhitungan:

Rata-rata Penjualan Harian: Dipakai data tahun lalu = 10 unit/hari.

Kebutuhan Stok Pemesanan: 10 unit * (5 hari + 1 hari) = 60 unit.

Stok Pengaman: Anda tentukan = 20 unit.

Total Stok Minimum: 60 + 20 = 80 unit.

Maka, Odoo akan menyarankan Anda memesan barang lagi ketika stok di gudang mencapai 80 unit.

Skenario B: Data TAHUN LALU + Stok Pengaman PERSENTASE
Anda memilih run_rate_type = 'get_last_year' dan safety_stock_select = 'percentage'.

Stok Pengaman (safety_stock): Anda isi 50%.

Perhitungan:

Rata-rata Penjualan Harian: Dipakai data tahun lalu = 10 unit/hari.

Kebutuhan Stok Pemesanan: 10 unit * (5 hari + 1 hari) = 60 unit.

Stok Pengaman (Persen): 50% dari 10 unit (rata-rata penjualan) = 5 unit.

Total Stok Minimum: 60 + 5 = 65 unit.

Maka, Odoo akan menyarankan Anda memesan barang lagi ketika stok di gudang mencapai 65 unit.

Skenario C: Data HARI TERAKHIR + Stok Pengaman JUMLAH TETAP
Anda memilih run_rate_type = 'get_past_days_data' dan safety_stock_select = 'fix_qty'.

Stok Pengaman (safety_stock): Anda isi 20 unit.

Perhitungan:

Rata-rata Penjualan Harian: Dipakai data 30 hari terakhir = 12 unit/hari.

Kebutuhan Stok Pemesanan: 12 unit * (5 hari + 1 hari) = 72 unit.

Stok Pengaman: Anda tentukan = 20 unit.

Total Stok Minimum: 72 + 20 = 92 unit.

Maka, Odoo akan menyarankan Anda memesan barang lagi ketika stok di gudang mencapai 92 unit.

Skenario D: Data HARI TERAKHIR + Stok Pengaman PERSENTASE
Anda memilih run_rate_type = 'get_past_days_data' dan safety_stock_select = 'percentage'.

Stok Pengaman (safety_stock): Anda isi 50%.

Perhitungan:

Rata-rata Penjualan Harian: Dipakai data 30 hari terakhir = 12 unit/hari.

Kebutuhan Stok Pemesanan: 12 unit * (5 hari + 1 hari) = 72 unit.

Stok Pengaman (Persen): 50% dari 12 unit (rata-rata penjualan) = 6 unit.

Total Stok Minimum: 72 + 6 = 78 unit.

Maka, Odoo akan menyarankan Anda memesan barang lagi ketika stok di gudang mencapai 78 unit.

4. Detail Teknis (Untuk Developer)
Fungsi: _onchange_run_rate_type(self)

Trigger (Pemicu): Fungsi ini idealnya dipanggil oleh @api.onchange pada field run_rate_type. Secara logika, field lain seperti safety_stock_select, safety_stock, dan lead_days juga harus memicu fungsi ini agar perhitungan tetap akurat saat diubah.

Tujuan: Menghitung dan mengisi nilai untuk dua field:

self.run_rate_qty: Diisi dengan rata-rata penjualan harian yang relevan (dari tahun lalu atau hari terakhir).

self.product_min_qty: Diisi dengan hasil kalkulasi akhir stok minimum.

Logika Rumus:

Replenishment Demand dihitung sebagai: (run_rate_qty * (self.lead_days if self.lead_days else 1)) + (run_rate_qty if self.lead_days >= 1 else 0) Ini adalah cara yang sedikit rumit untuk mengatakan run_rate_qty * (lead_days + 1) (dengan asumsi lead_days tidak pernah negatif).

Safety Stock ditambahkan setelahnya:

Jika fix_qty: + self.safety_stock

Jika percentage: + ((average_qty * self.safety_stock) / 100)

Catatan:

Baris print('ini adalah onchange yang mantap banget sih') adalah debug statement dan sebaiknya dihapus pada kode produksi.

Ada beberapa baris kode yang dikomentari (#) terkait penyesuaian self.lead_days. Saat ini, logika tersebut tidak aktif.

5. Penjelasan Kode Per Baris (Berdasarkan Kondisi)
Fungsi ini pada dasarnya adalah sebuah "kalkulator" yang aktif setiap kali Anda mengubah Metode Perhitungan (run_rate_type).

Penjelasan Awal
Python

def _onchange_run_rate_type(self):
    print('ini adalah onchange yang mantap banget sih')
Baris 1: Ini adalah nama fungsi/kalkulatornya.

Baris 2: Ini adalah pesan debug untuk programmer. Pesan ini akan muncul di log Odoo setiap kali fungsi ini berjalan. Ini aman untuk dihapus dan tidak memengaruhi perhitungan.

Kondisi Utama 1: "Saya ingin hitung berdasarkan DATA TAHUN LALU"
Python

    if self.run_rate_type == 'get_last_year':
Blok ini akan berjalan HANYA JIKA Anda memilih opsi "Ambil Data Tahun Lalu" pada field run_rate_type.

➡️ Kondisi 1.A: Data TAHUN LALU + Stok Pengaman JUMLAH TETAP (Fix Qty)

Python

        if self.safety_stock_select == 'fix_qty':
            run_rate_qty = self.average_quantity_last_year
            
            self.run_rate_qty = run_rate_qty
            self.product_min_qty = (run_rate_qty * (self.lead_days if self.lead_days else 1)) + (run_rate_qty if self.lead_days >= 1 else 0) + self.safety_stock
Trigger: Terjadi jika Anda memilih Stok Pengaman (safety_stock_select) sebagai "Jumlah Tetap".

Aksi:

run_rate_qty = ..._last_year: Ambil nilai Rata-rata Penjualan Harian Tahun Lalu (misal: 10 unit).

self.run_rate_qty = run_rate_qty: Tampilkan angka 10 unit itu di layar (di field run_rate_qty).

self.product_min_qty = ...: Hitung Stok Minimum dengan rumus:

(Rata-rata Harian Tahun Lalu * (Waktu Tunggu + 1)) + Jumlah Stok Pengaman Tetap

➡️ Kondisi 1.B: Data TAHUN LALU + Stok Pengaman PERSENTASE

Python

        if self.safety_stock_select == 'percentage' and self.run_rate_qty > 0:
            run_rate_qty = self.average_quantity_run_rate_days
            
            self.run_rate_qty = run_rate_qty
            self.product_min_qty = (run_rate_qty * (self.lead_days if self.lead_days else 1)) + (run_rate_qty if self.lead_days >= 1 else 0) + + (self.average_quantity_last_year * self.safety_stock) / 100
Trigger: Terjadi jika Anda memilih Stok Pengaman (safety_stock_select) sebagai "Persentase".

Aksi:

run_rate_qty = ..._run_rate_days: Ambil nilai Rata-rata Penjualan Harian dari Beberapa Hari Terakhir (misal: 12 unit).

self.run_rate_qty = run_rate_qty: Tampilkan angka 12 unit itu di layar.

self.product_min_qty = ...: Hitung Stok Minimum dengan rumus hybrid (campuran):

Kebutuhan Pemesanan: (Rata-rata Harian Hari Terakhir * (Waktu Tunggu + 1))

Stok Pengaman: + (Rata-rata Harian Tahun Lalu * Persentase %)

Catatan: Di kondisi ini (1.B), kode Anda menggunakan dua sumber data yang berbeda: Kebutuhan pemesanan dihitung dari data hari terakhir, tapi stok pengamannya dihitung dari data tahun lalu.

Kondisi Utama 2: "Saya ingin hitung berdasarkan DATA HARI TERAKHIR"
Python

    elif self.run_rate_type == 'get_past_days_data':
        run_rate_qty = self.average_quantity_run_rate_days
Blok ini akan berjalan HANYA JIKA Anda memilih opsi "Ambil Data Beberapa Hari Terakhir".

Aksi Awal: run_rate_qty = ..._run_rate_days: Ambil nilai Rata-rata Penjualan Harian dari Beberapa Hari Terakhir (misal: 12 unit). Nilai ini akan dipakai di semua perhitungan di bawah ini.

➡️ Kondisi 2.A: Data HARI TERAKHIR + Stok Pengaman JUMLAH TETAP (Fix Qty)

Python

        if self.safety_stock_select == 'fix_qty':
            
            self.run_rate_qty = run_rate_qty
            self.product_min_qty = (run_rate_qty * (self.lead_days if self.lead_days else 1)) + (run_rate_qty if self.lead_days >= 1 else 0) + self.safety_stock
Trigger: Terjadi jika Anda memilih Stok Pengaman (safety_stock_select) sebagai "Jumlah Tetap".

Aksi:

self.run_rate_qty = run_rate_qty: Tampilkan angka 12 unit itu di layar.

self.product_min_qty = ...: Hitung Stok Minimum dengan rumus:

(Rata-rata Harian Hari Terakhir * (Waktu Tunggu + 1)) + Jumlah Stok Pengaman Tetap

➡️ Kondisi 2.B: Data HARI TERAKHIR + Stok Pengaman PERSENTASE

Python

        if self.safety_stock_select == 'percentage' and self.run_rate_qty > 0:
            
            self.run_rate_qty = run_rate_qty
            self.product_min_qty = (run_rate_qty * (self.lead_days if self.lead_days else 1)) + (run_rate_qty if self.lead_days >= 1 else 0) + ((self.average_quantity_run_rate_days * self.safety_stock) / 100)
Trigger: Terjadi jika Anda memilih Stok Pengaman (safety_stock_select) sebagai "Persentase".

Aksi:

self.run_rate_qty = run_rate_qty: Tampilkan angka 12 unit itu di layar.

self.product_min_qty = ...: Hitung Stok Minimum dengan rumus:

(Rata-rata Harian Hari Terakhir * (Waktu Tunggu + 1)) + (Rata-rata Harian Hari Terakhir * Persentase %)

Tindakan Terakhir (Penutup)
Python

    self._compute_min_gt_forecast()
Trigger: Kode ini akan selalu berjalan setelah salah satu dari 4 kalkulasi di atas selesai.

Aksi: Ini memanggil fungsi lain (_compute_min_gt_forecast). Tujuannya kemungkinan untuk melakukan pengecekan tambahan, misalnya: "Apakah Stok Minimum yang baru dihitung ini lebih besar dari stok perkiraan (forecast)?" atau sekadar untuk menyegarkan tampilan data lain.


### kesimpulan untuk beberapa field 

1. run_rate_qty (Rata-rata Penjualan Harian)
Tujuan Field: Menampilkan angka rata-rata penjualan harian (disebut juga "Run Rate") yang sedang aktif digunakan sebagai dasar perhitungan stok minimum.

Apa Isinya: Sebuah angka (bisa desimal) yang merepresentasikan: "Berapa unit produk ini laku terjual per harinya?"

Asal Value: Nilai ini dihitung dan diisi otomatis oleh sistem (@api.onchange). Ini BUKAN input manual. Nilainya diambil berdasarkan pilihan pengguna pada field "Metode Perhitungan" (run_rate_type):

Jika Metode = 'Data Tahun Lalu': Nilainya akan disalin dari field average_quantity_last_year.

Jika Metode = 'Data Hari Terakhir': Nilainya akan disalin dari field average_quantity_run_rate_days.

Peran dalam Kalkulasi: Ini adalah komponen pengali utama dalam menentukan "Kebutuhan Stok Pemesanan". Angka inilah yang memberi tahu sistem seberapa cepat stok Anda akan habis.

Contoh Penggunaan dalam Kode: Nilai ini pertama-tama di-set ke dalam variabel run_rate_qty, kemudian ditampilkan di field self.run_rate_qty dan dipakai untuk menghitung self.product_min_qty.

Python

# Contoh dari Kondisi 1.A ('get_last_year' + 'fix_qty')

# 1. Mengambil nilai (dari field lain) ke variabel
run_rate_qty = self.average_quantity_last_year

# 2. Menampilkan nilai di field 'run_rate_qty'
self.run_rate_qty = run_rate_qty

# 3. Menggunakan nilai untuk kalkulasi stok minimum
self.product_min_qty = (run_rate_qty * (self.lead_days if self.lead_days else 1)) + (run_rate_qty if self.lead_days >= 1 else 0) + self.safety_stock
2. run_rate_period_after (Tanggal Mulai Periode)
Tujuan Field: Menentukan tanggal mulai (start date) untuk periode analisis penjualan.

Apa Isinya: Sebuah nilai Tanggal (misal: 01/09/2025).

Asal Value: Input manual oleh pengguna. Pengguna memilih tanggal ini dari kalender.

Peran dalam Kalkulasi: Field ini hanya aktif jika Metode Perhitungan = 'Data Hari Terakhir'. Field ini bekerja bersama run_rate_period_before untuk memberi perintah kepada sistem: "Tolong hitung total penjualan dari tanggal INI..."

Contoh Penggunaan dalam Kode: Field ini tidak digunakan secara langsung di dalam potongan kode _onchange_run_rate_type. Namun, field ini (bersama run_rate_period_before) digunakan oleh fungsi lain sebelumnya untuk menghitung nilai self.average_quantity_run_rate_days.

Nilai average_quantity_run_rate_days tersebut kemudian digunakan oleh kode ini:

Python

# Contoh dari Kondisi 2.A ('get_past_days_data')

# Nilai 'run_rate_qty' di sini berasal dari perhitungan
# yang menggunakan 'run_rate_period_after' dan 'run_rate_period_before'
run_rate_qty = self.average_quantity_run_rate_days

self.run_rate_qty = run_rate_qty
self.product_min_qty = ...
3. run_rate_period_before (Tanggal Akhir Periode)
Tujuan Field: Menentukan tanggal akhir (end date) untuk periode analisis penjualan.

Apa Isinya: Sebuah nilai Tanggal (misal: 30/09/2025).

Asal Value: Input manual oleh pengguna. Pengguna memilih tanggal ini dari kalender.

Peran dalam Kalkulasi: Field ini hanya aktif jika Metode Perhitungan = 'Data Hari Terakhir'. Field ini memberi perintah kepada sistem: "...sampai tanggal INI."

Gabungan: Nilai dari run_rate_period_after dan run_rate_period_before digunakan untuk menghitung field average_quantity_run_rate_days (yang kemudian akan mengisi run_rate_qty).

Contoh Penggunaan dalam Kode: Sama seperti run_rate_period_after, field ini tidak digunakan secara langsung di dalam potongan kode ini. Field ini adalah input untuk fungsi lain yang menghasilkan self.average_quantity_run_rate_days.

Python

# Contoh dari Kondisi 2.A ('get_past_days_data')

# Nilai 'run_rate_qty' di sini berasal dari perhitungan
# yang menggunakan 'run_rate_period_after' dan 'run_rate_period_before'
run_rate_qty = self.average_quantity_run_rate_days

self.run_rate_qty = run_rate_qty
self.product_min_qty = ...
4. lead_days (Waktu Tunggu Pengiriman)
Tujuan Field: Mencatat total waktu (dalam hari) yang dibutuhkan sejak Anda memesan barang ke supplier sampai barang tersebut benar-benar tiba dan siap digunakan di gudang Anda.

Apa Isinya: Sebuah angka (jumlah hari), misal: 5 (artinya butuh 5 hari).

Asal Value: Input manual oleh pengguna. Angka ini biasanya didapat dari kesepakatan dengan supplier atau berdasarkan data historis pengiriman sebelumnya.

Peran dalam Kalkulasi: Ini adalah faktor risiko utama. Semakin besar angkanya (semakin lama waktu tunggu), semakin banyak stok yang harus Anda siapkan untuk bertahan selama masa tunggu tersebut.

Contoh Penggunaan dalam Kode: Field ini dipakai langsung di setiap rumus kalkulasi product_min_qty.

Python

# Contoh dari Kondisi 2.A ('get_past_days_data' + 'fix_qty')

self.product_min_qty = (run_rate_qty * (self.lead_days if self.lead_days else 1)) + (run_rate_qty if self.lead_days >= 1 else 0) + self.safety_stock
(self.lead_days if self.lead_days else 1): Bagian ini berarti "gunakan nilai lead_days, tapi jika lead_days kosong atau 0, anggap saja 1 hari".

(run_rate_qty if self.lead_days >= 1 else 0): Ini adalah cara untuk menambahkan +1 hari (seperti run_rate_qty * 1).