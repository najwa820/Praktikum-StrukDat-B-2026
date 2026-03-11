'''
Soal 5. Integrasi Lengkap Sistem PyBook Store
Topik: Function, Procedure, List, Dict, Set, Tuple, Menu Interaktif | Estimasi waktu: 25
menit
Tuliskan jawaban kode Python Anda pada file: soal5.py (jangan ubah nama file)
Deskripsi:

Gabungkan semua komponen dari soal 1 hingga 4 menjadi satu program lengkap PyBook
Store dengan menu interaktif berbasis teks. Pada soal ini, semua fungsi dan prosedur yang
telah dibuat di soal1.py hingga soal4.py ditulis ulang dan digabungkan dalam satu file
soal5.py.

Ketentuan Program:
Program menampilkan menu berikut dan berjalan dalam perulangan hingga user memilih
menu 5:
=== PyBook Store ===
1. Tambah Buku
2. Tampilkan Semua Buku
3. Beli Buku
4. Laporan Penjualan
5. Keluar

1. Menu 1 - Tambah Buku: Gunakan fungsi tambah_buku() dan simpan hasilnya ke
dalam list katalog.

2. Menu 2 - Tampilkan Semua Buku: Tampilkan seluruh isi katalog dalam format
tabel yang rapi menggunakan f-string.

3. Menu 3 - Beli Buku: Gunakan prosedur proses_transaksi(). Simpan setiap
transaksi berhasil sebagai tuple (nama_buku, jumlah, total) ke list log_transaksi.
'''

from soal1 import tambah_buku
from soal2 import cari_buku
from soal3 import prosedur_transaksi
from soal4 import hitung_diskon

print("=== PyBook Store ===")
def menu(pilihan):
    if pilihan == 1:
        tambah_buku()
    elif pilihan == 2:
        print("Tampilan")
    elif pilihan == 3:
        prosedur_transaksi()
    elif pilihan == 4:
        print

y = True

while y:
    match(menu):
        case 1:
            print("1. Tambah Buku")
        case 2:
            print("2. Tampilkan Semua Buku")
        case 3:
            print("3. Beli Buku")
        case 4:
            print("4. Laporan Penjualan")
        case 5:
            print("5. keluar")