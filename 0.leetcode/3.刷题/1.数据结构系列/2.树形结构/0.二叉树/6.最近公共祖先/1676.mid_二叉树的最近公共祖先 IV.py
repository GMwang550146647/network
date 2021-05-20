from fundamentals.test_time import test_time
from fundamentals.tree import Tree

class Solution():
    def __init__(self):
        pass

    @test_time
    def func(self,root,nodes):
        def search(root):
            if not root or root.val in nodes:
                return root
            else:
                left=search(root.left)
                right=search(root.right)
                if left and right:
                    return root
                else:
                    return left if left else right
        nodes=set(nodes)
        return search(root)

    def main(self):
        root=Tree().build_tree_from_level_recur_list([3,5,1,6,2,0,8,None,None,7,4])
        nodes=[1,4,7]
        self.func(root,nodes)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
