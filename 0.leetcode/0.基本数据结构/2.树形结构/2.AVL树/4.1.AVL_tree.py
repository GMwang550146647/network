class node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.key = data
        self.height = 1

    def calheight(self):
        if not self.left:
            if not self.right:
                return 1
            else:
                return 1 + self.right.height
        else:
            if not self.right:
                return 1 + self.left.height
            else:
                return max(self.left.height,self.right.height)+1
    def rrotate(self):
        p=self.left
        self.left=p.right
        p.right=self
        self=p
        self.right.calheight()
        self.calheight()
        return self
    def lrotate(self):
        p=self.right
        self.right=p.left
        p.left=self
        self=p
        self.left.calheight()
        self.calheight()
        return self
    def dlrotate(self):
        self.right = self.right.rrotate()
        self = self.lrotate()
        return self
    def drrotate(self):
        self.left = self.left.lrotate()
        self = self.rrotate()
        return self
    def bal(self):
        if not self.left:
            if not self.right:
                return 0
            else:
                return -(self.right.height)
        else:
            if not self.right:
                return self.left.height
            else:
                return (self.left.height-self.right.height)
    def insert(self,data):
        if (data < self.key):
            if not self.left:
                self.left = node(data)
            else:
                self.left = self.left.insert(data)
                if(self.bal() == 2):
                    print( self.height,"\t",self.left.bal(),"\t",self.bal(),"\t",self.key)
                    if(self.left.bal() == 1):
                        self = self.rrotate()
                    else:
                        self = self.drrotate()
        elif (data > self.key):
            if not self.right:
                self.right = node(data)
            else:
                self.right = self.right.insert(data)
                if(self.bal() == -2):
                    print (self.height,"\t",self.right.bal(),"\t",self.bal(),"\t",self.key)
                    if(self.right.bal() == -1):
                        self = self.lrotate()
                    else:
                        self = self.dlrotate()
        else:
            print ("Key Already Exists")
        self.height=self.calheight()
        return self
    def delete(self,data):
        if (data < self.key):
            self.left = self.left.delete(data)
        elif (data > self.key):
            self.right = self.right.delete(data)
        else:
            if not self.left:
                if not self.right:
                    temp = self
                    self = None
                else:
                    temp = self.right
                    self = temp
                del temp
            elif not self.right:
                if not self.left:
                    temp = self
                    self = None
                else:
                    temp = self.left
                    self = temp
                del temp
            else:
                temp = self.right
                while temp.left:
                    temp = temp.left
                self.key = temp.key
                self.right = self.right.delete(temp.key)
            if self:
                self.height=self.calheight()
                if(self.bal() > 1):
                    if(self.left.bal() > 0):
                        self = self.rrotate()
                    else:
                        self = self.drrotate()
                elif(self.bal() < -1):
                    if(self.right.bal() < 0):
                        self = self.lrotate()
                    else:
                        self = self.dlrotate()
        return self

    def show(self,root):
        def _show(node, nt=0):
            if node:
                _show(node.left, nt + 1)
                print('\t' * nt, node.key)
                _show(node.right, nt + 1)
        _show(root)

if __name__ == '__main__':
    import random

    n = input("Enter number of nodes: ")
    l = random.sample(range(-10000, 10001), n)
    root = node(l[0])
    for x in l:
        root = root.insert(x)
    print(root.key)

    print("Your tree is\n")

    root.inorder()
    k = input("Enter integer to insert: ")
    root.insert(k)
    root.inorder()
    k = input("Enter integer to delete: ")
    root.delete(k)
    root.inorder()