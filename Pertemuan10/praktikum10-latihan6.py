# ==========================================================
# Rafif Muhammad Faiz
# TPL B2 J0403251024
# Latihan 5: Rotasi Kanan pada BST Tidak Seimbang
# ==========================================================

# Class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

# ==========================================================
# Alur fungsi preorder:
# 1. Cek apakah node tidak kosong
# 2. Cetak data node (root)
# 3. Telusuri subtree kiri
# 4. Telusuri subtree kanan
# ==========================================================
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)
    

# ==========================================================
# Alur fungsi tampil_struktur:
# 1. Menampilkan node saat ini beserta posisinya
# 2. Rekursif ke child kiri dan kanan
# ==========================================================
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print(" " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")


# ==========================================================
# Alur fungsi rotate_right:
# 1. Simpan child kiri dari node y ke dalam variabel x
# 2. Simpan subtree kanan dari x ke dalam T2
# 3. Lakukan rotasi:
#    x.right menjadi y
#    y.left diisi dengan T2
# 4. x menjadi root baru
# ==========================================================
def rotate_right(y):
    x = y.left        # child kiri jadi calon root baru
    T2 = x.right      # simpan subtree kanan dari x
    
    # proses rotasi
    x.right = y
    y.left = T2
    
    return x

# -----------------------------
# Program utama
# -----------------------------
# Membuat tree tidak seimbang (miring ke kiri)
#    30
#   /
#  20
# /
#10
root = Node(30)
root.left = Node(20)
root.left.left = Node(10)

print("Preorder sebelum rotasi kanan:")
preorder(root)

print("\n\nStruktur sebelum rotasi kanan:")
tampil_struktur(root)

# Rotasi kanan
root = rotate_right(root)

print("\nPreorder sesudah rotasi kanan:")
preorder(root)

print("\n\nStruktur sesudah rotasi kanan:")
tampil_struktur(root)