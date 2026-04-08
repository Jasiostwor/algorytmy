import math
from node import Node

def dsw_balance(root):
    """
    Główna funkcja algorytmu DSW.
    Równoważy drzewo BST w czasie O(n).
    """
    if not root:
        return None

    # Tworzymy tymczasowy węzeł pomocniczy (dummy), aby ułatwić rotacje na korzeniu
    dummy = Node(0)
    dummy.right = root

    # Faza 1: Tworzenie "kręgosłupa" (Vine/Spine)
    # Zamieniamy drzewo w posortowaną listę (tylko prawe dzieci) za pomocą rotacji w prawo.
    count = 0
    parent = dummy
    curr = dummy.right

    while curr:
        if curr.left:
            # Jeśli istnieje lewe dziecko, wykonujemy rotację w prawo
            left_child = curr.left
            curr.left = left_child.right
            left_child.right = curr
            parent.right = left_child
            curr = left_child  # Nowy wierzchołek do sprawdzenia
        else:
            # Jeśli nie ma lewego dziecka, idziemy w prawo
            count += 1
            parent = curr
            curr = curr.right

    # Faza 2: Kompresja (Vine -> Balanced Tree)
    # Wykonujemy serie rotacji w lewo, aby "zwinąć" listę z powrotem w drzewo.
    
    # Obliczamy m = 2^(floor(log2(count+1))) - 1
    # m to liczba węzłów w najbliższym pełnym drzewie binarnym
    h = int(math.log2(count + 1))
    m = 2**h - 1

    # Pierwsza seria rotacji dla nadmiarowych węzłów
    _compress(dummy, count - m)

    # Kolejne serie rotacji, aż m osiągnie 0
    while m > 1:
        m //= 2
        _compress(dummy, m)

    return dummy.right

def _compress(parent, n):
    """
    Funkcja pomocnicza wykonująca n rotacji w lewo wzdłuż prawego kręgosłupa.
    """
    curr = parent.right
    for _ in range(n):
        if not curr or not curr.right:
            break
        child = curr.right
        # Rotacja w lewo
        curr.right = child.left
        child.left = curr
        parent.right = child
        
        # Przesuwamy wskaźniki, aby kontynuować wzdłuż kręgosłupa
        parent = child
        curr = parent.right