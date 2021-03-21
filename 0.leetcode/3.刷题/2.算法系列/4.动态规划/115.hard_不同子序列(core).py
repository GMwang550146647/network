from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def numDistinct_recur(self, s, t):
        """
        纯递归解法
        """

        def solve(s, t):
            if len(t) == 1:
                count = 0
                for item in s:
                    if t == item:
                        count += 1
                return count
            else:
                count = 0
                for i in range(len(s)):
                    if t[0] == s[i]:
                        count += solve(s[i + 1:], t[1:])
                return count

        return solve(s, t)

    @test_time
    def numDistinct(self, s, t):
        """
        dp[i][j]的意思是 t中前i个词 在 s中 前j个词中的重复次数！
        """
        def solve(s, t):
            dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(t) + 1)]
            for i in range(len(s) + 1):
                dp[0][i] = 1
            for j in range(1, len(s) + 1):
                for i in range(1, len(t) + 1):
                    if t[i - 1] == s[j - 1]:
                        dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
                    else:
                        dp[i][j] = dp[i][j - 1]
            return dp[-1][-1]
        return solve(s, t)

    def main(self):
        s = "babgbag"
        t = "bag"
        self.numDistinct_recur(s, t)
        self.numDistinct(s, t)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
