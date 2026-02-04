# ==================================================
# Praktikum 2 : Konsep ADT dan file Handling
# Latihan Dasar 1: Membuat fungsi lload data
# ==================================================

nama_file = "data_mahasiswaDua.txt"

def baca_data_mahasiswa(nama_file):
    data_dict = {}  #inisialisasi
    
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            nim, nama, nilai = baris.split(",")
            #Simpan data mahasiswa ke dictionary dengan key NIM
            data_dict[nim] = {
                "nama": nama,
                "nilai": int(nilai)
                }
    return data_dict

#memanggil fungsi baca_data_mahasiswa
# buka_data = baca_data_mahasiswa(nama_file)
# print("Jumlah Data Mahasiswa", len(buka_data))
# print()

# ==================================================
# Praktikum 2 : Konsep ADT dan file Handling
# Latihan Dasar 2: Membuat fungsi menampilkan data
# ==================================================

def tampil_data(data_dict):
    
    if len(data_dict) == 0:
        print("Tidak ada data mahasiswa")
        return
    
    # membuat header table
    print("\n===== Daftar Mahasiswa =====")
    print(f"{"NIM": <10} | {"Nama" : <12} | {"Nilai": >5}")
    print("-" * 32) #membuat garis header table
    
    # untuk tampilan yang rqapi, atur f string formating
    # {"NIM" : < 10} artinya : tampilkan nim dengan lebar 10 dan rata kiri
    # {"Nama" : < 12} artinya : tampilkan nama dengan lebar 12 dan rata kiri
    # {"Nilai" : < > 5} artinya : tampilkan nama dengan lebar 5 dan rata kanan
    
    
    for nim in sorted(data_dict.keys()):
        nama=data_dict[nim]["nama"]
        nilai=data_dict[nim]["nilai"]
        print(f"{nim: <10} | {nama: <12} | {nilai: >5}")
        
# memanggil fungsi tampil_data
# tampil_data(buka_data)


# ==================================================
# Praktikum 2 : Konsep ADT dan file Handling
# Latihan Dasar 3 : Membuat fungsi mencari data
# ==================================================
def cari_data(data_dict):
    # mencari data mahasiswa berdasarkan nim
    nim_cari = input("Masukkan NIM yang ingin dicari: ").strip()
    
    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]
        
        print(f"===== Data berhasil ditemukan =====")
        print(f"NIM: {nim_cari}")
        print(f"Nama: {nama}")
        print(f"Nilai: {nilai}")
    else:
        print(f"Data dengan NIM {nim_cari} tidak ditemukan")

# cari_data(buka_data)

# ==================================================
# Praktikum 2 : Konsep ADT dan file Handling
# Latihan Dasar 4: Membuat fungsi update nilai
# ==================================================

def update_nilai(data_dict):
    
    nim = input("Masukkan NIM mahasiswa: ").strip()
    
    if nim not in data_dict:
        print("NIM tidak ditemukan, update tidak dilakukan")
        return
    #masukkan nilai baru
    try:
        nilai_baru = int(input("Masukkan nilai baru(0-100): ").strip())
    except ValueError:
        print("Nilai harus berupa angka")
        return
    
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus berupa antara 0 sampai 100. Update dibatalkan")
    else:
        nilai_lama = data_dict[nim]["nilai"]
        #masukkan nilai baru ke dict
        data_dict[nim]["nilai"] = nilai_baru
        print(f"Update Berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")
    
# update_nilai(buka_data)

# ==================================================
# Praktikum 2 : Konsep ADT dan file Handling
# Latihan Dasar 5: Membuat fungsi menyimpan nilai
# ==================================================

def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")
            print("Data berhasil disimpan")



# ==================================================
# Praktikum 2 : Konsep ADT dan file Handling
# Latihan Dasar 6: Membuat fungsi menyimpan nilai
# ==================================================

def main():
    
    # menjalankan fungsi 1 load data
    buka_data = baca_data_mahasiswa(nama_file)

    while True:
        print("\n===== Menu Utama =====")
        print("1. Tampilkan Data Mahasiswa") #fs no 2
        print("2. Cari Data Mahasiswa berdasarkan NIM") #fs no 3
        print("3. Update Nilai Mahasiswa")
        print("4. Simpan Data Mahasiswa")
        print("0. Keluar")
        
        pilihan = input("Pilih menu: ").strip()
        
        if pilihan == "1":
            tampil_data(buka_data)
        elif pilihan == "2":
            cari_data(buka_data)
        elif pilihan == "3":
            update_nilai(buka_data)
        elif pilihan == "4":
            simpan_data(nama_file, buka_data)
            print("Data berhasil disimpan")
        elif pilihan == "0":
            print("Terima kasih sudah menggunakan program ini")
            break
        else:
            print("Pilihan tidak valid")
            
if __name__ == "__main__":
    main()