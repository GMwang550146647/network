from fundamentals.test_time import test_time
'''
1, 2, 3, 4,   5, 6,    8,    9, 10, 12    15  16      18     20    24     25   27    30
   2  3  2x2  5  2x3 2x2x2 3x3 2x5 2x2x3 3x5 2x2x2x2 2x3x3 2x2x5 2x2x2x3 5x5  3x3x3  2x3x5
'''

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
