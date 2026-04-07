def get_inorder(node, result):
    if node.left is not None:
        get_inorder(node.left, result)
    result.append(str(node.value))
    if node.right is not None:
        get_inorder(node.right, result)
    

def get_preorder(node, result):
    result.append(str(node.value))
    if node.left is not None:
        get_preorder(node.left, result)
    if node.right is not None:
        get_preorder(node.right, result)