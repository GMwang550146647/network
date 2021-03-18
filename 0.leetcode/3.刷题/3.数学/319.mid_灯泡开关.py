from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def bulbSwitch(self, n):
        return int(n ** 0.5)

    def main(self):
        nums = 17
        self.bulbSwitch(nums)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
