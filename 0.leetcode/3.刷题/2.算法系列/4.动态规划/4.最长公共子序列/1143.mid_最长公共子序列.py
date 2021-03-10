from fundamentals.test_time import test_time

import bisect
import numpy as np


class Solution():
    def __init__(self):
        pass

    @test_time
    def longestCommonSubsequence_dp_table(self, text1, text2):
        """
        数组版本比较省事
        """
        width = len(text1) + 1
        length = len(text2) + 1
        dp = [[0 for _ in range(length)] for _ in range(width)]
        for i in range(1, width):
            for j in range(1, length):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

    @test_time
    def longestCommonSubsequence_recur(self, text1, text2):
        """
        递归版本 非常耗时
        """

        def solve_dp(i, j):
            if i == 0 or j == 0:
                return 0
            elif (i, j) in dp:
                return dp[(i, j)]
            else:
                if text1[i - 1] == text2[j - 1]:
                    dp[(i, j)] = solve_dp(i - 1, j - 1) + 1
                else:
                    dp[(i, j)] = max(solve_dp(i - 1, j), solve_dp(i, j - 1))
                return dp[(i, j)]

        dp = {}
        width = len(text1)
        length = len(text2)
        result = solve_dp(width, length)
        return result

    def main(self):
        text1 = "bsbininm"
        text2 = "jmjkbkjkv"
        self.longestCommonSubsequence_dp_table(text1, text2)
        self.longestCommonSubsequence_recur(text1, text2)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
