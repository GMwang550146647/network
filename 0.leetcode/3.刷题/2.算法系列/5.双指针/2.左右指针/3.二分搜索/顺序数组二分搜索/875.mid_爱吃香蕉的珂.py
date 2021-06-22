from fundamentals.test_time import test_time

import math


class Solution():
    def __init__(self):
        pass

    @test_time
    def minEatingSpeed(self, piles, h):
        '''自己写的：相当于二分搜索左边界！'''

        def get_hour(piles, speed):
            count = 0
            for pile_i in piles:
                count += math.ceil(pile_i / speed)
            return count

        left = 1
        right = 10 ** 9
        while left < right:
            mid = (left + right) // 2
            demand_time = get_hour(piles, mid)
            if demand_time < h:
                right = mid
            elif demand_time > h:
                left = mid + 1
            else:
                right = mid
        return right

    @test_time
    def minEatingSpeed2(self, piles, h):
        '''这个辅助函数比较容易理解'''

        def canFinish(piles, speed, h):
            count = 0
            for pile_i in piles:
                count += math.ceil(pile_i / speed)
            return count <= h

        left = 1
        right = 10 ** 9
        while left < right:
            mid = (left + right) // 2
            finish = canFinish(piles, mid, h)
            if finish:
                right = mid
            else:
                left = mid + 1
        return right

    def main(self):
        piles = [30, 11, 23, 4, 20]
        H = 5
        piles = [30, 11, 23, 4, 20]
        H = 6
        self.minEatingSpeed(piles, H)
        self.minEatingSpeed2(piles, H)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
