from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def subsets(self, nums):
        """
        循环解决问题:
            迭代：（每一次都是在前面的情况下 + 下一个元素）+前面的情况
        """
        sets = [[]]
        for i in range(len(nums)):
            new_set = [item + [nums[i]] for item in sets]
            sets.extend(new_set)
        return sets

    @test_time
    def subsets_recur1(self, nums):
        '''
        每一层代表每个数 选与不选
        '''

        def backtrack(cur_path, nums, i):
            if i >= len(nums):
                solutions.append(cur_path.copy())
            else:
                backtrack(cur_path, nums, i + 1)
                cur_path.append(nums[i])
                backtrack(cur_path, nums, i + 1)
                cur_path.pop(-1)

        solutions = []
        backtrack([], nums, 0)
        return solutions

    @test_time
    def subsets_recur2(self, nums):
        '''
        每一层代表以某个数开头的组合(每一个节点都算，不只是叶节点)
        '''

        def backtrack(cur_path, nums, start):
            solutions.append(cur_path.copy())
            for i in range(start, len(nums)):
                cur_path.append(nums[i])
                backtrack(cur_path, nums, i + 1)
                cur_path.pop(-1)

        solutions = []
        backtrack([], nums, 0)
        return solutions

    def main(self):
        nums = [1, 2, 3]
        self.subsets(nums)
        self.subsets_recur1(nums)
        self.subsets_recur2(nums)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
