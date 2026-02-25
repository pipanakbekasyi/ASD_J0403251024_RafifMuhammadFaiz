#==============================================
#
#Rafif Muhammad Faiz
#J0403251024
#TPL B / P2
#================================================

#================================================
#
# Studi Kasus: Sistem Antrian Layanan Akademik
#Impelementasi Queue
# Stack -> Front -> C  -> B -> A -> None
#Enqueue -> Memindahkan pointer rear(nambah data baeru dari belakang)
#Dequeue -> Memindahkan pointer front(menghapus data dari depan)
# Front -> A ->Rear
#=================================================

#1 Membuat class node (unit dasar linked list)
class Node:
    def __init__(self, nim, nama):
        self.nim  = nim  #menyimpan nim mahasiswa
        self.nama  = nama #menyimpan nama mahasiswa
        self.next  = None #pointer ke node berikutnya

#2 Mendefinisikan queue terdiri dari front dan rear
class queuAkademik:
    def __init__(self):
        self.front = None #pointer ke node pertama
        self.rear = None  #pointer ke node terakhir
    def is_empty(self):
        #Ketika queue kosong maka front = rear = mone
        return self.front is None
    
    #menambah data baru ke bagian belakang
    def enqueue(self, nim, nama):
        nodeBaru = Node(nim, nama)
        #jika queue masih kosong
        if self.is_empty():
            self.front =nodeBaru
            self.rear = nodeBaru
            return
        #membuat node baru dari queue yang tidak kosong dengan data baru diletakkan setelah rear dan dijadikan rear
 
        self.rear.next = nodeBaru
        self.rear = nodeBaru
    
    #menghapus data paling depan (memberikan layanan  akademik)
    def dequeu(self):
        if self.is_empty():
            print("Antrian Kosong. Tidak ada mahasiswa yang dilayani")
            return None
        
        #lihat data bagian dari front, simmpan di variabel data yang akan dihapus (dilayani)
        node_dilayani = self.front
        
        #geser pointer ke next front
        self.front = self.front.next
        
        #Jiika front menjadi none (data antrian terakhir yang dilayani), maka front = rear = none
        if self.front is None:
            self.rear = None
        
        return node_dilayani

    #menampilkan antrian
    def tampilkan(self):
        print("Antrian Mahasiswa(Front -> Rear): ")
        if self.is_empty():
            print("Antrian Kosong")
            return
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. {current.nim} - {current.nama}")
            current = current.next
            no += 1

#Program Utama
def main():
    #instantiasi queue
    q = queuAkademik()
    while True:
        print("Menu:")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Tampilkan Antrian")
        print("4. Keluar")
        
        pilihan = input("Masukkan pilihan menu (1-4): ").strip()
        
        if pilihan == "1":
            nim = input("Masukkan NIM Mahasiswa: ").strip()
            nama = input("Masukkan Nama Mahasiswa: ").strip()
            q.enqueue(nim, nama)
            print("Mahasiswa berhasil ditambahkan ke antrian.")
        
        elif pilihan == "2":
            node_dilayani = q.dequeu()
            if node_dilayani is not None:
                print(f"Mahasiswa dengan NIM {node_dilayani.nim} - {node_dilayani.nama} telah dilayani.")
        
        elif pilihan == "3":
            q.tampilkan()
        
        elif pilihan == "4":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

if __name__ == "__main__": #penanda eksekusi file utama
    main()