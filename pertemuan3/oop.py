#Penulisan kode berorientasi objek
#agar punya struktur yang clear, mudah dibaca, dan di debug
#oop ga lepas dari class (cetak biru) dan objek (hasil dari blue print)


#__init__ method
class Person:
  def __init__(self, name, age):  #self menunjuk ke objek yang baru dibuat
    self.name = name #atribut. atribut adalah hal-hal yang dimiliki semuanya
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)