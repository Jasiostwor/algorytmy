from node import Node

def insert(node, value, current_height, max_height):
    if max_height[0] < current_height:
        max_height[0] = current_height
    if value > node.value:
        if node.right is None:
            node.right = Node(value)
            if max_height[0] < current_height + 1:
                max_height[0] = current_height + 1
        else:
            insert(node.right, value, current_height + 1, max_height)
    elif value < node.value:
        if node.left is None:
            node.left = Node(value)
            if max_height[0] < current_height + 1:
                max_height[0] = current_height + 1
        else:
            insert(node.left, value, current_height + 1, max_height)

def build_degenerate_bst(numbers):
    if not numbers:
        return None, 0
    max_height = [0]
    root = Node(numbers[0])
    for number in numbers[1:]:
        insert(root, number, 0, max_height)
    return root, max_height[0]

def get_height_after(node):
    if node is None:
        return -1
    return 1 + max(get_height_after(node.left), get_height_after(node.right))

