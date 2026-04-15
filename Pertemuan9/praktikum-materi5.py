#==================================================================
#Latihan 5 Traversal PostOrder
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
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")
        
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
postorder(root)

#===============================================================
# PENJELASAN
#===============================================================
# Traversal Postorder memiliki urutan:
# Left (kiri) → Right (kanan) → Root (akar)

# Fungsi postorder() menggunakan rekursi:
# Jika node tidak kosong (not None), maka:
#   1. Kunjungi subtree kiri
#   2. Kunjungi subtree kanan
#   3. Cetak data node

# Struktur tree yang dibuat:
#        A
#       / \
#      B   C
#     / \
#    D   E
#===============================================================
# KESIMPULAN
#===============================================================
# Traversal Postorder mengunjungi node dengan urutan kiri, kanan, lalu akar.
# Metode ini sering digunakan untuk menghapus tree atau evaluasi ekspresi
# karena child diproses terlebih dahulu sebelum parent.