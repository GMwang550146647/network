from fundamentals.test_time import test_time
import numpy as np

class Solution():
    def __init__(self):
        pass

    @test_time
    def select(self,seq,k):
        def partition(seq):
            pi = seq[0]
            lo = [x for x in seq[1:] if x <= pi]
            hi = [x for x in seq[1:] if x > pi]
            return lo,pi,hi
        def solve(seq,k):
            lo,pi,hi=partition(seq)
            m=len(lo)+1
            if m==k:
                return pi
            elif m<k:
                return solve(hi,k-m)
            else:
                return solve(lo,k)
        return solve(seq,k)


    def main(self):
        k=2
        arr=np.random.randn(3)
        print(arr)
        # arr=list(range(100))
        self.select(arr,k)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
