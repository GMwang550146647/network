from collections import defaultdict


class Node():
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None

    def __gt__(self, other):
        if self.val > other.val:
            return True
        elif self.val == other.val:
            return self.key < other.key
        else:
            return False


class Heap():
    def __init__(self, arr=[]):
        self.stack = [[], ]
        self.size = 0
        if arr:
            for ai in arr:
                self.push(*ai)

    def up(self, i):
        while i > 1:
            if self.stack[i] > self.stack[i // 2]:
                self.stack[i], self.stack[i // 2] = self.stack[i // 2], self.stack[i]
                i = i // 2
            else:
                break

    def down(self, i):
        def get_max_child(i):
            if i * 2 + 1 > self.size:
                return i * 2
            else:
                return i * 2 if self.stack[i * 2] > self.stack[i * 2 + 1] else i * 2 + 1

        while i * 2 <= self.size:
            max_child = get_max_child(i)
            if self.stack[max_child] > self.stack[i]:
                self.stack[max_child], self.stack[i] = self.stack[i], self.stack[max_child]
                i = max_child
            else:
                break

    def push(self, x, y):
        new_node = Node(x, y)
        self.stack.append(new_node)
        self.size += 1
        self.up(self.size)

    def pop(self):
        retval = self.stack[1]
        self.stack[1] = self.stack[-1]
        self.stack.pop()
        self.size -= 1
        self.down(1)
        return retval


class Solution:
    def topKstrings(self, strings, k):
        record = defaultdict(int)
        for si in strings:
            record[si] += 1

        heap = Heap()
        for ri in record:
            heap.push(ri, record[ri])
        result = []
        for i in range(k):
            cur_node = heap.pop()
            result.append([cur_node.key, cur_node.val])
        return result


if __name__ == '__main__':
    strings = ["plpaboutit", "jnoqzdute", "sfvkdqf", "mjc", "nkpllqzjzp", "foqqenbey", "ssnanizsav", "nkpllqzjzp",
               "sfvkdqf", "isnjmy", "pnqsz", "hhqpvvt", "fvvdtpnzx", "jkqonvenhx", "cyxwlef", "hhqpvvt", "fvvdtpnzx",
               "plpaboutit", "sfvkdqf", "mjc", "fvvdtpnzx", "bwumsj", "foqqenbey", "isnjmy", "nkpllqzjzp", "hhqpvvt",
               "foqqenbey", "fvvdtpnzx", "bwumsj", "hhqpvvt", "fvvdtpnzx", "jkqonvenhx", "jnoqzdute", "foqqenbey",
               "jnoqzdute", "foqqenbey", "hhqpvvt", "ssnanizsav", "mjc", "foqqenbey", "bwumsj", "ssnanizsav",
               "fvvdtpnzx", "nkpllqzjzp", "jkqonvenhx", "hhqpvvt", "mjc", "isnjmy", "bwumsj", "pnqsz", "hhqpvvt",
               "nkpllqzjzp", "jnoqzdute", "pnqsz", "nkpllqzjzp", "jnoqzdute", "foqqenbey", "nkpllqzjzp", "hhqpvvt",
               "fvvdtpnzx", "plpaboutit", "jnoqzdute", "sfvkdqf", "fvvdtpnzx", "jkqonvenhx", "jnoqzdute", "nkpllqzjzp",
               "jnoqzdute", "fvvdtpnzx", "jkqonvenhx", "hhqpvvt", "isnjmy", "jkqonvenhx", "ssnanizsav", "jnoqzdute",
               "jkqonvenhx", "fvvdtpnzx", "hhqpvvt", "bwumsj", "nkpllqzjzp", "bwumsj", "jkqonvenhx", "jnoqzdute",
               "pnqsz", "foqqenbey", "sfvkdqf", "sfvkdqf"]
    k = 10
    result = Solution().topKstrings(strings, k)
    print(result)
