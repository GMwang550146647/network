from fundamentals.test_time import test_time
from collections import defaultdict

class Solution():
    def __init__(self):
        pass

    @test_time
    def subsetsWithDup(self, nums):
        '''
        例如： [1,2,2,3,3,3]
            先构建一个数字 nums_count
            先考虑1(重复了1次):  [] <- [1] 选或不选  产生 ->  [] [1]
            再考虑2(重复了2次):  [] [1] <- [2] [2,2]选或不选  产生 ->  [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
            再考虑3(重复了3次):  ...
        '''
        result = [[]]
        nums_count = defaultdict(int)
        for numi in nums:
            nums_count[numi] += 1
        for numi, counti in nums_count.items():
            new_com = []
            candidates = [[numi] * (i + 1) for i in range(counti)]
            for candi in candidates:
                for curi in result:
                    new_com.append(curi + candi)
            result.extend(new_com)
        return result

    def main(self):
        nums = [1,2,2,3,3,3]
        self.subsetsWithDup(nums)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
