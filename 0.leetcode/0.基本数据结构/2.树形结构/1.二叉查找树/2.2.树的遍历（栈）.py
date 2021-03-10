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
    '''1.栈：层次遍历:先第一行全部，然后第二行全部...'''
    #诀窍：栈左边的弹出，分成两个，丢到栈右边（保证每次解决的都是同级别的，不同级别的在列表另一边
    def cengci(self,root):
        result=[]
        q=[root]
        while q:
            current=q.pop(0)
            result.append(current.elem)
            if current.lchild!=None:
                q.append(current.lchild)
            if current.rchild!=None:
                q.append(current.rchild)
        print(result)
    '''2.栈：前序遍历'''
    #诀窍：栈右边元素输出，然后分成两个，再丢到右边（要保证最右边的是左子树）
    def front_stack(self,root):
        result=[]
        q=[root]
        while q:
            current=q.pop()
            result.append(current.elem)
            if current.rchild!=None:
                q.append(current.rchild)
            if current.lchild!=None:
                q.append(current.lchild)
        print(result)
    '''3.栈：中序遍历'''
    #诀窍：中序遍历是左中右，把未分裂的节点放在undivided，分裂了的节点放在divided，一旦节点到了叶节点，divided就pop出两个进入result
    def middle_stack(self,root):
        '''自研方法：'''
        divided=[]
        undivided=[root]
        result=[]
        while undivided:
            current=undivided.pop()
            divided.append(current)
            if current.rchild!=None:
                undivided.append(current.rchild)
            if current.lchild!=None:
                undivided.append(current.lchild)
            if current.rchild==None and current.lchild==None:
                result.append(divided.pop().elem)
                if len(divided)>0:
                    result.append(divided.pop().elem)
        print(result)
        '''标准方法:非常巧妙，leftnodes只保存node的"左节点"，当node再也没有左节点了，node变为leftnodes最后一个节点的右节点，然后再穷尽该节点的左节点'''
        leftnodes=[]
        node=root
        result=[]
        while leftnodes or node:
            while node:
                leftnodes.append(node)
                node=node.lchild
            node=leftnodes.pop()
            result.append(node.elem)
            node=node.rchild
        print(result)

    '''4.栈：后序遍历'''
    #诀窍：后续是 '左右中'，前序遍历是'中左右'，只需要把前序遍历中的左右互换，然后reverse就可以解决问题（左右互换其实很简单）
    def back_stack(self, root):
        """利用堆栈实现树的后序遍历"""
        result=[]
        p=[root]
        while p:
            current=p.pop()
            result.append(current.elem)
            if current.rchild!=None:
                p.append(current.lchild)
            if current.lchild!=None:
                p.append(current.rchild)
        result.reverse()
        print(result)

    def main(self):
        print("---------------------------")
        self.cengci(self.root)
        print("---------------------------")
        self.front_stack(self.root)
        print("---------------------------")
        self.middle_stack(self.root)
        print("---------------------------")
        self.back_stack(self.root)
        print("---------------------------")
arr=[4,2,6,1,3,5,7]
t=tree(arr)
t.main()