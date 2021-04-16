from fundamentals.test_time import test_time
from fundamentals.tree import Tree


class Solution():
    def __init__(self):
        pass

    @test_time
    def pathSum(self, root, targetSum):
        """
        每个节点返回该节点所有的可能！
        """

        def recur(root):
            if not root:
                return []
            else:
                childs = recur(root.left) + recur(root.right)
                all_sum = [root.val + k for k in childs] + [root.val]
                nonlocal count
                for i in all_sum:
                    if i == targetSum:
                        count += 1
                return all_sum

        count = 0
        recur(root)
        return count

    @test_time
    def pathSum_prefix(self, root, targetSum):
        """
        前缀和
        """

        def recur(root, prefix):
            if root:
                prefix.append(root.val + prefix[-1])
                nonlocal count
                for i in range(len(prefix) - 1):
                    if prefix[-1] - prefix[i] == targetSum:
                        count += 1
                if root.left:
                    recur(root.left, prefix)
                if root.right:
                    recur(root.right, prefix)
                prefix.pop(-1)

        count = 0
        recur(root, [0])
        return count

    def main(self):
        root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
        Sum = 22
        root = Tree().build_tree_from_level_recur_list(root)
        self.pathSum(root, Sum)
        self.pathSum_prefix(root, Sum)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
