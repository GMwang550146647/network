from fundamentals.test_time import test_time
from fundamentals.tree import TreeNode

class Solution():
    def __init__(self):
        pass

    @test_time
    def generateTrees(self,n):
        def gen_tree(s,e):
            if s>=e:
                return [None]
            else:
                all_trees=[]
                for i in range(s,e):
                    left=gen_tree(s,i)
                    right=gen_tree(i+1,e)
                    for l in left:
                        for r in right:
                            rooti=TreeNode(i)
                            rooti.left=l
                            rooti.right=r
                            all_trees.append(rooti)
                return all_trees
        return gen_tree(1,n+1)

    def main(self):
        n=3
        self.generateTrees(n)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
