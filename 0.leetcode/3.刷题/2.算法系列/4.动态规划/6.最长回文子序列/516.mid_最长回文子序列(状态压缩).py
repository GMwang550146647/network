from fundamentals.test_time import test_time

import bisect
import numpy as np


class Solution():
    def __init__(self):
        pass

    @test_time
    def longestPalindromeSubseq_recur_record(self, s):
        """
        递归 记录版本
        """

        def dp(i, j):
            if i == j:
                return 1
            if i > j:
                return 0
            if (i, j) in dp_table:
                return dp_table[(i, j)]
            else:
                if s[i] == s[j]:
                    dp_table[(i, j)] = dp(i + 1, j - 1) + 2
                else:
                    dp_table[(i, j)] = max(dp(i, j - 1), dp(i + 1, j))
                return dp_table[(i, j)]

        dp_table = {}
        return dp(0, len(s) - 1)

    @test_time
    def longestPalindromeSubseq_dp(self, s):
        """
        翻转 横着遍历！（列表有一半是没用的）
        """
        len_s = len(s)
        dp = [[0 for _ in range(len(s))] for _ in range(len_s)]
        for i in range(len_s):
            dp[i][i] = 1
        for i in range(len_s - 2, -1, -1):
            for j in range(i + 1, len_s):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        return dp[0][-1]

    @test_time
    def longestPalindromeSubseq_dp_compress(self, s):
        """
        dp状态压缩，空间由 o(n2) -> o(n)
            特点：只和周围的有关，只需计算一次就够了
        """
        len_s = len(s)
        dp = [1 for _ in range(len(s))]
        for i in range(len_s - 2, -1, -1):
            for j in range(i + 1, len_s):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i][j])
        return dp[0][-1]

    def main(self):
        s = "bbbab"
        self.longestPalindromeSubseq_recur_record(s)
        self.longestPalindromeSubseq_dp(s)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
