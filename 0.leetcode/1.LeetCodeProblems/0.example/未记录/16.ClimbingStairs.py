'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''
import time
class Solution():
    def __init__(self):
        self.step=30
        self.result=[]
    '''我的方法:超级慢，因为不需要记录'''
    def myFun(self,goal,preList=[],presum=0):
        for i in range(1,3):
            preListi=preList.copy()
            preListi.append(i)
            presumi=presum+i
            if presumi>goal:
                pass
            elif presumi==goal:
                self.result.append(preListi)
            else:
                self.myFun(goal,preListi,presumi)
    '''我的方法：改进版本'''
    '''答案方法1'''
    def climbStairs(self,n):
        if n<=1:
            return 1
        pre,ppre=1,1
        for i in range(2,n+1): #原理是第n步肯定是从n-1或者n-2来的，所以等于n-1和n-2的和，其实就是斐波拉契数列
            tmp=pre
            pre=ppre+pre
            ppre=tmp
        return pre
    def fib(self,n):
        if n<=1:
            return 1
        List=[1,1]
        for i in range(n-1):
            List.append(List[i]+List[i+1])
        return List[-1]

    def testTime(self,fun,step):
        # 计时
        start = time.process_time()
        result = fun(step)
        elapsed = (time.process_time() - start)
        print(fun.__name__,":")
        print("Time used:", elapsed)
        print('result:', result)
    def main(self):
        # self.testTime(self.myFun,self.step)
        self.testTime(self.fib,self.step)
        print(len(self.result))
        self.testTime(self.climbStairs,self.step)
SL=Solution()
SL.main()