from fundamentals.test_time import test_time
from fundamentals.tree import Tree

class Solution():
    def __init__(self):
        pass

    @test_time
    def hasPathSum(self, root, targetSum):
        def dfs(root,tempt_sum):
            if not root:
                return False
            else:
                tempt_sum+=root.val
                if not root.left  and not root.right and tempt_sum==targetSum:
                    return True
                else:
                    return dfs(root.left,tempt_sum) or dfs(root.right,tempt_sum)
        return dfs(root,0) if root else False

    def main(self):
        root = [5,4,8,11,None,13,4,7,2,None,None,None,1]
        root=Tree.build_tree_from_level_recur_list(root)
        targetSum = 22
        self.hasPathSum(root,targetSum)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
