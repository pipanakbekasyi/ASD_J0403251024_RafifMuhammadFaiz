#==================================================================
#Latihan 3 Traversal Preorder
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


#Fungsi Preorder: Root, Left, Right
def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)
# membuat root (di luar class)
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

#Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#Menjalankan traversal preorder
print("Hasil Traversal Preorder: ")
preorder(root)

#===============================================================
# PENJELASAN (Pemahaman Penelusuran Kode)
#===============================================================
# Program ini melakukan traversal Preorder pada binary tree
# dengan menggunakan fungsi rekursif.

# Langkah penelusuran dimulai dari pemanggilan:
# preorder(root) → node pertama adalah "A"
# Urutan kunjungan node yang terjadi:
# A → B → D → E → C

# Penelusuran ini mengikuti konsep Preorder:
# Root → Left → Right

# Rekursi berhenti ketika node bernilai None,
# yang menandakan tidak ada child lagi yang bisa ditelusuri.