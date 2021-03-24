from fundamentals.test_time import test_time


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack=[]
        self.stack=[]

    def push(self, val: int) -> None:
        if not self.min_stack or (self.min_stack and val<self.min_stack[-1]):
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])
        self.stack.append(val)

    def pop(self) -> None:
        self.min_stack.pop(-1)
        return self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

class Solution():
    def __init__(self):
        pass

    @test_time
    def func(self, nums):
        pass

    def main(self):
        nums = [2, 7, 9, 3, 1]
        self.func(nums)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
