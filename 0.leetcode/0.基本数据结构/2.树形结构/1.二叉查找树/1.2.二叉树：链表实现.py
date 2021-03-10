class BinaryTree:
    def __init__(self,rootObj):
        self.key=rootObj
        self.left=None
        self.right=None
    def insertLeft(self,newBranch):
        newb=BinaryTree(newBranch)
        if self.left==None:
            self.left=newb
        else:
            tempt=self.left
            self.left=newb
            newb=tempt
    def insertRight(self,newBranch):
        newb=BinaryTree(newBranch)
        if self.right==None:
            self.right=newb
        else:
            tempt=self.right
            self.right=newb
            newb=tempt
    def getRootVal(self):
        return self.key
    def setRootVal(self,newVal):
        self.key=newVal
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
tr=BinaryTree('a')
tr.insertLeft('b')
tr.insertRight('c')
tr.getRight().setRootVal("hello")
tr.getLeft().insertRight('d')