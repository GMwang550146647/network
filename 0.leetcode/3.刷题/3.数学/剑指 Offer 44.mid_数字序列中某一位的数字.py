from fundamentals.test_time import test_time


def create():
    s = ''
    for i in range(100000):
        s += str(i)
    return s


class Solution():
    def __init__(self):
        self.divs = [0, 10]
        i = 1
        while i < 11:
            self.divs.append((i + 1) * 9 * 10 ** i + self.divs[-1])
            i += 1

    @test_time
    def findNthDigit(self, n):
        if n<=9:
            return n
        i = 0
        while n > self.divs[i]:
            i += 1
        tempt = (n - self.divs[i - 1])
        ith = tempt // i + 10 ** (i - 1)
        jth = tempt % i
        print(i, "该数字是：", ith, '第{}位置'.format(jth))

        return int(str(ith)[jth])

    def main(self):
        s = create()
        n = 9999
        res = self.findNthDigit(n)
        print('answer:', s[n])


if __name__ == '__main__':
    SL = Solution()
    SL.main()
