#==============================================
#Implementasi Dasar: Queue Pada linked list
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

#Queue dengan 2 pointer front and rear
class QueueLL:
    def __init__(self): #konstruktor
        self.front = None #pointer ke node pertama
        self.rear = None #pointer ke node terakhir
        
    def is_empty(self):
        return self.front is None
    
    def enqueue(self, data): #enqueue
        # membuat node baru
        nodeBaru = Node(data) #memanggil class node
        
        # Jika queue masih kosong, front dan rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        # Jika queue tidak kosong:
        #Rear lama menunjuk ke node baru
        self.rear.next = nodeBaru
        
        # rear pindah ke node baru
        self.rear = nodeBaru
    def dequeue(self):
        #menghapus data dari depan
        
        #lihat data yang paling depan
        data_terhapus = self.front.data
        
        #geser front ke node berikutnya
        self.front = self.front.next
        
        # Jika setelah geser front menjadi none, maka queue kosong
        # rear juga haru jadi none
        if self.front is None:
            self.rear = None
        
        return data_terhapus
        
    def tampilkan(self):
        #Menampilkan queue
        current = self.front
        print("Front", end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        
        print("Rear")
        
#instantiasi objek class QueueLL
q = QueueLL()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()

q.dequeue()
q.tampilkan()