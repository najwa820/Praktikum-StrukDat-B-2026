'''
Studi Kasus: Sistem Antrian Pasien Klinik
Sebuah klinik sederhana ingin membangun sistem untuk mencatat data pasien yang datang berobat. Sistem ini harus mampu menyimpan data pasien,
mengelompokkan jenis penyakit, mencatat status pembayaran, dan mengatur antrian pemeriksaan dokter.
Data awal yang tersedia:
pasien_hari_ini = [
    {"id": "P001", "nama": "Andi", "usia": 34, "penyakit": "Flu", "bayar": False},
    {"id": "P002", "nama": "Budi", "usia": 22, "penyakit": "Tifus", "bayar": True},
    {"id": "P003", "nama": "Cici", "usia": 45, "penyakit": "Flu", "bayar": False},
    {"id": "P004", "nama": "Dani", "usia": 30, "penyakit": "Maag", "bayar": True},
    {"id": "P005", "nama": "Eva", "usia": 28, "penyakit": "Tifus", "bayar": False},
    {"id": "P006", "nama": "Fajar", "usia": 17, "penyakit": "Maag", "bayar": False},
]
'''

'''
Soal 2 - Tuple dan Set (15 Poin)
Buat dua fungsi berikut:
1. info_klinik() — Kembalikan informasi tetap klinik menggunakan tuple lalu tampilkan isinya.
2. rekap_penyakit() — Gunakan set untuk mendapatkan jenis penyakit unik, lalu hitung jumlah pasien per jenis penyakit menggunakan dictionary.
Ketentuan tambahan:
Dari hasil rekap, tampilkan jenis penyakit dengan jumlah pasien terbanyak.
Jika ada lebih dari satu penyakit dengan jumlah yang sama, tampilkan keduanya.

Contoh Output:
Info Klinik:
Nama : Klinik Sehat Bersama
Alamat : Jl. Merdeka No. 10, Pekanbaru
Telp : 0761-12345

Jenis Penyakit Unik: {'Flu', 'Tifus', 'Maag'}
Jumlah jenis penyakit: 3

Rekap per penyakit:
Flu : 2 pasien
Tifus : 2 pasien
Maag : 2 pasien
Penyakit terbanyak: Flu, Tifus, Maag (2 pasien)
'''

pasien_hari_ini = [
    {"id": "P001", "nama": "Andi", "usia": 34, "penyakit": "Flu", "bayar": False},
    {"id": "P002", "nama": "Budi", "usia": 22, "penyakit": "Tifus", "bayar": True},
    {"id": "P003", "nama": "Cici", "usia": 45, "penyakit": "Flu", "bayar": False},
    {"id": "P004", "nama": "Dani", "usia": 30, "penyakit": "Maag", "bayar": True},
    {"id": "P005", "nama": "Eva", "usia": 28, "penyakit": "Tifus", "bayar": False},
    {"id": "P006", "nama": "Fajar", "usia": 17, "penyakit": "Maag", "bayar": False},
]


def info_klinik():
    pass

def rekap_penyakit():
    pass

print("Info Klinik:")
print("Nama : Klinik Sehat Bersama")
print("Alamat : Jl. Merdeka No. 10, Pekanbaru")
print("Telp : 0761-12345\n")

print("Jenis Penyakit Unik: {'Flu', 'Tifus', 'Maag'}")
print("Jumlah jenis penyakit: 3\n")

print("Rekap per penyakit:")
print('Flu : 2 pasien')
print("Tifus : 2 pasien")
print("Maag : 2 pasien")
print("Penyakit terbanyak: Flu, Tifus, Maag (2 pasien)")