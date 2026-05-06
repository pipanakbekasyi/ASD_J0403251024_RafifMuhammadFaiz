#===============================================================
# Rafif Muhammad Faiz
# J0403251024 - TPL B
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
#===============================================================

import heapq  # untuk priority queue

# Graph lokasi kampus (bobot = waktu tempuh dalam menit)
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    # Inisialisasi semua jarak = tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke dirinya sendiri = 0
    distances[start] = 0

    # Priority queue (min-heap)
    priority_queue = [(0, start)]

    # Proses selama queue tidak kosong
    while priority_queue:
        # Ambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(priority_queue)

        # Lewati kalau bukan jarak terbaik
        if current_distance > distances[current_node]:
            continue

        # Cek semua tetangga
        for neighbor, weight in graph[current_node].items():
            # Hitung jarak baru
            distance = current_distance + weight

            # Update kalau jarak lebih kecil
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Jalankan dari Gerbang
hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")


# =========================
# Jawaban Analisis:
# =========================

# 1. Lokasi mana yang paling dekat dari Gerbang?
# Kantin (2 menit)

# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
# 7 menit (Gerbang -> Kantin -> Lab -> Aula = 2 + 4 + 1)

# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
# Tidak. Jalur tidak langsung bisa lebih cepat.
# Contohnya ke Aula jarak langsung dari Kantin ke Aula = 7,
# tapi lewat Lab jadi 2 + 4 + 1 = 7 (sama), bahkan di kasus lain bisa lebih kecil.

# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
# Karena semua bobot (waktu tempuh) bernilai positif,
# dan kita ingin mencari jalur tercepat ke setiap lokasi.
# Dijkstra efisien dan akurat untuk kondisi seperti ini