from fundamentals.tree import TreeNode, Tree
import time


class Solution():
    def __init__(self):
        pass

    '''我的方法'''

    def permute(self, nums):
        """
        RECUR  pop insert heavy load (核心：重复的就不分枝了，但是要时刻知道剩下什么数字)
        """

        def permuteAssist(nums, tempt_list):
            if len(nums) == 0:
                all_rank.append(tempt_list.copy())
            for node_i in list(set(nums)):
                index = nums.index(node_i)
                tempt_list.append(nums.pop(index))
                permuteAssist(nums, tempt_list)
                nums.insert(index, tempt_list.pop(-1))

        all_rank = []
        permuteAssist(nums, [])
        return all_rank

    def peremute_answer(self, nums):
        """
        方法是一样的，但是使用了一个新列表记录是否已经使用了 各个数，以及每次分支不重复！
        """
        def backtrack(sol, nums, check):
            if len(sol) == len(nums):
                self.res.append(sol)
                return

            for i in range(len(nums)):
                if check[i] == 1:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:
                    continue
                check[i] = 1
                backtrack(sol + [nums[i]], nums, check)
                check[i] = 0

        nums.sort()
        self.res = []
        check = [0 for i in range(len(nums))]

        backtrack([], nums, check)
        return self.res

    def testTime(self, fun, args, test_times=10):
        # 计时
        start = time.process_time()
        for i in range(test_times):
            result = fun(*args)
        elapsed = (time.process_time() - start)
        print(fun.__name__, ":")
        print("Time used:", elapsed)
        print("Result:", result)

    def main(self):
        n = [1, 2, 1]
        self.testTime(self.permute, args=(n,))
        self.testTime(self.peremute_answer, args=(n,))


if __name__ == '__main__':
    SL = Solution()
    SL.main()
