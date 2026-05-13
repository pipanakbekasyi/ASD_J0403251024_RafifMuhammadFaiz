# ==========================================================
# Latihan 1
# Rafif Muhammad Faiz
# J0403251024 - TPL B
# ==========================================================

# Daftar edge graph 
edges = [
 ('A', 'B'),
 ('A', 'C'),
 ('A', 'D'),
 ('C', 'D'),
 ('B', 'D')
]

# Daftar edge untuk Spanning Tree 
spanning_tree = [
 ('A', 'C'),
 ('C', 'D'),
 ('D', 'B')
]

# Menampilkan semua edge yang ada pada graf awal
print("Edge pada graph:")
for edge in edges:
    print(edge) # Mencetak setiap tuple edge satu per satu

# Menampilkan edge yang terpilih menjadi bagian dari Spanning Tree
print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge) # Mencetak setiap tuple edge pada spanning tree

# Menampilkan jumlah total edge pada graf asli
print("\nJumlah edge graph =", len(edges))

# Menampilkan jumlah edge yang membentuk spanning tree
print("Jumlah edge spanning tree =", len(spanning_tree))

# ==========================================================
# Jawaban Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
#    Graph awal adalah struktur data keseluruhan yang bisa memiliki banyak jalur 
#    antar node dan boleh memiliki cycle. Sedangkan Spanning Tree 
#    adalah subgraf (bagian) dari graph awal yang menghubungkan SEMUA node 
#    tetapi hanya menggunakan jumlah edge minimal.

# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    Karena secara definisi, graf terhubung yang tidak memiliki siklus. 
#    Jika terdapat cycle, maka ada setidaknya satu 
#    edge yang "mubazir" karena node tersebut sudah bisa dicapai melalui jalur lain.

# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    Karena tujuannya adalah efisiensi hubungan. Jika sebuah graf memiliki 'n' node, 
#    maka Spanning Tree selalu memiliki tepat 'n - 1' edge. Jumlah ini adalah 
#    jumlah minimum untuk memastikan semua node terhubung tanpa ada jalur ganda 
#    atau perulangan.
# ==========================================================