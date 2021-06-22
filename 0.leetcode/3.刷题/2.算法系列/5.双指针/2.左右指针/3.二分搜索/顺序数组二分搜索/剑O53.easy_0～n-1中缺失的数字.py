from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def missingNumber(self, nums):
        if nums[-1]==len(nums)-1:
            return len(nums)
        left=0
        right=len(nums)
        while left<right:
            mid=(left+right)//2
            if nums[mid]==mid:
                left=mid+1
            else:
                right=mid+1
        return left

    def main(self):
        nums = [0,1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
        nums=[0]
        self.missingNumber(nums)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
