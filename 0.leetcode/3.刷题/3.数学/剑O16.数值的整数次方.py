from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def myPow_recur(self, x: float, n: int) -> float:
        flag = True if n >= 0 else False
        n = abs(n)

        def solve(cur, n):
            if n == 0:
                return 1
            else:
                if n % 2 == 1:
                    return cur * solve(cur * cur, n // 2)
                else:
                    return solve(cur * cur, n // 2)

        t = solve(x, n)
        return t if flag else 1 / t


    def main(self):
        x = 2.00000
        n = -2000000000
        self.myPow_recur(x, n)
        self.myPow(x, n)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
