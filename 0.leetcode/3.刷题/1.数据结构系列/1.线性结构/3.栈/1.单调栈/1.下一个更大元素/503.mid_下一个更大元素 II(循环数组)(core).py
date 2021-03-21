from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def nextGreaterElement(self, nums):
        """
        采取物理 数组*2的操作
        """
        stack = []
        len_num = len(nums)
        nums = nums + nums
        record = [-1 for _ in range(len_num * 2)]
        # 从后往前处理
        for i in range(len(nums) - 1, -1, -1):
            # 2.1.如果比栈顶要大：一直pop到比当前值要大的值为止，如果空了，就返回-1，如果没空，返回栈顶，并加入当前值到stack
            while stack and stack[-1] <= nums[i]:
                stack.pop(-1)
            if not stack:
                record[i] = -1
                stack.append(nums[i])
            else:
                record[i] = stack[-1]
                stack.append(nums[i])
        return record[:len_num]

    @test_time
    def nextGreaterElement_fast(self, nums):
        """
        采取虚幻数组*2的操作：不占据多余内存
        """
        stack = []
        len_nums=len(nums)
        record = [-1 for _ in nums]
        # 从后往前处理
        for i in range(len(nums)*2 - 1, -1, -1):
            index=i%len_nums
            # 2.1.如果比栈顶要大：一直pop到比当前值要大的值为止，如果空了，就返回-1，如果没空，返回栈顶，并加入当前值到stack
            while stack and stack[-1] <= nums[index]:
                stack.pop(-1)
            if not stack:
                record[index] = -1
                stack.append(nums[index])
            else:
                record[index] = stack[-1]
                stack.append(nums[index])
        return record

    def main(self):
        nums = [1, 2, 1]
        self.nextGreaterElement(nums)
        self.nextGreaterElement_fast(nums)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
