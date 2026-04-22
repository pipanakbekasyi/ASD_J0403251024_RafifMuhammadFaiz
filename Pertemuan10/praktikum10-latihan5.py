# ==========================================================
# Rafif Muhammad Faiz
# TPL B2 J0403251024
# Latihan 5: Rotasi Kiri pada BST Tidak Seimbang
# ==========================================================

# Class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

# Alur fungsi preorder:
# 1. Cek apakah node tidak kosong
# 2. Cetak data node (root)
# 3. Telusuri subtree kiri
# 4. Telusuri subtree kanan
# 5. Menggunakan rekursi hingga semua node dikunjungi
# Fungsi preorder untuk melihat isi tree
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)
    

# Alur fungsi tampil_struktur:
# 1. Menampilkan node saat ini beserta posisinya (Root, L, R)
# 2. Memberi spasi sesuai level untuk menunjukkan kedalaman
# 3. Rekursif ke child kiri dengan level + 1
# 4. Rekursif ke child kanan dengan level + 1
# 5. Digunakan untuk melihat bentuk tree secara visual


# Fungsi untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print(" " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")


# Alur fungsi rotate_left:
# 1. Simpan child kanan dari node x ke dalam variabel y
# 2. Simpan subtree kiri dari y ke dalam T2 (sementara)
# 3. Lakukan rotasi:
#    y.left menjadi x (x turun ke kiri)
#    x.right diisi dengan T2
# 4. y menjadi root baru setelah rotasi
# 5. Mengembalikan y sebagai root yang baru


# Fungsi rotasi kiri
def rotate_left(x):
    # x adalah root lama
    y = x.right # y adalah child kanan x
    T2 = y.left # subtree kiri milik y disimpan sementara
    
    # Proses rotasi
    y.left = x # x menjadi child kiri dari y
    x.right = T2 # child kanan x diganti dengan T2
    
    # y menjadi root baru
    return y

# -----------------------------
# Program utama
# -----------------------------
# Membuat tree yang tidak seimbang:
# 10 -> 20 -> 30
root = Node(10)
root.right = Node(20)
root.right.right = Node(30)
print("Preorder sebelum rotasi kiri:")
preorder(root)
print("\n\nStruktur sebelum rotasi kiri:")
tampil_struktur(root)

# Melakukan rotasi kiri pada root
root = rotate_left(root)
print("\nPreorder sesudah rotasi kiri:")
preorder(root)
print("\n\nStruktur sesudah rotasi kiri:")
tampil_struktur(root)