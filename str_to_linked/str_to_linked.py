from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr == 'None':
        return ''
    lst_nums = list_repr.split(" -> ")
    head = Node(int(lst_nums[0]))
    head_copy = head
    for num in lst_nums[1:-1]:
        head_copy.next = Node(int(num))
        head_copy = head_copy.next
    return head
