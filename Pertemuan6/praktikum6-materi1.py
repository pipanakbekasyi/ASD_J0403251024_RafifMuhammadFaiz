#===========================================================
# Rafif Muhammad Faiz
# TPl B2
# J0403251024
# ============================================================

#===========================================================
# Insertion Soret(Ascending)
#===========================================================

def insertion_sort(data):
    #Loop mulai dari data ke dua / index ke satu
    for i in range(1, len(data)):
        key = data[i] #simpan nilai yang disisipkan
        j = i - 1 #index elemen terakhir di bagian kiri
        
        #geser
        while j>=0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1
        #sisipkan key ke posisi yang benar
        data[j+1] = key
    return data  

angka = [7,8,5,2,4,6]
print("Hasil Dari " ,insertion_sort(angka))