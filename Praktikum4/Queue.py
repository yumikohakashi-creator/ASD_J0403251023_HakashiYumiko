#==================================================
# Nama: Hakashi Yumiko Masfat
# NIM: J0403251023
# Kelas: TPL A2
#==================================================

#==================================================
# Implementasi Dasar: Queue 
#==================================================

class Node:
    #kostruktor yang diajalankan secara otomatis ketika class node dipanggil/ diinstantiasi
    def __init__(self,data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)

class queue:
    #buat konstuktor untuk inisialisasi variabel front dan rear
    def __init__(self):
        self.front = None #node paling depan
        self.rear = None #node paling belakang

    def is_empty(self):
        return self.front is None

    #membuat fungsi untuk menambahkan data baru
    def enqueue(self,data):
        nodeBaru = Node(data)

        #jika node kosong, front dan rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        #jika queue tidak kosong, maka letakkan data baru setelah rear, dan jadikan data baru sebagai rear
        self.rear.next = nodeBaru #letakkan data baru pada setelah rear
        self.rear = nodeBaru #jadikan data baru sebagai rear

    def dequeue(self):
        #menghapus data dari depan/ front
        data_terhapus = self.front.data #lihat data paling depan

        #geser front ke node berikutnya
        self.front = self.front.next

        #jika setelah geser front menjadi none, maka queue menjadi kosong
        #rear juga harus none
        if self.front is None:
            self.rear = None

        return data_terhapus

    def tampilkan(self):
        current = self.front
        print("front ->", end=" ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print ("Rear")

#instalasi class queue
q = queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()

