#==============================================
#Rafif Muhammad Faiz
#J0403251024
#TPL B / P2
#================================================

#==============================================
# Latihan Rekursif 1: Rekursi Pangkat
# 2^4 = 2 x 2 x 2 x 2
# bisa ditulis menjadi:
# 2^4 = 2 x (2^3)
#==============================================
def pangkat(a, n):
    
    # Base case
    # Jika pangkat = 0, hasilnya selalu 1
    # karena a^0 = 1
    if n == 0:
        return 1
    # Recursive case
    # Fungsi memanggil dirinya sendiri
    # a^n = a * a^(n-1)
    return a * pangkat(a, n - 1)

# Memanggil fungsi
print(pangkat(2, 4)) # Output: 16