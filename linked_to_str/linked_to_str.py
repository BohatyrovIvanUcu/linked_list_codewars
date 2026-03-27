def stringify(node):
    head = node

    if head is None:
        return "None"

    num_lst = []
    while head != None:
        num_lst.append(str(head.data))
        head = head.next

    res_str = " -> ".join(num_lst) + " -> None"

    return res_str
