from fundamentals.tree import TreeNode, Tree
import time


class Solution():
    def __init__(self):
        pass

    '''我的方法'''

    def permute(self, nums):
        """
        RECUR  pop insert heavy load
        """
        def permuteAssist(nums,tempt_list):
            if len(nums)==0:
                all_rank.append(tempt_list.copy())
            for node_i in nums:
                index=nums.index(node_i)
                tempt_list.append(nums.pop(index))
                permuteAssist(nums,tempt_list)
                nums.insert(index,tempt_list.pop(-1))
        all_rank=[]
        permuteAssist(nums,[])
        return all_rank

    def permute2(self, nums):
        """
        RECUR  pop insert heavy load
        """
        def permuteAssist(nums,tempt_list):
            if len(nums)==len(tempt_list):
                all_rank.append(tempt_list.copy())
            for node_i in nums:
                if node_i not in tempt_list:
                    tempt_list.append(node_i)
                    permuteAssist(nums,tempt_list)
                    tempt_list.pop(-1)
        all_rank=[]
        permuteAssist(nums,[])
        return all_rank
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
        n = [1,2,3]
        self.testTime(self.permute, args=(n,))
        self.testTime(self.permute2, args=(n,))


if __name__ == '__main__':
    SL = Solution()
    SL.main()
