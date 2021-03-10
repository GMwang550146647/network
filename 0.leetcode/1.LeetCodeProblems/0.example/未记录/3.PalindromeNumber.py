'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true

Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:

Coud you solve it without converting the integer to a string?
'''
import time
class Solution():
    def __init__(self):
        self.num=19235713455431753291

    '''我的方法'''
    def myFun(self,num):
        N = 0
        for i in range(100):
            if num // 10 ** i == 0:
                N = i
                break
        for i in range(int(N / 2)):
            forwardNum = num // 10 ** (N - 1 - i) % 10
            backwardNum = num // 10 ** i % 10
            if forwardNum != backwardNum:
                return False
        return True

    '''答案方法1'''
    '''原理：把数字翻转之后看看和原来的一样不'''
    def normalWay(self,x):
        z=x
        y=0
        while x>0:
            y=y*10+x%10
            x=x//10
        return z==y
    '''答案方法2'''
    def fastWay(self,x):
        if x<0 or (x!=0 and x%10==0):
            return False
        half=0
        while x>half:
            half=half*10+x%10
            x=x//10
        return x==half or half/10==x
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
        self.testTime(self.normalWay,self.num)
        self.testTime(self.fastWay,self.num)
SL=Solution()
SL.main()