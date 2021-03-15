class Node():
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None


class DoubleList():
    def __init__(self):
        self.head = Node('HEAD', 'HEAD')
        self.tail = Node('TAIL', 'TAIL')
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0

    def add_last(self, node):
        node.next = self.tail
        node.pre = self.tail.pre
        self.tail.pre.next = node
        self.tail.pre = node
        self.size += 1

    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        self.size -= 1

    def remove_first(self):
        if self.head.next == self.tail:
            return None
        else:
            tempt = self.head.next
            self.remove(tempt)
            return tempt

    def show(self, reverse=True):
        tempt = []
        if reverse:
            pt = self.tail
            while (pt):
                tempt.append(pt.val)
                pt = pt.pre
        else:
            pt = self.head
            while (pt):
                tempt.append(pt.val)
                pt = pt.next
        print(tempt)
        return tempt[1:-1]
