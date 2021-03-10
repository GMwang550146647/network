import numpy as np
import time
from pandas import DataFrame
'''
问题描述：
背包一定容量，装价值总和尽量大的物品，但是每个物品占一定容量
(不一定要等于总容量）
'''
'''
解决方法描述：
1.对每一个value ，对所有的可能的前置重量范围j搜索 其增量k

'''

class getMaxValue():
    def __init__(self,volumn):
        # self.itemValueWeight={1:[2,3],2:[3,4],3:[4,8],4:[5,8],5:[9,10]}
        self.valueWeight=[[3,4,8,8,10],[2,3,4,5,9]]
        self.volumn=volumn
    #用递归计算会产生好多无效的计算过程，需要用字典记录或者使用字典优化
    def DP(self,volumn):
        arr=[list(range(volumn+1)),[[]]*(volumn+1)]
        minweight=min(self.valueWeight[1])
        maxweight=max(self.valueWeight[1])
        arr[0][minweight]=self.valueWeight[0][np.argmin(self.valueWeight[1])]
        arr[1][minweight]=[np.argmin(self.valueWeight[1])+1]
        for i in range(minweight+1,volumn+1):  #i代表当前的value=i情况下最好的组合
            maxValue=-1
            maxindexj=-1
            maxindexk=-1
            minj=max(minweight,i-maxweight)
            for j in range(minj,i):         #j代表当前i的前一个节点要选哪个
                for k in range(len(self.valueWeight[1])):
                    if j+self.valueWeight[1][k]<=i:  #k代表在j的情况下，选哪个k
                        totalvalue=arr[0][j]+self.valueWeight[0][k]
                    else:
                        totalvalue=arr[0][j]
                    if totalvalue> maxValue:
                        maxindexj=j
                        maxindexk=k
                        maxValue=totalvalue
            arr[0][i]=maxValue
            maxlist=arr[1][maxindexj].copy()
            maxlist.append(maxindexk+1)
            arr[1][i]=maxlist
        return DataFrame(arr)
    def testTime(self,fun,volumn):
        # 计时
        start = time.process_time()
        result = fun(volumn)
        elapsed = (time.process_time() - start)
        print(fun.__name__,":")
        print("Time used:", elapsed)
        print('result:\n', result)
    def main(self):
        timeCost=self.testTime(self.DP,self.volumn)



gmc=getMaxValue(20)
gmc.main()