from fundamentals.test_time import test_time
from fundamentals.tree import Tree
from bsttree import BSTTree
class Solution():
    def __init__(self):
        pass

    @test_time
    def isValidBST(self,root):
        return BSTTree.isValidBST(root)

    def main(self):
        tree = [2, 1, 3, None, None, None, 4]
        root = Tree().build_tree_from_list(tree)
        Tree().mid_recur_tree(root)
        self.isValidBST(root)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
