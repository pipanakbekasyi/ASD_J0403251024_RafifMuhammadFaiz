# ==========================================================
# Implementasi Kruskal
# Rafif Muhammad Faiz
# J0403251024 - TPL B
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
 (1, 'C', 'D'),   # Edge C-D dengan bobot 1
 (2, 'A', 'C'),   # Edge A-C dengan bobot 2
 (3, 'B', 'D'),   # Edge B-D dengan bobot 3
 (4, 'A', 'B'),   # Edge A-B dengan bobot 4
 (5, 'A', 'D')    # Edge A-D dengan bobot 5
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

# List untuk menyimpan hasil Minimum Spanning Tree
mst = []

# Variabel untuk menghitung total bobot MST
total_weight = 0

# Set untuk menyimpan node yang sudah terhubung
connected = set()

# Melakukan perulangan pada setiap edge
for weight, u, v in edges:

 # Mengecek edge membentuk cycle sederhana
 # Jika salah satu node belum terhubung,
 # maka edge dapat dimasukkan ke MST
    if u not in connected or v not in connected:

        # Menambahkan edge ke MST
        mst.append((u, v, weight))

        # Menambahkan bobot edge ke total bobot
        total_weight += weight

    # Menambahkan node ke set connected
    connected.add(u)
    connected.add(v)

# Menampilkan hasil MST
print("Minimum Spanning Tree:")

# Menampilkan setiap edge pada MST
for edge in mst:
    print(edge)

# Menampilkan total bobot MST
print("Total bobot =", total_weight)


# ==========================================================
# Penjelasan Program
# ==========================================================
#
# Langkah pertama adalah membuat daftar edge yang berisi
# hubungan antar node beserta bobotnya.
#
# Semua edge diurutkan dari bobot terkecil
# ke terbesar menggunakan sort().
# Program kemudian melakukan pengecekan satu per satu
# terhadap edge yang sudah diurutkan.
#
# Jika edge tidak membentuk cycle sederhana,
# maka edge akan dimasukkan ke dalam MST dan
# bobotnya ditambahkan ke total bobot.
#
# Set connected digunakan untuk menandai node yang
# sudah terhubung.
#
# Hasil akhir program menampilkan:
# 1. Edge yang termasuk ke dalam Minimum Spanning Tree
# 2. Total bobot minimum dari graph
#
# ==========================================================