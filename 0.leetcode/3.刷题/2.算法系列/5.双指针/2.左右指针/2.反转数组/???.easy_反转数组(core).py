from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    '''我的方法'''

    @test_time
    def reverseList(self, nums):
        nums=nums.copy()
        left=0
        right=len(nums)-1
        while(left<right):
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        return nums


    def main(self):
        nums = [2, 7, 11, 15,90]
        self.reverseList(nums)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
