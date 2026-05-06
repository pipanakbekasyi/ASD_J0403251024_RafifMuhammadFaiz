#===============================================================
# Rafif Muhammad Faiz
# J0403251024 - TPL B
# Latihan 1: Weighted Graph dan Perhitungan Jalur
#===============================================================

# Representasi weighted graph menggunakan dictionary bersarang
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D']  # A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D']  # A -> C -> D

# Menampilkan hasil perhitungan
print(f"Jalur 1: A -> B -> D = {jalur_1}")
print(f"Jalur 2: A -> C -> D = {jalur_2}")

# Logika penentuan jalur terpendek
if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")
    
# Jawaban Analisis:
# 1. Berapa total bobot jalur A -> B -> D?
# 2. Berapa total bobot jalur A -> C -> D?
# 3. Jalur mana yang dipilih sebagai jalur terpendek?
# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit? 

# =================================================================
# JAWABAN:
# =================================================================

# 1. Total bobot jalur A -> B -> D adalah 9 (4 + 5).
# 2. Total bobot jalur A -> C -> D adalah 3 (2 + 1).
# 3. Jalur yang dipilih sebagai jalur terpendek adalah A -> C -> D.
# 4. Karena di "weighted graph", setiap edge memiliki beban/bobot yang berbeda - beda.
#     Meskipun jumlah edge-nya sedikit, jika bobot tiap edge-nya sangat besar, 
#    maka total biayanya akan lebih mahal dibandingkan jalur dengan banyak edge 
#    namun memiliki bobot yang kecil.