class node(object):
    def __init__(self,elem=-1,lchild=None,rchild=None):
        self.elem=elem
        self.lchild=lchild
        self.rchild=rchild
class tree(object):
    def __init__(self,arr):
        self.root=node()
        self.myqueue=[]
        self.add_arr(arr)
    def add_one(self,value,present_position):
        if present_position.elem==-1:
            tempt_node=node(value)
            self.root=tempt_node
        elif value<present_position.elem:
            if present_position.lchild==None:
                present_position.lchild=node(value)
            else:
                self.add_one(value,present_position.lchild)
        elif value>=present_position.elem:
            if present_position.rchild==None:
                present_position.rchild=node(value)
            else:
                self.add_one(value,present_position.rchild)
    def add_arr(self,arr):
        for item in arr:
            self.add_one(item,self.root)
        return self.root


    '''1.递归：前序遍历'''
    def front_digui(self,root,nc=0):
        if root!=None:
            print('\t'*nc,root.elem)
            self.front_digui(root.lchild,nc+1)
            self.front_digui(root.rchild,nc+1)
    '''2.递归：中序遍历'''
    def middle_digui(self,root,nc=0):
        if root!=None:
            self.middle_digui(root.lchild,nc+1)
            print('\t' * nc, root.elem)
            self.middle_digui(root.rchild,nc+1)
    '''3.递归：后序遍历'''
    def back_digui(self,root,nc=0):
        if root!=None:
            self.back_digui(root.lchild,nc+1)
            self.back_digui(root.rchild,nc+1)
            print('\t' * nc, root.elem)

    def main(self):
        print("---------------------------")
        self.front_digui(self.root)
        print("---------------------------")
        self.middle_digui(self.root)
        print("---------------------------")
        self.back_digui(self.root)
        print("---------------------------")
arr=[4,2,6,1,3,5,7]
t=tree(arr)
t.main()