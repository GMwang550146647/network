from fundamentals.test_time import test_time
from fundamentals.tree import Tree,TreeNode

class Solution():
    def __init__(self):
        pass

    @test_time
    def flipBinaryTree(self, root, leaf):
        new_root=None
        def change(root):
            if root:
                nonlocal new_root
                if new_root:
                    return
                change(root.left)
                if root.val==leaf:
                    new_root=root
                    new_parent=None
                    while root:
                        print(root.parent.val if root.parent else root.parent)
                        if root.parent and root.left and root.left!=new_parent:
                            root.right=root.left
                        tempt=root.parent
                        root.parent=new_parent
                        root.left=tempt
                        new_parent=root
                        root=tempt
                if new_root:
                    return
                change(root.right)
        change(root)
        return new_root

    def main(self):
        root=Tree.build_tree_from_level_recur_list([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        leaf=0
        self.flipBinaryTree(root,leaf)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
