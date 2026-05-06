#===============================================================
# Rafif Muhammad Faiz
# J0403251024 - TPL B
# Implementasi Dijkstra
#===============================================================
import heapq

# Struktur data graf
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    # Menyimpan jarak minimum ke semua node
    distances = {node: float('inf') for node in graph}
    
    # Jarak node awal ke dirinya sendiri adalah 0
    distances[start] = 0
    
    # Inisialisasi Priority Queue
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # Jika jarak yang baru diambil lebih besar dari yang sudah tercatat, abaikan
        if current_distance > distances[current_node]:
            continue
            
        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Jika ditemukan jalur yang lebih pendek ke tetangga
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                
    return distances

# Eksekusi fungsi
hasil = dijkstra(graph, 'A')
print(hasil)