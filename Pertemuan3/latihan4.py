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
        # kalau list pertama kosong, langsung pakai list kedua
        if not self.head:
            self.head = other.head
            return

        # kalau list kedua kosong, ngga perlu ngapa-ngapain
        if not other.head:
            return

        # cari node terakhir list pertama
        temp1 = self.head
        while temp1.next != self.head:
            temp1 = temp1.next

        # cari node terakhir list kedua
        temp2 = other.head
        while temp2.next != other.head:
            temp2 = temp2.next

        # sambungin dua list biar tetap circular
        temp1.next = other.head
        temp2.next = self.head
# Linked List pertama
cll1 = CircularSinglyLinkedList()

data1 = input(
    "Masukkan elemen Circular Linked List 1 (pisahkan dengan koma): "
).strip()

if data1:
    for data in data1.split(","):
        cll1.insert_at_end(int(data.strip()))

print("\nCircular Linked List 1:")
cll1.display()


# Linked List kedua
cll2 = CircularSinglyLinkedList()

data2 = input(
    "\nMasukkan elemen Circular Linked List 2 (pisahkan dengan koma): "
).strip()

if data2:
    for data in data2.split(","):
        cll2.insert_at_end(int(data.strip()))

print("\nCircular Linked List 2:")
cll2.display()


# Merge kedua list
cll1.merge(cll2)

print("\nHasil penggabungan Circular Linked List:")
cll1.display()