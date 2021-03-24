from fundamentals.test_time import test_time
from math import ceil


class Solution():
    def __init__(self):
        pass

    # @test_time
    # def find132pattern_ans(self, nums):
    #     if len(nums) < 3:
    #         return False
    #
    #     pre_mins = [nums[0]]
    #     for i in range(1, len(nums)):
    #         pre_mins.append(min(pre_mins[-1], nums[i]))
    #     stack_k = []
    #     for j in range(len(nums) - 1, -1, -1):
    #         if nums[j] > pre_mins[j]:
    #             while stack_k and pre_mins[j] >= stack_k[-1]:
    #                 stack_k.pop()
    #
    #             if stack_k and stack_k[-1] < nums[j]:
    #                 return True
    #
    #             stack_k.append(nums[j])
    #
    #     return False

    @test_time
    def find132pattern(self, nums):
        if len(nums) < 3:
            return False
        pre_mins = [nums[0]]
        for i in range(1, len(nums)):
            pre_mins.append(min(pre_mins[-1], nums[i]))
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > pre_mins[i]:
                while stack and pre_mins[i] >= stack[-1]:
                    stack.pop(-1)
                if stack and stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])
        return False

    def main(self):
        nums = [3, 5, 0, 3, 4]
        nums = [1, 2, 3, 4, 5]
        nums = [-1, 3, 2, 0]
        # nums = [1, 0, 1, -4, -3]
        nums = [-2, 1, 2, -2, 1, 2]
        # nums = [3,1,4,2]
        # nums = [-1,3,2,0]
        print(self.find132pattern(nums))
        print(self.find132pattern_ans(nums))


if __name__ == '__main__':
    SL = Solution()
    SL.main()
