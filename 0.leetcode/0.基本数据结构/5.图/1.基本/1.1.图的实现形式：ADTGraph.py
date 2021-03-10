class Vertex():
    def __init__(self,key):
        self.id=key
        self.connectedTo={}

    '''节点加入邻居'''
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr]=weight

    '''该点的连接对象'''
    def __str__(self):
        return str(self.id)+' connectedTo:' +str([x.id for x in self.connectedTo])

    def getConnections(self, vkey):
        return self.connectedTo.keys()

    '''返回节点id和权重'''
    def getId(self):
        return self.id
    def gertWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph():
    def __init__(self):
        self.vertList={}  #{key:vertex}键值对的字典
        self.numVertices=0

    '''1.图中加入定点'''
    def addVertex(self, key):
        self.numVertices=self.numVertices+1
        newVertex=Vertex(key)
        self.vertList[key]=newVertex
        return newVertex

    '''2.查找名称为vkey的定点'''
    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None
    def __contains__(self, key):
        return key in self.vertList
    '''3.图中添加有向边（带权）'''
    def addEdge(self, fromVert, toVert, weight=0):
        if fromVert not in self.vertList:
            nv=self.addVertex(fromVert)
        if toVert not in self.vertList:
            nv=self.addVertex(toVert)
        self.vertList[fromVert].addNeighbor(self.vertList[toVert],weight)

    '''返回图中所有顶点列表'''
    def getVertices(self):
        return self.vertList.keys()
    def __iter__(self):
        return iter(self.vertList.values())



