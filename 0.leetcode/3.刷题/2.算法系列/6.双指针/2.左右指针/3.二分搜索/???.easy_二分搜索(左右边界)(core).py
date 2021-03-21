from fundamentals.test_time import test_time
from math import ceil

class Solution():
    def __init__(self):
        pass

    '''我的方法'''

    @test_time
    def search_left_bound(self, nums, target):
        """
        保证right 所在的位置是>=target的，然后等left靠过来就行了
        保证：该节点及之前的都是>=target的
        """
        left = 0
        right = len(nums)
        while (left < right):
            mid = int((right - left) / 2 + left)
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left

    @test_time
    def search_right_bound(self, nums, target):
        """
        保证left 所在的位置是<=target的，等待right靠过来就行了
        保证： 该节点及之前的都是<=target
        """
        left = -1
        right = len(nums)-1
        while (left < right):
            mid = ceil((right - left) / 2 + left)
            if nums[mid] == target:
                left = mid
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid
        return left

    def main(self):
        nums = [-1, 0, 3, 3, 3, 3, 3, 5, 9, 12]
        target = -2
        left=self.search_left_bound(nums, target)
        right=self.search_right_bound(nums, target)
        print(nums[left:right+1])

if __name__ == '__main__':
    SL = Solution()
    SL.main()
