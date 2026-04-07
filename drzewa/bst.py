from node import Node

# Do zmiany, kAmien zrob jak na zajeciach bo to gemini generated
def insert_bst(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert_bst(root.left, value)
    elif value > root.value:
        root.right = insert_bst(root.right, value)
    return root

def build_degenerate_bst(tab):
    root = None
    for val in tab:
        root = insert_bst(root, val)
    return root