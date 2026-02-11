'''
Buatlah sebuah class dengan 
-minimal 3 atribut/prorperty
-2 method

Lalu buatlah 3 object dari class tersebut
Lalu ubahlah salah satu atribut dari object tersebut
'''

class Liburan:
    def __init__(self, kota, destinasi, tahun):
        self.kota = kota
        self.destinasi = destinasi
        self.tahun = tahun

    def suhu(self):
        print("disini panas " + holiday.kota)

    def makanan(self):
        print("makanan khas nya enak " + holiday.kota)

holiday = Liburan("bali", "candi", 2025)
holiday2 = Liburan("padang", "pantai", 2026)
holiday3 = Liburan("yogyakarta", "candi", 2023)

print(holiday.kota, holiday.destinasi, holiday.tahun)
print(holiday2.kota, holiday2.destinasi, holiday2.tahun)
print(holiday3.kota, holiday3.destinasi, holiday3.tahun)
holiday2.suhu()
holiday3.makanan()

holiday3.destinasi = "gunung"
print(holiday3.destinasi)