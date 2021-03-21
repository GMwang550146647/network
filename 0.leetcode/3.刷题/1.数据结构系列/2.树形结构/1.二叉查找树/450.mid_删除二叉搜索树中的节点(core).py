from fundamentals.test_time import test_time
from fundamentals.tree import Tree
from fundamentals.tree import TreeNode
from bsttree import BSTTree


class Solution():
    def __init__(self):
        pass

    @test_time
    def deleteNode(self, root, key):
        return BSTTree.deleteNode(root,key)

    def main(self):
        tree = [5, 3, 6, 2, 4, None, 7]
        key = 3
        root = Tree().build_tree_from_list(tree)
        Tree().mid_recur_tree(root)
        result=self.deleteNode(root, key)
        Tree().mid_recur_tree(result)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
