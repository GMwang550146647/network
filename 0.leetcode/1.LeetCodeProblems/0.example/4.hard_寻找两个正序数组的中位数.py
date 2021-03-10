"""
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

 

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
"""
import time
class Solution():
    def __init__(self):
        self.num=19235713

    '''我的方法'''


    def myFun(self, nums1, nums2):
        def get_element_k(k):
            pass
        len_num1=len(nums1)
        len_num2=len(nums2)
        if len_num1==0:
            return nums2[len_num2//2] if len_num2%2==1 else (nums2[len_num2//2]+nums2[len_num2//2-1])/2.0
        if len_num2==0:
            return nums1[len_num1//2] if len_num1%2==1 else (nums1[len_num1//2]+nums1[len_num1//2-1])/2.0
        total_length=len_num2+len_num1
        if total_length%2==1:
            return get_element_k((total_length+1)//2)
        else:
            return (get_element_k(total_length//2) +get_element_k(total_length//2+1))/2.0

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
        nums1=[1,2,3,4]
        nums2=[]
        self.testTime(self.myFun,args=(nums1,nums2,))
        self.testTime(self.myFun, args=(nums1, nums2,))

if __name__=='__main__':
    SL=Solution()
    SL.main()