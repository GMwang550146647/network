class Node(object):
    def __init__(self, value=None, prev=None, next=None):
        self.value, self.prev, self.next = value, prev, next


class CirculaDoubleLinkedList(object):
    def __init__(self, msxsize=None):
        # msxsize=None代表无限大
        self.maxsize = msxsize
        node = Node()
        node.next, node.prev = node, node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        # 根节点的prev指向尾节点
        return self.root.prev

    def append(self, value):
        # 判断当前最大值是否超过了允许的最大值
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception("Full")
        node = Node(value=value)
        tailnode = self.tailnode()
        # 最后一个节点指向新的最后节点
        tailnode.next = node
        # 新的最后节点指向前节点
        node.prev = tailnode
        # node的下一个节点指向root
        node.next = self.root
        # 根节点的上一个节点指向新的最后节点，形成闭环
        self.root.prev = node
        self.length += 1

    def appendleft(self, value):
        # 判断当前最大值是否超过了允许的最大值
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception("Full")
        node = Node(value=value)
        # 如果根节点的下一个节点是自己，则证明是空的
        if self.root.next is self.root:
            # 新节点的下一个指向根节点
            node.next = self.root
            # 新节点的上一个指向根节点
            node.prev = self.root
            # 根节点的下一个指向新节点
            self.root.next = node
            # 根节点的上一个指向新节点
            self.root.prev = node
        else:
            # 新节点的上一个节点指向根节点
            node.prev = self.root
            # 获取头节点
            headnode = self.headnode()
            # 新节点的下一个指向头节点
            node.next = headnode
            # 头节点的上一个指向新节点
            headnode.prev = node
            # 根节点的下一个指向新节点
            self.root.next = node
            self.length+=1

    def remove(self, node):
        # O(1)  node is not value
        if node is self.root:
            return
        else:
            # 被删除节点的上一个节点的next指向被删除节点的下一个节点
            node.prev.next = node.next
            # 被删除节点的下一个节点的prev指向被删除节点的上一个节点
            node.next.prev = node.prev
        self.length -= 1
        return node

    def iter_node(self):
        if self.root.next is self.root:
            return
        curnode = self.root.next
        while curnode is not self.root:
            yield curnode
            curnode = curnode.next
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node_reverse(self):
        if self.root.next is self.root:
            return
        curnode = self.root.prev
        while curnode is not self.root:
            yield curnode
            curnode = curnode.prev
        yield curnode