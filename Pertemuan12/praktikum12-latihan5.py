#===============================================================
# Rafif Muhammad Faiz
# J0403251024 - TPL B
# Latihan 5: 
# Algoritma: Dijkstra
#===============================================================

import heapq  # untuk priority queue

# 1. Representasi graph berbobot (antar kota)
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

# 2. Fungsi Dijkstra
def dijkstra(graph, start):
    # Inisialisasi semua jarak = tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke dirinya sendiri = 0
    distances[start] = 0

    # Priority queue (min-heap) untuk ambil jarak terkecil
    priority_queue = [(0, start)]

    # Proses selama queue masih ada
    while priority_queue:
        # Ambil node dengan jarak paling kecil
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip jika sudah ada jarak lebih kecil
        if current_distance > distances[current_node]:
            continue

        # Iterasi semua tetangga
        for neighbor, weight in graph[current_node].items():
            # Hitung jarak baru
            distance = current_distance + weight

            # Update jika lebih kecil
            if distance < distances[neighbor]:
                distances[neighbor] = distance

                # Masukkan ke queue untuk diproses
                heapq.heappush(priority_queue, (distance, neighbor))

    # Kembalikan hasil jarak
    return distances


# 3. Node awal (ditentukan dalam program)
start_node = 'Bogor'

# Jalankan algoritma
hasil = dijkstra(graph, start_node)

# 4. Output hasil jarak terpendek
print(f"Jarak terpendek dari {start_node}:")
for kota, jarak in hasil.items():
    print(kota, "=", jarak)


# =========================
# Jawaban Analisis:
# =========================

# 1. Node awal yang digunakan apa?
# Bogor

# 2. Node mana yang memiliki jarak paling kecil dari node awal?
# Depok (2), karena dari Bogor langsung ke Depok dengan bobot paling kecil

# 3. Node mana yang memiliki jarak paling besar dari node awal?
# Bandung (8), karena membutuhkan beberapa jalur untuk mencapainya

# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat
# Secara deskriptif:
# Algoritma dimulai dari node Bogor dengan jarak 0.
# Dari Bogor, ada dua pilihan yaitu ke Jakarta (5) dan ke Depok (2).
# Karena 2 lebih kecil, Depok diproses terlebih dahulu.
# Dari Depok, ditemukan jalur ke Jakarta dengan total jarak 4 (2+2),
# yang lebih kecil dibanding jalur langsung Bogor ke Jakarta (5),
# sehingga jarak ke Jakarta diperbarui.
#
# Selanjutnya, dari Depok juga ada jalur ke Bandung dengan total 8.
# Kemudian dari Jakarta ke Bandung menghasilkan jarak 11,
# tetapi tidak dipilih karena lebih besar dari 8.
#
# Proses ini terus berjalan dengan memilih jarak terkecil,
# sampai semua node mendapatkan jarak terpendeknya.