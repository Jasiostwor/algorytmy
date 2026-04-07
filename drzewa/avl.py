from node import Node

def create_avl(tab):
    max_height = [0]
    root = create_avl_recursive(tab, 0, max_height)
    return root,max_height[0]

def create_avl_recursive(tab, current_height, max_height):
    if len(tab) > 0:
        if max_height[0] < current_height:
            max_height[0] = current_height

    if len(tab) > 2:
        mid = (len(tab)-1) // 2
        node = Node(tab[mid])
        node.left = create_avl_recursive(tab[:mid], current_height + 1, max_height)
        node.right = create_avl_recursive(tab[mid+1:], current_height + 1, max_height)
        return node
    elif len(tab) == 2:
        if tab[0] < tab[1]:
            node = Node(tab[0])
            node.right = Node(tab[1])
        else:
            node = Node(tab[0])
            node.left = Node(tab[1])
        return node
    elif len(tab) == 1:
        return Node(tab[0])
    else:
        return None