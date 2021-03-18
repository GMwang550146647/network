
from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    '''我的方法'''
    @test_time
    def permute_recur1(self, nums):
        """
        RECUR  pop insert heavy load
            每次都判断是否在之前的集合里面了
        """

        def permuteAssist(nums, tempt_list):
            if len(nums) == 0:
                all_rank.append(tempt_list.copy())
            else:
                for node_i in nums:
                    index = nums.index(node_i)
                    tempt_list.append(nums.pop(index))
                    permuteAssist(nums, tempt_list)
                    nums.insert(index, tempt_list.pop(-1))

        all_rank = []
        permuteAssist(nums, [])
        return all_rank

    @test_time
    def permute_recur2(self,nums):
        """
        RECUR  pop insert heavy load
            用多一个变量记录剩下哪些值
        """
        def backtrack(cur_path,left_nums):
            if not left_nums:
                solutions.append(cur_path.copy())
            else:
                for i in range(len(left_nums)):
                    cur_val=left_nums.pop(i)
                    cur_path.append(cur_val)
                    backtrack(cur_path,left_nums)
                    cur_path.pop(-1)
                    left_nums.insert(i,cur_val)
        solutions=[]
        backtrack([],nums)
        return solutions


    def main(self):
        n = [1, 2, 3]
        self.permute_recur1(n)
        self.permute_recur2(n)




if __name__ == '__main__':
    SL = Solution()
    SL.main()
