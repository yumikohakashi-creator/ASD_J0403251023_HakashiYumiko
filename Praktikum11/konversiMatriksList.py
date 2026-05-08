#################################
# NAMA  : Hakashi Yumiko Masfat
# NIM   : J0403251023
# KELAS : TPL A2
#################################

matrix = [
    [0,1,1,0],
    [1,0,1,0],
    [1,1,0,1],
    [0,0,1,0]
]
adj_list = {}
for i in range(len(matrix)):
    neighbors = []
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            neighbors.append(j)
    adj_list[i] = neighbors

print("Hasil Adjacency List:")
for node, neighbors in adj_list.items():
    print(f"{node}: {neighbors}")