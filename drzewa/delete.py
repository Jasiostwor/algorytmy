from node import Node

def delete_node(root, key):
    if root is None:
        return root

    if key < root.value:
        root.left = delete_node(root.left, key)
    elif key > root.value:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = _get_min_value_node(root.right)
        root.value = temp.value
        root.right = delete_node(root.right, temp.value)

    return root

def _get_min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def delete_tree_postorder(node):
    if node:
        delete_tree_postorder(node.left)
        delete_tree_postorder(node.right)
        node.left = None
        node.right = None
        return None