#================================================
#Rafif Muhammad Faiz
#J0403251024
#TPL B / P2
#================================================

#==============================================
#Materi Rekursif Call Stack
# Tracing bilangan (masuk-keluar)
# input 3
# 3-2-1 | 1-2-3
#==============================================

def hitung(n):
    #base case
    if n == 0:
        print("Selesai")
        return
    
    print("Masuk: ", n)
    hitung(n-1)
    print("Keluar: ", n)
    
print("==============Program Hitung=============")
hitung(3)