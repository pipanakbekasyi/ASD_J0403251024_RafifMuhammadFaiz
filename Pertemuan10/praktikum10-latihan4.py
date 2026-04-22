# ==========================================================
# Rafif Muhammad Faiz
# TPL B2 J0403251024
# Latihan 4: Membuat BST yang Tidak Seimbang
# ==========================================================


# Class Node untuk menyimpan data BST
class Node:
    def __init__(self, data):
        self.data = data # nilai pada node
        self.left = None # child kiri
        self.right = None # child kanan
        

# Alur fungsi insert:
# 1. Jika root kosong = buat node baru sebagai root
# 2. Jika data lebih kecil dari root = masuk ke subtree kiri
# 3. Jika data lebih besar dari root = masuk ke subtree kanan
# 4. Proses dilakukan secara rekursif sampai menemukan posisi kosong
# 5. Mengembalikan root setelah proses penyisipan selesai

# Fungsi insert untuk BST
def insert(root, data):
 # Jika root kosong, buat node baru
    if root is None:
        return Node(data)
    # Jika data lebih kecil, masuk ke subtree kiri
    if data < root.data:
        root.left = insert(root.left, data)
    # Jika data lebih besar, masuk ke subtree kanan
    elif data > root.data:
        root.right = insert(root.right, data)
    return root


# Alur fungsi preorder:
# 1. Kunjungi node (cetak data root)
# 2. Telusuri subtree kiri
# 3. Telusuri subtree kanan
# 4. Menggunakan rekursi sampai semua node dikunjungi
# Fungsi preorder untuk melihat bentuk tree
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)
        

# Alur fungsi tampil_struktur:
# 1. Menampilkan node saat ini beserta posisinya (Root, L, R)
# 2. Menambahkan spasi sesuai level untuk menunjukkan kedalaman tree
# 3. Rekursif ke child kiri (level + 1)
# 4. Rekursif ke child kanan (level + 1)
# 5. Digunakan untuk visualisasi struktur tree secara sederhana

# Fungsi sederhana untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print(" " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

# -----------------------------
# Program utama
# -----------------------------
root = None
# Data dimasukkan berurutan naik
data_list = [10, 20, 30]
for data in data_list:
 root = insert(root, data)
print("Preorder BST:")
preorder(root)
print("\n\nStruktur BST:")
tampil_struktur(root)