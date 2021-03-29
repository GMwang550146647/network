from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def numTrees(self, n: int) -> int:
        def build_tree(n):
            if n<=1:
                return 1
            if n in record:
                return record[n]
            else:
                count=0
                for i in range(n):
                    count+=build_tree(i) *build_tree(n-i-1)
                record[n]=count
                return count
        record={}
        return build_tree(n)

    def main(self):
        nums = 4
        self.numTrees(nums)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
