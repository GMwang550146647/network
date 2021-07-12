from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def eraseOverlapIntervals(self, intervals):
        """
        动态规划，计算每个interval 的互不重叠区间！
        o(n2) 超出时间限制
        """
        intervals = sorted(intervals)
        dp = [1 for _ in range(len(intervals))]
        for i in range(1, len(intervals)):
            for j in range(i):
                if intervals[i][0] >= intervals[j][1]:
                    dp[i] =max(dp[i],dp[j]+1)
        return len(intervals) - max(dp)

    @test_time
    def eraseOverlapIntervals_tanxin(self, intervals):
        """
        贪心算法核心:
            最早结束的那个区间有更好的机会去构建更长的链条！
        """
        intervals = sorted(intervals,key=lambda x:x[1])
        right=intervals[0][1]
        nums=1
        for i in range(1,len(intervals)):
            if intervals[i][0]>=right:
                nums+=1
                right=intervals[i][1]
        return len(intervals)-nums

    def main(self):
        intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
        # intervals = [[1, 2], [1, 2], [1, 2]]
        self.eraseOverlapIntervals(intervals)
        self.eraseOverlapIntervals_tanxin(intervals)



if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
