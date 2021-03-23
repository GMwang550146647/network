from fundamentals.test_time import test_time
from fundamentals.tree import Tree


class Solution():
    def __init__(self):
        pass

    @test_time
    def maxDepth_dfs(self, root):
        def recur(root, depth=0):
            if root:
                nonlocal max_depth
                if depth + 1 > max_depth:
                    max_depth = depth + 1
                recur(root.left, depth + 1)
                recur(root.right, depth + 1)

        max_depth = 0
        recur(root)
        return max_depth

    @test_time
    def maxDepth_bfs(self, root):
        stack = [root]
        step = 0
        while stack:
            for i in range(len(stack)):
                cur_node = stack.pop(0)
                if cur_node.left:
                    stack.append(cur_node.left)
                if cur_node.right:
                    stack.append(cur_node.right)
            step += 1
        return step

    def main(self):
        tree = [3, 9, 20, None, None, 15, 7]
        root = Tree().build_tree_from_list(tree)

        self.maxDepth_dfs(root)
        self.maxDepth_bfs(root)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
