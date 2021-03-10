import numpy as np
import time
'''
问题描述：
有25，10，5，1的纸币，然后找找零50元，如何才能用最少的纸币数量
'''
'''1.未经优化的原始递归方法'''
class getMinCoins():
    def __init__(self,goal,coins=[1, 5, 10, 25]):
        self.left=goal
        self.coins=coins
        self.goalList=[]
    #用递归计算会产生好多无效的计算过程，需要用字典记录或者使用字典优化
    def recMC(self,left,currentList=[]):
        for i in range(len(self.coins)):
            goali = currentList.copy()
            if left==self.coins[i]:
                goali.append(self.coins[i])
                self.goalList.append(goali)
            if left>self.coins[i]:
                goali.append(self.coins[i])
                self.recMC(left-self.coins[i],goali)
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
        target=self.goalList[np.argmin(np.array([len(arr) for arr in self.goalList]))]
        print("best:",target)
gmc=getMinCoins(39,[25,10,5,1])
gmc.main()

