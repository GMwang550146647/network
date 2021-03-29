from fundamentals.test_time import test_time
from fundamentals.tree import Tree


class Solution():
    def __init__(self):
        pass

    @test_time
    def inorderTraversal(self, root):
        """
        中序遍历！栈实现
        """
        left_nodes = []
        node = root
        result = []
        while left_nodes or node:
            while node:
                left_nodes.append(node)
                node = node.left
            node = left_nodes.pop()
            result.append(node.val)
            node = node.right

        return result

    def main(self):
        root = [1, None, 2, None, None, 3]
        root = Tree().build_tree_from_list(root)
        self.inorderTraversal(root)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
