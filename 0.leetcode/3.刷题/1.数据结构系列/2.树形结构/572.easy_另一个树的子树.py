from fundamentals.test_time import test_time
from fundamentals.tree import TreeNode, Tree


class Solution():
    def __init__(self):
        pass

    @test_time
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        """
        一个一个节点对比是不是subtree
        """

        def solve(s, t):
            def tell_same(t1, t2):
                if t1 is None and t2 is None:
                    return True
                elif t1 is None or t2 is None:
                    return False
                else:
                    if t1.val == t2.val:
                        return tell_same(t1.left, t2.left) and tell_same(t1.right, t2.right)
                    else:
                        return False

            if s is None and t is None:
                return True
            elif s is None or t is None:
                return False
            else:
                if s.val == t.val and tell_same(s, t):
                    return True
                else:
                    return solve(s.left, t) or solve(s.right, t)

        return solve(s, t)

    @test_time
    def isSubtree_serialize(self, s: TreeNode, t: TreeNode) -> bool:
        """
        前序遍历，如果有相同部分，即序列化后会重叠一部分
        """
        def recur(root, cur_path=''):
            if root:
                cur_path += str(root.val) + ' ' + recur(root.left) + ' ' + recur(root.right)
                return cur_path
            else:
                cur_path += ' '
                return cur_path

        s = recur(s, ' ') + ' '
        t = recur(t, ' ') + ' '
        return t in s

    def main(self):
        t1 = Tree.build_tree_from_level_recur_list([1, None, 2, 4])
        t2 = Tree.build_tree_from_level_recur_list([3, 2])
        self.isSubtree(t1, t2)
        self.isSubtree_serialize(t1, t2)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
