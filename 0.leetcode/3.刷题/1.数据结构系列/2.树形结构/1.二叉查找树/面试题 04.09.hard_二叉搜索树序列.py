from fundamentals.test_time import test_time
from fundamentals.tree import Tree

class Solution():
    def __init__(self):
        pass

    @test_time
    def BSTSequences(self,root):
        if not root:
            return [[]]
        solutions=[]
        def solve(root,candidates,cur):
            if root.left:
                candidates.append(root.left)
            if root.right:
                candidates.append(root.right)
            if not candidates:
                solutions.append(cur.copy())
            else:
                for i in range(len(candidates)):
                    solve(candidates[i],candidates[:i]+candidates[i+1:],cur+[candidates[i].val])
        solve(root,[],[root.val])
        return solutions
    def main(self):
        root=Tree().build_tree_from_list([2,1,3])
        self.BSTSequences(root)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
