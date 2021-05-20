from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def numTrees(self, n):
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[-1]

    def main(self):
        n = 3
        self.numTrees(n)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
