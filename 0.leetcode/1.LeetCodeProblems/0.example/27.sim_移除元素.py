"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

 

示例 1:

给定 nums = [3,2,2,3], val = 3,

函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,1,2,2,3,0,4,2], val = 2,

函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

注意这五个元素可为任意顺序。

你不需要考虑数组中超出新长度后面的元素。
"""


import time
class Solution():
    def __init__(self):
        pass
    '''我的方法'''
    def myFun(self, nums, val):
        cur_index=0
        cur_fill_index=0
        while(cur_index<len(nums)):
            if nums[cur_index]!=val:
                nums[cur_fill_index] = nums[cur_index]
                cur_fill_index += 1
            cur_index+=1

        return cur_fill_index,nums[:cur_fill_index]
    '''答案方法1'''

    def testTime(self,fun,args):
        # 计时
        start = time.process_time()
        result = fun(*args)
        elapsed = (time.process_time() - start)
        print(fun.__name__,":")
        print("Time used:", elapsed)
        print('result:', result)
    def main(self):
        nums = [0,1,2,2,3,0,4,2]
        val = 2
        self.testTime(self.myFun,args=(nums,val,))
if __name__=='__main__':
    SL=Solution()
    SL.main()
