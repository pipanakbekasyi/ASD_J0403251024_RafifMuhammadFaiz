# ==========================================================
# Implementasi Algoritma Prim
# Rafif Muhammad Faiz
# J0403251024 - TPL B
# ==========================================================

# Import library heapq untuk membuat priority queue
import heapq

# Representasi graph menggunakan dictionary
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

# Fungsi algoritma Prim
def prim(graph, start):

    # Set untuk menyimpan node yang sudah dikunjungi
    visited = set([start])

    # List priority queue untuk menyimpan edge
    edges = []

    # Memasukkan semua edge dari node awal ke priority queue
    for neighbor, weight in graph[start].items():

        # Menambahkan edge ke heap
        # (bobot, node_asal, node_tujuan)
        heapq.heappush(edges, (weight, start, neighbor))

    # List untuk menyimpan hasil MST
    mst = []

    # Variabel untuk menyimpan total bobot MST
    total_weight = 0

    # Perulangan selama masih ada edge pada heap
    while edges:

        # Mengambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges)

        # Jika node tujuan belum dikunjungi
        if v not in visited:

            # Menandai node sebagai sudah dikunjungi
            visited.add(v)

            # Menambahkan edge ke MST
            mst.append((u, v, weight))

            # Menambahkan bobot ke total bobot MST
            total_weight += weight

            # Mengecek semua tetangga dari node baru
            for neighbor, w in graph[v].items():

                # Jika tetangga belum dikunjungi
                if neighbor not in visited:

                    # Menambahkan edge baru ke heap
                    heapq.heappush(edges, (w, v, neighbor))

    # Mengembalikan hasil MST dan total bobot
    return mst, total_weight


# Memanggil fungsi Prim dimulai dari node A
mst, total = prim(graph, 'A')

# Menampilkan hasil MST
print("Minimum Spanning Tree:")

# Menampilkan setiap edge pada MST
for edge in mst:
    print(edge)

# Menampilkan total bobot MST
print("Total bobot =", total)


# ==========================================================
# Penjelasan Program
# ==========================================================
#
# Graph disimpan dalam bentuk dictionary yang berisi
# node, tetangga, dan bobot edge.
#
# Program dimulai dari node awal, yaitu node A.
# Semua edge yang terhubung ke node awal dimasukkan
# ke dalam priority queue (heap).
#
# Program kemudian melakukan perulangan:
# 1. Mengambil edge dengan bobot terkecil
# 2. Mengecek apakah node tujuan sudah dikunjungi
# 3. Jika belum, edge dimasukkan ke MST
# 4. Node ditandai sebagai visited
# 5. Semua edge baru dari node tersebut dimasukkan ke heap
#
# Hasil akhir program menampilkan:
# 1. Edge yang termasuk dalam MST
# 2. Total bobot minimum graph
#
# Sehingga total bobot minimum = 6
#
# ==========================================================