'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2

Example 2:

Input: [1,3,5,6], 2
Output: 1

Example 3:

Input: [1,3,5,6], 7
Output: 4

Example 4:

Input: [1,3,5,6], 0
Output: 0
'''
import time
class Solution():
    def __init__(self):
        self.arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
        self.num1=10
        self.num2=10.5

    '''我的方法:不太好'''
    def myFun(self,num):
        length=len(self.arr)
        max=length
        min=0
        while(num!=self.arr[int((max+min)/2)] and min!=max):
            if num>self.arr[int((max+min)/2)]:
                min=int((max+min)/2)+1
            else:
                max=int((max+min)/2)
        index=int((max+min)/2)
        return index

    '''答案方法1'''
    def searchInsert(self,num):
        lo=0
        hi=len(self.arr)
        while lo<hi:
            mid=int((lo+hi)/2)
            if self.arr[mid]>num:
                hi=mid
            elif self.arr[mid]<num:
                lo=mid+1
            else:
                return mid
        return lo

    def testTime(self,fun,num):
        # 计时
        start = time.process_time()
        result = fun(num)
        elapsed = (time.process_time() - start)
        print(fun.__name__,":")
        print("Time used:", elapsed)
        print('result:', result)
    def main(self):
        self.testTime(self.myFun, self.num1)
        self.testTime(self.myFun,self.num2)
        self.testTime(self.searchInsert, self.num1)
        self.testTime(self.searchInsert, self.num2)
SL=Solution()
SL.main()