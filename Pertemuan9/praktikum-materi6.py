#==================================================================
#Latihan 6 Struktur Organisasi Perusahaan
#Rafif Muhammad Faiz
#TPL B2
#J0403251024
#===================================================================

class Node:
    def __init__(self, data):
        self.data = data  # menyimpan nilai node
        self.left = None  # child kiri
        self.right = None  # child kanan

def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)
       
# membuat tree struktur direktur
root = Node("Direktur")

# Membuat child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

#Membuat child level 2
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")

root.right.left = Node("Staff 3")



#Menjalankan traversal preorder
print("Struktur Organisasi: ")
preorder(root)

#===============================================================
# PENJELASAN
#===============================================================
# Program ini menampilkan struktur organisasi perusahaan.
# Struktur ini terdiri dari direktur, manajer, dan staff.

# Langkah penelusuran dimulai dari pemanggilan:
# preorder(root) → node pertama adalah "Direktur"
# Rekursi berhenti ketika node bernilai None,