#===============================================================
# Rafif Muhammad Faiz
# J0403251024 - TPL B
# Latihan 2: Implementasi Dijkstra
#===============================================================

import heapq  # buat priority queue (antrian prioritas)

# Graph berbobot 
graph = {
    'A': {'B': 4, 'C': 2},  # dari A ke B = 4, A ke C = 2
    'B': {'D': 5},          # dari B ke D = 5
    'C': {'D': 1},          # dari C ke D = 1
    'D': {}                 # D tidak memiliki tetangga
}

def dijkstra(graph, start):
  
    #Fungsi untuk mencari jarak terpendek dari node start
    #ke seluruh node lain menggunakan algoritma Dijkstra.
  

    # Inisialisasi semua jarak = tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke dirinya sendiri = 0
    distances[start] = 0

    # Priority queue (min-heap), isi (jarak, node)
    priority_queue = [(0, start)]

    # Selama queue masih ada isinya
    while priority_queue:
        # Ambil node dengan jarak paling kecil
        current_distance, current_node = heapq.heappop(priority_queue)

        # Lewati kalau jarak ini udah bukan yang terbaik
        if current_distance > distances[current_node]:
            continue

        # Iterasi semua tetangga dari node sekarang
        for neighbor, weight in graph[current_node].items():
            # Hitung jarak baru
            distance = current_distance + weight

            # Jika jarak lebih kecil, update jarak
            if distance < distances[neighbor]:
                distances[neighbor] = distance

                # Masukin ke queue buat diproses lagi
                heapq.heappush(priority_queue, (distance, neighbor))

    # Balikin hasil akhir semua jarak
    return distances


# Panggil fungsi dari node A
hasil = dijkstra(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# =========================
# Jawaban Analisis:
# =========================

# 1. Jarak terpendek dari A ke B?
# 4

# 2. Jarak terpendek dari A ke C?
# 2

# 3. Jarak terpendek dari A ke D?
# 3 (A -> C -> D = 2 + 1)

# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
# Karena:
# Ketika algoritma berjalan, dari node A terdapat dua pilihan jalur awal:
# ke B dengan biaya 4 dan ke C dengan biaya 2. Karena 2 lebih kecil,
# algoritma akan memproses node C terlebih dahulu.

# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
# Untuk mengambil node dengan jarak paling kecil terlebih dahulu,
# sehingga proses pencarian jalur terpendek jadi optimal

# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
# Karena algoritma ini mengasumsikan bahwa jarak yang sudah ditemukan
# tidak akan berubah. Jika ada bobot negatif, bisa muncul jalur yang
# lebih pendek di belakang, sehingga hasil jadi tidak akurat