# algoritma-pemdas-1

Soal 1: Rekapitulasi Nilai Mata Kuliah
##TABEL RANCANGAN FUNGSI
#hitung_nilai
Input: tugas, uts, uas
Proses: tugas x 30% + uts x 30% + uas x 40%
Output: nilai akhir
#nilai_huruf
Input: nilai
Proses: cek rentang nilai
Output: A / B / C / D / E
#kelulusan
Input: huruf
Proses: A, B, C = lulus
Output: LULUS / TIDAK LULUS
#tampilkan_nilai
Input: nama, tugas, uts, uas
Proses: panggil 3 fungsi di atas
Output: print hasil
#main
Input: -
Proses: simpan data, loop 5 mahasiswa, hitung rata-rata dan jumlah lulus
Output: print rekap

Konversi huruf: >= 85 A, >= 70 B, >= 55 C, >= 40 D, di bawah 40 E

##PERHITUNGAN MANUAL
Andi: 24 + 21 + 36 = 81 -> B -> LULUS
Bunga: 27 + 25,5 + 35,2 = 87,7 -> A -> LULUS
Citra: 18 + 13,5 + 20 = 51,5 -> D -> TIDAK LULUS
Dimas: 22,5 + 24 + 26 = 72,5 -> B -> LULUS
Eka: 9 + 12 + 14 = 35 -> E -> TIDAK LULUS

total = 327,7
rata-rata = 327,7 : 5 = 65,54
jumlah lulus = 3

##PENJELASAN
program menghitung nilai akhir tiap mahasiswa dengan bobot tugas 30%, UTS 30%, dan UAS 40%. Nilai diubah menjadi huruf, lalu ditentukan statusnya: A, B, C lulus, selain itu tidak lulus. Fungsi main memproses 5 mahasiswa dengan perulangan, lalu menampilkan rata-rata kelas dan jumlah mahasiswa yang lulus.


soal 2: Struk Pengiriman Toko Daring
##TABEL RANCANGAN FUNGSI
Nama Fungsi: tampilkan_judul
Parameter: -
Mengembalikan Nilai: Tidak (Void)
Tugas yang Dikerjakan: Menampilkan judul program "STRUK PENGIRIMAN TOKO DARING" lengkap dengan garis pemisahnya

Nama Fungsi: biaya_berat
Parameter: berat
Mengembalikan Nilai: Ya (Non-void)
Tugas yang Dikerjakan: Menghitung biaya sesuai berat paket (Rp10.000 untuk berat <= 2 kg, ditambah Rp4.000 untuk setiap kg berikutnya)

Nama Fungsi: biaya_jarak
Parameter: jarak
Mengembalikan Nilai: Ya (Non-void)
Tugas yang Dikerjakan: Menentukan biaya tambahan berdasarkan jarak (Rp0 bila <= 20 km, Rp5.000 bila > 20 km)

Nama Fungsi: diskon
Parameter: ongkir, anggota
Mengembalikan Nilai: Ya (Non-void)
Tugas yang Dikerjakan: Menghitung potongan 10% dari ongkir apabila anggota bernilai "Ya", jika tidak maka Rp0

Nama Fungsi: tampilkan_struk
Parameter: nama, berat, jarak, anggota
Mengembalikan Nilai: Ya (Non-void)
Tugas yang Dikerjakan: Menghitung ongkir serta total setelah diskon, menampilkan struk tiap pelanggan, kemudian mengembalikan nilai total

Nama Fungsi: main
Parameter: -
Mengembalikan Nilai: Tidak (Void)
Tugas yang Dikerjakan: Memanggil judul, memproses 5 pelanggan, menjumlahkan total pendapatan, lalu menampilkannya

##PERHITUNGAN MANUAL
Perhitungan Manual Ongkir Akhir. Rina (berat: 1 kg, jarak: 10 km, anggota: bukan) biaya berat: 1 kg <= 2 kg maka Rp10.000, biaya jarak: 10 <= 20 maka Rp0, subtotal: 10.000 + 0 = 10.000 (tidak ada potongan karena bukan anggota), ongkir akhir: Rp10.000 (hasil program sama). Sari (berat: 5 kg, jarak: 25 km, anggota: bukan) biaya berat: 10.000 + (5 - 2) x 4.000 = 22.000, biaya jarak: 25 > 20 maka Rp5.000, subtotal: 22.000 + 5.000 = 27.000 (tidak ada potongan karena bukan anggota), ongkir akhir: Rp27.000 (hasil program sama). Tono (berat: 5 kg, jarak: 25 km, anggota: ya) biaya berat: Rp22.000, biaya jarak: Rp5.000, subtotal: 22.000 + 5.000 = 27.000, potongan anggota (10%): 0,10 x 27.000 = 2.700, ongkir akhir: 27.000 - 2.700 = Rp24.300 (hasil program sama). Umar (berat: 2 kg, jarak: 30 km, anggota: ya) biaya berat: 2 kg maka Rp10.000, biaya jarak: 30 > 20 maka Rp5.000, subtotal: 10.000 + 5.000 = 15.000, potongan anggota (10%): 0,10 x 15.000 = 1.500, ongkir akhir: 15.000 - 1.500 = Rp13.500 (program terbukti berhasil). Vina (berat: 8 kg, jarak: 15 km, anggota: bukan) biaya berat: 10.000 + (8 - 2) x 4.000 = 34.000, biaya jarak: 15 <= 20 maka Rp0, subtotal: 34.000 + 0 = 34.000 (tidak ada potongan karena bukan anggota), ongkir akhir: Rp34.000 (hasil program sama). Total pendapatan: 10.000 + 27.000 + 24.300 + 13.500 + 34.000 = Rp108.800.

##BAGIAN KODE YANG HARUS DIUBAH
Apabila toko mengganti batas jarak menjadi 15 km dan biaya tambahan jarak menjadi Rp7.000, maka hanya fungsi biaya_jarak(jarak) yang perlu diubah: def biaya_jarak(jarak): if jarak <= 15: (diubah dari 20 menjadi 15) return 0 else: return 7000 (diubah dari 5000 menjadi 7000). Karena kode sudah dibagi secara modular ke dalam fungsi-fungsi tersendiri, saya cukup mengubah satu fungsi saja tanpa menyentuh fungsi main maupun fungsi lainnya. Hal ini membuktikan bahwa pemisahan tugas membuat kode jauh lebih mudah diubah.

##PENJELASAN
Program ini menghitung ongkir pengiriman berdasarkan biaya berat dan biaya jarak. Fungsi biaya_berat menetapkan tarif dasar Rp10.000 untuk berat hingga 2 kg, kemudian menambahkan Rp4.000 untuk setiap kg kelebihannya. Fungsi biaya_jarak menambahkan Rp5.000 bila jarak lebih dari 20 km. Fungsi diskon memberikan potongan 10% dari ongkir bila pelanggan merupakan anggota ("Ya"). Fungsi tampilkan_struk menggabungkan ketiga fungsi tersebut, menampilkan rincian tiap pelanggan, lalu mengembalikan total ongkir akhir. Fungsi main memanggil tampilkan_struk untuk 5 pelanggan, menjumlahkan seluruh totalnya menjadi total_pendapatan, lalu menampilkannya. Karena diskon memakai 0.1 (float), hasil yang tercetak bisa berbentuk 24300.0, 13500.0, dan 108800.0, namun nilainya tetap sama dengan perhitungan manual.

