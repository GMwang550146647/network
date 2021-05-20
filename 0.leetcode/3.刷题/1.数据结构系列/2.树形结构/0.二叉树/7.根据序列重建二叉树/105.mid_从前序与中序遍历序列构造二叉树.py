from fundamentals.test_time import test_time
from fundamentals.tree import TreeNode


class Solution():
    def __init__(self):
        pass

    @test_time
    def buildTree(self, preorder, inorder):
        def build_tree_assist(ps, pe, ins, ine):
            if (ps >= pe or ins >= ine):
                return None
            root = TreeNode(preorder[ps])
            root_pos = in_map[root.val]
            root.left = build_tree_assist(ps + 1, ps + root_pos - ins + 1, ins, root_pos)
            root.right = build_tree_assist(ps + root_pos - ins + 1, pe, root_pos + 1, ine)
            return root

        in_map = {val: key for key, val in enumerate(inorder)}
        ps = ins = 0
        pe = ine = len(preorder)
        return build_tree_assist(ps, pe, ins, ine)

    def main(self):
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        self.buildTree(preorder, inorder)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
