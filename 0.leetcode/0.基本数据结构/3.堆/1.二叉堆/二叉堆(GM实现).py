from random import shuffle
class Heap(object):
    def __init__(self, arr=None):
        self.heap = [0]
        self.size = 0
        if arr:
            self.buildHeap(arr)

    def insert(self, num):
        self.heap.append(num)
        self.size += 1
        self.percUp(self.size)

    def del_min(self):
        if not self.heap:
            print("Error! heap is empty")
        else:
            result = self.heap[1]
            self.heap[1] = self.heap[-1]
            self.heap.pop()
            self.size-=1
            self.percDown()

            return result

    def percUp(self, i):
        while i // 2 > 0:
            if  self.heap[i // 2] > self.heap[i]:
                self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i // 2]
                i = i // 2
            else:
                break

    def percDown(self, i=1):
        def min_child(ith):
            if ith * 2 + 1 > self.size:
                return ith * 2

            else:
                return ith * 2 if self.heap[ith * 2] <= self.heap[ith * 2 + 1] else ith * 2 + 1

        while i*2 <= self.size:
            mc = min_child(i)

            if mc <= self.size:
                if self.heap[mc]<self.heap[i]:
                    self.heap[mc], self.heap[i] = self.heap[i], self.heap[mc]
                    i = mc
                else:
                    break

    def buildHeap(self, arr):
        for item in arr:
            self.insert(item)

    def __str__(self):
        return str(self.heap)


if __name__ == '__main__':
    lt=list(range(100))
    shuffle(lt)
    heap = Heap(lt)
    for i in range(10, 20):
        heap.insert(i)
    for i in range(heap.size):
        print(heap.del_min())
