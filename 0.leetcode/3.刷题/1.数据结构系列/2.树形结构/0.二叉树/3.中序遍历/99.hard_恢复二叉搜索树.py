from fundamentals.test_time import test_time
from fundamentals.tree import Tree

class Solution():
    def __init__(self):
        pass

    # @test_time
    def recoverTree(self, root):
        """
        中序遍历，再修改 错误位置
        """
        tempt_list = []

        def mid_recur_tree(root):
            if root is not None:
                mid_recur_tree(root.left)
                tempt_list.append(root)
                mid_recur_tree(root.right)
        mid_recur_tree(root)
        record = []
        for i in range(len(tempt_list) - 1):
            if tempt_list[i].val > tempt_list[i + 1].val:
                record.append(tempt_list[i])
                record.append(tempt_list[i + 1])
        record[0].val, record[-1].val = record[-1].val, record[0].val
        return tempt_list[0]

    def main(self):
        nums = [1,3,None,None,2,None,None]
        root=Tree().build_tree_from_list(nums)
        Tree().mid_recur_tree(root)
        print(self.recoverTree(root))


if __name__ == '__main__':
    SL = Solution()
    SL.main()
