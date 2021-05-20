from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    '''我的方法'''

    @test_time
    def search(self, nums, target):
        """
        解释：
            left的位置是能检查的（因为向下取整）
            right的位置是检查不到的（所以初始值也是不可达，而且向下取整使该值最后不能作为中值检查）
            当left==right的时候，是left最后一次向right靠近，此时已经检查了所有的节点！
            关于更新：
                由于mid已经检查，而right节点是不检查的，所以right=mid
                由于mid已经检查，但是left的节点最终是会被检查的，没有必要重复检查，而且+1会有助于最后循环的退出
        """
        left = 0
        right = len(nums)
        while (left < right):
            mid = int((right - left) / 2 + left)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        # 还有一种情况就是left==right的时候
        return -1

    def main(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 9
        self.search(nums, target)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
