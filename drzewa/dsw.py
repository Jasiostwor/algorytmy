import math
from node import Node

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
            left_child = curr.left
            curr.left = left_child.right
            left_child.right = curr
            parent.right = left_child
            curr = left_child
        else:
            count += 1
            parent = curr
            curr = curr.right

    h = int(math.log2(count + 1))
    m = 2**h - 1

    _compress(dummy, count - m)

    while m > 1:
        m //= 2
        _compress(dummy, m)

    return dummy.right

def _compress(parent, n):
    curr = parent.right
    for _ in range(n):
        if not curr or not curr.right:
            break
        child = curr.right
        curr.right = child.left
        child.left = curr
        parent.right = child
        
        parent = child
        curr = parent.right