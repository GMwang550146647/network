import numpy as np
'''
每一次循环都查找可行解最少的数字，然后填一个
'''
class shudu():
    def __init__(self):
        self.problem=np.array([
            [3, -1, -1,    6, -1, 5,     -1, 1, -1],
            [-1, 8, 2,    -1, 3, -1,     -1, -1, 7],
            [4, -1, -1,    7, -1, -1,     8, -1, 3],

            [9, 1, -1,    3, -1, -1,     -1, -1, 5],
            [6, -1, -1,    8, 7, -1,     -1, -1, 2],
            [9, -1, -1,    -1, -1, 1,     -1, 3, 9],

            [5, -1, 3,    -1, -1, 7,     -1, -1, 8],
            [7, -1, -1,    -1, 9, -1,     3, 5, -1],
            [-1, 6, -1,    5, -1, 3,     -1, -1, 1],
        ])
        self.sortedNum=[]
    def countAll(self):
        dictNnum={}
        for i in range(1,10):
            dictNnum[i]=(self.problem==i).sum()
        sortedNum=sorted(dictNnum.items(),key=lambda a:a[1],reverse=True)
        sortedNum=[item[0] for item in sortedNum]
        self.sortedNum=sortedNum

    '''对现时的temptProblem(注意，要复制矩阵）对某个num进行可行位置判断'''
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
    def solveSdNum(self,leftNums,presentProblem):

        leftNumscpy=leftNums.copy()
        #退出条件：再没有可以填的空格（或者再没有可行解）
        if len(leftNums)!=0:
            # 找出可填空格最少的那个变量
            minNum = 1000
            minSuitablePlace = []
            min_index=-1
            deleteNum=[]
            for numi in leftNumscpy:
                temptsuit = self.findSuitablePlace(numi, presentProblem)
                if len(temptsuit)==0 and (presentProblem==numi).sum()!=9:
                    #失败了,有数字无解
                    print("#####FAIL######",numi)
                    # print(presentProblem)
                    return
                if len(temptsuit)==0 and (presentProblem==numi).sum()==9:
                    deleteNum.append(numi)
                elif len(temptsuit) < minNum and len(temptsuit)!=0:
                    minSuitablePlace = temptsuit
                    minNum=len(temptsuit)
                    min_ndex=numi
            if min_index==-1:
                return
            leftNumscpy=list(set(leftNumscpy)-set(deleteNum))
            # print(leftNumscpy,":",min_index)
            # print(temptsuit)

            if len(presentProblem == -1) == 0:  # 成功填满的情况
                print("###############success!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!###################")
                print(presentProblem)
            else:
                currentNum=min_index
                if len(minSuitablePlace)!=0 and len(presentProblem==-1)!=0:
                    for placei in minSuitablePlace:
                        presentProblemi = presentProblem.copy()
                        presentProblemi[placei[0],placei[1]]=currentNum
                        self.solveSdNum(leftNumscpy.copy(),presentProblemi.copy())

    def main(self):
        self.countAll()
        self.solveSdNum(self.sortedNum,self.problem)
sd=shudu()
sd.main()