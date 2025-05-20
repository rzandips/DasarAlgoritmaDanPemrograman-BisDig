# DasarAlgoritmaDanPemrograman-BisDig
Rezandi Pratama Sidik (24110310069) 2B BISNIS DIGITAL

Manfaat Penggunaan Fungsi
Fungsi dalam pemrograman memberikan banyak manfaat, di antaranya:
1.	Modularitas: Memecah program menjadi bagian-bagian kecil yang lebih mudah dipahami dan dikelola.
2.	Reusabilitas: Kode yang sama dapat digunakan berulang kali tanpa perlu menulis ulang.
3.	Abstraksi: Menyembunyikan detail implementasi, sehingga pengguna fungsi hanya perlu tahu input dan output.
4.	Pemeliharaan: Mempermudah proses debugging dan pembaruan kode karena perubahan hanya perlu dilakukan di satu tempat.
5.	Keterbacaan: Meningkatkan keterbacaan kode dengan memberikan nama yang deskriptif untuk operasi tertentu.
6.	Scope Variabel: Membantu mengelola ruang lingkup variabel, mencegah konflik nama variabel.
7.	Pengujian: Memudahkan pengujian program karena fungsi dapat diuji secara terpisah.
Cara Kerja Rekursi dalam Menghitung Faktorial
Rekursi adalah teknik di mana suatu fungsi memanggil dirinya sendiri untuk menyelesaikan masalah. Untuk bekerja dengan benar, fungsi rekursif harus memiliki:
1.	Kasus Basis: Kondisi yang menghentikan pemanggilan rekursif (mencegah infinite loop).
2.	Kasus Rekursif: Kondisi dimana fungsi memanggil dirinya sendiri dengan parameter yang lebih sederhana.
Dalam kasus faktorial:
1.	Definisi matematika: n! = n × (n-1) × (n-2) × ... × 2 × 1
2.	Definisi rekursif: n! = n × (n-1)!
3.	Kasus basis: 0! = 1! = 

Penggunaan Perulangan dan Array
Perulangan
Dalam program ini, perulangan digunakan untuk:
1.	Mengumpulkan input nilai dari 5 siswa secara berurutan menggunakan perulangan for
2.	Memungkinkan input ulang jika terjadi kesalahan input (error handling)
Array (List)
Array/list dalam Python digunakan untuk:
1.	Menyimpan nilai kelima siswa dalam satu variabel (nilai = [])
2.	Memudahkan pencarian nilai tertinggi dengan fungsi max()
3.	Menentukan posisi/indeks siswa dengan nilai tertinggi menggunakan fungsi index()
Struktur Kontrol Percabangan untuk Logika Diskon
Struktur kontrol percabangan adalah komponen fundamental dalam pemrograman yang memungkinkan program untuk menjalankan blok kode tertentu berdasarkan kondisi yang dievaluasi.
Penggunaan Percabangan dalam Kasus Diskon E-Commerce:
1.	Kondisi yang Dievaluasi: 
o	Apakah total belanja pelanggan > Rp500.000?
2.	Jalur Eksekusi: 
o	Jika kondisi bernilai TRUE (total belanja > Rp500.000): 
	Berikan diskon 10% dari total belanja
	Tampilkan pesan selamat mendapatkan diskon
o	Jika kondisi bernilai FALSE (total belanja ≤ Rp500.000): 
	Tidak berikan diskon (diskon = 0)
	Tampilkan pesan informasi syarat mendapatkan diskon
3.	Perhitungan Akhir: 
o	Total bayar = Total belanja - Nilai diskon

Langkah-langkah Algoritma untuk Sistem Kasir Toko
Algoritma adalah urutan langkah-langkah yang terstruktur untuk menyelesaikan suatu masalah. Untuk sistem kasir sederhana yang menghitung total harga 3 barang, berikut langkah-langkahnya:
1. Tahap Persiapan
•	Mulai program
•	Inisialisasi variabel total_harga = 0 untuk menyimpan total harga pembelian
2. Tahap Input Data
•	Untuk setiap barang dari 3 barang: 
o	Minta pengguna memasukkan harga barang
o	Validasi input: 
	Pastikan input berupa angka (bukan huruf atau karakter khusus)
	Pastikan nilai tidak negatif (harga tidak mungkin negatif)
o	Jika validasi gagal, minta input ulang
3. Tahap Proses
•	Untuk setiap harga barang yang diinput: 
o	Tambahkan ke variabel total_harga
4. Tahap Output
•	Tampilkan total harga pembelian dalam format yang sesuai
•	Selesai

Peran Tipe Data dalam Perhitungan Nilai Rata-Rata
Tipe data adalah klasifikasi nilai yang menentukan jenis operasi yang dapat dilakukan dan penyimpanan memori yang dibutuhkan. Dalam program ini, beberapa tipe data yang berperan penting:
1. Float (Bilangan Pecahan)
•	Penggunaan: Menyimpan nilai mata pelajaran dan hasil perhitungan rata-rata
•	Peran: Memungkinkan presisi dalam perhitungan karena nilai ujian bisa berupa bilangan desimal
•	Contoh: nilai = float(input("Nilai Matematika: ")) dan rata_rata = total_nilai / jumlah_mata_pelajaran
2. List (Daftar)
•	Penggunaan: Menyimpan kumpulan nilai dari 3 mata pelajaran
•	Peran: Memudahkan penyimpanan dan pengolahan sekumpulan nilai yang sejenis
•	Contoh: nilai_mata_pelajaran = [] untuk menyimpan nilai-nilai mata pelajaran
3. String (Teks)
•	Penggunaan: Menyimpan nama mata pelajaran dan status kelulusan
•	Peran: Menyimpan dan menampilkan informasi teks
•	Contoh: status = "LULUS" atau status = "TIDAK LULUS"
4. Boolean (Nilai Logika)
•	Penggunaan: Hasil evaluasi kondisi dalam pernyataan if
•	Peran: Menentukan alur eksekusi program berdasarkan kondisi
•	Contoh: if rata_rata >= 75: menghasilkan nilai True atau False
