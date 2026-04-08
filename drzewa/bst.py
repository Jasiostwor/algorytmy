from node import Node

def insert(node, value):
    """Pomocnicza funkcja do wstawiania węzła do BST."""
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

def build_degenerate_bst(numbers):
    """
    To jest funkcja, której szuka Twój main.py.
    Tworzy drzewo BST z listy liczb.
    """
    if not numbers:
        return None
    
    root = Node(numbers[0])
    for number in numbers[1:]:
        insert(root, number)
    return root