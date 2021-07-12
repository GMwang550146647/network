from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def ysf(self , n , m ):
        res=list(range(1,n+1))
        i=0
        for j in range(n-1):
            i=(i+m-1)%(n-j)
            del res[i]
        return res[0]

    def main(self):
        self.ysf(1000,9001)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
