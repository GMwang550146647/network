# -*- coding:utf-8 -*-
class Heap():
    def __init__(self, arr):
        self.arr = [0]
        self.size = 0
        for numi in arr:
            self.push(numi)

    def up(self, i):
        while i // 2 > 0:
            if self.arr[i // 2] > self.arr[i]:
                self.arr[i // 2], self.arr[i] = self.arr[i], self.arr[i // 2]
                i = i // 2
            else:
                break

    def down(self, i):
        def get_min_child(i):
            left_child = i * 2
            right_child = i * 2 + 1
            if right_child >= len(self.arr):
                return left_child
            else:
                return right_child if self.arr[right_child] < self.arr[left_child] else left_child

        while i * 2 < len(self.arr):
            new_c = get_min_child(i)
            if self.arr[i]> self.arr[new_c]:
                self.arr[i], self.arr[new_c] = self.arr[new_c], self.arr[i]
                i = new_c
            else:
                break

    def push(self, num):
        self.arr.append(num)
        self.size += 1
        self.up(self.size)

    def pop(self, ):
        if self.size == 0:
            return None
        elif self.size == 1:
            return self.arr.pop()
        else:
            target = self.arr[1]
            self.arr[1] = self.arr.pop()
            self.size -= 1
            self.down(1)
            return target


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        heap = Heap(tinput)
        result = []
        print(heap.arr)
        for i in range(k):
            result.append(heap.pop())
        return result

if __name__ == '__main__':
    tinput,k=[4,5,1,6,2,7,3,8],4
    result=Solution().GetLeastNumbers_Solution(tinput,k)
    print(result)