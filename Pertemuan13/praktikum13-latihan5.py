# ==========================================================
# Implementasi Algoritma Kruskal
# Kasus 1 : Jaringan Jalan Antar Kota
# Rafif Muhammad Faiz
# J0403251024 - TPL B
# ==========================================================

# Daftar edge graph dalam format:
# (bobot, kota1, kota2)
edges = [
    (5, 'Bogor', 'Jakarta'),     # Jalan Bogor - Jakarta bobot 5
    (2, 'Bogor', 'Depok'),       # Jalan Bogor - Depok bobot 2
    (3, 'Depok', 'Jakarta'),     # Jalan Depok - Jakarta bobot 3
    (6, 'Jakarta', 'Bandung'),   # Jalan Jakarta - Bandung bobot 6
    (4, 'Depok', 'Bandung')      # Jalan Depok - Bandung bobot 4
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

# List untuk menyimpan hasil Minimum Spanning Tree
mst = []

# Variabel untuk menyimpan total bobot MST
total_weight = 0

# Set untuk menyimpan kota yang sudah terhubung
connected = set()

# Perulangan untuk memeriksa setiap edge
for weight, u, v in edges:

    # Jika salah satu kota belum terhubung,
    # maka edge dapat dimasukkan ke MST
    if u not in connected or v not in connected:

        # Menambahkan edge ke MST
        mst.append((u, v, weight))

        # Menambahkan bobot ke total bobot
        total_weight += weight

    # Menandai kota sebagai sudah terhubung
    connected.add(u)
    connected.add(v)

# Menampilkan hasil MST
print("Minimum Spanning Tree:")

# Menampilkan setiap edge pada MST
for edge in mst:
    print(edge)

# Menampilkan total bobot MST
print("Total bobot minimum =", total_weight)


# ==========================================================
# Jawaban Analisis
# ==========================================================
#
# 1. Kasus apa yang dipilih?
# Kasus yang dipilih adalah
# "Jaringan Jalan Antar Kota".
#
# 2. Algoritma apa yang digunakan?
# Algoritma yang digunakan adalah algoritma Kruskal.
#
#
# 3. Edge mana saja yang dipilih dalam MST?
# Edge yang dipilih:
# - Bogor - Depok = 2
# - Depok - Jakarta = 3
# - Depok - Bandung = 4
#
#
# 4. Berapa total bobot MST?
# Total bobot MST:
# 2 + 3 + 4 = 9
#
#
# 5. Mengapa edge tertentu tidak dipilih?
# Karena edge tersebut memiliki bobot lebih besar
# atau dapat membentuk cycle.
# - Bogor - Jakarta = 5 tidak dipilih karena
#   Bogor dan Jakarta sudah terhubung melalui Depok
#   dengan total bobot yang lebih kecil.
# - Jakarta - Bandung = 6 tidak dipilih karena
#   sudah ada jalur Depok - Bandung dengan bobot 4
#   yang lebih minimum.
#
# ==========================================================