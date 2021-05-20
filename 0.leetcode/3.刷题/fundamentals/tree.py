class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right


class Tree():
    @staticmethod
    def build_tree_from_level_recur_list(tree_list):
        root = TreeNode(tree_list[0])
        stack = [root]
        index = 0
        while stack and index + 2 < len(tree_list):
            for i in range(len(stack)):
                cur_node = stack.pop(0)
                if tree_list[index + 1] is not None:
                    left = TreeNode(tree_list[index + 1])
                    cur_node.left = left
                    stack.append(left)
                if tree_list[index + 2] is not None:
                    right = TreeNode(tree_list[index + 2])
                    cur_node.right = right
                    stack.append(right)
                index += 2
                if index >= len(tree_list) - 1:
                    break
        return root

    def build_tree_from_list(self, tree_list, current_index=0):
        if len(tree_list) == 0:
            return None
        if current_index >= len(tree_list):
            return None
        # 防止该节点是None的时候
        if tree_list[current_index] is None:
            return None
        root = TreeNode(tree_list[current_index])
        root.left = self.build_tree_from_list(tree_list, current_index=current_index * 2 + 1)
        root.right = self.build_tree_from_list(tree_list, current_index=current_index * 2 + 2)
        return root

    @staticmethod
    def mid_recur_tree(root, depth=0):
        if root is None:
            return None
        Tree.mid_recur_tree(root.left, depth + 1)
        print('\t' * depth + str(root.val))
        Tree.mid_recur_tree(root.right, depth + 1)


if __name__ == '__main__':
    tree_list = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    tree = Tree.build_tree_from_level_recur_list(tree_list)
    Tree().mid_recur_tree(tree)
