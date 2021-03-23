import logging
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


def my_nextGreaterElement(nums):
    """
    用的是自己写的栈~要调用上面的类~
    """
    stack = Stack()
    record = [0 for _ in range(len(nums))]
    # 对nums 进行倒序操作
    for i in range(len(nums) - 1, -1, -1):
        print(f"######################{i}#######################")
        print(f'当前index {i},该数字是{nums[i]},此时栈为{stack},record为{record}')
        # 如果栈不为空，pop到满足 nums[i] <栈顶 或者栈空为止！
        while stack and stack.top() <= nums[i]:
            stack_top = stack.pop()
            print(f"pop 出 较 {nums[i]}小的数 {stack_top}")
        # 如果栈为空，返回当前对象，并丢入栈
        if not stack:
            record[i] = nums[i]
            print(f"此时栈为空！所以取自身的值{nums[i]},record 更新为 {record}")
        # 栈不为空（但是已经保证当前栈顶比nums[i]要大了）
        else:
            record[i] = stack.top()
            print(f"此时栈非空！所以取栈顶值{stack.top()},record 更新为 {record}")

        stack.push(nums[i])
        print(f'{nums[i]}入栈~栈更新为{stack}')
    print("Enjoy~最终结果是：{}".format(record))
    return record


def nextGreaterElement(nums):
    """
    用的是python的自带"栈" 可以随便用
    """
    stack = []
    record = [0 for _ in range(len(nums))]
    # 对nums 进行倒序操作
    for i in range(len(nums) - 1, -1, -1):
        print(f"######################{i}#######################")
        print(f'当前index {i},该数字是{nums[i]},此时栈为{stack},record为{record}')
        # 如果栈不为空，pop到满足 nums[i] <栈顶 或者栈空为止！
        while stack and stack[-1] <= nums[i]:
            stack_top = stack.pop()
            print(f"pop 出 较 {nums[i]}小的数 {stack_top}")
        # 如果栈为空，返回当前对象，并丢入栈
        if not stack:
            record[i] = nums[i]
            print(f"此时栈为空！所以取自身的值{nums[i]},record 更新为 {record}")
        # 栈不为空（但是已经保证当前栈顶比nums[i]要大了）
        else:
            record[i] = stack[-1]
            print(f"此时栈非空！所以取栈顶值{stack[-1]},record 更新为 {record}")

        stack.append(nums[i])
        print(f'{nums[i]}入栈~栈更新为{stack}')
    print("Enjoy~最终结果是：{}".format(record))
    return record


if __name__ == '__main__':
    nums = [3, 1, 2, 7, 4, 6]
    my_nextGreaterElement(nums)
    # nextGreaterElement(nums)
