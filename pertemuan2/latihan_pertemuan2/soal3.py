'''
Diberikan dua set mata kuliah pilihan:
kelas_A = {"Struktur Data", "Basis Data", "AI",
"Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI",
"Cloud Computing"}
1. Tentukan mata kuliah yang diambil oleh kedua kelas.
2. Tentukan mata kuliah yang hanya diambil kelas A.
3. Tentukan seluruh mata kuliah unik yang diambil oleh kelas A dan B.
'''

kelas_A = {"Struktur Data", "Basis Data", "AI", "Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI", "Cloud Computing"}

# mata kuliah yg diambil keduanya
kelas_A = {"Struktur Data", "Basis Data", "AI", "Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI", "Cloud Computing"}

matkul_sama = kelas_A.intersection (kelas_B) #intersection(kelas_B) akan menampilkan mana saja yang nilainya sama antara kelas_A dan kelas_B
print (matkul_sama)

# mata kuliah yang hanya diambil kelas A
print(kelas_A)

#yang benar
difference = kelas_A.difference(kelas_B)
print(difference)

# Seluruh mata kuliah yg diambil kelas A dan B
kelas_A = {"Struktur Data", "Basis Data", "AI", "Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI", "Cloud Computing"}

kelas_A.update (kelas_B) #kelas_B akan ditambahkan ke kelas_A sehingga akan menampilkan mata kuliah seluruhnya
print (kelas_A)