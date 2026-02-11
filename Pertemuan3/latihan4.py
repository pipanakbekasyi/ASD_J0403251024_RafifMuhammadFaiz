class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        # bikin node baru
        new_node = Node(data)

        # kalau list masih kosong
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def display(self):
        # kalau list kosong
        if not self.head:
            print("Circular Linked List kosong")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(kembali ke head)")

    def merge(self, other):
        # cek list kedua kosong atau tidak
        if not self.head:
            self.head = other.head
            return

        # cek list kedua kosong atau engga
        if not other.head:
            return

        # mencari node terakhir list pertama
        temp1 = self.head
        while temp1.next != self.head:
            temp1 = temp1.next

        # mencari node terakhir list kedua
        temp2 = other.head
        while temp2.next != other.head:
            temp2 = temp2.next

        # menyambungkan kedua list
        temp1.next = other.head
        temp2.next = self.head
# Linked List pertama
cll1 = CircularSinglyLinkedList()
n1 = int(input("Masukkan jumlah elemen Circular Linked List 1: "))

for i in range(n1):
    data = int(input(f"Masukkan elemen ke-{i+1} list 1: "))
    cll1.insert_at_end(data)

print("\nCircular Linked List 1:")
cll1.display()


# Linked List kedua
cll2 = CircularSinglyLinkedList()
n2 = int(input("\nMasukkan jumlah elemen Circular Linked List 2: "))

for i in range(n2):
    data = int(input(f"Masukkan elemen ke-{i+1} list 2: "))
    cll2.insert_at_end(data)

print("\nCircular Linked List 2:")
cll2.display()


# Merge kedua list
cll1.merge(cll2)

print("\nHasil penggabungan Circular Linked List:")
cll1.display()
