#==================================================================
#Latihan 4 Traversal Inorder
#Rafif Muhammad Faiz
#TPL B2
#J0403251024
#===================================================================

class Node:
    def __init__(self, data):
        self.data = data  # menyimpan nilai node
        self.left = None  # child kiri
        self.right = None  # child kanan

#Membuat fungsi inorder: left -> root -> right
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

# membuat root (di luar class)
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

#Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#Menjalankan traversal preorder
print("Hasil Traversal iniorder: ")
inorder(root)

#===============================================================
# PENJELASAN
#===============================================================
# Urutan Traversal Inorder:
# Left  → Root → Right 

# Fungsi inorder() menggunakan rekursi untuk menelusuri node:
# - Jika node tidak kosong (not None), maka:
#   1. Kunjungi subtree kiri
#   2. Cetak data node
#   3. Kunjungi subtree kanan
#===============================================================
# KESIMPULAN
#===============================================================
# Traversal Inorder mengunjungi node dari kiri ke akar lalu ke kanan.
# Metode ini sering digunakan pada Binary Search Tree (BST)
# karena menghasilkan data yang terurut (ascending).