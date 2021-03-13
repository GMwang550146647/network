from fundamentals.test_time import test_time

import sys

sys.setrecursionlimit(10000)


class Solution():
    def __init__(self):
        pass

    @test_time
    def package_recur_record(self, n, w, wt, val):
        def dp(i, j):
            '''
            :param : 如今的重量
            :param j: 选择了前j个物品了
            :return:
            '''
            if i == 0 or j == 0:
                return 0
            elif (i, j) in dp_record:
                return dp_record[(i, j)]
            else:
                max_val = -1
                for k in range(n):
                    if i - wt[k] > 0:
                        max_val = max(max_val, max(dp(i, j - 1), dp(i - wt[k], j - 1) + val[k]))
                    else:
                        max_val = max(max_val, dp(i, j - 1))
                dp_record[(i, j)] = max_val
                return max_val

        dp_record = {}
        return dp(w, n)

    @test_time
    def package_dp1(self, n, w, wt, val):
        """
        记录最优路径的禁忌搜索 list of [list & val]
        """
        # dp的index 代表重量， value代表该重量能达到的价值
        dp = [[0, []] for _ in range(w + 1)]
        min_w = min(wt)
        for i in range(min_w, len(dp)):
            # 选出重量为i 时最好的组合
            for j in range(len(wt)):
                # 能够装
                if i - wt[j] > 0:
                    # 而且最大 而且不在 已添加队列里面
                    if j not in dp[i - wt[j]][1] and dp[i - wt[j]][0] + val[j] > dp[i][0]:
                        dp[i][0] = dp[i - wt[j]][0] + val[j]
                        dp[i][1] = dp[i - wt[j]][1][:] + [j]
        return max([wi[0] for wi in dp])

    @test_time
    def package_dp2(self, n, w, wt, val):
        """
        记录只有前n个物品时候w的最优选择
        """
        # dp的index 代表重量， value代表该重量能达到的价值
        dp = [[0 for _ in range(w + 1)] for _ in range(n + 1)]
        for i in range(1, w + 1):
            for j in range(1, n + 1):
                if i - wt[j - 1] > 0:
                    dp[j][i] = max(dp[j - 1][i], dp[j - 1][i - wt[j - 1]] + val[j - 1])
                else:
                    dp[j][i] = dp[j - 1][i]
        return dp[n][w]

    def main(self):
        N = 3
        W = 4
        wt = [2, 1, 3]
        val = [4, 2, 3]
        self.package_recur_record(N, W, wt, val)
        self.package_dp1(N, W, wt, val)
        self.package_dp2(N, W, wt, val)



if __name__ == '__main__':
    SL = Solution()
    SL.main()
