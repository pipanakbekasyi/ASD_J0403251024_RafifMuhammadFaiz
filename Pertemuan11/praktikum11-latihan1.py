#=========================================
# Nama: Rafif Muhammad Faiz
# NIM: (isi sesuai kebutuhan)
# Kelas: TPL B2
# Implementasi BFS (Breadth-First Search)
# Studi kasus: Jalur lokasi dari Rumah
#=========================================

# import deque untuk membuat struktur data antrian (queue)
from collections import deque

# representasi graph menggunakan dictionary
graph = {
    'Rumah': ['Sekolah', 'Toko'],
    'Sekolah': ['Perpustakaan'],
    'Toko': ['Pasar'],
    'Perpustakaan': [],
    'Pasar': []
}

def bfs(graph, start):

   # Fungsi untuk melakukan traversal graph menggunakan BFS
   # graph : dictionary (representasi graph)
   # start : node awal
    
    
    # membuat antrian kosong
    queue = deque()
    
    # set untuk menyimpan node yang sudah dikunjungi
    visited = set()
    
    # memasukkan node awal ke antrian
    queue.append(start)
    
    # menandai node awal sudah dikunjungi
    visited.add(start)
    
    # perulangan selama antrian masih ada isi
    while queue:
        
        # mengambil node paling depan dari antrian
        node = queue.popleft()
        
        # menampilkan node
        print(node, end=' ')
        
        # mengecek semua tetangga dari node tersebut
        for neighbor in graph[node]:
            
            # jika tetangga belum pernah dikunjungi
            if neighbor not in visited:
                
                # masukkan ke antrian
                queue.append(neighbor)
                
                # tandai sebagai sudah dikunjungi
                visited.add(neighbor)

# menjalankan BFS dari node "Rumah"
print("BFS dari Rumah:")
bfs(graph, 'Rumah')

# 1. Node mana yang dikunjungi pertama?
# Node yang dikunjungi pertama adalah "Rumah", karena BFS selalu dimulai dari node awal (start node)
#yang dimasukkan pertama kali ke dalam queue.

# 2. Mengapa BFS cocok untuk mencari jalur terdekat?
# karena bekerja secara level (melebar).yaitu BFS akan mengunjungi semua node yang jaraknya 1 langkah dari node awal,
# Dengan cara ini, node tujuan pertama kali ditemukan melalui jalur terpendek
# (jumlah edge paling sedikit).BFS juga menjamin solusi optimal
# pada graph yang tidak memiliki bobot (unweighted graph).

# 3. Apa perbedaan urutan BFS jika struktur graph diubah?
# Urutan BFS akan berubah jika:
# - Urutan tetangga (adjacency list) di dalam graph diubah
# - Struktur hubungan antar node berubah
# Karena BFS mengikuti urutan tetangga saat dimasukkan ke queue,
# maka perubahan kecil pada graph dapat menghasilkan urutan traversal yang berbeda. Tetapi prinsip BFS tetap sama yaitu menjelajah per level dari node awal.