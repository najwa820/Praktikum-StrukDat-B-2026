'''
Sebuah data mahasiswa disimpan dalam bentuk dictionary:
mahasiswa = {
"A001": {"nama": "Budi", "prodi": "Informatika",
"ipk": 3.45},
"A002": {"nama": "Siti", "prodi": "Sistem
Informasi", "ipk": 3.20},
"nama": "Budi", "prodi": "Informatika",
"ipk": 3.45}
}
1. Tampilkan nama mahasiswa yang memiliki IPK di atas 3.5.
2. Hitung rata-rata IPK seluruh mahasiswa.
3. Tambahkan satu data mahasiswa baru ke dalam dictionary tersebut.
'''

mahasiswa = {
    "A001": {
        "nama": "Budi", "prodi": "Informatika", "ipk": 3.45
        },
    "A002": {
        "nama": "Siti", "prodi": "SistemInformasi", "ipk": 3.20
        },
    "A003": {"nama": "Andi", "prodi": "Informatika","ipk": 3.75
             }
}
# Menampilkan nama mahasiswa yang IPK diatas 3.5

# Hitung rata rata

# tambahkan satu data
mahasiswa ["A004"] = {"nama": "Najwa", "prodi": "Informatika", "ipk": 4.00}
print (mahasiswa)