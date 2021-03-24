from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def findNthDigit(self, n):
        divs=[10]
        i=1
        while divs[-1]<2**21:
            divs.append(9*10**i*)

    def main(self):
        n=100
        self.findNthDigit(n)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
