class Solution:
    def LCS(self, str1, str2):
        # write code here
        dp = [[''] * (len(str2) + 1) for _ in range(len(str1) + 1)]
        for i in range(1, len(str1) + 1):
            for j in range(1, len(str2) + 1):
                add = str1[i - 1] if str1[i - 1] == str2[j - 1] else ''
                new_str = dp[i - 1][j - 1] + add
                dp[i][j] = new_str if len(new_str) > len(dp[i][j - 1]) else dp[i][j - 1]
        return dp[-1][-1]
