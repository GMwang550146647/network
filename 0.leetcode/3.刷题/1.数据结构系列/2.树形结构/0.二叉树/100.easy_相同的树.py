from fundamentals.test_time import test_time
from fundamentals.tree import Tree

class Solution():
    def __init__(self):
        pass

    @test_time
    def isSameTree(self,p,q):
        def recur(p,q):
            if p is None and  q is None:
                return True
            if p is None or q is None:
                return False
            if p.val == q.val:
                return recur(p.left, q.left) and recur(p.right, q.right)
            else:
                return False
        return recur(p,q)
    def main(self):
        t1=[1,2,3,4,5,6]
        t2=[1,2,3,4,5,5]
        root1=Tree().build_tree_from_list(t1)
        root2=Tree().build_tree_from_list(t2)
        self.isSameTree(root1,root2)


if __name__ == '__main__':
    SL = Solution()
    SL.main()