from fundamentals.test_time import test_time

import bisect
import numpy as np


class Solution():
    def __init__(self):
        pass

    @test_time
    def minInsertions_recur_record(self, s):
        """
        recursion dp +record_dict
        """
        dp_table = {}

        def dp(i, j):
            if i >= j:
                return 0
            elif (i, j) in dp_table:
                dp_table[(i + 1, j - 1)] = dp_table[(i, j)]
            elif s[i] == s[j]:
                dp_table[(i, j)] = dp(i + 1, j - 1)
            else:
                dp_table[(i, j)] = min(dp(i + 1, j), dp(i, j - 1)) + 1
            return dp_table[(i, j)]

        return dp(0, len(s) - 1)

    @test_time
    def minInsertions_dp(self, s):
        """
        iteration dp
        """
        len_s = len(s)
        dp = [[0 for _ in range(len_s)] for _ in range(len_s)]
        for i in range(len_s - 1, -1, -1):
            for j in range(i + 1, len_s):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i + 1][j]) + 1
        return dp[0][-1]

    @test_time
    def minInsertions_dp_compress_list(self, s):
        """
        iteration dp + compression( addition list dp_cpy)
        """
        len_s = len(s)
        dp = [0 for _ in range(len_s)]
        for i in range(len_s - 1, -1, -1):
            dp_cpy = dp.copy()
            for j in range(i + 1, len_s):
                if s[i] == s[j]:
                    dp[j] = dp_cpy[j - 1]
                else:
                    dp[j] = min(dp[j - 1], dp[j]) + 1
        return dp[-1]

    @test_time
    def minInsertions_dp_compress_var(self, s):
        """
        iteration dp + compression (addition var pre)
        """
        len_s = len(s)
        dp = [0 for _ in range(len_s)]
        for i in range(len_s - 1, -1, -1):
            pre =0
            for j in range(i + 1, len_s):
                tempt=dp[j]
                if s[i] == s[j]:
                    dp[j] = pre
                else:
                    dp[j] = min(dp[j - 1], dp[j]) + 1
                pre=tempt
        return dp[-1]

    def main(self):
        s = "mbadm"
        self.minInsertions_recur_record(s)
        self.minInsertions_dp(s)
        self.minInsertions_dp_compress_list(s)
        self.minInsertions_dp_compress_var(s)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
