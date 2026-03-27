from preloaded import Node

def swap_pairs(head):
    if head is None or head.next is None:
        return head

    new_head = head.next

    prev = None
    curr = head

    while curr is not None and curr.next is not None:
        a = curr
        b = curr.next
        rest = b.next

        b.next = a
        a.next = rest

        if prev is not None:
            prev.next = b

        prev = a
        curr = rest

    return new_head
