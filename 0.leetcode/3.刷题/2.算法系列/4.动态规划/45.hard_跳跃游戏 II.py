from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    # @test_time
    def jump(self, nums):
        '''
        从后往前算！！！！
        '''
        len_nums=len(nums)
        dp=[len_nums for _ in nums]
        dp[-1]=0
        for i in range(len(nums)-2,-1,-1):
            for j in range(i+1,min(len(nums),i+nums[i]+1)):
                dp[i]=min(dp[i],dp[j]+1)
        return dp[0]

    def main(self):
        # nums = [2,3,1,1,4]
        nums = [2,3,1,1,4]
        self.jump(nums)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
