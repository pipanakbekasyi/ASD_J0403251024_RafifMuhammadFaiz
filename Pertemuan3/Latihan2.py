class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def search(self, key):
        if not self.head:
            print("Circular Linked List kosong. Tidak ada elemen yang bisa dicari.")
            return

        temp = self.head
        while True:
            if temp.data == key:
                print(f"Elemen {key} ditemukan dalam Circular Linked List.")
                return
            temp = temp.next
            if temp == self.head:
                break

        print(f"Elemen {key} tidak ditemukan dalam Circular Linked List.")
cll = CircularSinglyLinkedList()

n = int(input("Masukkan jumlah elemen Circular Linked List: "))

for i in range(n):
    data = int(input(f"Masukkan elemen ke-{i+1}: "))
    cll.insert_at_end(data)

# Tetap jalan walaupun n = 0
cari = int(input("Masukkan elemen yang ingin dicari: "))
cll.search(cari)
