class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    start = source.data
    source = source.next

    desteny = Node(start)
    desteny.next = dest
    dest = desteny
    return Context(source, dest)
