from fundamentals.test_time import test_time
from fundamentals.tree import Tree
import sys

sys.setrecursionlimit(10000)


class Solution():
    def __init__(self):
        pass

    @test_time
    def rob_recur_dict(self, root):
        def dp(node):
            if node is None:
                return 0
            if node in dp_dict:
                return dp_dict[node]
            else:
                res1 = dp(node.left) + dp(node.right)
                res2 = node.val + (0 if node.left is None else dp(node.left.left) + dp(node.left.right)) + (
                    0 if node.right is None else dp(node.right.left) + dp(node.right.right))
                dp_dict[node] = max(res1, res2)
                return dp_dict[node]

        dp_dict = {}
        return dp(root)

    def main(self):
        tree = [3, 2, 3, None, 3, None, 1]
        tree = [3, 4, 5, 1, 3, None, 1]
        root = Tree().build_tree_from_list(tree)
        Tree().mid_recur_tree(root)

        self.rob_recur_dict(root)
        # self.rob_dp(root)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
