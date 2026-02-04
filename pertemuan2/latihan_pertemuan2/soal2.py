'''
Diberikan sebuah tuple data mahasiswa:
mahasiswa = ("A001", "Budi", "Informatika")
1. Tampilkan nama mahasiswa dari tuple tersebut.
2. Tampilkan seluruh isi tuple menggunakan perulangan for.
3. Jelaskan satu alasan mengapa tuple tidak bisa diubah.
'''

# Menampilkan nama
mahasiswa = ("A001", "Budi", "Informatika")
print (mahasiswa[1])

# Menampilkan isi tuple
for x in mahasiswa:
    print (x)

# Alasan kenapa tuple tidak bisa diubah
# Karena tuple bukan bersifat immutable setelah dideklarasikan