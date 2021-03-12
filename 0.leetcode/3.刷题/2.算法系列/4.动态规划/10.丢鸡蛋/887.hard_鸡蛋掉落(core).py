from fundamentals.test_time import test_time

import sys

sys.setrecursionlimit(10000)


class Solution():
    def __init__(self):
        pass

    @test_time
    def superEggDrop_recur_lineSearch(self, k, n):
        """
        线性搜索：时间太慢了
        """

        def dp(k, n):
            # base
            # 如果丢到第0层，就不用丢了，肯定是0
            if n == 0:
                return 0
            # 如果剩下一个鸡蛋，只能从低往高丢了
            elif k == 1:
                return n
            elif (k, n) in dp_table:
                return dp_table[(k, n)]
            else:
                res = 10000
                for i in range(1, n + 1):
                    res = min(res, max(dp(k, n - i), dp(k - 1, i - 1)) + 1)
                dp_table[(k, n)] = res
                return res

        dp_table = {}
        return dp(k, n)

    @test_time
    def superEggDrop_recur_binarySearch(self, k, n):
        """
        二分搜索：快一点了
        """

        def dp(k, n):
            # base
            # 如果丢到第0层，就不用丢了，肯定是0
            if n == 0:
                return 0
            # 如果剩下一个鸡蛋，只能从低往高丢了
            elif k == 1:
                return n
            elif (k, n) in dp_table:
                return dp_table[(k, n)]
            else:
                low, high = 1, n + 1
                res = 10000
                while (low < high):
                    mid = (low + high) // 2
                    broken = dp(k - 1, mid - 1)
                    not_broken = dp(k, n - mid)
                    if broken > not_broken:
                        high = mid
                        res = min(res, broken + 1)
                    else:
                        low = mid + 1
                        res = min(res, not_broken + 1)
                dp_table[(k, n)] = res
                return res

        dp_table = {}
        return dp(k, n)

    @test_time
    def superEggDrop_dp(self, k, n):
        """
        非常可怕的想法！！！
        反向思维(dp和recur一般都是反向的)： 给你k个鸡蛋，丢m次 什么时候至少能丢n层楼？
        """
        dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
        m = 0
        while (dp[k][m] < n):
            m += 1
            for k_i in range(1, k + 1):
                dp[k_i][m] = dp[k_i - 1][m - 1] + dp[k_i][m - 1] + 1
        return m

    def main(self):
        K = 3
        N = 14
        # self.superEggDrop_recur_lineSearch(K,N)
        # self.superEggDrop_recur_binarySearch(K, N)
        self.superEggDrop_dp(K, N)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
