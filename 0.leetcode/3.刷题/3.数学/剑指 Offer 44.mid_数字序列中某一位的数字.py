from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        self.divs = [0,10]
        i = 1
        while self.divs[-1] < 2 ** 21:
            self.divs.append((i + 1) * 9 * 10 ** i)
            i += 1
    @test_time
    def findNthDigit(self, n):
        len_n=len(str(n))


        return divs

    def main(self):
        n=100
        self.findNthDigit(n)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
