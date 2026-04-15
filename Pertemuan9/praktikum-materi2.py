#==================================================================
#Latihan 2 membuat node tree
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

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

#Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")


#menampilkan isi node
print("Data pada root", root.data)
print("Data pada child kiri", root.left.data)
print("Data pada child kanan", root.right.data)
print("Child kiri dari B:", root.left.left.data)
print("Child kanan dari B:", root.left.right.data)
print("Child kiri dari C:", root.right.left.data)
print("Child kanan dari C:", root.right.right.data)


#===============================================================
# PENJELASAN
#===============================================================
# Program diatas bagian  dari pembuatan node sebelumnya,
# yaitu dengan menambahkan child (anak) pada root sehingga membentuk
# struktur tree sederhana.

# Class Node digunakan sebagai blueprint untuk membuat node yang
# memiliki tiga atribut: data, left, dan right.

# Node A dibuat sebagai root (akar dari tree).
# Kemudian ditambahkan dua child pada level 1:
# B sebagai child kiri dari root
# C sebagai child kanan dari root
# root.left = Node("B")  -> menghubungkan node B ke kiri root
# root.right = Node("C") -> menghubungkan node C ke kanan root
# Output
# - root.data menghasilkan "A"
# - root.left.data menghasilkan "B"
# - root.right.data menghasilkan "C"
# Kemudian ditambahkan dua child pada level 2:
# D sebagai child kiri dari B
# E sebagai child kanan dari B
# F sebagai child kiri dari C
# G sebagai child kanan dari C
# root.left.left = Node("D") -> menghubungkan node D ke kiri B
# root.left.right = Node("E") -> menghubungkan node E ke kanan B
# root.right.left = Node("F") -> menghubungkan node F ke kiri C
# root.right.right = Node("G") -> menghubungkan node G ke kanan C

# Struktur tree yang terbentuk:
#        A
#       / \
#      B   C
#     / \ / \
#    D  E F  G