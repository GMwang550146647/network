from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def minmumNumberOfHost(self , n , startEnd ):
        starts=sorted(item[0] for item in startEnd)
        ends=sorted(item[1] for item in startEnd)
        speakers=0
        end=0
        for i in range(len(ends)):
            if starts[i]>= ends[end]:
                end+=1
            else:
                speakers+=1
        return speakers

    def main(self):
        n,startEnd=2,[[1,2],[3,4]]
        self.minmumNumberOfHost(n,startEnd)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
