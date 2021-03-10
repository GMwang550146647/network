class Node:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key=key
        self.val=val
        self.left=left
        self.right=right
        self.parent=parent
    def hasLeftChild(self):
        return self.left
    def hasRightChild(self):
        return self.right
    def isLeft(self):
        return self.parent and self.parent.left==self
    def isRight(self):
        return self.parent and self.parent.right==self
    def isRoot(self):
        return not self.parent
    def isLeaf(self):
        return not(self.right or self.left)
    def hasAnyChildren(self):
        return self.right or self.left
    def hasBothChildren(self):
        return self.right and self.left
    def replaceNodeData(self,key,value,lc,rc):
        self.key=key
        self.payload=value
        self.left=lc
        self.right=rc
        if self.hasLeftChild():
            self.left.parent=self
        if self.hasRightChild():
            self.right.parent=self

    '''3.迭代器
            封装：使得树的遍历操作像是列表一样简单
            __iter__:把树封装成列表，其检索方式实质上是黑箱子（递归）
            warning:这个函数比较难理解 for elem in self.left其实这里是调用了自己
    '''
    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.left:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.right:
                    yield elem
class BinarySearchTree():
    def __init__(self):
        self.root=None
        self.size=0
    def length(self):
        return self.size
    def __len__(self):
        return self.size

    def show(self):
        self._show(self.root)
    def _show(self,node,nt=0):
        if node:
            self._show(node.left,nt+1)
            print('\t'*nt,node.key)
            self._show(node.right,nt+1)


    '''1.put:
        功能：把一个key，value对存入binarytree
        封装：把一个value放进binaryTree,把其包装为可以tree[key]=value的模式
        例如：mytree[3]='red' 就相当于插入一个 key=3,val='red'的节点
    '''
    def __setitem__(self, key, val):
        self.put(key,val)
    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root=Node(key,val)
        self.size+=1
    def _put(self,key,val,node):
        if key<=node.key:
            if node.hasLeftChild():
                self._put(key,val,node.left)
            else:
                node.left=Node(key,val,parent=node)
        else:
            if node.hasRightChild():
                self._put(key,val,node.right)
            else:
                node.right=Node(key,val,parent=node)
    '''2.get:
        功能：把key对应的值取出来，类似于字典的dict[key]
        封装：只需要tree[key]就可以取出相应的值，若不存在会返回None
            __contains__: xx in tree的判断,归属判断运算符
            __getitem__: 获取tree[key]的值
    '''
    def __contains__(self, key):
        if self._get(key,self.root):
            return True
        else:
            return False
    def __getitem__(self,key):
        return self.get(key)
    def get(self,key):
        if self.root:
            node=self._get(key,self.root)
            return node.val if node!=None else None
        else:
            return None
    def _get(self,key,node):
        if not node:
            return None
        elif key==node.key:
            return node
        elif key<node.key:
            return self._get(key,node.left)
        else:
            return self._get(key,node.right)

    '''迭代器，见3.'''
    def __iter__(self):
        return self.root.__iter__()

    '''4.delete:
        封装： __delitem__：解决del tr[keyi]的情况，删除该key
    '''
    def __delitem__(self, key):
        self.delete(key)
    def delete(self,key):
        if self.size>1:
            nodeToRemove=self._get(key,self.root)
            if nodeToRemove:
                self._delete(nodeToRemove)
                self.size-=1
            else:
                raise KeyError("Error,key not in tree")
        elif self.size==1 and self.root.key==key:
            self.root=None
            self.size-=1
        else:
            raise KeyError("Error,key not in tree")
    def _delete(self,nodeToRemove):  #注意这个是不包含只有一个root的情况
        #1.该节点无左右子树:直接令parent的指向为None（要判断del的是其左还是右）
        if not nodeToRemove.hasRightChild() and not nodeToRemove.hasLeftChild():
            if nodeToRemove.isRight():  #如果该删除节点是父节点的右节点，那么父节点的右节点为None
                nodeToRemove.parent.right=None
            else:
                nodeToRemove.parent.left=None
        #2.该节点有左子树
        elif not nodeToRemove.hasRightChild() and nodeToRemove.hasLeftChild():
            nodeToRemove.left.parent = nodeToRemove.parent  #2.1.子节点的父节点是要删除的节点的父节点
            if nodeToRemove.parent!=None:
                if nodeToRemove.isRight():                      #2.2.(删除的不是根节点）该删除节点的父节点的指向应该更新为该删除节点的左节点
                    nodeToRemove.parent.right=nodeToRemove.left
                else:
                    nodeToRemove.parent.left=nodeToRemove.left
            else:                                                   #2.3.（删除的是根节点）
                self.root=nodeToRemove.left
        #3.该节点有右子树
        elif nodeToRemove.hasRightChild() and not nodeToRemove.hasLeftChild():
            nodeToRemove.right.parent = nodeToRemove.parent  # 3.1.子节点的父节点是要删除的节点的父节点
            if nodeToRemove.parent!=None:
                if nodeToRemove.isRight():                       # 3.2.(删除的不是根节点）该删除节点的父节点的指向应该更新为该删除节点的右节点
                    nodeToRemove.parent.right = nodeToRemove.right
                else:
                    nodeToRemove.parent.left = nodeToRemove.right
            else:
                self.root=nodeToRemove.right                    #3.3.（删除的是根节点）

        #4.该节点有左右子树：注意4.1.和4.2.可以调转
        else:
            #4.1.用左子树的最大节点填补（或者用右子树的最小节点填补）
            nodeSubstitube=nodeToRemove.left
            while nodeSubstitube.right:  #迭代直至找到左子树的最大节点（其实就是最右的节点）
                nodeSubstitube=nodeSubstitube.right
            nodeToRemove.key=nodeSubstitube.key
            nodeToRemove.val=nodeSubstitube.val
            #4.2.该空格再递归填补
            self._delete(nodeSubstitube)







tr=BinarySearchTree()

'''1.put测试'''
arr=[15,5,3,7,16,24,19]
for num in arr:
    tr[num]=num**2
tr.show()
print(tr.get(7))
print("____________________")
'''2.get测试'''
print(6 in tr)
print(tr[7])
print("____________________")
'''3.测试__iter__'''
for key in tr:
    print(key,':',tr[key])
print("____________________")

'''4.测试__del__'''
for item in arr:
    del tr[item]
    tr.show()
    print("#############")