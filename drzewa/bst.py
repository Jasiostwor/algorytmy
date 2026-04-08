from node import Node

class Node:
    def __init__(self, value):
        # Wartosc przechowywana w wezle
        self.value = value
        # Lewy syn
        self.left = None
        # Prawy syn
        self.right = None


# Rekurencyjne przeszukiwanie drzewa inorderem lkp
def search(node):
    if node.left is not None:
        search(node.left)
    print(node.value, end=" ")
    if node.right is not None:
        search(node.right)
#klp
def preorder(node):
    print(node.value, end =" ")
    if node.left is not None:
        preorder(node.left)
    if node.right is not None:
        preorder(node.right)

def insert(node, value):
    if value > node.value:
        if node.right is None:
            node.right = Node(value)
        else:
            insert(node.right, value)
    elif value < node.value:
        if node.left is None:
            node.left = Node(value)
        else:
            insert(node.left, value)

numbers = [5,3,4,6,7,8,2,1]


# Korzen drzewa
root = Node(numbers[0])
# Dodajemy dzieci "recznie"
#root.left = Node(4)
#root.right = Node(9)
#root.left.right = Node(5)
for number in numbers[1:]:
    insert(root, number)

# Przeszukujemy drzewo w kolejnosci in-order
print("in-order")
(search(root))
print("\n")
print("preorder")
(preorder(root))