from fundamentals.test_time import test_time

import sys

sys.setrecursionlimit(10000)


class Solution():
    def __init__(self):
        pass

    @test_time
    def canPartition_dp(self, nums):

        target = sum(nums)
        if target % 2 == 0:
            target = target // 2
        else:
            return False
        n = len(nums)
        dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True
        for i in range(1, target + 1):
            for j in range(1, n + 1):
                if i - nums[j - 1] >= 0:
                    dp[j][i] = dp[j - 1][i] or dp[j - 1][i - nums[j - 1]]
                else:
                    dp[j][i] = dp[j - 1][i]
        print("#############")
        for row in dp:
            print(row)

        return dp[n][target]


    def main(self):
        nums = [1, 5, 11, 5,2]
        self.canPartition_dp(nums)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
