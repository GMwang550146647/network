from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def dicesProbability(self, n):
        dp=[1/6 for i in range(6)]
        for i in range(2,n+1):
            new_dp=[0 for _ in range(5*i+1)]
            for j in range(5*i+1):
                for k in range(max(0,j-5),min(len(dp),j+1)):
                    new_dp[j]+= dp[k]/6
            dp=new_dp
        return dp

    def main(self):
        n=4
        self.dicesProbability(n)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
