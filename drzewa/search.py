def get_inorder(node, result):
    """
    Przechodzi drzewo w kolejności: Lewy, Korzeń, Prawy.
    Wynik w BST jest zawsze posortowany rosnąco.
    """
    if node is None:
        return
    
    get_inorder(node.left, result)
    result.append(str(node.value))
    get_inorder(node.right, result)

def get_preorder(node, result):
    """
    Przechodzi drzewo w kolejności: Korzeń, Lewy, Prawy.
    Używane często do kopiowania struktury drzewa.
    """
    if node is None:
        return
    
    result.append(str(node.value))
    get_preorder(node.left, result)
    get_preorder(node.right, result)