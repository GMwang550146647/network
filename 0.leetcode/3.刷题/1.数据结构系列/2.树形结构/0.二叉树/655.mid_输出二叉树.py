from fundamentals.test_time import test_time
from fundamentals.tree import Tree
import sys

sys.setrecursionlimit(10000)


class Solution():
    def __init__(self):
        pass

    @test_time
    def printTree(self, root):
        tree_nodes = [[root.val]]
        stack = [root]
        while stack:
            len_stack = len(stack)

            all_next_nodes = []
            for i in range(len_stack):
                current_node = stack.pop(0)
                if current_node.left:
                    stack.append(current_node.left)
                    all_next_nodes.append(current_node.left.val)
                else:
                    all_next_nodes.append('')
                if current_node.right:
                    stack.append(current_node.right)
                    all_next_nodes.append(current_node.right.val)
                else:
                    all_next_nodes.append('')
            tree_nodes.append(all_next_nodes)
        print(tree_nodes)

    def main(self):
        tree = [1, 2, 3, None, 4, None, None]
        root=Tree().build_tree_from_list(tree)
        Tree().mid_recur_tree(root)
        self.printTree(root)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
