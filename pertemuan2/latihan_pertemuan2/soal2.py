'''
Diberikan sebuah tuple data mahasiswa:
mahasiswa = ("A001", "Budi", "Informatika")
1. Tampilkan nama mahasiswa dari tuple tersebut.
2. Tampilkan seluruh isi tuple menggunakan perulangan for.
3. Jelaskan satu alasan mengapa tuple tidak bisa diubah.
'''

# Menampilkan nama
mahasiswa = ("A001", "Budi", "Informatika") #tuple bernama mahasiswa yang berisi nama, nim, dan prodi
print (mahasiswa[1]) #menampilkan index ke-1 pada tuple

# Menampilkan isi tuple
for x in mahasiswa: #untuk setiap x pada tuple mahasiswa
    print (x)

# Alasan kenapa tuple tidak bisa diubah
# Karena tuple bukan bersifat immutable setelah dideklarasikan