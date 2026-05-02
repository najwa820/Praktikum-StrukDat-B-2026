print('SISTEM AUDIT DISTRIBUSI "CEPAT SAMPAI"')
print("======================================")
print("[INFO] Membangun Struktur Gudang...")
print("[INFO] Struktur berhasil dibuat.\n")

print("HASIL AUDIT:")
print(f"1. Pre-Order    : ")
{preorder(tree.root)}
print(f"2. In-Order     : ")
{inorder(tree.root)}
print(f"Post-Order      : ")
{postorder(tree.root)}

print(f"[DATA] Gudang Ujung (Leaf Nodes): {leaf_nodes(tree.root)}")
print("======================================")
print("Audit Selesai!")