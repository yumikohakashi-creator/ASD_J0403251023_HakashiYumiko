#################################
# NAMA : Hakashi Yumiko Masfat
# NIM   : J0403251023
# KELAS : TPL A2
#################################

#Studi Kasus: Jaringan Komputer.  
#Topologi: Star-Mesh Hybrid
# 1. Representasi Adjacency List
graph = {
    "Router Utama": ["Server", "Switch", "PC-Admin"],
    "Server": ["Router Utama", "Switch", "PC-Admin"],
    "Switch": ["Router Utama", "Server", "PC-Admin", "Access Point"],
    "PC-Admin": ["Router Utama", "Server", "Switch"],
    "Access Point": ["Switch"]
}

# 2. Representasi Adjacency Matrix
nodes = ["Router Utama", "Server", "Switch", "PC-Admin", "Access Point"]
matrix = [
    [0, 1, 1, 1, 0], # Router Utama
    [1, 0, 1, 1, 0], # Server
    [1, 1, 0, 1, 1], # Switch
    [1, 1, 1, 0, 0], # PC-Admin
    [0, 0, 1, 0, 0]  # Access Point
]
print("=== REPRESENTASI GRAPH JARINGAN KOMPUTER ===")

print("\n1. Adjacency List:")
for node, neighbors in graph.items():
    print(f"{node}: {neighbors}")

print("\n2. Adjacency Matrix:")
print("             ", end="")
for n in range(len(nodes)):
    print(f"[{n}] ", end="")
print()
for i in range(len(matrix)):
    print(f"Node [{i}] {nodes[i]:<12}: {matrix[i]}")

print("\n3. Daftar Nama Node (Vertex):")
for i, node in enumerate(nodes):
    print(f"Indeks {i}: {node}")

print("\n4. Hubungan Antar Node (Edges):")
for node, neighbors in graph.items():
    for neighbor in neighbors:
        if node < neighbor: 
            print(f"- {node} terhubung dengan {neighbor}")