def print_tree(node, prefix="", is_left=None, result_list=None):
    if result_list is None:
        result_list = []

    if node is not None:
        # 1. Prawy syn (rysujemy "wyżej" w konsoli)
        right_prefix = prefix + ("│   " if is_left is True else "    ")
        print_tree(node.right, right_prefix, False, result_list)

        # 2. Rysujemy obecny węzeł
        if is_left is None:
            connector = "─── "  # Korzeń
        elif is_left is False:
            connector = "┌── "  # Prawy syn (gałąź w górę)
        else:
            connector = "└── "  # Lewy syn (gałąź w dół)
        
        result_list.append(prefix + connector + str(node.value))

        # 3. Lewy syn (rysujemy "niżej" w konsoli)
        left_prefix = prefix + ("│   " if is_left is False else "    ")
        print_tree(node.left, left_prefix, True, result_list)

    return result_list