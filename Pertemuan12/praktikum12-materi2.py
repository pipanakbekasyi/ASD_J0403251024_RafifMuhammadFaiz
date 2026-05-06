#===============================================================
# Rafif Muhammad Faiz
# J0403251024 - TPL B
# Implementasi Bellman-Ford
#===============================================================

def bellman_ford(graph, start):
    # Inisialisasi jarak ke semua node dengan nilai tak hingga
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Relaksasi semua edge sebanyak (V - 1) kali
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                # Jika jarak ke node asal sudah diketahui (bukan inf) 
                # dan ditemukan jalur yang lebih pendek
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    
    return distances

#Inisialisasi graf dengan bellman ford
# Contoh data graf
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Memanggil fungsi dan menyimpan hasilnya
hasil_jarak = bellman_ford(graph, 'A')

# Menampilkan output
print("Jarak terpendek dari titik A:")
for node, jarak in hasil_jarak.items():
    print(f"Ke node {node}: {jarak}")