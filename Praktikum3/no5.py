###Latihan	5:	Tambahkan	metode	untuk	membalik (reverse) sebuahsin gle linked	list tanpa	membuat	linked list baru.	

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def print_list(self):
        temp = self.head
        while temp:
            print(f"{temp.data} -> ", end="")
            temp = temp.next
        print("null")
    
    def reverse(self):
        prev = None #biar ke node sebelumnya
        current = self.head #ke node sekarang
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current =  next_node
        self.head = prev

if __name__ == "__main__":
    llist = linkedlist()
    elemen_input = input("masukkan elemen untukk linked list (pisahkan dengan koma)")
    data_list = [e.strip()for e in elemen_input.split(",")]
    for d in data_list:
        llist.append(d)
    print("linked list sebelum dibalik: ", end="")
    llist.print_list()
    llist.reverse()
    print("linked list setelah dibalik: ", end="")
    llist.print_list()

    ##yeyyyy
=======
###Latihan	5:	Tambahkan	metode	untuk	membalik (reverse) sebuahsin gle linked	list tanpa	membuat	linked list baru.	

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def print_list(self):
        temp = self.head
        while temp:
            print(f"{temp.data} -> ", end="")
            temp = temp.next
        print("null")
    
    def reverse(self):
        prev = None #biar ke node sebelumnya
        current = self.head #ke node sekarang
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current =  next_node
        self.head = prev

if __name__ == "__main__":
    llist = linkedlist()
    elemen_input = input("masukkan elemen untukk linked list (pisahkan dengan koma)")
    data_list = [e.strip()for e in elemen_input.split(",")]
    for d in data_list:
        llist.append(d)
    print("linked list sebelum dibalik: ", end="")
    llist.print_list()
    llist.reverse()
    print("linked list setelah dibalik: ", end="")
    llist.print_list()
