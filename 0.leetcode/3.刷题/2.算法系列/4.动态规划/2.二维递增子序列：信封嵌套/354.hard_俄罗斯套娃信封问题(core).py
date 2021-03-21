from fundamentals.test_time import test_time

import bisect
class Solution():
    def __init__(self):
        pass

    '''我的方法'''

    @test_time
    def maxEnvelopes(self,envelopes):
        """
        先排序，然后退化为最长递增子序列问题
        """
        envelopes=sorted(envelopes,key=lambda a:(a[0],-a[1]))
        dp=[1]*len(envelopes)
        for i in range(1,len(envelopes)):
            for j in range(i):
                if envelopes[i][1]>envelopes[j][1]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)

    def main(self):
        envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
        self.maxEnvelopes(envelopes)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
