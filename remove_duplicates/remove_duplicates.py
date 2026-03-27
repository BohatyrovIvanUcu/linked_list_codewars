class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None :
        return None
    head_orig = head


    while head.next is not None:
        if head.next.data == head.data :
            head.next = head.next.next
        else :
            head = head.next
    return head_orig
