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
    def DPMC(self,left):
        arr=[list(range(1,left+1)),[[]]*left]
        arr[0][0]=1
        arr[1][0]=[1]
        for i in range(left):
            bestPrei=-1
            Mincoins=100000000
            for j in [c for c in self.coins if i+1>=c]:
                temptPrei=i-j
                if len(arr[1][temptPrei])<Mincoins:
                    Mincoins=len(arr[1][temptPrei])
                    bestPrei=temptPrei
            temptlist=list(arr[1][bestPrei])
            temptlist.append(i-bestPrei)
            arr[1][i]=temptlist
        return arr[1][-1]
    def testTime(self,fun,left):
        # 计时
        start = time.process_time()
        result = fun(left)
        elapsed = (time.process_time() - start)
        print(fun.__name__,":")
        print("Time used:", elapsed)
        print('result:', result,"\nlen:",len(result))
    def main(self):
        timeCost=self.testTime(self.DPMC,self.left)



gmc=getMinCoins(1000,[25,10,5,1])
gmc.main()