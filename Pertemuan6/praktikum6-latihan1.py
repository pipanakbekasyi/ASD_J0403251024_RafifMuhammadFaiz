#===========================================================
# Rafif Muhammad Faiz
# TPl B2
# J0403251024
# ============================================================

#===========================================================
# Ltihan Insertion Sort
#===========================================================
def insertion_sort(data):
    
    for i in range(1, len(data)):
        
       
        key = data[i]
        
        j = i - 1

        while j >= 0 and data[j] > key:
            
            
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data


angka = [13, 7, 28, 5, 19, 36, 4]
print("Hasil Sorting:", insertion_sort(angka))

# 1. Mengapa perulangan dimulai dari indeks 1?
# Jawaban = Karena indeks ke 0 dianggap sudah berurut 
#           dan perulangan sebenarnya dimulai dari indeks ke 1
# 2. Apa fungsi variabel key?
# Jawaban = Key sebagai pointer untuk menyimpan nilai yang ingin di sort 
#           untuk di sisipkan ke posisi yang benar
# 3. Mengapa digunakan while, bukan for?
# Jawaban = Penggunaan iterasi while digunakan karena perulangan yang dilakukan
#           bukan jumlah yang pasti (menyesuaikan elemen yang ingin disort)
# 4. Operasi apa yang terjadi di dalam while?
# Jawaban = di dalam while terjadi pergeseran elemen dengan 
#           elemen yang lebih bessar dari key digeser satu langkah ke kanan(key digeser ke kiri)