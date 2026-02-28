#==============================================
#Rafif Muhammad Faiz
#J0403251024
#TPL B / P2
#================================================


# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================

def cari_maks(data, index=0):          # Fungsi rekursif untuk mencari nilai terbesar

    if index == len(data) - 1:         # Base case = jika sudah di elemen terakhir
        return data[index]             # kembalikan nilai terakhir

    maks_sisa = cari_maks(data, index + 1)  # Recursive call = cari maksimum di sisa data

    if data[index] > maks_sisa:        # Bandingkan nilai sekarang
        return data[index]             # lebih besar, jadikan maksimum
    else:
        return maks_sisa               # pakai maksimum dari sisa data


angka = [3, 7, 2, 9, 5]                # Data angka
print("Nilai maksimum:", cari_maks(angka))  # Menampilkan nilai terbesar