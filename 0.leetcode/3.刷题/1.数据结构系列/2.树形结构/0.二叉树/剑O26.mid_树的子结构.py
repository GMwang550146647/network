from fundamentals.test_time import test_time
from fundamentals.tree import Tree


class Solution():
    def __init__(self):
        pass

    @test_time
    def isSubStructure(self, A, B):
        def is_same_tree(root1, root2):
            if not root2:
                return True
            elif not root1:
                return False
            else:
                return root1.val == root2.val and is_same_tree(root1.right, root2.right) \
                       and is_same_tree(root1.left,root2.left)

        def recur_tree(root1, root2):
            if not root1:
                return False
            else:
                return is_same_tree(root1, root2) or recur_tree(root1.left, root2) or recur_tree(root1.right, root2)

        if not B:
            return False
        else:
            return recur_tree(A, B)

    def main(self):
        nums1 = [4, 2, 3, 4, 5, 6, 7, 8, 9]
        nums2 = [4, 8, 9]
        root1 = Tree().build_tree_from_list(nums1)
        root2 = Tree().build_tree_from_list(nums2)
        print("#####################")
        Tree().mid_recur_tree(root1)
        print("#####################")
        Tree().mid_recur_tree(root2)
        print("#####################")
        self.isSubStructure(root1, root2)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
