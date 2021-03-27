from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def func(self):
        pass

    def main(self):
        self.func()


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
