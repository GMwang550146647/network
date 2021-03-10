import numpy as np
'''
每一次循环都查找可行解最少的数字，然后把该数字填满
'''
from pandas import DataFrame
import pandas
import itertools
import pandas as pd
class shudu():
    def __init__(self):
        self.problem1=np.array([
            [8, 7, -1,    -1, 4, 1,      -1, 2, -1],
            [-1, -1, 3,    -1, -1, 5,     4, -1, 7],
            [-1, 2, -1,    -1, -1, 3,     -1, 1, -1],

            [-1, -1, 7,      -1, 2, 8,     6, -1, 1],
            [-1, -1, 1,    7, -1, -1,     8, -1, -1],
            [2, -1, 6,    1, -1, -1,     3, -1, -1],

            [-1, 1, -1,    8, -1, -1,     -1, 9, -1],
            [7, -1, 8,     4, -1, -1,     1, -1, -1],
            [-1, 4, -1,    5, 1, -1,     -1, 8, 6],
        ])
        self.problem2=np.array([
            [5, 9, -1,     -1, -1, -1,     -1, -1, 1, ],
            [-1, 4, -1,     -1, 5, -1,     -1, -1, -1, ],
            [-1, -1, -1,     4, 7, -1,     6, -1, -1, ],

            [-1, -1, 3,     -1, -1, -1,     -1, -1, -1, ],
            [-1, 6, -1,     -1, -1, -1,     -1, -1, -1, ],
            [-1, -1, -1,     -1, -1, -1,     2, -1, -1, ],

            [-1, -1, 1,     -1, 4, 2,     -1, -1, -1, ],
            [-1, -1, -1,     -1, 8, -1,     -1, 5, -1, ],
            [6, -1, -1,     -1, -1, -1,     -1, 8, 7, ],
        ])
        self.problem=np.array([
            [4, -1, -1,     -1, -1, 8,     -1, 5, -1],
            [-1, -1, -1,     -1, 7, -1,     2, 9, -1],
            [-1, -1, -1,     -1, -1, -1,     -1, 3, -1],

            [-1, -1, -1,     -1, -1, 4,     -1, -1, 8],
            [-1, 6, -1,     -1, 3, -1,     -1, 7, -1],
            [1, -1, -1,     5, -1, -1,     -1, -1, -1],

            [-1, 9, -1,     -1, -1, -1,     -1, -1, -1],
            [-1, 7, 3,     -1, 6, -1,     -1, -1, -1],
            [-1, 4, -1,     2, -1, -1,     -1, -1, 5],
        ])
        self.sortedNum=[]
    '''一开始要来排序的，将出现的数字从频数多到少排序（现在不用）'''
    def countAll(self):
        dictNnum={}
        for i in range(1,10):
            dictNnum[i]=(self.problem==i).sum()
        sortedNum=sorted(dictNnum.items(),key=lambda a:a[1],reverse=True)
        sortedNum=[item[0] for item in sortedNum]
        self.sortedNum=sortedNum

    '''对现时的temptProblem(注意，要复制矩阵）对某个num进行可行位置判断，返回该数字所有可能的填写位置（list）'''
    def findSuitablePlace(self,num,temptProblem):
        suitablePlace=[]
        for row in range(9):
            for column in range(9):
                if temptProblem[row,column]==-1:
                    #对于空位检查同行同列的有没有相同
                    if (temptProblem[row,:]==num).sum()!=0: #行
                        continue
                    if (temptProblem[:,column]==num).sum()!=0: #列
                        continue
                    #对于空位检查同一个九宫格里面的
                    bigSquarePosi=int(row/3)
                    bigSquarePosj=int(column/3)
                    flag=1 #1表示可行，如果九宫格出现同样的说明不可行
                    for i in range(bigSquarePosi*3,(bigSquarePosi+1)*3):
                        for j in range(bigSquarePosj*3,(bigSquarePosj+1)*3):
                            if temptProblem[i,j]==num:
                                flag=-1
                    if flag==1:
                        suitablePlace.append([row,column])
        return suitablePlace.copy()
    '''对于某个数字判断该矩阵是否符合游戏规则，被用于findSuitableGroupPosition函数中，因为该函数要遍历该数字的各种填写方式（填写方式不一定合法）'''
    def judgePresentProblem(self,num,presentProblem):
        for row in range(9):
            for column in range(9):
                if presentProblem[row,column]==num:
                    #检查行列是否有相同的
                    if (presentProblem[row,:]==num).sum()>1: #行
                        return -1
                    if (presentProblem[:,column]==num).sum()>1: #列
                        return -1
                    # 对于空位检查同一个九宫格里面的
                    bigSquarePosi = int(row / 3)
                    bigSquarePosj = int(column / 3)
                    for i in range(bigSquarePosi * 3, (bigSquarePosi + 1) * 3):
                        for j in range(bigSquarePosj * 3, (bigSquarePosj + 1) * 3):
                            if presentProblem[i, j] == num:
                                if i==row and j==column:
                                    continue
                                else:
                                    return -1
        return 1
    '''对某个数字，对现有的问题找到所有可能的填写组合，被用于solveSdNum函数中'''
    def findSuitableGroupPosition(self,fillNum,presentProblem):
        numCount=(presentProblem==fillNum).sum() #该数字在problem中填写了几个
        print('numCount:',numCount)
        CountToFill=9-numCount  #该数字还需要填的个数
        suitablePlaces=self.findSuitablePlace(fillNum,presentProblem) #找到该数字所有的可填位置
        resultSuitableSet=[]

        #不够位置放，说明无解，返回-1
        if CountToFill>len(suitablePlaces):
            print("failure")
            return -1
        print(suitablePlaces)
        print(CountToFill)
        #一个数就不需要组合了，直接返回
        if len(suitablePlaces)==CountToFill and CountToFill==1:
            temptProblem=presentProblem.copy()
            temptProblem[suitablePlaces[0][0],suitablePlaces[0][1]]=fillNum
            print(temptProblem)
            return [temptProblem]

        #组合数：在可行位置中找CountToFill个出来填写fillNum，其中resultSuitableSet是用来装所有可行的填写了的problem
        combinationsSet=itertools.combinations(np.arange(len(suitablePlaces)),CountToFill)
        for combinationi in combinationsSet:
            temptProblem=presentProblem.copy()
            for posindex in combinationi:
                temptProblem[suitablePlaces[posindex][0],suitablePlaces[posindex][1]]=fillNum
            if self.judgePresentProblem(fillNum,temptProblem)==1:
                resultSuitableSet.append(temptProblem)
        if len(resultSuitableSet)!=0:
            print("len(resultSuitableSet)",len(resultSuitableSet))
            return resultSuitableSet
        else:
            return -1
    '''对于每个数字的每种组合进行递归树建立'''
    def solveSdNum(self,leftNums,presentProblem):
        print("#####################################")
        print("left:",leftNums)
        print("present:\n",presentProblem)

        leftNumscpy=leftNums.copy()
        #退出条件：再没有可以填的空格（或者再没有可行解）
        if len(leftNums)!=0:
            # 找出可填空格最少的那个数字（这样就可以分出尽量少的枝节）
            minNum = 1000
            minSuitablePlace = []
            minIndex=-1
            deleteNum=[]
            for numi in leftNumscpy:
                temptsuit = self.findSuitablePlace(numi, presentProblem)
                if len(temptsuit)==0 and (presentProblem==numi).sum()!=9:
                    #失败了,有数字无解
                    print("#####FAIL######",numi)
                    # print(presentProblem)
                    return
                # elif len(temptsuit)==0 and (presentProblem==numi).sum()==9:
                #     deleteNum.append(numi)
                elif len(temptsuit) < minNum:
                    minSuitablePlace = temptsuit
                    minNum = len(temptsuit)
                    minIndex = numi
            # leftNumscpy = list(set(leftNumscpy) - set(deleteNum))
            print('numtofill',minIndex)

            #找出该数字填写的所有的可能组合
            leftProblem=self.findSuitableGroupPosition(minIndex,presentProblem.copy())
            #在leftNumscpy中删除该数字（因为已经填写了）
            for i in range(len(leftNums)):
                if leftNums[i]==minIndex:
                    leftNumscpy.pop(i)
            #对于每一种可能进行分叉（递归求解）
            if leftProblem!=-1:
                print("ways:",len(leftProblem))
                for problemi in leftProblem:
                    self.solveSdNum(leftNumscpy,problemi)

        #成功了(leftNum不存在)
        else:
            print("success!!!!")
            print(presentProblem)
            DataFrame(presentProblem).to_csv('success1.csv',index=None,header=None)


    def main(self):
        self.problem=pd.read_csv('form.csv',header=None).values
        print(self.problem)
        self.countAll()
        self.solveSdNum(self.sortedNum,self.problem)
sd=shudu()
sd.main()