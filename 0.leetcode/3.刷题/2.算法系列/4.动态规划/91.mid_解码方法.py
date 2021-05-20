from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def numDecodings(self, s: str) -> int:
        dp=[1]+[0 for _ in range(len(s))]
        for i in range(1,len(s)+1):
            if s[i-1]!='0':
                dp[i]=dp[i-1]
            if i>1 and s[i-2]!='0' and int(s[i-2:i])<=26:
                dp[i]+=dp[i-2]
        return dp[-1]

    def main(self):
        s = "226"
        self.numDecodings(s)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
