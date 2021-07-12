from fundamentals.test_time import test_time
import functools


class Solution():
    def __init__(self):
        pass

    @test_time
    def singleNumbers(self, nums):
        x, y, n, m = 0, 0, 0, 1
        for num in nums:  # 1. 遍历异或
            n ^= num
        while n & m == 0:  # 2. 循环左移，计算 m
            m <<= 1
        for num in nums:  # 3. 遍历 nums 分组
            if num & m:
                x ^= num  # 4. 当 num & m != 0
            else:
                y ^= num  # 4. 当 num & m == 0
        return x, y  # 5. 返回出现一次的数字

    @test_time
    def singleNumbers1(self, nums):
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
        nums = [1, 2, 10, 4, 1, 4, 3, 3]
        self.singleNumbers(nums)
        self.singleNumbers1(nums)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
