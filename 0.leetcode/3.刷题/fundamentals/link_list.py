class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def show(self, limit=1000000):
        while self and limit > 0:
            print(self.val,end=' ')
            self = self.next
            limit -= 1
        print()

class LinkList():
    def __init__(self):
        self.root = None

    def build_link_list(self, arr, recur_index=-1):
        if len(arr) == 0:
            self.root = None
        else:
            head = cur_node = ListNode(arr[0])
            recur_node = None
            for i in range(1, len(arr)):
                cur_node.next = ListNode(arr[i])
                cur_node = cur_node.next
                if recur_index == i:
                    recur_node = cur_node
            if recur_node:
                cur_node.next = recur_node

            self.root = head
        return self.root

    def show(self, head=None, limit=1000000):
        node = self.root if head is None else head
        while node and limit > 0:
            print(node.val,end=' ')
            node = node.next
            limit -= 1
        print()