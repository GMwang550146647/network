from fundamentals.test_time import test_time
from fundamentals.tree import Tree

class Solution():
    def __init__(self):
        pass

    @test_time
    def largestBSTSubtree(self,root):
        def dfs( root):
            if root == None:
                return float('inf'), float('-inf'), 0  # 对所有的父节点。它都是配合的，ok的

            L_min, L_max, L_cnt = dfs(root.left)
            R_min, R_max, R_cnt = dfs(root.right)

            if L_max < root.val < R_min:  # 若能构成BST
                return min(L_min, root.val), max(root.val, R_max), L_cnt + R_cnt + 1

            else:  # 不能构成BST
                return float('-inf'), float('inf'), max(L_cnt, R_cnt)
        return dfs(root)[2]

    def main(self):
        root = [4, 2, 7, 2, 3, 5, None, 2, None, None, None, None, None, 1]
        root=Tree.build_tree_from_level_recur_list(root)
        self.largestBSTSubtree(root)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
