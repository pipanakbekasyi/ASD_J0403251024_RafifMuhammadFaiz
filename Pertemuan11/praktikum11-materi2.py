#=========================================
# Rafif Muhammad Faiz
# J0403251024 TPL B2
# Implementasi BFS
#=========================================

#struktur data untuk membuat antrian dan menggunakan library collections
from collections import deque

#representasi graph
graph = {
    'A':['B', 'C'],
    'B':['A', 'D'],
    'C':['A', 'D'],
    'D':['B', 'C'],
}

def bfs(graph, start):
    #Fungsi untuk melakukan graph dengan BFS
    #graph = dictionary yang menyimpan struktur dari graph
    #start = node awal
    #queue = antrian untuk menyimpan node yang akan dikunjungi
    queue = deque()
    
    #visited = variabel untuk menyimpan node yang sudah dikunjungi
    visited = set()
    
    #menambahkan node awal ke antrian
    queue.append(start)
    
    #menandai node awal yang sudah dikunjungi
    visited.add(start)
    
    while queue:
        #mengambil node dari antrian
        node = queue.popleft()
        
        #menampilkan node yang diambil
        print(node, end=' ')
        
        #periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]:
            #jika tetangga belum dikunjungi
            if neighbor not in visited:
                
                #menambahkan tetangga ke antrian
                queue.append(neighbor)
                
                #menandai tetangga yang sudah dikunjungi    
                visited.add(neighbor)

#Menambahkan bfs dari A
bfs(graph, 'A')
        