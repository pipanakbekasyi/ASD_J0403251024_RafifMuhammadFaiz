#=============================================
# Rafif Muhammad Faiz
# TPL B2 J0403251024
# BST
#=============================================

# Class Node digunakan untuk membuat struktur dasar Binary Search Tree (BST)
class Node:
    def __init__(self, data):
        self.data = data      # menyimpan nilai pada node
        self.left = None      # pointer ke child kiri
        self.right = None     # pointer ke child kanan
        

# Fungsi insert digunakan untuk menambahkan data ke dalam BST
# 1. Jika root kosong = buat node baru
# 2. Jika data lebih kecil dari root = masuk ke subtree kiri
# 3. Jika data lebih besar dari root = masuk ke subtree kanan
# 4. Proses dilakukan dengan melakukan rekursif sampai posisi ditemukan
def insert(root, data):
    if root is None:
        return Node(data)  # membuat node baru jika posisi kosong
    
    if data < root.data:
        root.left = insert(root.left, data)  # masuk ke kiri
    elif data > root.data:
        root.right = insert(root.right, data)  # masuk ke kanan
    return root  # mengembalikan root setelah penambahan


#mengisi data BST
root = None  # inisialisasi root kosong
data_list = [50, 30, 70, 20, 40, 50, 80]  # data yang akan dimasukkan ke BST

for data in data_list:
    root = insert(root, data)  # memasukkan data satu per satu ke BST
    
print("BST berhasil dibuat")  # konfirmasi BST sudah terbentuk


#=============================================
# Latihan 2: Traversal inorder
#=============================================

# Fungsi inorder digunakan untuk menelusuri BST dengan urutan:
# kiri → root → kanan
# 1. Kunjungi subtree kiri
# 2. Cetak data node
# 3. Kunjungi subtree kanan
# Hasil traversal inorder pada BST akan terurut (ascending)
def inorder(root):
    if root:
        inorder(root.left)              # ke kiri
        print(root.data, end=" ")       # cetak data
        inorder(root.right)             # ke kanan

print("Hasil Inorder: ")
inorder(root)  # menjalankan traversal inorder
print()


#=============================================
# Latihan 3: Search di BST
#=============================================

# Fungsi search digunakan untuk mencari suatu nilai dalam BST
# 1. Jika node kosong = data tidak ditemukan
# 2. Jika data sama dengan node = data ditemukan
# 3. Jika data lebih kecil = cari ke kiri
# 4. Jika data lebih besar = cari ke kanan
# Proses dilakukan secara rekursif
def search(root, key):
    if root is None:
        return False  # data tidak ditemukan
    
    if root.data == key:
        return True  # data ditemukan
    
    if key < root.data:
        return search(root.left, key)   # cari ke kiri
    else:
        return search(root.right, key)  # cari ke kanan

key = 40  # nilai yang ingin dicari

if search(root, key):
    print(f"{key} ditemukan dalam BST")  # hasil jika ditemukan
else:
    print(f"{key} tidak ditemukan dalam BST")  # hasil jika tidak ditemukan