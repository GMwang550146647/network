import numpy as np
import time
from pandas import DataFrame
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
    def DPMC(self,left):
        arr=[[0]*(left),[0]*(left)]
        arr[0][0]=1
        arr[1][0]=-1
        for i in range(1,left):
            bestPrei=-1
            Mincoins=100000000
            for j in [c for c in self.coins if i+1>=c]:
                temptPrei=i-j
                if arr[0][temptPrei]<Mincoins:
                    Mincoins=arr[0][temptPrei]
                    bestPrei=temptPrei
            arr[0][i]=Mincoins+1
            arr[1][i]=bestPrei
        bestChange=[]
        left=left-1
        while(left!=-1):
            preindex=arr[1][left]
            bestChange.append(left-preindex)
            left=preindex
        return len(bestChange),bestChange
    def testTime(self,fun,left):
        # 计时
        start = time.process_time()
        result = fun(left)
        elapsed = (time.process_time() - start)
        print(fun.__name__,":")
        print("Time used:", elapsed)
        print('result:', result)
    def main(self):
        timeCost=self.testTime(self.DPMC,self.left)



gmc=getMinCoins(1000,[25,10,5,1])
gmc.main()