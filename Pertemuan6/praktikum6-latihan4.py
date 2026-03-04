#===========================================================
# Rafif Muhammad Faiz
# TPl B2
# J0403251024
# ============================================================

#===========================================================
# Memahami kode program merge sort
#===========================================================

def merge_sort(data):
    if len(data) <= 1:
        return data
    

    mid = len(data) // 2
    left = data[:mid] 
    right = data[mid:] 
    
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    return merge(left_sorted, right_sorted)

def merge(left, right):
     
    result = []
    i = 0
    j = 0
     
     
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

angka = [13,7,28,5,19,36,4]
print("Hasil Sorting: ", merge_sort(angka))

# 1. Apa yang dimaksud dengan base case?
# Jawaban = Base case adalah kondisi yang membatasi perulangan rekursif yang mana perulangan 
#           tersebut akan berhenti jika data hanya ada 1 atau kosong
# 2. Mengapa fungsi memanggil dirinya sendiri?
# Jawaban = Karena fungsi tersebut digunakan untuk membagi data menjadi bagian yang lebih
#           kecil dan bagian yang lebih kecil untuk membuat proses merge sort
# 3. Apa tujuan fungsi merge()?
# Jawaban = Funngsi ini digunakan untuk menggabungkan dua bagian 
#           yang sudah diurutkan menjadi satu (left dan right) dengan membandingkan elemen kiri dan kanan 
#           lalu dimasukkan ke dalam result
