#==================================================
# Nama: Hakashi Yumiko Masfat
# NIM: J0403251023
# Kelas: TPL A2
#==================================================

#==================================================
# Implementasi Dasar: Node pada Linked List
#==================================================

class Node:
    #kostruktor yang diajalankan secara otomatis ketika class node dipanggil/ diinstantiasi
    def __init__(self,data):
        self.data = data #menyimpan nilai atau data pada list
        self.data = None #pointer ini menunjuk ke note berikutnya (awal=none)

#1) membuat node dengan intantiasi class node 
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2) menghubungkan node: A -> B -> C -> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#4) Traversal: menelurusi node dari head sampai ke None
current = head
while current is not None:
    print (current.data) #menampilkan data pada node saat ini
    current = current.next #pindah ke node berikutnya

