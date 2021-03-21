from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def removeDuplicates(self, nums):
        p1=p2=1
        while(p2<len(nums)):
            if nums[p2]!=nums[p1-1]:
                nums[p1]=nums[p2]
                p1+=1
            p2+=1
        return p1
    def main(self):
        nums = [0,0,1,1,1,2,2,3,3,4]
        self.removeDuplicates(nums)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
