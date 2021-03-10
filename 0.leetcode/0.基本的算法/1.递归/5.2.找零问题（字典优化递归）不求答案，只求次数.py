import numpy as np
import time
'''
问题描述：
有25，10，5，1的纸币，然后找找零50元，如何才能用最少的纸币数量
'''
'''1.未经优化的原始递归方法'''
class getMinCoins():
    def __init__(self,goal,coins=[1,5,10,25]):
        self.left=goal
        self.coins=coins

    #用递归计算会产生好多无效的计算过程，需要用字典记录或者使用字典优化
    def recMC(self,left,record={}):
        mincoins=left
        if left in self.coins:
            record[left]=1
            return 1
        elif record.get(left,-1)>0:
            return record[left]
        else:
            for i in [c for c in self.coins if c<=left]:
                numcoins=1+self.recMC(left-i,record)
                if numcoins<mincoins:
                    mincoins=numcoins
                    record[left]=mincoins
        return mincoins
    def testTime(self,fun,left):
        # 计时
        start = time.process_time()
        result = fun(left)
        elapsed = (time.process_time() - start)
        print(fun.__name__,":")
        print("Time used:", elapsed)
        print('result:', result)
    def main(self):
        timeCost=self.testTime(self.recMC,self.left)



gmc=getMinCoins(1000,[25,10,5,1])
gmc.main()