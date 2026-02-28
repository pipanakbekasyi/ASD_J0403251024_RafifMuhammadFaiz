#==============================================
#Rafif Muhammad Faiz
#J0403251024
#TPL B / P2
#================================================


# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================

def kombinasi(n, hasil=""):        # Fungsi rekursif untuk membuat kombinasi huruf

    if len(hasil) == n:            # Base case (jika panjang hasil sudah = n)
        print(hasil)               # menampilkan kombinasi
        return                     # menghentikan rekursi pada cabang ini

    kombinasi(n, hasil + "A")      # Recursive call = tambah huruf A
    kombinasi(n, hasil + "B")      # Recursive call = tambah huruf B


kombinasi(2)                       # Membuat kombinasi sepanjang 2 huruf


#  jumlah kombinasi = 2(jumla huruf)^n(jumlah kombinasi).
# yaitu: AA, AB, BA, BB