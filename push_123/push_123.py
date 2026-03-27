from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

def push(head, data):
    node = Node(data)
    node.next = head
    return node

def build_one_two_three():
    res_list = None
    for i in [3,2,1]:
        res_list = push(res_list,i)
    return res_list
