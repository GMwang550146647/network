from fundamentals.test_time import test_time

import functools


class Solution():
    def __init__(self):
        pass

    @test_time
    def singleNumber(self, nums):
        # 全部异或一次
        ret = functools.reduce(lambda x, y: x ^ y, nums)
        # 求出两数不相同的
        div = 1
        while div & ret == 0:
            div <<= 1
        a, b = 0, 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]

    def main(self):
        nums = [1, 2, 1, 3, 2, 5]
        self.singleNumber(nums)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
