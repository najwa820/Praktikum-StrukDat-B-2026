'''
Diberikan sebuah list angka:
angka = [10, 20, 30, 40, 50]
1. Tambahkan angka 60 ke dalam list.
2. Hapus angka 20 dari list.
3. Tampilkan angka tertinggi dan terendah
4. Hitung rata-rata angka setelah perubahan data
5. Tampilkan seluruh isi list setelah perubahan.
'''

angka = [10, 20, 30, 40, 50]

# Tambah 60 ke list
angka.append (60) #menggunakan append(60) untuk menambahkan ke list
print (angka)  #menampilkan output

# Hapus angka 20 dari list
angka.remove (20) #menggunakan remove(20) untuk menghapus nilaii 20 dari list
print (angka)

# Menampilkan tertinggi dan terendah
tertinggi = max(angka)
terendah = min(angka)
print (tertinggi)
print(terendah)

# Hitung rata-rata
jumlah = 0 #menyimpan jumlah angka yang dimulai dari 0
total = 0 #menyimpan total yang dimulai dari 0

for x in angka: #menggunakan perulangan for untuk menjumlahkan angka
    jumlah += x #jumlah akan bertambah setiap elemen x
    total += 1 #total akan bertambah 1
    rata = jumlah / total #operasi untuk menghitung rata-rata
print (rata)

# menampilkan seluruhnya setelah perubahan
print(angka)