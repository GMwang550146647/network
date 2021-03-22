from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def removeDuplicates(self, nums):
        p1 = p2 = 1
        pre = -10**5
        while (p2 < len(nums)):
            if nums[p2] == nums[p1 - 1] and nums[p2] == pre:
                # 和前面两个都一样，不忍了，p2向前走，直至替换该货
                p2 += 1
            elif nums[p2] == nums[p1 - 1]:
                # 只是和前一个相同，还有一次机会，但是要先用pre记录
                pre = nums[p2]
                nums[p1] = nums[p2]
                p1 += 1
                p2 += 1
            else:
                nums[p1] = nums[p2]
                p1 += 1
                p2 += 1
        return p1

    def main(self):
        nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        nums = [1, 1, 1, 2, 2, 3]
        nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        self.removeDuplicates(nums)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
