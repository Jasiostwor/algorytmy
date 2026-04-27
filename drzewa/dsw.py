import math
from node import Node 

def rotate_right(parent, node):
    left_child = node.left
    node.left = left_child.right
    left_child.right = node
    parent.right = left_child
    return left_child

def rotate_left(parent, node):
    right_child = node.right
    node.right = right_child.left
    right_child.left = node
    parent.right = right_child
    return right_child

def compress(dummy_root, times):
    parent = dummy_root
    curr = dummy_root.right
    for _ in range(times):
        if not curr or not curr.right:
            break
        rotate_left(parent, curr)
        parent = parent.right
        curr = parent.right


def dsw_balance(root):
    if not root:
        return None

    dummy = Node(0)
    dummy.right = root

    count = 0
    parent = dummy
    curr = dummy.right

    while curr:
        if curr.left:
            curr = rotate_right(parent, curr)
        else:
            count += 1
            parent = curr
            curr = curr.right

    height = int(math.log2(count + 1))
    perfect_tree_size = (2 ** height) - 1 
    
    leaves_to_compress = count - perfect_tree_size

    compress(dummy, leaves_to_compress)

    while perfect_tree_size > 1:
        perfect_tree_size //= 2
        compress(dummy, perfect_tree_size)

    return dummy.right