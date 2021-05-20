from fundamentals.test_time import test_time
from fundamentals.tree import Tree


class Solution():
    def __init__(self):
        pass

    @test_time
    def lowestCommonAncestor(self, root, p, q):
        """
        找到就返回
        """
        target_node = None

        def lcs(root, p, q):
            """
            找到一个就返回1
            """
            nonlocal target_node
            if not root:
                return 0
            else:
                left = lcs(root.left, p, q)
                right = lcs(root.right, p, q)
                cur = 1 if p == root.val or q == root.val else 0
                if left == 1 and right == 1:
                    target_node = root
                    return 1
                elif (left == 1 or right == 1) and cur == 1:
                    target_node = root
                    return 1
                else:
                    return max(left, right, cur)

        lcs(root, p, q)
        return target_node.val

    @test_time
    def lowestCommonAncestor_answer(self, root, p, q):

        def lcs(root, p, q):
            if root is None:
                return None
            elif root.val == p or root.val == q:
                return root
            else:
                left = lcs(root.left, p, q)
                right = lcs(root.right, p, q)
                if left and right:
                    return root
                elif left is None and right is None:
                    return None
                else:
                    return left if left else right

        return lcs(root, p, q)

    def main(self):
        root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
        p = 5
        q = 1
        root = Tree().build_tree_from_list(root)
        Tree().mid_recur_tree(root)
        self.lowestCommonAncestor(root, p, q)
        self.lowestCommonAncestor_answer(root, p, q)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
