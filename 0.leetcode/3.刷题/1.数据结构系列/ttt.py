from fundamentals.test_time import test_time
from fundamentals.tree import  TreeNode,Tree

class Solution():
    def __init__(self):
        pass

    def Serialize(self, root):
        # write code here
        def dfs(root, cur_s=[]):
            if not root:
                return cur_s + ['#']
            else:
                cur_s += [str(root.val)]
                cur_s = dfs(root.left, cur_s)
                cur_s = dfs(root.right, cur_s)
                return cur_s

        return ','.join(dfs(root, []))

    def Deserialize(self, s):
        # write code here
        trs = s.split(',')

        def build_tree(trs):
            if not trs:
                return None
            else:
                val = trs.pop(0)
                if val == '#':
                    return None
                else:
                    root = TreeNode(val)
                    root.left = build_tree(trs)
                    root.right = build_tree(trs)
                    return root

        return build_tree(trs)

    def main(self):
        tree=[8,6,10,5,7,9,11]
        root=Tree().build_tree_from_level_recur_list(tree)

        str_tree=self.Serialize(root)
        print(str_tree)
        new_root=self.Deserialize(str_tree)
        Tree().mid_recur_tree(new_root)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
