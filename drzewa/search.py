def get_min_path(node):
    path = []
    curr = node
    while curr:
        path.append(str(curr.value))
        curr = curr.left
    return path

def get_max_path(node):
    path = []
    curr = node
    while curr:
        path.append(str(curr.value))
        curr = curr.right
    return path