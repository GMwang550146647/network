from fundamentals.test_time import test_time
from fundamentals.tree import Tree,TreeNode


class Solution():
    def __init__(self):
        pass

    @test_time
    def lowestCommonAncestor(self, root, p, q):
        """
        找到就返回
        """
        target_node=None
        def find(root):
            if not root:
                return False
            else:
                nonlocal target_node
                if target_node is not None:
                    return False
                total=find(root.left) +find(root.right) +(root.val==p.val or root.val==q.val)
                if total>=2:
                    target_node=root
                    return True
                elif total==1:
                    return True
                else:
                    return False
        find(root)
        return target_node


    def main(self):
        root = [3,5,1,6,2,0,8,None,None,7,4]
        p = TreeNode(5)
        q = TreeNode(1)
        root = Tree().build_tree_from_level_recur_list(root)
        Tree().mid_recur_tree(root)
        self.lowestCommonAncestor(root, p, q)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
