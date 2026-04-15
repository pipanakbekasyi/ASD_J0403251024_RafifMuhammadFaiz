#==================================================================
#Latihan 1 Membuat Node
#Rafif Muhammad Faiz
#TPL B2
#J0403251024
#===================================================================
# class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data  # menyimpan nilai node
        self.left = None  # child kiri
        self.right = None  # child kanan


# membuat root (di luar class)
root = Node("A")

# menampilkan isi node
print("Data pada root", root.data)
print("Data pada child kiri", root.left)
print("Data pada child kanan", root.right)

#===============================================================
# PENJELASAN
#===============================================================
# Program ini membuat struktur dasar dari sebuah node pada binary tree.
# Setiap node memiliki 3 atribut utama:
# 1. data  -> untuk menyimpan nilai
# 2. left  -> menunjuk ke child kiri
# 3. right -> menunjuk ke child kanan
#
# Pada awal pembuatan node (root), child kiri dan kanan masih kosong (None).
# Hal ini karena node tersebut belum dihubungkan dengan node lain.
#
# Root adalah node pertama dalam tree yang menjadi titik awal struktur pohon.