#===========================================================
# Rafif Muhammad Faiz
# TPl B2
# J0403251024
# ============================================================

#===========================================================
# Melengkapi kode agar enjadi sorting ascending
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
# Soal:
# 1. Lengkapi kondisi agar menjadi sorting ascending.
# Jawaban = Kode diatas adalah ascending
# 2. Ubah agar menjadi descending.
# Jawaban = Kode diatas bisa menjadi descending dengan
#           mengubah > menjadi < pada kondisi while