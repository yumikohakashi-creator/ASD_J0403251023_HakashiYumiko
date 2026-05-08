#################################
# NAMA  : Hakashi Yumiko Masfat
# NIM   : J0403251023
# KELAS : TPL A2
#################################

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D',],
    'C': ['A', 'D'],
    'D': ['B', 'C'] 
}
print("Adjacency List:")
for node, neighbors in graph.items():
    print(f"{node}: {(neighbors)}")