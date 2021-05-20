from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    '''我的方法'''

    @test_time
    def twoSum_dict(self, nums, target):
        """
        一直比较在不在set里面比较慢
        """
        record_set=set()
        for i in range(len(nums)):
            if nums[i] in record_set:
                return (nums[i],target-nums[i])
            record_set.add(target-nums[i])
        return None

    @test_time
    def twoSum_TwoPoints(self,nums,target):
        """
        快一点
        """
        left=0
        right=len(nums)-1
        twosum=nums[left]+nums[right]
        while twosum!=target and left<right:
            if twosum>target:
                right-=1
            else:
                left+=1
            twosum=nums[left]+nums[right]
        return [nums[left],nums[right]]

    def main(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.twoSum_dict(nums, target)
        self.twoSum_TwoPoints(nums, target)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
