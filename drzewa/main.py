from node import Node, search, search_preorder

tab = [1,2,3,4,5,6,7,8,9,10]

def create_tree(tab):
    if len(tab) > 2:
        mid = (len(tab)-1) // 2
        node = Node(tab[mid])
        node.left = create_tree(tab[:mid])
        node.right = create_tree(tab[mid+1:])
        return node
    elif len(tab) == 2:
        if tab[0] < tab[1]:
            node = Node(tab[1])
            node.left = Node(tab[0])
        else:
            node = Node(tab[0])
            node.right = Node(tab[1])
        return node
    elif len(tab) == 1:
        return Node(tab[0])
    else:
        return None
    
tree = create_tree(tab)

# print(tree.value)
# print(tree.left.value)
# print(tree.right.value)
# print(tree.left.left.value)
# print(tree.left.right.value)
# print(tree.left.right.left.value)
search_preorder(tree)
