from fundamentals.test_time import test_time
from fundamentals.tree import Tree


class Solution():
    def __init__(self):
        pass

    @test_time
    def isBalanced(self, root):
        def depth_of_root(root):
            if not root:
                return 0
            else:
                left_depth = depth_of_root(root.left)
                right_depth = depth_of_root(root.right)
                if type(left_depth) == bool or type(right_depth) == bool:
                    return False
                elif abs(left_depth - right_depth) > 1:
                    return False
                else:
                    return max(left_depth, right_depth) + 1

        result = depth_of_root(root)
        return result if type(result) == bool else True

    def main(self):
        nums = [2, 7, 9, 3, 1]
        root = Tree().build_tree_from_list(nums)
        self.isBalanced(root)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
