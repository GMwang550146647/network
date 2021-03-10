"""
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false

"""

import time
class Solution():
    def __init__(self):
        pass
    '''我的方法'''
    def myFun(self,s):
        flag = True
        if p == q:
            return True
        elif p == None or q == None:
            return False
        stack_p = [p]
        stack_q = [q]
        while stack_p or stack_q:
            p_cur = stack_p.pop(-1)
            q_cur = stack_q.pop(-1)
            if p_cur.val == q_cur.val:
                if p_cur.right != None and q_cur.right != None:
                    stack_p.append(p_cur.right)
                    stack_q.append(q_cur.right)
                elif p_cur.right == None and q_cur.right == None:
                    pass
                else:
                    flag = False
                    break
                if p_cur.left != None and q_cur.left != None:
                    stack_p.append(p_cur.left)
                    stack_q.append(q_cur.left)
                elif p_cur.left == None and q_cur.left == None:
                    pass
                else:
                    flag = False
                    break
            else:
                flag = False
                break
        return flag
    '''答案方法1'''

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


    def testTime(self,fun,args):
        # 计时
        start = time.process_time()
        result = fun(*args)
        elapsed = (time.process_time() - start)
        print(fun.__name__,":")
        print("Time used:", elapsed)
        print('result:', result)
    def main(self):
        s='dfkljal'
        self.testTime(self.myFun,args=(s,))
if __name__=='__main__':
    SL=Solution()
    SL.main()
