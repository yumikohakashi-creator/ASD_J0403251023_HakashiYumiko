def bubbleSort(data):
    n = len(data) #total elemen yang ada di list
    for i in range(n):
        terjadi_tuker =False
        for j in range (0,n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                terjadi_tuker = True
        if not terjadi_tuker:
            break
        
    return data

nilai = [76, 58, 12, 43, 29, 61]
hasil= bubbleSort(nilai)
print(nilai)
        
