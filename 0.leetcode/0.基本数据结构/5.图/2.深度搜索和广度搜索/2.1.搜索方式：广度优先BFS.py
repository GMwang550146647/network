'''
骑士周游问题：
8*8的棋盘，骑士走日字型，走完所有的格子（都各自是一次）算一个解
（这里只列举5*5的，起点是（2，2），0开始数）
'''
import copy
import time


'''
result:
Time used: 73.700184
result: 64

'''
class knightTravel():
    def __init__(self,size=5,initPos=None):
        self.size=size
        self.initPos= initPos if initPos!=None else (size//2,size//2)
        #移动方式
        self.moveOffsets=[(-1,-2),(-1,2),(-2,-1),(-2,1),(1,-2),(1,2),(2,-1),(2,1)]
        #用来装答案的
        self.solutions = []
        self.numsolutions = 0
    '''层次遍历：广度优先'''
    def travel(self):
        unfinishedRoad=[[self.initPos]]
        while unfinishedRoad:
            currentRoad=unfinishedRoad.pop() #把栈的最后一条路
            suitableNodes=self.findSuitableNodes(currentRoad)
            for node in suitableNodes:
                temptRoad=copy.deepcopy(currentRoad)
                temptRoad.append(node)
                if len(temptRoad)==self.size**2:
                    # self.solutions.append(temptRoad)
                    self.numsolutions+=1
                else:
                    unfinishedRoad.insert(0,temptRoad)
    def findSuitableNodes(self,currentRoad):
        suitableNodes=[]
        currentNode=currentRoad[-1]
        for move in self.moveOffsets:
            newx=move[0]+currentNode[0]
            newy=move[1]+currentNode[1]
            if newx<5 and newy<5 and newx>=0 and newy>=0:
                if (newx,newy) not in currentRoad:
                    suitableNodes.append((newx,newy))
        return suitableNodes
    '''时间测试函数'''
    def testTime(self,fun):
        # 计时
        start = time.process_time()
        result = fun()
        elapsed = (time.process_time() - start)
        print(fun.__name__,":")
        print("Time used:", elapsed)
        print('result:', self.numsolutions)
    def main(self):
        self.testTime(self.travel)
kt=knightTravel()
kt.main()
