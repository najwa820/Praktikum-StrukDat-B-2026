#Binary Search Tree
class Node:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.left = None
        self.right = None

class BinarySearhTree:
    def __init__(self):
        self.root = None

    def insert(self, id_buku, judul):
        new = Node(id_buku, judul)

        if self.root == None:
            self.root = new
            print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
            return
        
        P = self.root
        Q = self.root

        while Q != None:
            P = Q
            if new.id_buku < P.id_buku:
                Q = P.left
            elif new.id_buku > P.id_buku:
                Q = P.right
            else:
                print("[INSERT] Data duplikat tidak dimasukkan")
                return
            
        if new.id_buku < P.id_buku:
            P.left = new
        else:
            P.right = new

        print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")

    def in_order(self, node, no = 1):
        if node is not None:
            no = self.in_order(node.left, no)
            print(f"{no}. {node.id_buku} - {node.judul}")
            no += 1
            no = self.in_order(node.right, no)
        return no

    def search(self, id_buku):
        current = self.root
        print(f"\n[SEARCH] Mencari ID {id_buku}...", end=" ")

        while current is not None:
            if id_buku == current.id_buku:
                print(f"Ditemukan! Judul: {current.judul}")
                return
            elif id_buku < current.id_buku:
                current = current.left
            else:
                current = current.right
        print(f"Data tidak ditemukan")

    def get_min(self):
        current = self.root
        while current.left != None:
            current = current.left
        return current.id_buku

    def get_maks(self):
        current = self.root
        while current.right != None:
            current = current.right
        return current.id_buku

    def height(self, node):
        if node == None:
            return -1
        left = self.height(node.left)
        right = self.height(node.right)      
        return max(left, right) + 1  
    
print('SISTEM KATALOG PERPUSTAKAAN "ILMU TERANG"')
print("=========================================")

bst = BinarySearhTree()

bst.insert(50, "Dasar Pemrograman")
bst.insert(30, "Struktur Data")
bst.insert(70, "Kecerdasan Buatan")
bst.insert(20, "Matematika Diskrit")
bst.insert(40, "Basis Data")
bst.insert(60, "Jaringan Komputer")
bst.insert(80, "Sistem Operasi")

print("\n[INFO] Koleksi Buku (In-Order Traversal): ")
bst.in_order(bst.root)

bst.search(60)
bst.search(100)

print(f"\n[STATISTIK] ID Terkecil: {bst.get_min()}")
print(f"[STATISTIK] ID Terbesar: {bst.get_maks()}")

print(f"[INFO] Tinggi (Height) Tree: {bst.height(bst.root)}")
print("=========================================")
print("Simulasi Selesai!")