from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def merge(self, intervals):
        intervals=sorted(intervals)
        result=[]
        for i in range(len(intervals)):
            if not result or intervals[i][0]>result[-1][1]:
                result.append(intervals[i])
            else:
                result[-1][1]=max(result[-1][1],intervals[i][1])
        return result

    def main(self):
        intervals=[[10,30],[20,60],[80,100],[150,180]]
        self.merge(intervals)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
