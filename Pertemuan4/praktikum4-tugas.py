#=====================================================================
# Nama:  Rafif Muhammad Faiz
# NIM:   J0403251024
# Kelas: TPL B / P2
#======================================================================

#=======================================================================
#
# Studi Kasus: Sistem Antrian Bengkel
#Impelementasi Queue
# Stack -> Front -> C  -> B -> A -> None
#Enqueue -> Memindahkan pointer rear(nambah data baeru dari belakang)
#Dequeue -> Memindahkan pointer front(menghapus data dari depan)
# Front -> A ->Rear
#=========================================================================

#1 Membuat class node (unit dasar linked list)
class Node:
    def __init__(self, no, nama, servis):
        self.no = no #menyimpan no antrian 
        self.nama = nama #menyimpan nama pelanggan
        self.servis = servis #menyimpan jenis servis yang dilakukan
        self.next = None #pointer ke node berikutnya
        
#2 Mendfinisikan queue terdiri dari front dan rear
class queueBengkel:
    def __init__(self):
        self.front = None #pointer ke node pertama
        self.rear = None #pointer ke node terakhir
    
    def is_empty(self):
        #Ketika queue kosong maka front = rear = none
        return self.front is None
    
    # mengecek apakah nomor antrian sudah ada
    def cek_no(self, no):
        current = self.front
        while current is not None:
            if current.no == no:
                return True   # nomor sudah ada
            current = current.next
        return False  # nomor belum ada
    
    #menambah data baru ke bagian belakang
    def enqueue(self, no, nama, servis):    

        nodeBaru = Node(no, nama, servis)

        # jika queue kosong
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return

        self.rear.next = nodeBaru
        self.rear = nodeBaru
    
    #menghapus data paling depan (memberikan layanan bengkel)
    def dequeue(self):
        if self.is_empty():
            print("Antrian Kosong. Tidak ada orang yang ingin servis")
            return None
        
        #lihat data bagian dari front, simpan di variabel data yang akan dihapus (dilayani)
        node_dilayani = self.front
        
        #geser pointer ke next front
        self.front = self.front.next
        
        #Jiika front menjadi none (data antrian terakhir yang dilayani), maka front = rear = none
        if self.front is None:
            self.rear = None
        
        return node_dilayani
    
    #menampilkan antrian
    def tampilkan(self):
        print("Antrian Bengkel(Front -> Rear): ")
        if self.is_empty():
            print("Antrian Kosong")
            return
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. {current.no} - {current.nama} - {current.servis}")
            current = current.next
            no += 1
            

#Program Utama
def main():
    #instantiasi queue
    q = queueBengkel()
    while True:
        print("Menu:")
        print("1. Tambah Antrian")
        print("2. Layani Antrian")
        print("3. Tampilkan Antrian")
        print("4. Keluar")
        
        pilihan = input("Masukkan pilihan menu (1-4): ").strip()
        
        if pilihan == "1":
            no = input("Masukkan no antrian: ").strip()
            # cek nomor
            if q.cek_no(no):
                print("Nomor antrian sudah digunakan!")
                continue   # langsung balik ke menu

            nama = input("Masukkan nama pelanggan: ").strip()
            servis = input("Masukkan jenis servis: ").strip()
            q.enqueue(no, nama, servis)
            print("Antrian berhasil ditambahkan.")
        
        elif pilihan == "2":
            node_dilayani = q.dequeue()
            if node_dilayani is not None:
                print(f"Antrian {node_dilayani.no} - {node_dilayani.nama} - {node_dilayani.servis} telah dilayani.")
        
        elif pilihan == "3":
            q.tampilkan()
        
        elif pilihan == "4":
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()