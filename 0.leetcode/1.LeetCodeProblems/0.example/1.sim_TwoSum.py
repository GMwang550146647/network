"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


import time
class Solution():
    def __init__(self):
        pass
    '''我的方法'''

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        record_dict = {}
        answer = []
        for i in range(len(nums)):
            print(record_dict)
            tempt = target - nums[i]
            if nums[i] in record_dict:
                answer = [i, record_dict[nums[i]]]
                break
            record_dict[tempt] = i
        return answer

    def testTime(self,fun,args):
        # 计时
        start = time.process_time()
        result = fun(*args)
        elapsed = (time.process_time() - start)
        print(fun.__name__,":")
        print("Time used:", elapsed)
        print('result:', result)
    def main(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.testTime(self.twoSum,args=(nums,target,))
if __name__=='__main__':
    SL=Solution()
    SL.main()
