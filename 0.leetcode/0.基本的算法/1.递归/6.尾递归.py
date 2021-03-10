'''
warning:由于python不支持尾递归，所以尾递归反而会慢会栈溢出
定义与区别：
非尾递归，下一个函数结束以后此函数还有后续，所以必须保存本身的环境以供处理返回值。
尾递归，进入下一个函数不再需要上一个函数的环境了，得出结果以后直接返回。

'''

'''1.普通递归，需要保护现场'''
def factDG(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factDG(n-1)

'''2.尾递归，不需要保护现场，只管返回就行'''
def factWDG(n,temptfn=1):
    if n==0 or n==1:
        return 1*temptfn
    else:
        return factWDG(n-1,n*temptfn)

import time
class Solution():
    def __init__(self):
        self.num=19235713

    '''1.普通递归'''
    def factDG(self,n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factDG(n - 1)
    def sumDG(self,n):
        if n==0:
            return 0
        else:
            return n+self.sumDG(n-1)
    '''2.尾递归'''
    def factWDG(self,n, temptfn=1):
        if n == 0 or n == 1:
            return 1 * temptfn
        else:
            return self.factWDG(n - 1, n * temptfn)
    def sumWDG(self,n,temptsum=0):
        if n==0:
            return temptsum
        else:
            return self.sumWDG(n-1,temptsum+n)
    def testTime(self,fun,n):
        # 计时
        start = time.process_time()
        result = fun(n)
        elapsed = (time.process_time() - start)
        print(fun.__name__,":")
        print("Time used:", elapsed)
        print('result:', result)
    def main(self):
        n=995
        self.testTime(self.factWDG, n)
        self.testTime(self.factDG,n)
        self.testTime(self.sumWDG,n)
        self.testTime(self.sumDG,n)


SL=Solution()
SL.main()