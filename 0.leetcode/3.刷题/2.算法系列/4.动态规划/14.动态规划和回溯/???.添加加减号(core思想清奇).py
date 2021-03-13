from fundamentals.test_time import test_time
from fundamentals.tree import Tree
import sys

sys.setrecursionlimit(10000)


class Solution():
    def __init__(self):
        pass

    @test_time
    def solve_backtrack(self, nums, target):
        """
        back track 全遍历 复杂度 o(2**N)
        """

        def backtrack(cur_nums, cur_res=0, cur_exp=''):
            if len(cur_nums) == 0:
                if cur_res == target:
                    solutions.append(cur_exp)
            else:
                for op_i in ops:
                    tempt_num = cur_nums.pop(-1)
                    backtrack(cur_nums, ops[op_i](cur_res, tempt_num), op_i + str(tempt_num) + cur_exp)
                    cur_nums.append(tempt_num)

        ops = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
        solutions = []
        backtrack(nums)
        print("*************")
        for soli in solutions:
            print(soli)
        return solutions

    @test_time
    def solve_recur_record(self, nums, target):
        def dp(cur_i, cur_target):
            if cur_i == len(nums):
                if cur_target == 0:
                    return 1
                return 0
            elif (cur_i, cur_target) in dp_record:
                return dp_record[(cur_i, cur_target)]
            else:
                res = dp(cur_i + 1, cur_target - nums[cur_i]) + dp(cur_i + 1, cur_target + nums[cur_i])
                dp_record[(cur_i, cur_target)] = res
                return res

        dp_record = {}
        return dp(0, target)

    @test_time
    def solve_dp(self, nums, target):
        """
        假设A 中全部正数 ， B中全部负数
        sum(A)-sum(B)=target
        2*sum(A)=target+sum(A+B)
        转化为求 其中一部分数的和 为(target+sum(A+B))/2
        PS: 若为小数，则不可能
        """
        # 1.若为小数，则不可能
        target = sum(nums) + target
        if target % 2 == 1:
            return 0
        else:
            target = target // 2
        # 2.问题转化为 在nums中抽取元素组成target，有多少种可能
        dp = [[0 for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            dp[i][0] = 1
        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):
                if j - nums[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[len(nums)][target]

    @test_time
    def solve_dp_compress(self, nums, target):
        """
        PS : 压缩 dp的时候为了防止重叠问题 ，要从后往前遍历~
        """
        # 1.若为小数，则不可能
        target = sum(nums) + target
        if target % 2 == 1:
            return 0
        else:
            target = target // 2
        # 2.问题转化为 在nums中抽取元素组成target，有多少种可能
        dp = [0 for _ in range(target + 1)]
        dp[0]=1
        for i in range(1, len(nums) + 1):
            for j in range(target,0,-1):
                if j - nums[i - 1] >= 0:
                    dp[j] = dp[j] + dp[j - nums[i - 1]]
        return dp[target]

    def main(self):
        nums = [1, 3, 1, 4, 2, 3, 2, 4, 5, 6, 4, 4]
        target = 5

        # self.solve_backtrack(nums, target)
        # self.solve_recur_record(nums, target)
        self.solve_dp(nums, target)
        self.solve_dp_compress(nums, target)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
