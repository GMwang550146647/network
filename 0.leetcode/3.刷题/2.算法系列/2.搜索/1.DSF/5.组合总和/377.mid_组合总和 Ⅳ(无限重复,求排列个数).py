from fundamentals.test_time import test_time

"""
顺序不同的序列被视作不同的组合。
"""


class Solution():
    def __init__(self):
        pass

    @test_time
    def combinationSum4_recur(self, nums, target):
        def dfs(target):
            if target == 0:
                return 1
            elif target in record_dict:
                return record_dict[target]
            else:
                total = 0
                for numi in nums:
                    if numi <= target:
                        total += dfs(target - numi)
                record_dict[target] = total
                return total

        record_dict = {}
        return dfs(target)

    @test_time
    def combinationSum4_dp(self, nums, target):
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[target]

    def main(self):
        nums = [1, 2, 3]
        target = 4
        self.combinationSum4_recur(nums, target)
        self.combinationSum4_dp(nums, target)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
