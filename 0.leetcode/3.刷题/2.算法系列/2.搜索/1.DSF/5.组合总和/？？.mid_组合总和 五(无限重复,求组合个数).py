from fundamentals.test_time import test_time

"""
顺序不同的序列被视作相同的组合。
"""
class Solution():
    def __init__(self):
        pass

    @test_time
    def combinationSum5(self,nums,target):
        dp=[[0]*(target+1)  for _ in range (len(nums)+1)]
        for i in range(len(nums)+1):
            dp[i][0]=1
        for i in range(1,len(nums)+1):
            for j in range(1,target+1):
                if nums[i-1]<=target:
                    dp[i][j]=dp[i][j-nums[i-1]]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]

    def main(self):
        nums = [1, 2, 3]
        target = 4
        self.combinationSum5(nums,target)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
