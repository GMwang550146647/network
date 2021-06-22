from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def func(self,nums,target):
        left=0
        right=len(nums)
        while left<right:
            mid=(left+right)//2
            if target==nums[mid]:
                return mid
            #中点在左序列
            if nums[0]<nums[mid]:
                # 目标在左序列中
                if nums[0]<=target<nums[mid]:
                    right=mid
                else:
                    left=mid+1
            #中点在右序列
            else:
                # 目标在有序列中
                if nums[mid]<target<=nums[-1]:
                    left=mid+1
                else:
                    right=mid
        return -1

    def main(self):
        nums=[2,3,4,0,1]
        target=0
        self.func(nums,target)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
