'''
Implement int sqrt(int x) .

Compute and return the square root of x , where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2

Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
  the decimal part is truncated, 2 is returned.

'''
import time
import numpy as np
class Solution():
    def __init__(self):
        self.num=192357134

    '''我的方法'''
    def myFun(self,num,precision=10**-9):
        #找出最靠近的那个先
        min=0
        max=num
        mid=(min+max)/2
        while(abs(mid**2-num)>=precision):
            mid=(min+max)/2
            if mid**2>num:
                max=mid
            else:
                min=mid
        return mid


    '''答案方法1:感觉没我的好，因为精度不够'''
    def mySqrt(self,num,precision=10**-9):
        lo=0
        hi=num
        while lo<=hi:
            mid=(hi+lo)/2
            v=mid**2
            if v<num:
                lo=mid+1
            elif v>num:
                hi=mid-1
            else:
                return mid
        return hi
    def testTime(self,fun,num):
        # 计时
        start = time.process_time()
        result = fun(num)
        elapsed = (time.process_time() - start)
        print(fun.__name__,":")
        print("Time used:", elapsed)
        print('result:', result)
    def main(self):
        self.testTime(self.myFun,self.num)
        self.testTime(self.mySqrt,self.num)
        self.testTime(np.sqrt,self.num)
SL=Solution()
SL.main()