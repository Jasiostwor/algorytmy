# Klasa reprezentujaca pojedynczy wezel drzewa
class Node:
    def __init__(self, value):
        # Wartosc przechowywana w wezle
        self.value = value
        # Lewy syn
        self.left = None
        # Prawy syn
        self.right = None


# Rekurencyjne przeszukiwanie drzewa
def search(node):
    if node.left is not None:
        search(node.left)
    print(node.value)
    if node.right is not None:
        search(node.right)

def search_preorder(node):
    print(node.value)
    if node.left is not None:
        search_preorder(node.left)
    if node.right is not None:
        search_preorder(node.right)

# # Korzen drzewa
# root = Node(7)
# # Dodajemy dzieci "recznie"
# root.left = Node(4)
# root.right = Node(9)
# root.left.right = Node(5)

# # Przeszukujemy drzewo w kolejnosci in-order
# search(root)