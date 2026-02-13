###Latihan	1:	Implementasikan	fungsi untuk menghapus node	dengan	nilai tertentu.

class Node:
    def __init__(self, data):
        self.data = data #buat nyimoen nilai
        self.next = None #buat ke yang selanjutnya

class linkedlist:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(f"{temp.data}->", end="")
            temp = temp.next
        print("None")

    def delete_node(self, key): 
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next #buat ngegeser head ke nodenya
            temp = None #ngehapus node lama dari memori
            print (f"Node{key} berhasil dihapus (Head)")
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            print(f"Node{key} tidak ditemukan")
            return
        prev.next = temp.next
        temp = None
        print(f"Node{key} berhasil dihapus")

if __name__ == "__main__":
    llist = linkedlist()
    llist.append(10)
    llist.append(20)
    llist.append(30)
    llist.append(40)

    print("isi linked list awal: ")
    llist.print_list()

    llist.delete_node(20)
    llist.delete_node(10)

    print("\nisi linked list setelah penghapusan: ")
    llist.print_list()