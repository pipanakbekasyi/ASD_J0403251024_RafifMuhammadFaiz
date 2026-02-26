#==============================================
# Rafif Muhammad Faiz
# J0403251024
# TPL B / P2
#================================================

#==============================================
# Kombinasi Biner dengan Batas '1' (Pruning)
#==============================================

def biner_batas(n, batas, hasil="", jumlah_1=0):

    # Pruning: kalau jumlah angka '1' sudah lebih dari batas,
    # rekursi dihentikan supaya tidak lanjut ke kombinasi lain
    if jumlah_1 > batas:
        return
    
    # Base case: jika panjang kombinasi sudah n,
    # maka hasil kombinasi ditampilkan
    if len(hasil) == n:
        print(hasil)
        return
    
    # Menambahkan '0' ke kombinasi
    # jumlah_1 tetap karena tidak menambah angka 1
    biner_batas(n, batas, hasil + "0", jumlah_1)
    
    # Menambahkan '1' ke kombinasi
    # jumlah_1 bertambah karena ada angka 1 baru
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)

biner_batas(4, 2)