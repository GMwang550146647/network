from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def exchange(self, nums):
        def find_next(start, moder=1):
            while start < len(nums):
                if nums[start] % 2 == moder:
                    return start
                start += 1
            return False
        odd_index = find_next(0, 1)
        even_index = find_next(0, 0)
        while odd_index is not  False:
            if odd_index > even_index:
                nums[odd_index], nums[even_index] = nums[even_index], nums[odd_index]
                even_index = find_next(even_index + 1, 0)
            odd_index = find_next(odd_index + 1, 1)
        return nums

    def main(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        self.exchange(nums)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
