def mergesort(data):
    if len(data) <= 1:
        return data
    
    #Divide
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]
    
    #rekursif
    left_sort = mergesort(left)
    right_sort = mergesort(right)
    
    return merge(left_sort, right_sort)

def merge(left, right):
    result = []
    i = 0
    j = 0
    
    
    #pembandingan kiri dan kanan
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

angka = [10, 8, 9, 5, 11, 12, 15]
print("Hasil sorting", mergesort(angka))
    
            