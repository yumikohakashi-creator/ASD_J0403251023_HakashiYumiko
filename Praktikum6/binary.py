#1. Mengembalikan posisi (indeks) pertama dari nilai yang dicari pada list.
# apabila nilai tidak ditemukan, kembalikan-1.

def binarySearchIndex(data, item):
    data.sort() 
    first = 0
    last = len(data) - 1
    found = False
    index = -1
    
    while first <= last and not found:
        midpoint = (first + last) // 2
        if data[midpoint] == item:
            found = True
            index = midpoint 
        else:
            if item < data[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return index

data = [1, 2, 32, 8, 17, 19, 42, 13, 0, 2]
print(f"indeks angka 13 (setelah diurutkan): {binarySearchIndex(data, 13)}") 
print(f"indeks angka 3  (tidak ada): {binarySearchIndex(data, 3)}")

#2. Mengembalikan seluruh posisi dari nilai yang dicari pada list (Contoh: pada
#saat mencari 2, nilai yang dikembalikan adalah [1, 9].

def binarySearchAll(data, item):
    data.sort() 
    first = 0
    last = len(data) - 1
    indices = []
    
    while first <= last:
        mid = (first + last) // 2
        if data[mid] == item:
            indices.append(mid)
            temp = mid - 1
            while temp >= 0 and data[temp] == item:
                indices.append(temp)
                temp -= 1
            temp = mid + 1
            while temp < len(data) and data[temp] == item:
                indices.append(temp)
                temp += 1
            return sorted(indices)
        elif item < data[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return indices

data = [1, 2, 32, 8, 17, 19, 42, 13, 0, 2]
print(f"seluruh posisi angka 2 (setelah diurutkan): {binarySearchAll(data, 2)}")