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
            if nums[left]<=nums[mid]:
                # 目标在左序列中
                if nums[0]<=target<nums[mid]:
                    right=mid
                else:
                    left=mid
            #中点在右序列
            else:
                # 目标在有序列中
                if nums[mid]<target<=nums[-1]:
                    left=mid
                else:
                    right=mid
        return -1

    @test_time
    def search(self, nums, target) -> bool:
        if not nums:
            return False

        n = len(nums)
        if n == 1:
            return nums[0] == target

        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            print(mid)
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid] and nums[mid] == nums[r]:
                l += 1
                r -= 1
            elif nums[l] <= nums[mid]:
                if nums[l] <= target and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target and target <= nums[n - 1]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False

    def main(self):
        nums = [2, 2,2, 0, 2]
        target = 0
        self.func(nums, target)
        # self.search(nums,target)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
