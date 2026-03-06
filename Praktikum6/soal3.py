###################################
# Nama: Hakashi Yumiko Masfat
# NIM : J0403251023
# Kelas : TPL A2
###################################

def sequential_filter(data, X):
    sama_dengan_X = []
    lebih_besar_X = []
    
    for i in range(len(data)):
        if data[i] == X:
            sama_dengan_X.append(data[i])
        elif data[i] > X:
            lebih_besar_X.append(data[i])
            
    return sama_dengan_X, lebih_besar_X

data_nilai = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
X = 50 

sama, besar = sequential_filter(data_nilai, X)
print(f"hasil sequential search (X={X}):")
print(f"- nilai sama dengan {X}: {sama}")
print(f"- nilai lebih besar dari {X}: {besar}")