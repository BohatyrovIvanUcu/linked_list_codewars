def loop_size(node):
    slow = node.next
    fast = node.next.next

    while slow != fast:
        slow = slow.next
        fast = fast.next.next

    size = 1
    fast = fast.next
    while slow != fast:
        fast = fast.next
        size += 1

    return size
