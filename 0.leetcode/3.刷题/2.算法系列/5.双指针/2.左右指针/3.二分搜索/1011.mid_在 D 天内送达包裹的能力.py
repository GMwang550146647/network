from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def shipWithinDays(self, weights, D):
        '''
        二分搜索左边界
        '''
        def canShip(weights, D, vol):
            count = 0
            tempt_sum = 0
            for wi in weights:
                if tempt_sum + wi <= vol:
                    tempt_sum += wi
                else:
                    if wi > vol:
                        return False
                    tempt_sum = wi
                    count += 1
            if tempt_sum != 0:
                count += 1
            return True if count <= D else False
        left = 1
        right = 10 ** 6
        while (left < right):
            mid = (left + right) // 2
            if canShip(weights, D, mid):
                right = mid
            else:
                left = mid + 1
        return right

    def main(self):
        weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        D = 5
        self.shipWithinDays(weights, D)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
