class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise Exception("error")

    first = head
    second = head.next
    first_head = first
    second_head = second

    while first.next is not None and second.next is not None:
        first.next = first.next.next
        second.next = second.next.next
        first = first.next
        second = second.next

    if first is not None:
        first.next = None
    if second is not None:
        second.next = None

    return Context(first_head, second_head)
