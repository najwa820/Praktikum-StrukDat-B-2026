'''
Soal 3. Prosedur Transaksi Pembelian dan Set Riwayat
Topik: Procedure, Set, Manipulasi List | Estimasi waktu: 20 menit
Tuliskan jawaban kode Python Anda pada file: soal3.py (jangan ubah nama file)
Deskripsi:

PyBook Store membutuhkan prosedur untuk memproses transaksi pembelian dan
mencatat riwayat buku yang pernah dibeli tanpa data duplikat.

Ketentuan Program:

1. Buat prosedur proses_transaksi(katalog, nama_buku, jumlah_beli) yang mencari
buku di katalog berdasarkan nama (exact match, case-insensitive).

2. Jika buku ditemukan dan stok mencukupi, kurangi stok buku tersebut dan cetak
total harga yang harus dibayar.

3. Jika stok tidak mencukupi, cetak pesan peringatan kepada user.

4. Jika buku tidak ditemukan di katalog, cetak pesan error.

5. Gunakan set bernama riwayat_transaksi untuk menyimpan nama buku yang
pernah dibeli tanpa duplikat. Lakukan 3 transaksi di program utama dan tampilkan
isi riwayat_transaksi di akhir.
'''
riwayat_transaksi = ()
for x in range(3):
    riwayat = input("Buku yang pernah dibeli: ")
    riwayat_transaksi += riwayat

def prosedur_transaksi(katalog, nama_buku, jumlah_beli):
    for x in riwayat_transaksi:
        if riwayat_transaksi == nama_buku & katalog > 0:
            stok -= 1
            return
        elif riwayat_transaksi == nama_buku & katalog < 0:
            return "Stok tidak cukup"
        else:
            return "Error"