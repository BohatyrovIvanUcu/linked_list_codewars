""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    if head is None:
        return Node(data)

    if data <= head.data:
        new_node = Node(data)
        new_node.next = head
        return new_node

    head_orig = head
    while head.next is not None:
        if head.next.data >= data:
            tail = head.next
            head.next = Node(data)
            head.next.next = tail
            return head_orig
        head = head.next

    head.next = Node(data)
    return head_orig
