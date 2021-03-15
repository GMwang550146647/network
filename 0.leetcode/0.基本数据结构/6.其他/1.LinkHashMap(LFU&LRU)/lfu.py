from base import Node, DoubleList
from lfu import LRUCache


class LFUCache():
    def __init__(self, cap):
        self.key2val={}
        self.key2freq={}
        self.freq2keys={}
        self.cap=cap
        self.min_freq=0

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
        if key not in self.key2freq:
            return default
        self.__increase_freq(key)
        return self.key2val[key].val

    def put(self, key, val):
        # 如存在，先删除
        if key in self.key2val:
            self.key2val[key]=val

        if len(self.key2val) >= self.cap:
            self.__remove_min_freq_key()

        self.key2val[key]=val
        self.key2freq[key]=1
        self.freq2keys.setdefault(1,LRUCache())
        self.freq2keys[1].add_last(Node(key,val))
        self.min_freq=1

    def show(self):
        return self.cache.show()


if __name__ == '__main__':
    lru = LRUCache(10)
    for i in range(150):
        lru.put(i, i)

        lru.show()
        print(lru.cache.size)
