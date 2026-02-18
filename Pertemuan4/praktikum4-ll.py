#==============================================
#Implementasi Dasar: Node Pada linked list
#
#Rafif Muhammad Faiz
#J0403251024
#TPL B / P2
#================================================

#Membuat class node yang merupakan unit dasar dari linked list
class Node:
    def __init__(self, data): #konstruktor
        self.data = data #menyimpan data
        self.next = None #pointer ke note berikutnya

#proses pertama membuat node secara satu per satu
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#Menghubungkan node: A -> B -> C -> None
nodeA.next = nodeB
nodeB.next = nodeC

# Menentukan node pertama(head)
head = nodeA

#Traversal : menelurusi dari head sampai none
current = head
while current is not None:
    print(current.data) #menampilkan data pada node saat ini
    current = current.next #pindah ke node berikutnya
    
# ================================================
# Implementasi Dasar : Linked List + Insert Awal
# ================================================

class LinkedList: #Class implementasi stack
    def __init__(self):
        self.head = None
    def insert_awal(self, data):
        # memnbuat node baru
        nodeBaru = Node(data) #memanggil class node
        
        #  node baru menunjuk ke head lama
        nodeBaru.next = self.head

        # head pindah ke node baru
        self.head = nodeBaru
        
    def hapus_awal(self):
        data_terhapus = self.head.data
        #menggeser head
        self.head = self.head.next
        print("Data", data_terhapus, "telah dihapus")
        
    def tampilkan(self): #sama dengan traversal
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
            
print("List Baru")
ll = LinkedList() #instantiasi objek ke class Linked List
ll.insert_awal("D")
ll.insert_awal("K")
ll.insert_awal("M")
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()