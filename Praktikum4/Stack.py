#==================================================
# Nama: Hakashi Yumiko Masfat
# NIM: J0403251023
# Kelas: TPL A2
#==================================================

#==================================================
# Implementasi Dasar: Stack
#==================================================

class Node: 
    #kostruktor yang diajalankan secara otomatis ketika class node dipanggil/ diinstantiasi
    def __init__(self,data):
        self.data = data #menyimpan nilai atau data pada list
        self.data = None #pointer ini menunjuk ke note berikutnya (awal=none)

#stack ada operasi push(memasukkan head baru) dan pop (menghapus head)
# A -> B -> C -> None

class stack:
    def __init__(self):
        self.top = None #top menunjuk ke noode paling atas (awalnya kosong)
    
    def is_empty(self):
        return self.top is None

    def push(self,data):
        #1 membuat node baru
        nodeBaru = Node(data) #instantiasi/ memanggil konstruktor pada class Node

        #2 node baru menunjuk ke top yang lama (head lama)
        nodeBaru.next = self.top

        #3 geser top pindah ke node baru
        self.top = nodeBaru

    def pop(self): #mengambil  / menghapus node paling atas (top/head)
        if self.is_empty:
            print("stack kosong, tidak bisa pop")
            return None
        data_terhapus = self.top.data #soroti bagian top dan simpan di variabel
        # B -> A -> None
        self.top = self.top.next #geser top ke node berikutnya
        return data_terhapus
    
    def peek(self):
        #melihat data yang paling atas tanpa menghapus
        if self.is_empty():
            return None
        return self.top.data

    def tampilkan(self):
        #Top -> A -> B
        current = self.top
        print ("Top ->" , end=" ")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")

#instantiasi class stack
s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print("peek (lihat top): ", s.peek())
s.pop()
s.tampilkan()
print("peek (lihat top): ", s.peek())
