from fundamentals.test_time import test_time

import sys

sys.setrecursionlimit(10000)


class Solution():
    def __init__(self):
        pass

    @test_time
    def change_dp(self, amount, coins):
        """
        d[i][j] 代表的意义是 只有前j个币组成i的次数总和
        :param amount:
        :param coins:
        :return:
        """

        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        for i in range(len(coins) + 1):
            dp[i][0] = 1
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):

                if j - coins[i - 1] >= 0:
                    dp[i][j] = dp[i][j - coins[i - 1]] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        print("%%%%%%%%%%%%%")
        for rowi in dp:
            print(rowi)
        return dp[len(coins)][amount]

    @test_time
    def change_dp_compress(self, amount, coins):
        """
        d[i][j] 代表的意义是 只有前j个币组成i的次数总和

        """

        dp = [0 for _ in range(amount + 1)]
        dp[0]=1
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if j - coins[i - 1] >= 0:
                    dp[j] = dp[j - coins[i - 1]] + dp[j]
                else:
                    dp[j] = dp[j]

        print("%%%%%%%%%%%%%")
        print(dp)
        return dp[-1]

    def main(self):
        amount = 5
        coins = [1, 2, 5]
        self.change_dp(amount, coins)
        self.change_dp_compress(amount, coins)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
