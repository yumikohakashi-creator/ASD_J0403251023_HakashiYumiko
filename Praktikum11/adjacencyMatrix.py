#################################
# NAMA : Hakashi Yumiko Masfat
# NIM   : J0403251023
# KELAS : TPL A2
#################################

V = 4
matrix = [
    [0,1,1,0],
    [1,0,1,0],
    [1,1,0,1],
    [0,0,1,0]
]
print("Adjacency Matrix:")
for row in matrix:
    print(row)

#baris 0 menunjukkan node 0 terhubung dengan node 1 dan node 2
#baris 1 menunjukkan node 1 terhubung dengan node 0, node 1, dan node 2
#baris 2 menunjukkan node 2 terhubung dengan node 0, node 1, dan node 3
#baris 3 menunjukkan node 3 terhubung dengan node 2