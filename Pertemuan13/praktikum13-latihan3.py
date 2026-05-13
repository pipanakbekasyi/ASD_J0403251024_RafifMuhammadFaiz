# ==========================================================
# Latihan 3
# Rafif Muhammad Faiz
# J0403251024 - TPL B
# Implementasi Algoritma Prim
#============================================================
import heapq

# Definisi graf (Dictionary dalam Dictionary)
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    visited = set([start])          # Menandai node awal sebagai node yang sudah dikunjungi
    edges = []                      # List untuk menampung edge yang tersedia (Priority Queue)
    
    # Memasukkan semua tetangga dari node awal ke dalam priority queue
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
    
    mst = []                        # List untuk menyimpan hasil akhir edge MST
    total_weight = 0                # Variabel untuk menghitung total bobot
    
   
    while edges:
        # Mengambil edge dengan bobot terkecil dari heap
        weight, u, v = heapq.heappop(edges)
        
        # Jika node tujuan (v) belum dikunjungi, maka tambahkan ke MST
        if v not in visited:
            visited.add(v)                  # Tandai node v sebagai dikunjungi
            mst.append((u, v, weight))      # Simpan jalur (u ke v) dan bobotnya
            total_weight += weight          # Tambahkan bobot ke total akumulasi
            
            # Cek semua tetangga dari node baru (v)
            for neighbor, w in graph[v].items():
                # Jika tetangga tersebut belum dikunjungi, masukkan ke priority queue
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
                    
    return mst, total_weight

# Menjalankan fungsi Prim dimulai dari node 'A'
mst, total = prim(graph, 'A')

# Menampilkan hasil eksekusi
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total bobot =", total)

# ==========================================================
# Jawaban Analisis:
# 1. Node awal apa yang digunakan?
#    Node awal yang digunakan adalah 'A' 

# 2. Edge mana yang dipilih pertama kali?
#    Edge (A, C) dengan bobot 2. Karena dari node 'A', tetangga dengan 
#    bobot terkecil adalah 'C' (bobot 2)

# 3. Bagaimana Prim menentukan edge berikutnya?
#    Prim selalu melihat semua edge yang terhubung dengan node-node yang sudah 
#    masuk dalam set 'visited', lalu memilih satu edge dengan bobot terkecil 
#    yang menghubungkan ke node yang BELUM dikunjungi.

# 4. Berapa total bobot MST yang dihasilkan?
#    Total bobotnya adalah 6.
#    Urutan pemilihannya: (A, C) bobot 2, lalu (C, D) bobot 1, lalu (D, B) bobot 3.

# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#    - Prim: Membangun MST dari satu titik awal (node-based). 
#    - Kruskal: Membangun MST dengan memilih edge terkecil dari seluruh graf 
#      (edge-based). Kruskal bisa membuat beberapa potongan kecil.
# ==========================================================