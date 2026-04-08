from node import Node

def delete_node(root, key):
    """
    Usuwa węzeł o podanym kluczu z drzewa BST/AVL.
    Zwraca nowy korzeń poddrzewa.
    """
    if root is None:
        return root

    # 1. Szukamy węzła do usunięcia
    if key < root.value:
        root.left = delete_node(root.left, key)
    elif key > root.value:
        root.right = delete_node(root.right, key)
    else:
        # Znaleźliśmy węzeł! 
        
        # PRZYPADEK 1 & 2: Brak dzieci lub tylko jedno dziecko
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # PRZYPADEK 3: Węzeł ma dwoje dzieci
        # Szukamy następcy (najmniejsza wartość w prawym poddrzewie)
        temp = _get_min_value_node(root.right)
        
        # Kopiujemy wartość następcy do tego węzła
        root.value = temp.value
        
        # Usuwamy następcę z prawego poddrzewa
        root.right = delete_node(root.right, temp.value)

    return root

def _get_min_value_node(node):
    """Pomocnicza funkcja do znalezienia najmniejszego węzła w drzewie."""
    current = node
    while current.left is not None:
        current = current.left
    return current


def delete_tree_postorder(node):
    """
    Usuwa całe drzewo przechodząc je metodą post-order (lewy, prawy, korzeń).
    W Pythonie polega to na rekurencyjnym czyszczeniu referencji.
    """
    if node:
        # Najpierw idziemy w głąb do dzieci
        delete_tree_postorder(node.left)
        delete_tree_postorder(node.right)
        
        # "Usuwamy" połączenia (pomaga GC i czyści strukturę)
        node.left = None
        node.right = None
        
        # Logika Twojego maina oczekuje, że funkcja zwróci None na końcu
        return None