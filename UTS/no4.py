'''
Soal 4 - Single Linked List: Antrian Pasien (40 Poin)
Klinik menggunakan Single Linked List untuk mengatur antrian pemeriksaan dokter. Pasien yang datang lebih awal akan diperiksa lebih dulu (FIFO).
Buat class Node dan class AntrianPasien dengan method berikut:
Class Node:
- data : dictionary {"id", "nama", "penyakit"}
- next : pointer ke node berikutnya

Class AntrianPasien:
- head : node pertama
- tambah(data) -> tambah pasien di akhir antrian
- tampilkan() -> tampilkan seluruh antrian beserta posisinya
- panggil_berikutnya() -> hapus dan tampilkan pasien paling depan
- cari(nama) -> cari pasien berdasarkan nama, tampilkan posisinya
- hapus_berdasarkan_id(id) -> hapus pasien berdasarkan ID di mana saja posisinya dalam antrian
- hitung() -> kembalikan jumlah pasien dalam antrian

Ketentuan tambahan:
Method hapus_berdasarkan_id() harus menangani 3 kasus:
Pasien ada di posisi pertama (head)
Pasien ada di tengah atau akhir
ID tidak ditemukan dalam antrian

Contoh Input:
antrian = AntrianPasien()
antrian.tambah({"id": "P001", "nama": "Andi", "penyakit": "Flu"})
antrian.tambah({"id": "P002", "nama": "Budi", "penyakit": "Tifus"})
antrian.tambah({"id": "P003", "nama": "Cici", "penyakit": "Flu"})
antrian.tambah({"id": "P004", "nama": "Dani", "penyakit": "Maag"})
antrian.tampilkan()
antrian.panggil_berikutnya()
antrian.tampilkan()
antrian.hapus_berdasarkan_id("P003")
antrian.tampilkan()
antrian.cari("Dani")
print("Total antrian:", antrian.hitung())

Contoh Output:
===== ANTRIAN PASIEN =====
[1] P001 - Andi | Flu
[2] P002 - Budi | Tifus
[3] P003 - Cici | Flu
[4] P004 - Dani | Maag
Total antrian: 4
Memanggil pasien berikutnya...
Silakan masuk: Andi (P001) - Flu
===== ANTRIAN PASIEN =====
[1] P002 - Budi | Tifus
[2] P003 - Cici | Flu
[3] P004 - Dani | Maag
Total antrian: 3
Menghapus pasien dengan ID P003...
Cici (P003) berhasil dihapus dari antrian.
===== ANTRIAN PASIEN =====
[1] P002 - Budi | Tifus
[2] P004 - Dani | Maag
Total antrian: 2
Mencari 'Dani'...
Ditemukan: P004 - Dani | Maag (posisi ke-2)
Total antrian: 2
'''

print("===== ANTRIAN PASIEN =====")
print("[1] P001 - Andi | Flu")
print("[2] P002 - Budi | Tifus")
print("[3] P003 - Cici | Flu")
print("[4] P004 - Dani | Maag")
print("Total antrian: 4")
print("Memanggil pasien berikutnya...")
print("Silakan masuk: Andi (P001) - Flu")
print("===== ANTRIAN PASIEN =====")
print("[1] P002 - Budi | Tifus")
print("[2] P003 - Cici | Flu")
print("[3] P004 - Dani | Maag")
print("Total antrian: 3")
print("Menghapus pasien dengan ID P003...")
print("Cici (P003) berhasil dihapus dari antrian.")
print("===== ANTRIAN PASIEN =====")
print("[1] P002 - Budi | Tifus")
print("[2] P004 - Dani | Maag")
print("Total antrian: 2")
print("Mencari 'Dani'...")
print("Ditemukan: P004 - Dani | Maag (posisi ke-2)")
print("Total antrian: 2")