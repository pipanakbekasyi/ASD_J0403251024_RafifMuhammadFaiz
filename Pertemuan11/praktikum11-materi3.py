#=========================================
# Rafif Muhammad Faiz
# J0403251024 TPL B2
# Implementasi DFS
#=========================================


#representasi graph
graph = {
    'A':['B', 'C'],
    'B':['D', 'E'],
    'C':['F', 'G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[]
}

def dfs(graph, node, visited):
    #Fungsi untuk melakukan graph dengan DFS
    #graph = dictionary yang menyimpan struktur dari graph
    #node = menyimpan node yang sedang dikunjungi
    #visited = menyimpan node yang sudah dikunjungi
  
    #menandai node saat ini yang sudah dikunjungi 
    visited.add(node)

    #menampilkan node saat ini
    print(node, end=' ')

   #periksa semua tetangga dari node saat ini 
    for neighbor in graph[node]:
            #jika tetangga belum dikunjungi
        if neighbor not in visited:
            #lakukan rekursif ke tetangga
            dfs(graph, neighbor, visited) 

#set visited
visited = set()
#Menambahkan dfs dari A
dfs(graph, 'A', visited)