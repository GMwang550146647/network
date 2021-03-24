from fundamentals.test_time import test_time
import logging
import numpy as np

'''
嘘~别说话，运行看输出就好~
'''


class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack():
    def __init__(self):
        self.head = None

    def pop(self):
        if self.head is None:
            logging.error('Stack Empty Error: Tried to pop from empty stack!')
            return None
        else:
            tempt = self.head.val
            self.head = self.head.next
            return tempt

    def push(self, val):
        new_head = ListNode(val)
        new_head.next = self.head
        self.head = new_head

    def top(self):
        if self.head:
            return self.head.val
        else:
            return None

    def __bool__(self):
        return True if self.head else False

    def __str__(self):
        def recur(root, from_bottom=False):
            if root:
                if from_bottom:
                    stack_list.append(root.val)
                recur(root.next)
                if not from_bottom:
                    stack_list.append(root.val)

        stack_list = []
        recur(self.head)
        return str(stack_list)



class Solution():
    def __init__(self):
        pass

    @test_time
    def my_nextGreaterElement(self,nums):
        """
        用的是自己写的栈~要调用上面的类~
        """
        stack = Stack()
        record = [0 for _ in range(len(nums))]
        # 对nums 进行倒序操作
        for i in range(len(nums) - 1, -1, -1):
            while stack and stack.top() <= nums[i]:
                stack_top = stack.pop()
            # 如果栈为空，返回当前对象，并丢入栈
            if not stack:
                record[i] = nums[i]
            # 栈不为空（但是已经保证当前栈顶比nums[i]要大了）
            else:
                record[i] = stack.top()

            stack.push(nums[i])
        return record

    @test_time
    def feifei_nextGreaterElement(self, arr):
        stack = []
        stack.append(0)
        result = [0 for _ in range(len(arr))]
        sum=0
        for i in range(1, len(arr)):
            sum+=len(stack)
            while stack:
                if arr[i] > arr[stack[-1]]:
                    pos = stack.pop()
                    result[pos] = arr[i]
                else:
                    stack.append(i)
                    break
            if not stack:
                stack.append(i)
        while stack:
            pos = stack.pop()
            result[pos] = arr[pos]
        # return result
        return sum/len(arr)

    @test_time
    def nextGreaterElement(self, nums):
        """
        用的是python的自带"栈" 可以随便用
        """
        stack = []
        record = [0 for _ in range(len(nums))]
        sum=0
        for i in range(len(nums) - 1, -1, -1):
            sum+=len(stack)
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            record[i] = stack[-1] if stack else nums[i]
            stack.append(nums[i])
        # return record
        return sum/len(nums)

    def main(self):
        print("###########Reverse:##############")
        # nums = np.random.rand(10000)

        nums = list(reversed(range(10000)))
        self.feifei_nextGreaterElement(nums)
        self.nextGreaterElement(nums)
        # self.my_nextGreaterElement(nums)
        print("###########Nornal:##############")
        nums = list(range(10000))
        self.feifei_nextGreaterElement(nums)
        self.nextGreaterElement(nums)
        # self.my_nextGreaterElement(nums)
        print("###########Random:##############")
        nums = np.random.rand(10000)
        self.feifei_nextGreaterElement(nums)
        self.nextGreaterElement(nums)
if __name__ == '__main__':
    SL = Solution()
    SL.main()
