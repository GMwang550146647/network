from base import Node,DoubleList

class LRUCache():
    def __init__(self, cap):
        self.map = {}
        self.cache = DoubleList()
        self.cap = cap

    def __make_recently(self, key):
        node = self.map[key]
        self.cache.remove(node)
        self.cache.add_last(node)

    def __add_recently(self, key, val):
        node = Node(key, val)
        self.cache.add_last(node)
        self.map[key] = node

    def __delete_key(self, key):
        node = self.map[key]
        self.cache.remove(node)
        del self.map[key]

    def __remove_least_recently(self):
        node = self.cache.remove_first()
        del self.map[node.key]

    def get(self, key, default=None):
        if key not in self.map:
            return default
        self.__make_recently(key)
        return self.map[key].val

    def put(self, key, val):
        # 如存在，先删除
        if key in self.map:
            self.__delete_key(key)

        if self.cache.size == self.cap:
            self.__remove_least_recently()

        self.__add_recently(key, val)

    def show(self):
        return self.cache.show()


if __name__ == '__main__':
    lru = LRUCache(10)
    for i in range(150):
        lru.put(i, i)

        lru.show()
        print(lru.cache.size)
