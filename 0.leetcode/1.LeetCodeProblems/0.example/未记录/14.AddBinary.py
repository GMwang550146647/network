'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0 .

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101
'''
import time
class Solution():
    def __init__(self):
        self.num1='101'
        self.num2='101'
    '''我的方法'''
    def myFun(self):
        len1=len(self.num1)
        len2=len(self.num2)
        longone,shortone=(self.num1,self.num2) if len1>=len2 else (self.num2,self.num1)
        biglen,shortlen=(len1,len2) if len1>=len2 else (len2,len1)
        sum=0
        bitadd=0
        for i in range(biglen):
            if i>=shortlen:
                bitsum = int(longone[-i - 1])  + bitadd
            else:
                bitsum=int(longone[-i-1])+int(shortone[-i-1])+bitadd
            if bitsum>1:
                bitsum-=2
                bitadd=1
            else:
                bitadd=0
            sum+=bitsum*10**i
            if bitadd == 1 and i==biglen-1:
                sum +=bitadd*10**biglen

        return str(sum)


    '''答案方法1'''
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
        self.addBinary()

SL=Solution()
SL.main()