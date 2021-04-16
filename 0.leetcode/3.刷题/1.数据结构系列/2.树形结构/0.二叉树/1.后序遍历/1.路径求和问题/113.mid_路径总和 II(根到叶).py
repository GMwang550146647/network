from fundamentals.test_time import test_time
from fundamentals.tree import Tree


class Solution():
    def __init__(self):
        pass

    @test_time
    def pathSum(self, root, targetSum):
        def dfs(root, target, cur_path):
            if root:
                cur_path.append(root.val)
                new_target = target - root.val
                if not root.left and not root.right:
                    if new_target == 0:
                        solutions.append(cur_path.copy())
                if root.left:
                    dfs(root.left, new_target, cur_path)
                if root.right:
                    dfs(root.right, new_target, cur_path)
                cur_path.pop(-1)

        solutions = []
        path = []
        dfs(root, targetSum, path)
        return solutions

    def main(self):
        root = [1, 2]
        targetSum = 1
        # root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None ,5, 1]
        # targetSum = 22
        root = Tree().build_tree_from_list(root)
        Tree().mid_recur_tree(root)
        self.pathSum(root, targetSum)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
