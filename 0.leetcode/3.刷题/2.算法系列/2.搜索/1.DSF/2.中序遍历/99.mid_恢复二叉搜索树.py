from fundamentals.tree import TreeNode, Tree
import time


class Solution():
    def __init__(self):
        pass

    '''我的方法'''

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
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
                print(record)
        record[0].val, record[-1].val = [record[-1].val, record[0].val]
        return tempt_list[0]

    '''答案方法1'''

    def testTime(self, fun, args):
        # 计时
        start = time.process_time()
        result = fun(*args)
        elapsed = (time.process_time() - start)
        print(fun.__name__, ":")
        print("Time used:", elapsed)
        print(Tree().mid_recur_tree(result))

    def main(self):
        root = [1, 3, None, None, 2]
        root = Tree().build_tree_from_list(root)
        Tree().mid_recur_tree(root)
        self.testTime(self.recoverTree, args=(root,))


if __name__ == '__main__':
    SL = Solution()
    SL.main()
