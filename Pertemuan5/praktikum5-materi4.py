#==============================================
#Rafif Muhammad Faiz
#J0403251024
#TPL B / P2
#================================================

#==============================================
#Materi Kombinasi Biner
#==============================================

def biner(n, hasil=""):
    # Base case: jika panjang string sudah n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return
    # Proses rekursif dengan menambahkan digit '0'
    biner(n, hasil + "0")
    # Proses rekursif dengan menambahkan digit '1'
    biner(n, hasil + "1")
biner(4)

