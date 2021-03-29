from fundamentals.test_time import test_time
from fundamentals.tree import Tree, TreeNode


class Solution():
    def __init__(self):
        pass

    @test_time
    def lowestCommonAncestor(self, root, p, q):
        def dfs(root, p, q):
            if root.val < p.val:
                return dfs(root.right, p, q)
            elif root.val > q.val:
                return dfs(root.left, p, q)
            else:
                return root

        p, q = (p, q) if p.val < q.val else (q, p)
        return dfs(root, p, q)

    def main(self):
        root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
        p = TreeNode(2)
        q = TreeNode(8)
        root = Tree().build_tree_from_list(root)
        self.lowestCommonAncestor(root, p, q)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
