# ==========================================================
# Implementasi Algoritma Kruskal
# Studi Kasus Jaringan Kabel Internet Antar Gedung
# Rafif Muhammad Faiz
# J0403251024 - TPL B
# ==========================================================

# Daftar edge graph
# (biaya, gedung1, gedung2)
edges = [
    (4, 'GedungA', 'GedungB'),   # Kabel A-B biaya 4
    (2, 'GedungA', 'GedungC'),   # Kabel A-C biaya 2
    (3, 'GedungB', 'GedungD'),   # Kabel B-D biaya 3
    (1, 'GedungC', 'GedungD'),   # Kabel C-D biaya 1
    (5, 'GedungA', 'GedungD')    # Kabel A-D biaya 5
]

# Mengurutkan edge berdasarkan biaya terkecil
edges.sort()

# List untuk menyimpan hasil Minimum Spanning Tree
mst = []

# Variabel untuk menyimpan total biaya minimum
total_cost = 0

# Set untuk menyimpan gedung yang sudah terhubung
connected = set()

# Perulangan untuk memeriksa setiap edge
for cost, u, v in edges:

    # Jika salah satu gedung belum terhubung,
    # maka edge dapat dimasukkan ke MST
    if u not in connected or v not in connected:

        # Menambahkan edge ke MST
        mst.append((u, v, cost))

        # Menambahkan biaya ke total biaya
        total_cost += cost

    # Menandai gedung sebagai sudah terhubung
    connected.add(u)
    connected.add(v)

# Menampilkan hasil MST
print("Jaringan Kabel Minimum:")

# Menampilkan edge yang dipilih
for edge in mst:
    print(edge)

# Menampilkan total biaya minimum
print("Total biaya minimum =", total_cost)


# ==========================================================
# Jawaban Analisis
# ==========================================================
#
# 1. Algoritma apa yang digunakan?
# Algoritma yang digunakan adalah algoritma Kruskal.
#
#
# 2. Edge mana saja yang dipilih?
# Edge yang dipilih:
# - GedungC - GedungD = 1
# - GedungA - GedungC = 2
# - GedungB - GedungD = 3
#
#
# 3. Berapa total biaya minimum?
# Total biaya minimum:
# 1 + 2 + 3 = 6
#
#
# 4. Mengapa MST cocok digunakan pada kasus ini?
# Karena MST dapat menghubungkan semua gedung
# dengan biaya total paling minimum tanpa
# membangun jalur kabel yang berlebihan.
#
# MST juga menghindari cycle sehingga jaringan
# menjadi lebih efisien dan hemat biaya.
#
# ==========================================================