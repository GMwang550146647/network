"""
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

 

示例 1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。

"""

import time
class Solution():
    def __init__(self):
        pass
    '''我的方法'''
    def myFun(self,nums):
        count = 1
        p1 = 0
        p2 = 1
        length = len(nums)
        while (p2 < length):
            if nums[p1] == nums[p2]:
                p2 += 1
            else:
                p1+=1
                nums[p1] = nums[p2]
                p2 += 1
                count += 1
        print(nums[:count])
        return count
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
        s=[1,1,2]
        self.testTime(self.myFun,args=(s,))
if __name__=='__main__':
    SL=Solution()
    SL.main()
