###Latihan	3:	Implementasikan	Pencarian pada	node tertentu Double Linked	List.	

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doublelinkedlist:
    def __init__(self,):
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
        new_node.prev = last
    def search_element(self, key):
        temp = self.head
        posisi = 0
        while temp:
            if temp.data == key:
                print(f"elemen {key} ditemykan dalam doubly linked list pada posisi {posisi}")
                return True
            temp = temp.next
            posisi +=1
        print(f"elemen {key} tidak ditemukan dalam doubly linked list")
        return False

if __name__ == "__main__":
    dll = doublelinkedlist()
    data_input = [2,6,9,14,20]
    for d in data_input:
        dll.append(d)
    print(f"masukkan elemen ke dalam doubly linked list: {','.join(map(str, data_input))}")
    cari = int(input("masukkan elemen yang ingin dicari: "))
    dll.search_element(cari)

    