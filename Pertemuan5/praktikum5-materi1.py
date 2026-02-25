#==============================================
#
#Rafif Muhammad Faiz
#J0403251024
#TPL B / P2
#================================================

#==============================================
#Materi Rekursif Faktorial
#rekursif case => 3! = 3 x 2 x 1
# base case => 0 berhenti
#==============================================

def faktorial(n):
    #base case
    if n == 0:
        return 1
    else:
        #rekursif case
        return n * faktorial(n-1) #n-1*n-2*1
print("==============Program Faktorial=============")
print ("Hasil Faktorial : ", faktorial(3))