from fundamentals.test_time import test_time

import sys

sys.setrecursionlimit(10000)


class Solution():
    def __init__(self):
        pass

    @test_time
    def rob_recur_dict(self, nums):
        """
        递归 备忘录
        """
        def dp(start=0):
            if start >= len(nums):
                return 0
            elif start in dp_record:
                return dp_record[start]
            else:
                dp_record[start] = max(dp(start + 1), dp(start + 2) + nums[start])
                return dp_record[start]

        dp_record = {}
        return dp()

    @test_time
    def rob_dp(self, nums):
        """
        标准动态规划
        """
        nums=nums.copy()
        if len(nums) <= 2:
            return max(nums)
        else:
            nums[1]=max(nums[0],nums[1])
            for i in range(2, len(nums)):
                nums[i] =max(nums[i-1],nums[i-2]+nums[i])
            return max(nums)

    def main(self):
        nums = [2, 7, 9, 3, 1]
        nums = [1, 2, 3, 1]
        nums = [2, 1, 1, 2]
        # nums = [2, 7, 9, 3, 1]
        # nums = [1, 3, 1, 3, 100]
        self.rob_recur_dict(nums)
        self.rob_dp(nums)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
