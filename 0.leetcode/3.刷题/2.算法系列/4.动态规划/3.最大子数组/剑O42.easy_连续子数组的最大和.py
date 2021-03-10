from fundamentals.test_time import test_time

import bisect


class Solution():
    def __init__(self):
        pass

    @test_time
    def maxSubArray_dp(self, nums):
        """
        dp 方法
            dp的每个地方都记录着已经在前面的集合还是不在集合里面的sum
        """
        for i in range(1, len(nums)):
            nums[i]=max(nums[i-1]+nums[i],nums[i])
        return max(nums)

    def main(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.maxSubArray_dp(nums)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
