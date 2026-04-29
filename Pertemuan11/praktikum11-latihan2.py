#=========================================
# Rafif Muhammad Faiz
# J0403251024 TPL B2
# Implementasi DFS
# Studi kasus: Jalur eksplorasi
#=========================================

# representasi graph sesuai soal
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(graph, node, visited):
    # Fungsi untuk melakukan traversal graph dengan DFS
    # graph = dictionary (struktur graph)
    # node = node yang sedang dikunjungi
    # visited = set untuk menyimpan node yang sudah dikunjungi

    # menandai node saat ini sudah dikunjungi
    visited.add(node)

    # menampilkan node
    print(node, end=' ')

    # mengecek semua tetangga dari node saat ini
    for neighbor in graph[node]:
        
        # jika tetangga belum dikunjungi
        if neighbor not in visited:
            
            # lakukan DFS secara rekursif
            dfs(graph, neighbor, visited)

# membuat set kosong untuk visited
visited = set()

# menjalankan DFS dari node A
print("DFS dari A:")
dfs(graph, 'A', visited)

# 1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
# DFS menggunakan pendekatan stack last in first out,
# sehingga ketika menemukan satu tetangga, maka akan langsung masuk
# ke node tersebut dan terus menelusuri hingga mencapai node paling dalam
# Setelah itu baru kembali (backtracking) ke node sebelumnya untuk mengecek jalur lain.

# 2. Apa yang terjadi jika urutan neighbor diubah?
# Maka urutan traversal DFS juga akan berubah, karena DFS selalu mengikuti urutan tetangga
# yang ada di dalam list.

# 3. Bandingkan hasil DFS dengan BFS pada graph yang sama.
# DFS dan BFS memiliki cara traversal yang berbeda:
# - DFS: menelusuri sampai mencapai node terdalam
# - BFS: menelusuri urut secara level 
#
# Contoh:
# DFS  : A B D E C F
# BFS  : A B C D E F
#
# - DFS langsung masuk ke cabang B -> D -> E sebelum pindah ke C
# - BFS mengunjungi semua tetangga A (B dan C) terlebih dahulu,
#   baru lanjut ke level berikutnya (D, E, F)
#
# Jadi BFS lebih cocok untuk mencari jalur terpendek,
# sedangkan DFS lebih cocok untuk eksplorasi mendalam.