#===============================================================
# Rafif Muhammad Faiz
# J0403251024 - TPL B
# Latihan 3: Implementasi Bellman-Ford
#===============================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},  # A ke B = 5, A ke C = 4
    'B': {},                # B ga punya tetangga
    'C': {'B': -2}          # C ke B = -2 (bobot negatif)
}

def bellman_ford(graph, start):
 
    # Fungsi untuk mencari jarak terpendek dari node start
    # ke seluruh node lain menggunakan algoritma Bellman-Ford.

    # Inisialisasi semua jarak = tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke dirinya sendiri = 0
    distances[start] = 0

    # Lakukan relaksasi sebanyak (jumlah node - 1) kali
    for _ in range(len(graph) - 1):

        # Iterasi semua node
        for node in graph:

            # Iterasi semua edge dari node tersebut
            for neighbor, weight in graph[node].items():

                # Kalau jarak ke node sudah diketahui
                # dan ditemukan jalur lebih pendek ke neighbor
                if distances[node] != float('inf') and \
                   distances[node] + weight < distances[neighbor]:

                    # Update jarak ke neighbor
                    distances[neighbor] = distances[node] + weight

    # Kembalikan hasil jarak
    return distances


# Panggil fungsi dari node A
hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


# =========================
# Jawaban Analisis:
# =========================

# 1. Berapa bobot langsung dari A ke B?
# 5

# 2. Berapa total bobot jalur A -> C -> B?
# 4 + (-2) = 2

# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
# Ada dua jalur dari A ke B, yaitu langsung (bobot 5)
# dan melalui C (4 lalu -2 jadi total 2).
# Karena 2 lebih kecil dari 5, jalur A -> C -> B lebih pendek
# meskipun tidak langsung karena ada bobot negatif.

# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
# Karena Bellman-Ford tidak langsung "mengunci" jarak seperti Dijkstra.
# Bellman Ford melakukan relaksasi berulang kali,
# sehingga bisa menemukan jalur yang lebih pendek walaupun ada bobot negatif.


# 5. Apa yang dimaksud dengan proses relaksasi edge?
# Relaksasi edge adalah proses mengecek apakah suatu jalur bisa dipersingkat.
# Jika jarak ke node tujuan bisa dibuat lebih kecil lewat jalur tertentu,
# maka nilai jaraknya akan diperbarui (di-update)

# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
# - Dijkstra:
#   Lebih cepat, tapi hanya bisa untuk bobot positif
# - Bellman-Ford:
#   Lebih lambat, tapi bisa menangani bobot negatif
#   dan lebih fleksibel dalam berbagai kondisi graph