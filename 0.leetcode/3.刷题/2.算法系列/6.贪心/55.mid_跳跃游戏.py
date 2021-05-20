from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def canJump(self, nums):
        max_index=0
        for i in range(len(nums)):
            if max_index>=i:
                max_index=max(max_index,i+nums[i])
            else:
                return False
        return True

    def main(self):
        # nums = [2,3,1,1,4]
        nums = [3,2,1,0,4]
        self.canJump(nums)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
