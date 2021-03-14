from fundamentals.test_time import test_time
from fundamentals.tree import Tree

class Solution():
    def __init__(self):
        pass

    @test_time
    def isValidBST(self,root):
        def mid_recur(root):
            nonlocal  recorder
            if root:
                if not mid_recur(root.left):
                    return False
                if recorder is not None and root.val<=recorder:
                    return False
                else:
                    recorder=root.val
                if not mid_recur(root.right):
                    return False
                return True
            else:
                return True
        recorder=None
        return mid_recur(root)

    def main(self):
        tree = [2, 1, 3, None, None, None, 4]
        root = Tree().build_tree_from_list(tree)
        Tree().mid_recur_tree(root)
        self.isValidBST(root)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
