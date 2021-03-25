from fundamentals.test_time import test_time
from functools import cmp_to_key


class Solution():
    def __init__(self):
        pass

    @test_time
    def minNumber(self, nums):
        def cmp(n1, n2):
            c1 = int(n1 + n2)
            c2 = int(n2 + n1)
            if c1 > c2:
                return 1
            else:
                return -1
        nums=[str(numi) for numi in nums]
        nums=sorted(nums,key=cmp_to_key(cmp))
        return ''.join(nums)

    def main(self):
        nums = [3, 30, 34, 5, 9,1,22,33,34,36,27,83,45,63]#"122273033334343645563839"
        # nums = [121,12,61212]
        self.minNumber(nums)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
