def sequentialSearch (data, value):
    pos = 0
    found = False
    while pos <len (data) and not found:
        if data[pos] == value:
            found = True
        else:
            pos = pos + 1
    return found
data = [1, 2, 32, 8, 17, 19, 42, 13, 0, 2]
print (sequentialSearch (data, 3))
print (sequentialSearch (data, 13))

# 1. Mengembalikan posisi (indeks) pertama dari nilai yang dicari pada list.
#Apabila nilai tidak ditemukan, kembalikan -1.
def sequentialSearchFirst(data, value):
    pos = 0
    found = False
    
    while pos < len(data) and not found:
        if data[pos] == value:
            found = True
        else:
            pos = pos + 1
            
    if found:
        return pos
    else:
        return -1

data = [1, 2, 32, 8, 17, 19, 42, 13, 0, 2]
print(f"indeks pertama angka 13: {sequentialSearchFirst(data, 13)}") 
print(f"indeks pertama angka 3 : {sequentialSearchFirst(data, 3)}") 

# 2.  Mengembalikan seluruh posisi dari nilai yang dicari pada list 
# Contoh: pada saat mencari 2, nilai yang dikembalikan adalah[1,9]
def sequentialSearchAll(data, value):
    pos = 0
    list_indeks = [] 
    
    while pos < len(data):
        if data[pos] == value:
            list_indeks.append(pos)
        pos = pos + 1
            
    return list_indeks

data = [1, 2, 32, 8, 17, 19, 42, 13, 0, 2]
print(f"seluruh posisi angka 2: {sequentialSearchAll(data, 2)}")
print(f"seluruh posisi angka 3: {sequentialSearchAll(data, 3)}") 