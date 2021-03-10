import numpy as np
class Graph():
    def __init__(self,size=10):
        self.size=size
        self.graph=np.zeros((self.size,self.size))
        print(self.graph)
    '''图中加入定点'''

    def addVertex(self, vert):
        pass

    '''图中添加有向边（带权）'''

    def addEdge(self, fromVert, toVert, weight=0):
        pass

    '''查找名称为vkey的定点'''

    def getVertex(self, vkey):
        pass

    '''返回图中所有顶点列表'''

    def getVertices(self):
        pass

    def __contains__(self, item):
        pass
G=Graph(6)
G.addEdge(0,1,5)
G.addEdge(0,5,2)
G.addEdge(1,2,4)
G.addEdge(2,3,9)
G.addEdge(3,4,7)
G.addEdge(3,5,3)
G.addEdge(4,0,1)
G.addEdge(5,4,8)
G.addEdge(5,2,1)

