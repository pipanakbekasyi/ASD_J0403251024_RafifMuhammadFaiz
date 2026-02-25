#==============================================
#
#Rafif Muhammad Faiz
#J0403251024
#TPL B / P2
#================================================

#==============================================
#Materi Menjumlah elemen list
#==============================================

def jumlah_list(data, index=0):
    #base case
    if index == len(data):
        return 0
    
    #rekursif case
    return data[index] + jumlah_list(data, index+1) 

print("==============Program Menjumlah List=============")
print(jumlah_list([2,4,5]))
