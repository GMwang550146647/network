from fundamentals.test_time import test_time

import sys

sys.setrecursionlimit(10000)


class Solution():
    def __init__(self):
        pass

    @test_time
    def maxCoins_recur(self, nums):
        '''
        recur 全遍历版本
        '''

        def get_score(cur_balls, i):
            return (cur_balls[i] * (cur_balls[i - 1] if i - 1 >= 0 else 1) * (
                cur_balls[i + 1] if i + 1 < len(nums) else 1))

        def backtrack(cur_balls, cur_score):
            nonlocal max_score
            if len(cur_balls) == 0:
                if cur_score > max_score:
                    max_score = cur_score
            else:
                for i in range(len(cur_balls)):
                    score_add = get_score(cur_balls, i)
                    tempt_ball = cur_balls.pop(i)
                    backtrack(cur_balls, cur_score + score_add)
                    cur_balls.insert(i, tempt_ball)

        max_score = -1
        backtrack(nums, 0)
        return max_score

    @test_time
    def maxCoins_dp(self, nums):
        # 初始化base case
        nums=nums.copy()
        nums.insert(0, 1)
        nums.append(1)
        len_nums = len(nums)
        dp = [[1 for _ in range(len_nums)] for _ in range(len_nums)]
        for i in range(len_nums):
            dp[i][i] = nums[i]

        # 转换方程 dp[i][j]=dp[i][k]+dp[k][j]+nums[i]*nums[j]*nums[k]
        # 从底往上遍历
        for i in range(len_nums - 2, 0, -1):
            for j in range(i + 1, len_nums):
                for k in range(i + 1, j):  # 之所以是i+1 -> j-1 是因为当j-k==1的时候不计算了，就是0（dp的默认值）
                    dp[i][j]=max(dp[i][j],dp[i][k]+dp[k][j]+nums[i]*nums[k]*nums[j])
        return dp[1][-1]

    def main(self):
        nums = [3, 1, 5, 8]
        self.maxCoins_recur(nums)
        self.maxCoins_dp(nums)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
