from fundamentals.test_time import test_time
from fundamentals.tree import Tree, TreeNode


class Solution():
    def __init__(self):
        pass

    def front_serialize(self, root):
        def front_recur(root):
            if root:
                nums.append(root.val)
                front_recur(root.left)
                front_recur(root.right)
            else:
                nums.append('#')

        nums = []
        front_recur(root)
        return ','.join([str(num) for num in nums])

    def front_deserialize(self, data):
        def build_tree(nums):
            if len(nums) == 0:
                return None
            else:
                root = TreeNode(nums.pop(0))
                if root.val == '#':
                    return None
                root.left = build_tree(nums)
                root.right = build_tree(nums)
                return root

        nums = [int(num) if num != '#' else '#' for num in data.split(',')]
        return build_tree(nums)

    def mid_serialize(self, root):
        def mid_recur(root):
            if root:
                mid_recur(root.left)
                nums.append(root.val)
                mid_recur(root.right)
            else:
                nums.append('#')

        nums = []
        mid_recur(root)
        return ','.join([str(num) for num in nums])

    def mid_deserialize(self, nums):
        """
        不可能实现！放弃吧！
        :param nums:
        :return:
        """

        def build_tree(nums):
            pass

        nums = [int(num) if num != '#' else '#' for num in nums.split(',')]
        return build_tree(nums)

    def back_serialize(self, root):
        def back_recur(root):
            if root:
                back_recur(root.left)
                back_recur(root.right)
                nums.append(root.val)
            else:
                nums.append('#')

        nums = []
        back_recur(root)
        return ','.join([str(num) for num in nums])

    def back_deserialize(self, data):
        def build_tree(nums):
            if len(nums) == 0:
                return None
            else:
                root = TreeNode(nums.pop(-1))
                if root.val == '#':
                    return None
                root.right = build_tree(nums)
                root.left = build_tree(nums)

                return root

        nums = [int(num) if num != '#' else '#' for num in data.split(',')]
        return build_tree(nums)

    def level_serialize(self, root):
        nums = []
        stack = [root]
        while stack:
            cur_node = stack.pop(0)
            if cur_node is None:
                nums.append('#')
            else:
                nums.append(cur_node.val)
                stack.append(cur_node.left)
                stack.append(cur_node.right)
        return ','.join([str(num) for num in nums])

    def level_deserialize(self, data):
        data = [int(num) if num != '#' else '#' for num in data.split(',')]
        if data[0] == '#':
            return None
        root = TreeNode(data[0])
        # 队列存储的都是父节点
        stack = [root]
        cur_index = 1
        while (cur_index < len(data)):
            cur_node = stack.pop(0)
            left_val = data[cur_index]
            right_val = data[cur_index + 1]
            if left_val != '#':
                cur_node.left = TreeNode(left_val)
                stack.append(cur_node.left)
            else:
                cur_node.left = None
            if right_val != '#':
                cur_node.right = TreeNode(right_val)
                stack.append(cur_node.right)
            else:
                cur_node.right = None
            cur_index += 2

        return root

    def main(self):
        nums = []
        root = Tree().build_tree_from_list(nums)
        Tree().mid_recur_tree(root)
        nums = self.front_serialize(root)
        root = self.front_deserialize(nums)
        print(nums)
        # nums = self.mid_serialize(root)
        # root = self.mid_deserialize(nums)
        nums = self.back_serialize(root)
        root = self.back_deserialize(nums)
        nums = self.level_serialize(root)
        root = self.level_deserialize(nums)
        print(nums)
        Tree().mid_recur_tree(root)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
