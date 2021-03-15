from fundamentals.test_time import test_time
from fundamentals.tree import Tree
from fundamentals.tree import TreeNode
from bsttree import BSTTree
class Solution():
    def __init__(self):
        pass

    @test_time
    def insertIntoBST(self, root, val):
        return BSTTree.insertIntoBST(root,val)

    def main(self):
        tree = [4, 2, 7, 1, 3]
        val = 5
        root = Tree().build_tree_from_list(tree)
        Tree().mid_recur_tree(root)
        self.insertIntoBST(root, val)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
