# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Rafif Muhammad Faiz
# NIM     : J0403251024
# Kelas   : TPL B2
# ==============================================================================

# ==================================================
# FILE HANDLING - MEMBACA DATA BUKU
# ==================================================

nama_file = "buku.txt"

# 1. FILE HANDLING & DICTIONARY (Sub-CPMK 1) [cite: 31]

def muat_data_buku(nama_file):
    """
    Fungsi untuk membaca 'buku.txt' dan menyimpannya ke Dictionary.
    Format file: kode_buku,judul,harga
    """
    database_buku = {}

    #Membuka file buku.txt
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()

                kode, judul, harga = baris.split(",")

                database_buku[kode] = {
                    "judul": judul,
                    "harga": int(harga)
                }

    #Jika buku.txt tidak terbaca
    except FileNotFoundError:
        print("File buku.txt tidak ditemukan")

    return database_buku


# ==================================================
# LINKED LIST - PROMOSI
# ==================================================
# 2. LINKED LIST - MANAJEMEN PROMOSI (Sub-CPMK 2) [cite: 32]
class Node:

    def __init__(self, judul):
        self.judul = judul
        self.next = None


class LinkedListPromosi:

    def __init__(self):
        self.head = None


    def tambah_buku_promosi(self, judul):

        node_baru = Node(judul)
        #Kalau belum ada buku di promosi tambahkan menjadi node pertama
        if self.head is None:
            self.head = node_baru
        else:
            current = self.head
            #Mencari node terakhir untuk menjadi node selanjutnya
            while current.next:
                current = current.next

            current.next = node_baru

        print("Buku berhasil ditambahkan ke promosi")


    def tampilkan_promosi(self):

        #Jika belum ada buku di promosi tampilkan pesan
        if self.head is None:
            print("Belum ada buku promosi")
            return

        #Menentukan node pertama
        current = self.head
        no = 1

        print("\nDaftar Buku Promosi:")

        while current:
            print(no, ".", current.judul)
            current = current.next
            no += 1


# ==================================================
# QUEUE - ANTREAN KASIR
# ==================================================
# 3. QUEUE - ANTIREAN KASIR (Sub-CPMK 3) [cite: 33]
class AntreanKasir:

    def __init__(self):
        self.antrean = []


    def tambah_antrean(self, nama):
        #Melakukan penambahan data dengan append
        self.antrean.append(nama)
        print(nama, "masuk antrean")

    #Melayani pelanggan dengan melakukan pop
    def layani_pelanggan(self):
        #Kondisi untuk mengecek apakah terdapat antrean atau tidak
        if len(self.antrean) == 0:
            print("Tidak ada antrean")
        else:
            pelanggan = self.antrean.pop(0)
            print("Melayani pelanggan:", pelanggan)


    def lihat_antrean(self):

        if len(self.antrean) == 0:
            print("Antrean kosong")
        else:
            print("\nDaftar Antrean:")

            for i, nama in enumerate(self.antrean, start=1):
                print(i, ".", nama)


# ==================================================
# SORTING - INSERTION SORT
# ==================================================
# 4. SORTING - LAPORAN TRANSAKSI (Sub-CPMK 4) [cite: 34]
def urutkan_transaksi(data):

    list_harga = data.copy()

    for i in range(1, len(list_harga)):

        key = list_harga[i]
        j = i - 1

        #Mengurutkan secara ascending
        while j >= 0 and list_harga[j] > key:
            list_harga[j+1] = list_harga[j]
            j -= 1

        list_harga[j+1] = key

    return list_harga


# ==================================================
# MAIN PROGRAM
# ==================================================

def main():
    
    #melakukan instantiasi
    data_buku = muat_data_buku(nama_file)
    list_promosi = LinkedListPromosi()
    antrean_toko = AntreanKasir()
    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]

    while True:

        print("\n=== SISTEM MANAJEMEN TOKO BUKU ===")
        print("1. Lihat Katalog Buku")
        print("2. Kelola Daftar Promosi")
        print("3. Kelola Antrean Kasir")
        print("4. Lihat Laporan Penjualan Terurut")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

# ==============================
# MENU 1 KATALOG BUKU
# ==============================

        if pilihan == "1":
            print("\nKatalog Buku")
            for kode in data_buku:
                judul = data_buku[kode]["judul"]
                harga = data_buku[kode]["harga"]

                print(kode, "-", judul, "-", harga)


# ==============================
# MENU 2 PROMOSI
# ==============================

        elif pilihan == "2":

            while True:
                #Menu Tambahan untuk promosi
                print("\n--- Menu Promosi ---")
                print("1. Tambah Buku Promosi")
                print("2. Lihat Buku Promosi")
                print("0. Kembali")

                p = input("Pilih: ")

                if p == "1":

                    judul = input("Masukkan judul buku: ")

                    ditemukan = False

                    for kode in data_buku:
                        #Melakukan requirement apakah input sama dengan data yang ada
                        if data_buku[kode]["judul"].lower() == judul.lower():

                            list_promosi.tambah_buku_promosi(judul)

                            ditemukan = True
                            break

                    if not ditemukan:
                        print("Buku tidak ditemukan di katalog")


                elif p == "2":

                    list_promosi.tampilkan_promosi()


                elif p == "0":
                    break

                else:
                    print("Pilihan tidak valid")


# ==============================
# MENU 3 ANTREAN
# ==============================

        elif pilihan == "3":

            while True:
                #Menu Tambahan untuk mengelola antrean kasir
                print("\n--- Menu Antrean Kasir ---")
                print("1. Tambah Antrean")
                print("2. Layani Pelanggan")
                print("3. Lihat Antrean")
                print("0. Kembali")

                a = input("Pilih: ")

                if a == "1":

                    nama = input("Nama pelanggan: ")
                    antrean_toko.tambah_antrean(nama)
                elif a == "2":
                    antrean_toko.layani_pelanggan()
                elif a == "3":
                    antrean_toko.lihat_antrean()
                elif a == "0":
                    break
                else:
                    print("Pilihan tidak valid")


# ==============================
# MENU 4 SORTING
# ==============================

        elif pilihan == "4":
            print("Harga sebelum urut:", riwayat_transaksi)
            hasil = urutkan_transaksi(riwayat_transaksi)
            print("Harga setelah urut:", hasil)

        elif pilihan == "5":
            print("Program selesai")
            break

        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    main()