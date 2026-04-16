def print_tree(node, prefix="", is_left=None, result_list=None):
    if result_list is None:
        result_list = []

    if node is not None:
        right_prefix = prefix + ("│   " if is_left is True else "    ")
        print_tree(node.right, right_prefix, False, result_list)
        if is_left is None:
            connector = "─── "  
        elif is_left is False:
            connector = "┌── "  
        else:
            connector = "└── "  
        result_list.append(prefix + connector + str(node.value))

        left_prefix = prefix + ("│   " if is_left is False else "    ")
        print_tree(node.left, left_prefix, True, result_list)

    return result_list