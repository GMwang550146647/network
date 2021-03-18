from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def slidingPuzzle(self, nums):
        neighbours=[
            [1,3],[0,4,2],[1,5],[0,4],[3,1,5],[4,2]
        ]
        start=''
        target='123450'
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                start+=str(nums[i][j])
        visted={}


    def main(self):

        board = [[1, 2, 3], [4, 0, 5]]
        self.slidingPuzzle(board)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
