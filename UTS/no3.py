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
Soal 3 - OOP (20 Poin)
Buat class Pasien dan class turunannya PasienPrioritas dengan ketentuan
berikut:
Class Pasien:
- Atribut private: __id, __nama, __penyakit
- Getter untuk setiap atribut
- Method tampilkan_info()
- Method static hitung_pasien() -> mengembalikan total objek Pasien yang sudah dibuat (gunakan class variable sebagai counter)

Class PasienPrioritas (turunan Pasien):
- Tambahkan atribut: prioritas ("Darurat" / "Biasa")
- Override tampilkan_info() untuk menyertakan info prioritas
- Jika prioritas = "Darurat", tampilkan pesan peringatan: "** Segera tangani! **"

Contoh Output:
ID : P001
Nama : Andi
Penyakit: Flu
ID : P007
Nama : Ghani
Penyakit : Sesak Napas
Prioritas : Darurat
** Segera tangani! **
Total pasien terdaftar: 2
'''
pasien_hari_ini = [
    {"id": "P001", "nama": "Andi", "usia": 34, "penyakit": "Flu", "bayar": False},
    {"id": "P002", "nama": "Budi", "usia": 22, "penyakit": "Tifus", "bayar": True},
    {"id": "P003", "nama": "Cici", "usia": 45, "penyakit": "Flu", "bayar": False},
    {"id": "P004", "nama": "Dani", "usia": 30, "penyakit": "Maag", "bayar": True},
    {"id": "P005", "nama": "Eva", "usia": 28, "penyakit": "Tifus", "bayar": False},
    {"id": "P006", "nama": "Fajar", "usia": 17, "penyakit": "Maag", "bayar": False},
]

nama = pasien_hari_ini[0]["nama"]
print(nama)

class Pasien:
    def __init__(self, id, nama, penyakit):
        self.id = id
        self.nama = nama
        self.penyakit = penyakit

    def tampilkan_info(self):
        id = pasien_hari_ini[0]["id"]
        nama = pasien_hari_ini[0]["nama"]
        penyakit = pasien_hari_ini[0]["penyakit"]
        return id, nama, penyakit

    def hitung_pasien(self):
        pass

class PasienPrioritas:
    def __init__(self, prioritas):
        self.prioritas = prioritas
        if prioritas == "Darurat":
            return "** Segera Tangani! **"
        
    def tampilkan_info(self):
        print(self.prioritas)

print("ID : P001")
print("Nama : Andi")
print("Penyakit: Flu")
print("ID : P007")
print("Nama : Ghani")
print('Penyakit : Sesak Napas')
print("Prioritas : Darurat")
print("** Segera tangani! **")
print("Total pasien terdaftar: 2")