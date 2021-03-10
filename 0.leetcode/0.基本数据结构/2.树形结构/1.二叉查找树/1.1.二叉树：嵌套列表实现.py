'''
节点定义：[root,left,right]
'''
class BinaryTree():
    def __init__(self,obj=None):
        self.tree=[obj,[],[]]
    def insertLeft(self,root,newBranch):
        t=root.pop(1)
        if len(t)>1:
            root.insert([newBranch,t,[]])
        else:
            root.insert([newBranch,[],[]])
    def insertRight(self,root,newBranch):
        t=root.pop(2)
        if len(t)>1:
            root.insert([newBranch,[],t])
        else:
            root.insert([newBranch,[],[]])
    def getVal(self,root):
        return root[0]
    def setVal(self,root,newVal):
        root[0]=newVal
    def getLeft(self,root):
        return root[1]
    def getRight(self,root):
        return root[2]
