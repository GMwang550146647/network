#问题描述：
# 4*4=16个大小相同的岛屿呈正方形排列，只有相邻的岛屿（包括斜着相邻）之间有渡船，不相邻的岛不连通。
# 从这16个岛屿中选出若干个岛屿形成一个“岛群”，若人能够不返回且不走到其它未选中的岛屿而走遍选中的所有岛屿，
# 那么称这个岛群为“好岛群”，问所有的岛群有多少个
#这里只计算从（0，0）到（3，3)的

import numpy as np
import copy
class road():
    def __init__(self):
        self.passed=[]  #记录已经历过的点
        self.road=[]    #按顺序记录经历过的点
class Tu():
    def __init__(self,n=4):
        self.n=n
        self.tu=np.arange(n**2).reshape(n,n)
        print(self.tu)
    #对于每个位置都找出下一次可能的方向
    def find_direction(self,pos):
        x,y=pos
        possible_next_pos=np.array([[x-1,y-1],[x-1,y],[x-1,y+1],[x,y-1],[x,y+1],[x+1,y-1],[x+1,y],[x+1,y+1]])
        xs=possible_next_pos[:,0]
        ys=possible_next_pos[:,1]
        x_true=(xs>=0)&(xs<self.n)
        y_true=(ys>=0)&(ys<self.n)
        result=possible_next_pos[x_true & y_true]
        if len(result)==0:
            return []
        else:
            result=[tuple(item) for item in result]
            return result
    #任意给两个点（前面是起点，后面是终点）,计算出所有可能的路程
    def find_way(self,sp,ep):
        count=0
        allways_buliding=[]
        allways_finished=[]
        next_points=self.find_direction(sp)
        for i in range(len(next_points)):
            if next_points[i]==ep:
                allways_finished.append([sp,next_points[i]])
            else:
                allways_buliding.append([sp,next_points[i]])
        while(len(allways_buliding)!=0):
            road=copy.deepcopy(allways_buliding[-1])
            allways_buliding.pop(-1)
            nps=self.find_direction(road[-1])
            # print(road)
            if len(nps)==0:
                continue
            for i in range(len(nps)):
                if nps[i]==ep:
                    roadi=copy.deepcopy(road)
                    roadi.append(nps[i])
                    # print(roadi in allways_finished)
                    allways_finished.append(roadi)
                    count+=1
                    print(count)
                elif nps[i] not in road:
                    #如果该节点是没走过的，那么在allways_building中添加该未完成的路，如果该路是死路，那么就忽略
                    roadi=copy.deepcopy(road)
                    roadi.append(nps[i])
                    allways_buliding.append(roadi)
                    # print(roadi)

        return allways_finished

tu=Tu()
allways=tu.find_way((0,0),(3,3))
print(len(allways))