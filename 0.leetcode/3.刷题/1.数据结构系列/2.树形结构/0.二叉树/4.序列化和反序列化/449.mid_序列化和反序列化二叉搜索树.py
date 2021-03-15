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

    def front_deserialize(self, nums):
        def build_tree(nums):
            if len(nums) == 0:
                return None
            else:
                if nums[0] == '#':
                    return None
                root = TreeNode(nums.pop(0))
                root.left = build_tree(nums)
                root.right = build_tree(nums)
                return root

        nums = [int(num) if num != '#' else '#' for num in nums.split(',')]
        return build_tree(nums)

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

    def back_deserialize(self, nums):
        def build_tree(nums):
            if len(nums) == 0:
                return None
            else:
                if nums[-1] == '#':
                    return None
                root = TreeNode(nums.pop(-1))
                root.right = build_tree(nums)
                root.left = build_tree(nums)

                return root

        nums = [int(num) if num != '#' else '#' for num in nums.split(',')]
        return build_tree(nums)

    def main(self):
        nums = [1, 2, 3, None, 4]
        root = Tree().build_tree_from_list(nums)
        Tree().mid_recur_tree(root)
        nums = self.front_serialize(root)
        root = self.front_deserialize(nums)
        # nums = self.mid_serialize(root)
        # root = self.mid_deserialize(nums)
        nums = self.back_serialize(root)
        root = self.back_deserialize(nums)
        print(nums)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
