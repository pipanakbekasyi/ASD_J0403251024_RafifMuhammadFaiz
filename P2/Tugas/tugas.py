# ==================================================
# tugas 2 : Konsep ADT dan file Handling
# sub tugas 1: Membuat fungsi load data
# ==================================================

nama_file = "stok.txt"

def baca_data_stok(nama_file):
    data_dict = {}  #inisialisasi
    
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            kode_barang, nama_barang, stok = baris.split(",")
            #Simpan data barang ke dictionary dengan key kode_barang
            data_dict[kode_barang] = {
                "nama_barang": nama_barang,
                "stok": int(stok)
                }
    return data_dict



# ==================================================
# tugas 2 : Konsep ADT dan file Handling
# sub tugas 2: Membuat fungsi menampilkan data
# ==================================================

def tampil_data(data_dict):
    
    if len(data_dict) == 0:
        print("Tidak ada data barang")
        return
    
    # membuat header table
    print("\n===== Daftar Stok Barang =====")
    print(f"{"Kode Barang": <10} | {"Nama_Barang" : <15} | {"Stok": >5}")
    print("-" * 40) #membuat garis header table
    
    # untuk tampilan yang rqapi, atur f string formating
    # {"kode_barang" : < 10} artinya : tampilkan kode_barang dengan lebar 10 dan rata kiri
    # {"nama_barang" : < 12} artinya : tampilkan nama dengan lebar 12 dan rata kiri
    # {"stok" : < > 5} artinya : tampilkan nama dengan lebar 5 dan rata kanan
    
    
    for kode_barang in sorted(data_dict.keys()):
        nama_barang=data_dict[kode_barang]["nama_barang"]
        stok=data_dict[kode_barang]["stok"]
        print(f"{kode_barang: <10} | {nama_barang: <15} | {stok: >5}")
        
# memanggil fungsi tampil_data
# tampil_data(buka_data)


# ==================================================
# tugas 2 : Konsep ADT dan file Handling
# sub tugas 3 : Membuat fungsi mencari data
# ==================================================
def cari_data(data_dict):
    # mencari data barang berdasarkan kode_barang
    kode_barang_cari = input("Masukkan Kode Barang yang ingin dicari: ").strip()
    
    if kode_barang_cari in data_dict:
        nama_barang = data_dict[kode_barang_cari]["nama_barang"]
        stok = data_dict[kode_barang_cari]["stok"]
        
        print(f"===== Data berhasil ditemukan =====")
        print(f"kode_barang: {kode_barang_cari}")
        print(f"Nama: {nama_barang}")
        print(f"stok: {stok}")
    else:
        print(f"Data dengan kode_barang {kode_barang_cari} tidak ditemukan")

# cari_data(buka_data)

# ==================================================
# tugas 2 : Konsep ADT dan file Handling
# sub tugas 4: Membuat fungsi update stok
# ==================================================

def update_stok(data_dict):
    
    kode_barang = input("Masukkan kode_barang: ").strip()
    
    if kode_barang not in data_dict:
        print("kode_barang tidak ditemukan, update tidak dilakukan")
        return
    #masukkan stok baru
    try:
        stok_baru = int(input("Masukkan stok baru(0-100): ").strip())
    except ValueError:
        print("stok harus berupa angka")
        return
    
    if stok_baru < 0 or stok_baru > 100:
        print("stok harus berupa antara 0 sampai 100. Update dibatalkan")
    else:
        stok_lama = data_dict[kode_barang]["stok"]
        #masukkan stok baru ke dict
        data_dict[kode_barang]["stok"] = stok_baru
        print(f"Update Berhasil. stok {kode_barang} berubah dari {stok_lama} menjadi {stok_baru}")
    
# update_stok(buka_data)

# ==================================================
# tugas 2 : Konsep ADT dan file Handling
# sub tugas 5: Membuat fungsi menyimpan stok
# ==================================================

def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode_barang in sorted(data_dict.keys()):
            nama_barang = data_dict[kode_barang]["nama"]
            stok = data_dict[kode_barang]["stok"]
            file.write(f"{kode_barang},{nama_barang},{stok}\n")

# simpan_data(nama_file, buka_data)


# ==================================================
# tugas 2 : Konsep ADT dan file Handling
# sub tugas 2: Membuat fungsi menambah barang
# ==================================================
def tambah_barang(data_dict):
    kode_barang = input("Masukkan Kode Barang: ").strip()

    if kode_barang in data_dict:
        print("Kode barang sudah ada. Kembali ke menu.")
        return

    nama_barang = input("Masukkan Nama Barang: ").strip()

    # cek nama barang sudah ada atau belum
    for kode in data_dict:
        if data_dict[kode]["nama_barang"].lower() == nama_barang.lower():
            print("Nama barang sudah ada. Kembali ke menu.")
            return

    try:
        stok = int(input("Masukkan Stok Barang (0-100): ").strip())
    except ValueError:
        print("Stok harus berupa angka. Kembali ke menu.")
        return

    if stok < 0 or stok > 100:
        print("Stok harus antara 0 sampai 100. Kembali ke menu.")
        return

    # simpan ke dictionary
    data_dict[kode_barang] = {
        "nama_barang": nama_barang,
        "stok": stok
    }

    # simpan ke file
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode_barang in sorted(data_dict.keys()):
            nama_barang = data_dict[kode_barang]["nama_barang"]
            stok = data_dict[kode_barang]["stok"]
            file.write(f"{kode_barang},{nama_barang},{stok}\n")

    print("Barang berhasil ditambahkan.")

        

# ==================================================
# tugas 2 : Konsep ADT dan file Handling
# sub tugas 6: Membuat fungsi menu
# ==================================================

def main():
    
    # menjalankan fungsi 1 load data
    buka_data = baca_data_stok(nama_file)

    while True:
        print("\n===== Menu Utama =====")
        print("1. Tampilkan Data Barang") #fs no 2
        print("2. Cari Data Barang berdasarkan kode_barang") #fs no 3
        print("3. Update stok Barang")
        print("4. Tambah Data Barang")
        print("0. Keluar")
        
        pilihan = input("Pilih menu: ").strip()
        
        if pilihan == "1":
            tampil_data(buka_data)
        elif pilihan == "2":
            cari_data(buka_data)
        elif pilihan == "3":
            update_stok(buka_data)
        elif pilihan == "4":
            tambah_barang(buka_data)
        elif pilihan == "0":
            print("Terima kasih sudah menggunakan program ini")
            break
        else:
            print("Pilihan tidak valid")
            
if __name__ == "__main__":
    main()