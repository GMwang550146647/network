#-*- coding:utf-8 -*- 
import numpy as np
import pandas as pd
import sklearn
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
arr=[4,2,6,1,3,5,7]
class node(object):
    def __init__(self,value,l=None,r=None,p=None,view=0):
        self.lchild=l
        self.rchild=r
        self.value=value
        self.view=view
        self.parent=p

class tree(object):
    def __init__(self,value=None,view=0):
        self.root=node(value,view=view)
        self.position=[]
    def insert(self,arr):
        # arr.sort()
        # n=len(arr)
        # arr1=[]
        # if n%2==0:
        #     for i in range(n//2-1,-1,-1):
        #         arr1.append(arr[i])
        #         arr1.append(arr[n-1-i])
        # if n%2==1:
        #     arr1.append(arr[n//2])
        #     for i in range(n//2-1,-1,-1):
        #         arr1.append(arr[i])
        #         arr1.append(arr[n-1-i])
        for nodek in arr:
            self.insert_one(self.root,nodek)
    def insert_one(self,root,num,parent=None):
        if root.value==None:
            root.value=num
            return
        elif num<=root.value and root.lchild==None:
            root.lchild=node(num,p=root)
        elif num<=root.value and root.lchild!=None:
            self.insert_one(root.lchild,num,parent=root)
        elif num>root.value and root.rchild==None:
            root.rchild=node(num,p=root)
        elif num>root.value and root.rchild!=None:
            self.insert_one(root.rchild,num,parent=root)
        else:
            pass
    def show(self,root,i=-10):
        i+=10
        if root.lchild!=None:
            self.show(root.lchild,i)
        print(' '*i,root.value)
        if root.rchild!=None:
            self.show(root.rchild,i)
    def search(self,root,num,dummy):
        if num==root.value:
            dummy.append(root)
        elif num<=root.value and root.lchild!=None:
            self.search(root.lchild,num,dummy)
        elif num<=root.value and root.lchild==None:
            dummy.append(-1)
        elif num>root.value and root.rchild!=None:
            self.search(root.rchild,num,dummy)
        elif num>root.value and root.rchild==None:
            dummy.append(-1)
        else:
            pass
    def find_left_largest_node(self,root,dummy):
        if root.rchild!=None:
            self.find_left_largest_node(root.rchild,dummy)
        else:
            dummy.append(root)
    def delete(self,root,num):
        self.search(root,num,self.position)
        if tree1.position[0]==-1:
            print('Number not in tree')
            return
        node_to_del=self.position.pop()
        if node_to_del.lchild==None and node_to_del.rchild==None:
            if node_to_del.value>node_to_del.parent.value:      #该点是父节点的右节点
                node_to_del.parent.rchild=None
                del node_to_del
            else:                                               #左节点
                node_to_del.parent.lchild=None
                del node_to_del
        elif node_to_del.lchild==None and node_to_del.rchild!=None:     #该点只有右节点
            if node_to_del.value>node_to_del.parent.value:      #该点是父节点的右节点
                node_to_del.parent.rchild=node_to_del.rchild
                node_to_del.rchild.parent=node_to_del.parent
                del node_to_del
            else:                                               #左节点
                node_to_del.parent.lchild=node_to_del.rchild
                node_to_del.rchild.parent=node_to_del.parent
        elif node_to_del.rchild==None and node_to_del.lchild!=None:     #该节点只有左节点
            if node_to_del.value>node_to_del.parent.value:      #该点是父节点的右节点
                node_to_del.parent.rchild=node_to_del.lchild
                node_to_del.lchild.parent=node_to_del.parent
                del node_to_del
            else:                                               #左节点
                node_to_del.parent.lchild=node_to_del.lchild
                node_to_del.lchild.parent=node_to_del.parent
        else:
            self.find_left_largest_node(node_to_del.lchild,self.position)
            substitude=self.position.pop()
            print(substitude.value)
            flag=0                                             #若该点的左节点非替代点时为0，为替代点时，且只有一个点时为1
            if substitude.value>substitude.parent.value:      #该点是父节点的右节点
                substitude.parent.rchild=None
            else:                                               #左节点
                substitude.parent.lchild=None
                flag=1
            if flag==1:
                if node_to_del.parent==None or node_to_del.value>node_to_del.parent.value :     #该点是父节点的右节点
                    substitude.rchild=node_to_del.rchild
                    substitude.parent=node_to_del.parent
                    node_to_del.rchild.parent=substitude
                    if node_to_del.parent!=None:
                        node_to_del.parent.rchild=substitude
                    else:
                        self.root=substitude
                else:                                               #左节点
                    substitude.rchild=node_to_del.rchild
                    substitude.parent=node_to_del.parent
                    node_to_del.rchild.parent=substitude
                    if node_to_del.parent!=None:
                        node_to_del.parent.lchild=substitude
            elif flag==0:
                if node_to_del.parent==None or node_to_del.value>node_to_del.parent.value :      #该点是父节点的右节点
                    substitude.rchild=node_to_del.rchild
                    substitude.lchild=node_to_del.lchild
                    substitude.parent=node_to_del.parent
                    node_to_del.lchild.parent=substitude
                    node_to_del.rchild.parent=substitude
                    if node_to_del.parent!=None:
                        node_to_del.parent.rchild=substitude
                    else:
                        self.root=substitude
                else:                                               #左节点
                    substitude.rchild=node_to_del.rchild
                    substitude.lchild=node_to_del.lchild
                    substitude.parent=node_to_del.parent
                    node_to_del.lchild.parent=substitude
                    node_to_del.rchild.parent=substitude
                    if node_to_del.parent!=None:
                        node_to_del.parent.lchild=substitude

    def tear_apart(self,root,arr):
        if root.value!=None:
            arr.append(root.value)
        if root.lchild!=None:
            self.tear_apart(root.lchild,arr)
        elif root.rchild!=None:
            self.tear_apart(root.rchild,arr)
        else:
            return
tree1=tree()
tree1.insert(arr)
tree1.show(tree1.root)
tree1.delete(tree1.root,4)
print('----------------------------')
tree1.show(tree1.root)

