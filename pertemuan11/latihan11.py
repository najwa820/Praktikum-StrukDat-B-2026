class Node:
  def __init__(self, nama, keluhan):
    self.nama = nama
    self.keluhan = keluhan
    self.next = None

class Queue:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def enqueue(self, nama, keluhan):
    new_node = Node(nama, keluhan)
    if self.tail is None:
      self.head = self.tail = new_node
      self.size += 1
      return
    self.tail.next = new_node
    self.tail = new_node
    self.size += 1

  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty"
    temp = self.head
    self.head = temp.next
    self.size -= 1
    if self.head is None:
      self.tail = None
    return temp.nama

  def peek(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.head.nama, self.head.keluhan

  def isEmpty(self):
    return self.size == 0

  def size(self):
    return self.size
  
  def clear(self):
    self.head = None
    self.tail = None
    self.size = 0
  
  def printQueueDaftar(self):
    temp = self.head
    nomor = 1
    while temp:
      print(f"[DAFTAR] {temp.nama} terdaftar dengan keluhan: {temp.keluhan} (No. Antrian: {nomor})")
      temp = temp.next
      nomor += 1
    print()

  def printQueue(self):
    temp = self.head
    print("[ANTRIAN SAAT INI]")
    while temp:
      print(temp.nama, '->', temp.keluhan, end="\n")
      temp = temp.next
    print()

print("====================================")
print("     SISTEM ANTRIAN POLI UMUM")
print("         RS Sehat Bersama")
print("====================================")

pasien = Queue()

print(f'[CEK] Apakah antrian kosong? -> {pasien.isEmpty()}, antrian masih kosong\n')

pasien.enqueue('Budi', 'demam tinggi')
pasien.enqueue('Ani', 'batuk pilek')
pasien.enqueue('Citra', 'sakit kepala')

pasien.printQueueDaftar()

print(f"[INFO] Jumlah pasien menunggu: {pasien.size} ")
print(f"[PEEK] Pasien berikutnya: {pasien.peek()}\n")

print(f'[PANGGIL] Dokter memanggil {pasien.dequeue()}\n')

pasien.printQueue()

print(f"[PANGGIL] Dokter memanggil {pasien.dequeue()}\n")
print(f"[INFO] Jumlah pasien masih menunggu: {pasien.size} ")

print(f"[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.")
pasien.clear()