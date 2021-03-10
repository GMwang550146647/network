import numpy as np
import time
'''
问题描述：
有25，10，5，1的纸币，然后找找零50元，如何才能用最少的纸币数量
'''
'''1.未经优化的原始递归方法'''
class getMinCoins():
    def __init__(self,goal,coins=[25,10,5,1]):
        self.left=goal
        self.coins=coins
    #用递归计算会产生好多无效的计算过程，需要用字典记录或者使用字典优化
    def recMC(self,left,currentList=[],record={}):
        if record.get(left)!=None:
            return record[left]
        elif left in self.coins:
            goali=currentList.copy()
            goali.append(left)
            return goali
        bestList=[]
        minnum=1000
        for i in range(len(self.coins)):
            goali = currentList.copy()
            if left>self.coins[i]:
                goali.append(self.coins[i])
                temptlist=self.recMC(left-self.coins[i],goali,record)
                if len(temptlist)<minnum:
                    bestList=temptlist
                    minnum=len(bestList)
            record[left]=bestList.copy()
        return bestList.copy()

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
gmc=getMinCoins(1000)
gmc.main()

