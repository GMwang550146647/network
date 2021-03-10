'''
Given an integer array nums , find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:

If you have figured out the O( n ) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''
import time
class Solution():
    def __init__(self):
        self.arr=[-2,-1,-3,4,-5,6,-4,3,2,-9]

    '''我的方法:理解错误，解法错了'''
    def myFun(self):
        maxsum=self.arr[0] #记录最大的数
        temptSum=self.arr[0]#记录加到现时最大的数
        maxIndex=-1 #记录之前加到最大的数的index
        for i in range(1,len(self.arr)):
            temptSum+=self.arr[i]
            if temptSum>maxsum:
                maxIndex=i
                maxsum=temptSum
        return (maxIndex,maxsum)
    '''答案方法1'''
    def maxSubArray(self):
        if len(self.arr)==0:
            return 0
        preSum=maxSum=self.arr[0]
        for i in range(1,len(self.arr)):
            preSum=max(preSum+self.arr[i],self.arr[i])
            maxSum=max(maxSum,preSum)
        return maxSum
    def testTime(self,fun):
        # 计时
        start = time.process_time()
        result = fun()
        elapsed = (time.process_time() - start)
        print(fun.__name__,":")
        print("Time used:", elapsed)
        print('result:', result)
    def main(self):
        self.testTime(self.myFun)
        self.testTime(self.maxSubArray)
SL=Solution()
SL.main()