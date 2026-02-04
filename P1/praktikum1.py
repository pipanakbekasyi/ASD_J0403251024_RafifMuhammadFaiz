# ================================================
# Praktikum 1: Konsep ADT dan file Handling
# Latihan Dasar 1A : Membaca seluruh isi file
# ================================================

# membuka file dengan mode read ('r')

with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    isi_file = file.read() #membaca file keseluruhan isi file dalam satu string

print(isi_file)
print("")
print("===Hasil Read====")
print("Tipe Data: ", type(isi_file))
print("Jumlah Karakter: ", len(isi_file)) 
print("Jumlah Baris: ", isi_file.count('\n')+1)

# membuka file perbaaris
print("======Membaca Fie per Baris=======")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() #ambil baris tanpa spasi
        print("Baris ke-", jumlah_baris)
        print("Isinya : ", baris)
print()    
        
# ================================================
# Praktikum 1: Konsep ADT dan file Handling
# Latihan Dasar 2 : Parsing baris menjadi kolom data
# ================================================

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",") #parsing data berdasarkan karakter ,
        print("NIM: ", nim, " | Nama: ", nama, " | Nilai: ", nilai)
        

# ================================================
# Praktikum 1: Konsep ADT dan file Handling
# Latihan Dasar 3 : Membaca file dan menyimpan ke list
# ================================================

print()
data_list = [] #List untuk menampung data mahasiswa

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        #simpan sebagai list "[nim, nama, nilai]"
        data_list.append([nim, nama, int(nilai)])

print("=====Data Mahasiswa dalam LIST=====")
print(data_list)

print("======Jumlah Record dalam LIST======")
print("Jumlah Record ", len(data_list))

print("======Contoh Record Pertama======")
print("Contoh Record Pertama: ", data_list[0])

# ================================================
# Praktikum 1: Konsep ADT dan file Handling
# Latihan Dasar 4 : Membaca file dan menyimpan ke dictionary
# ================================================

print()
data_dict = {} #Dictionary untuk menampung data mahasiswa

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        #Simpan data mahasiswa ke dictionary dengan key NIM
        data_dict[nim] = {
            "nama": nama,
            "nilai": int(nilai)
            }

print("=====Data Mahasiswa dalam DICTIONARY=====")
print(data_dict)
print()
print()
print("======Jumlah Record dalam DICTIONARY======")
print("Jumlah Record ", len(data_dict))
print()
print("======Contoh Record Pertama======")
print("Contoh Record Pertama: ", data_dict["J0403001"])