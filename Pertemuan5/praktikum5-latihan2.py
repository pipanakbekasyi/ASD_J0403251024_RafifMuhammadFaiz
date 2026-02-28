#==============================================
#Rafif Muhammad Faiz
#J0403251024
#TPL B / P2
#================================================

#==============================================
# Latihan Rekursif 2: Tracing Rekursi
#==============================================
def countdown(n):
    #Base Case
    # Jika n sudah 0, rekursi dihentikan
    if n == 0:
        print("Selesai")  # Ditampilkan ketika batas akhir tercapai
        return
    # Bagian sebelum rekursi dipanggil
    print("Masuk:", n)
    
    # Fungsi memanggil dirinya sendiri
    # nilai n dikurangi 1 setiap pemanggilan
    countdown(n - 1)
    
    # Bagian setelah rekursi selesai
    print("Keluar:", n) # "Keluar" muncul terbalik karena rekursi memakai sistem stack (LIFO),

# Pemanggilan fungsi
countdown(3)