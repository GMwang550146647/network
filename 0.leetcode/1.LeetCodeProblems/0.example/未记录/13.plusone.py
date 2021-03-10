'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''
import time
class Solution():
    def __init__(self):
        self.num=[1,9,9,4,9,9,9,9,9,9,9,9,9,9,9]

    '''我的方法'''
    def myFun(self):
        num=self.num.copy()
        if num[-1]<=8:
            num[-1]+=1
            return num
        else:
            i=len(num)-1
            while(num[i]==9 and i>=0):
                num[i]=0
                i-=1
            if i==-1:
                num.insert(0,1)
            else:
                num[i]+=1
        return num
    '''答案方法1'''
    def plusOne(self):
        digits=self.num.copy()
        carry=1
        for i in reversed(range(len(self.num))):
            digit=(digits[i]+carry)%10
            carry=1 if digit<digits[i] else 0
            digits[i]=digit
        if carry==1:
            return[1]+digits
        return digits
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
        self.testTime(self.plusOne)
SL=Solution()
SL.main()