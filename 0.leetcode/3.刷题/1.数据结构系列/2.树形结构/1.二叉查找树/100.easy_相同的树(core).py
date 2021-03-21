from fundamentals.test_time import test_time
from fundamentals.tree import Tree
from bsttree import BSTTree


class Solution():
    def __init__(self):
        pass

    @test_time
    def isSameTree(self, p, q):
        return BSTTree.isSameTree(p, q)

    def main(self):
        t1 = [1, 2, 3, 4, 5, 6]
        t2 = [1, 2, 3, 4, 5, 5]
        root1 = Tree().build_tree_from_list(t1)
        root2 = Tree().build_tree_from_list(t2)
        self.isSameTree(root1, root2)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
