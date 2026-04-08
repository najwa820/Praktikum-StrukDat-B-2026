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
Soal 1 - List dan Dictionary (25 Poin)
Buat dua fungsi berikut:
1. tampilkan_pasien() — Tampilkan semua data pasien dalam format tabel.
2. filter_belum_bayar() — Kembalikan list berisi nama-nama pasien yang belum membayar, lalu tampilkan total jumlah mereka.
Ketentuan tambahan:
Urutkan hasil filter_belum_bayar() berdasarkan nama secara alfabetis (A-Z) sebelum ditampilkan. Gunakan metode sorting pada list, bukan library sort tambahan.
Gunakan list comprehension untuk mengambil data pasien yang belum bayar.
Contoh Output:
===== DATA PASIEN KLINIK =====
No | ID | Nama | Usia | Penyakit | Status Bayar
---+------+-------+------+----------+-------------
1 | P001 | Andi | 34 | Flu | Belum Bayar
2 | P002 | Budi | 22 | Tifus | Lunas
3 | P003 | Cici | 45 | Flu | Belum Bayar
4 | P004 | Dani | 30 | Maag | Lunas
5 | P005 | Eva | 28 | Tifus | Belum Bayar
6 | P006 | Fajar | 17 | Maag | Belum Bayar
===== PASIEN BELUM BAYAR =====
1. Andi
2. Cici
3. Eva
4. Fajar
Total belum bayar: 4 pasien
'''

pasien_hari_ini = [
    {"id": "P001", "nama": "Andi", "usia": 34, "penyakit": "Flu", "bayar": False},
    {"id": "P002", "nama": "Budi", "usia": 22, "penyakit": "Tifus", "bayar": True},
    {"id": "P003", "nama": "Cici", "usia": 45, "penyakit": "Flu", "bayar": False},
    {"id": "P004", "nama": "Dani", "usia": 30, "penyakit": "Maag", "bayar": True},
    {"id": "P005", "nama": "Eva", "usia": 28, "penyakit": "Tifus", "bayar": False},
    {"id": "P006", "nama": "Fajar", "usia": 17, "penyakit": "Maag", "bayar": False},
]

#ubah pasien_hari_ini dari list ke dictionary

def tampilkan_pasien():
    print("===== DATA PASIEN KLINIK =====")
    print("No | ID | Nama | Usia | Penyakit | Status Bayar")
    print("---+------+-------+------+----------+-------------")

    no = 1
    for id, nama, usia, penyakit, bayar in pasien_hari_ini:
        print(f"{no} | {id} | {nama} | {usia} | {penyakit} | {bayar}")
        no += 1

    id1 = pasien_hari_ini[0]["id"]
    id2 = pasien_hari_ini[1]["id"]
    id3 = pasien_hari_ini[2]["id"]
    id4 = pasien_hari_ini[3]["id"]
    id5 = pasien_hari_ini[4]["id"]
    id6 = pasien_hari_ini[5]["id"]

    print("\n")

    nama1 = pasien_hari_ini[0]["nama"]
    nama2 = pasien_hari_ini[1]["nama"]
    nama3 = pasien_hari_ini[2]["nama"]
    nama4 = pasien_hari_ini[3]["nama"]
    nama5 = pasien_hari_ini[4]["nama"]
    nama6 = pasien_hari_ini[5]["nama"]

    usia1 = pasien_hari_ini[0]["usia"]
    usia2 = pasien_hari_ini[1]["usia"]
    usia3 = pasien_hari_ini[2]["usia"]
    usia4 = pasien_hari_ini[3]["usia"]
    usia5 = pasien_hari_ini[4]["usia"]
    usia6 = pasien_hari_ini[5]["usia"]

    penyakit1 = pasien_hari_ini[0]["penyakit"]
    penyakit2 = pasien_hari_ini[1]["penyakit"]
    penyakit3 = pasien_hari_ini[2]["penyakit"]
    penyakit4 = pasien_hari_ini[3]["penyakit"]
    penyakit5 = pasien_hari_ini[4]["penyakit"]
    penyakit6 = pasien_hari_ini[5]["penyakit"]

    bayar1 = pasien_hari_ini[0]["bayar"]
    bayar2 = pasien_hari_ini[1]["bayar"]
    bayar3 = pasien_hari_ini[2]["bayar"]
    bayar4 = pasien_hari_ini[3]["bayar"]
    bayar5 = pasien_hari_ini[4]["bayar"]
    bayar6 = pasien_hari_ini[5]["bayar"]

    print(f"1 | {id1} | {nama1} | {usia1} | {penyakit1} | {bayar1}")
    print(f"2 | {id2} | {nama2} | {usia2} | {penyakit2} | {bayar2}")
    print(f"3 | {id3} | {nama3} | {usia3} | {penyakit3} | {bayar3}")
    print(f"4 | {id4} | {nama4} | {usia4} | {penyakit4} | {bayar4}")
    print(f"5 | {id5} | {nama5} | {usia5} | {penyakit5} | {bayar5}")
    print(f"6 | {id6} | {nama6} | {usia6} | {penyakit6} | {bayar6}")

tampilkan_pasien()

print("\n")

def filter_belum_bayar():
      print("===== PASIEN BELUM BAYAR =====")
      no = 1

      for i in pasien_hari_ini:
            if "bayar" == False:
                return "bayar"
            print(f"{no}. {"bayar"} ")
            no += 1
filter_belum_bayar()