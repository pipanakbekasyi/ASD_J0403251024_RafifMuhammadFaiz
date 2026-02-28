#==============================================
#Rafif Muhammad Faiz
#J0403251024
#TPL B / P2
#================================================


# ==========================================================
# Studi Kasus: Generator PIN
# ==========================================================

def buat_pin(panjang, hasil=""):          # Fungsi rekursif untuk membuat kombinasi PIN

    if len(hasil) == panjang:             # Base case = panjang PIN sudah sesuai
        print("PIN:", hasil)              # menampilkan PIN
        return                            # menghentikan rekursi

    for angka in ["0", "1", "2"]:         # Pilihan angka yang bisa digunakan
        if angka not in hasil:            # Mencegah angka yang sama muncul berulang
            buat_pin(panjang, hasil + angka)  # Tambahkan angka lalu lanjut rekursi


buat_pin(3)                               # Membuat PIN sepanjang 3 digit

# Angka dicek terlebih dahulu, sehingga angka yang sudah dipakai
