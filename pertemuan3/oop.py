#Penulisan kode berorientasi objek
#agar punya struktur yang clear, mudah dibaca, dan di debug
#oop ga lepas dari class (cetak biru) dan objek (hasil dari blue print)
#di oop juga memiliki method dan atribut 

#__init__ method
class Person:
  def __init__(self, name, age):  #self menunjuk ke objek yang baru dibuat
    self.name = name #atribut. atribut adalah hal-hal yang dimiliki semuanya
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

#Contoh 2
class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25
p1.city = "Oslo"

print(p1.name)
print(p1.age)
print(p1.city)

#Contoh 3
class Student:
  def __init__(self, name, grade):
    self.name = name
    self.grade = grade

s1 = Student("Anna", "A")
print(s1.grade)
s1.grade = "B"
print(s1.grade)

#Contoh 4
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def area(self):
    return self.width*self.height

r1 = Rectangle(5, 3)
print(r1.area())