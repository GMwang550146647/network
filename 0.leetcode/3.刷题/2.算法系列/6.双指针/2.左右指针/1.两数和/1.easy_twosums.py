from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def twoSum_iteration(self, nums, target):
        '''
        双重循环计算twosum
            空间：o(1)
            时间：o(N2)
        '''
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return [-1,-1]
    @test_time
    def twoSum_dict(self, nums, target):
        """
        字典记录
            空间： o(N)
            时间： o(N)
        """
        record = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in record:
                return [record[nums[i]], i]
            else:
                record[diff] = i
        return [-1, -1]



    def main(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.twoSum_dict(nums, target)
        # self.twoSum_iteration(nums, target)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
