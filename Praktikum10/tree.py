# identitas
print("Nama : Hakashi Yumiko Masfat")
print("NIM  : J0403251023") 

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# fungsi traversal
def inorder(root, result):
    if root:
        inorder(root.left, result)
        result.append(root.data)
        inorder(root.right, result)

def preorder(root, result):
    if root:
        result.append(root.data)
        preorder(root.left, result)
        preorder(root.right, result)

def postorder(root, result):
    if root:
        postorder(root.left, result)
        postorder(root.right, result)
        result.append(root.data)

# mempersiapkan data
nim_last_two = 23
root_val = nim_last_two
data_list = [root_val, root_val + 20, root_val + 30, root_val + 10, root_val + 30, root_val + 15] 

# membangun tree
root = Node(root_val)
for val in data_list:
    root.insert(val)

# menampilkan hasil
in_res, pre_res, post_res = [], [], []
inorder(root, in_res)
preorder(root, pre_res)
postorder(root, post_res)

print("In-order Traversal  :", in_res)
print("Pre-order Traversal :", pre_res)
print("Post-order Traversal:", post_res)
