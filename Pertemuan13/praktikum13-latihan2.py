# ==========================================================
# Latihan 2
# Rafif Muhammad Faiz
# J0403251024 - TPL B
# Implementasi Sederhana Algoritma Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan daftar edge berdasarkan bobot (elemen pertama dari tuple) secara ascending
edges.sort()

mst = []                # Inisialisasi list untuk menyimpan hasil edge MST
total_weight = 0        # Inisialisasi variabel untuk menghitung akumulasi bobot
connected = set()       # Menggunakan set untuk mencatat node yang sudah terhubung ke MST

# Melakukan perulangan untuk setiap edge dalam daftar yang sudah terurut
for weight, u, v in edges:
    # Memeriksa apakah node u atau node v belum ada di set 'connected'
    # (mencegah cycle)
    if u not in connected or v not in connected:
        mst.append((u, v, weight))      # Menambahkan edge terpilih ke daftar MST
        total_weight += weight          # Menambahkan bobot edge tersebut ke total_weight
        connected.add(u)                # Memasukkan node u ke dalam set connected
        connected.add(v)                # Memasukkan node v ke dalam set connected

# Menampilkan judul output
print("Minimum Spanning Tree:")
# Iterasi untuk menampilkan setiap edge yang masuk dalam MST
for edge in mst:
    print(edge)

# Menampilkan hasil akhir total bobot
print("Total bobot =", total_weight)

# ==========================================================
# Jawaban Analisis:
# 1. Edge mana yang dipilih pertama kali?
#    Edge ('C', 'D') dengan bobot 1. Karena algoritma Kruskal memproses 
#    edge berdasarkan urutan bobot terkecil setelah dilakukan pengurutan.

# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#    Karena Kruskal adalah algoritma "greedy" yang bertujuan mencari total bobot 
#    paling minimal. Dengan mengambil bobot terkecil di setiap langkah, kita 
#    berusaha membangun pohon dengan biaya serendah mungkin.

# 3. Berapa total bobot MST yang dihasilkan?
#    Total bobotnya adalah 6. Hasil ini didapat dari penjumlahan edge:
#    (C, D) bobot 1 + (A, C) bobot 2 + (B, D) bobot 3 = 6.

# 4. Mengapa edge tertentu tidak dipilih?
#    Edge (A, B) dengan bobot 4 dan (A, D) dengan bobot 5 tidak dipilih karena 
#    node-node tersebut sudah masuk ke dalam set 'connected'.
#    Menambah edge ke node yang sudah terhubung akan 
#    menciptakan cycle (sirkuit), yang mana hal tersebut dilarang.
# ==========================================================