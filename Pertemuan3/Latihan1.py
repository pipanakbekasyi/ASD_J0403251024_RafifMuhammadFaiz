class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):        
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_node(self, key):
        temp = self.head

        # Jika node yang dihapus adalah head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print(f"Data {key} tidak ditemukan")
            return

        prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

# Membuat linked list
ll = LinkedList()

# Menambahkan data
ll.insert_at_end(5)
ll.insert_at_end(10)
ll.insert_at_end(15)
ll.insert_at_end(20)

print("Linked List sebelum penghapusan:")
ll.display()

# Menghapus data
hapus = int(input("Masukkan data yang ingin dihapus: "))
ll.delete_node(hapus)

print(f"\nLinked List setelah penghapusan data {hapus}:")
ll.display()

