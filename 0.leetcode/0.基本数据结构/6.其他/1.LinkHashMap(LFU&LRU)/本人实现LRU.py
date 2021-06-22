class Node():
    def __init__(self, x, y, next=None, pre=None):
        self.key = x
        self.val = y
        self.next = next
        self.pre = pre


class DoubleList():
    def __init__(self):
        self._head = Node('HEAD', 'HEAD')
        self._tail = Node('TAIL', 'TAIL')
        self._head.next = self._tail
        self._tail.pre = self._head
        self.size = 0

    def _add_first(self, x, y):
        new_node = Node(x, y)
        # 该节点的两边指向
        new_node.pre = self._head
        new_node.next = self._head.next
        # 该节点周围的连接
        self._head.next.pre = new_node
        self._head.next = new_node
        self.size += 1
        return new_node

    def _add_last(self, x, y):
        new_node = Node(x, y)
        # 该节点的两方指向
        new_node.next = self._tail
        new_node.pre = self._tail.pre
        # 该节点周围的连接
        self._tail.pre.next = new_node
        self._tail.pre = new_node
        self.size += 1
        return new_node

    def _remove_first(self):
        if self.size == 0:
            return None
        else:
            return self._remove_node(self._head.next)

    def _remove_last(self):
        if self.size == 0:
            return None
        else:
            return self._remove_node(self._tail.pre)

    def _remove_node(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        self.size -= 1
        return node

    def show(self):
        cur = self._head
        arr = []
        while cur:
            arr.append((cur.key, cur.val))
            cur = cur.next
        return arr


class LRU():
    def __init__(self, cap):
        self.cache = DoubleList()
        self.map = {}
        self.cap = cap


    def get(self, x):
        if x in self.map:
            # cache 和map中都要删除
            node = self.map[x]
            node = self.cache._remove_node(node)

            #map 和cache都要添加
            self.map[x]=self.cache._add_first(node.key, node.val)
            del node
            return self.map[x].val
        else:
            return -1

    def set(self, x, y):
        # 如果已经存在了，先删掉
        if x in self.map:
            self.cache._remove_node(self.map[x])
            del self.map[x]
        # 再添加到头
        new_node = self.cache._add_first(x, y)
        # 如果超过容量，删除最后一个
        while self.cache.size > self.cap:
            del_val = self.cache._remove_last()
            if del_val is not None:
                del self.map[del_val.key]
        self.map[x] = new_node


class Solution:
    def lru(self, operators, k):
        # write code here
        obj = LRU(k)
        result = []
        for opi in operators:
            if opi[0] == 1:
                obj.set(opi[1], opi[2])
            else:
                result.append(obj.get(opi[1]))
            print(opi,obj.cache.show())
        return result


if __name__ == '__main__':
    operators, n = [[1,1,1],[1,2,2],[1,3,2],[2,1],[1,4,4],[2,2]],3

    print(Solution().lru(operators, n))
