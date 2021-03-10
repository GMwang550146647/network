"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−2^31 ,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
import time


class Solution():
    def __init__(self):
        pass

    '''我的方法'''

    def myFun(self, num):
        # 32位最大是4294967296
        sign=1 if num>=0 else -1
        num=num*sign
        result=0
        while(num>0):
            result=result*10+num%10
            num=num//10
        return sign * result if result <= 2 ** 31 else 0

    '''答案方法1'''

    def SA(self, num):
        sign = 1 if num >= 0 else -1
        num = num if num >= 0 else -num
        result = 0
        while (num > 0):
            result = result * 10 + num % 10
            num = num // 10
        return sign * result if result <= 2 ** 31 else 0

    def testTime(self, fun, args):
        # 计时
        start = time.process_time()
        result = fun(*args)
        elapsed = (time.process_time() - start)
        print(fun.__name__, ":")
        print("Time used:", elapsed)
        print('result:', result)

    def main(self):
        num = -294987498

        # self.testTime(self.myFun, args=(num,))
        # time.sleep(1)
        self.testTime(self.SA, args=(num,))
        self.testTime(self.SA, args=(num,))
        self.testTime(self.SA, args=(num,))



if __name__ == '__main__':
    SL = Solution()
    SL.main()
