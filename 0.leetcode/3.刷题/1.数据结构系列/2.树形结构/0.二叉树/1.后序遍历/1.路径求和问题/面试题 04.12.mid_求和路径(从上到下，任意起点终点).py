from fundamentals.test_time import test_time
from fundamentals.tree import Tree


class Solution():
    def __init__(self):
        pass

    @test_time
    def pathSum(self, root, Sum):
        """

        :param root:
        :param Sum:
        :return:
        """
        def recur(root):
            if not root:
                return []
            else:
                childs = recur(root.left) + recur(root.right)
                all_sum = [root.val + k for k in childs] + [root.val]
                nonlocal count
                for i in all_sum:
                    if i == Sum:
                        count += 1
                return all_sum

        count = 0
        recur(root)
        return count

    def main(self):
        root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
        Sum = 22
        root = Tree().build_tree_from_level_recur_list(root)
        self.pathSum(root, Sum)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
