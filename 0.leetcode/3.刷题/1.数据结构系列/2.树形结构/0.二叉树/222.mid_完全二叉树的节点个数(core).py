from fundamentals.test_time import test_time
from fundamentals.tree import Tree

class Solution():
    def __init__(self):
        pass

    @test_time
    def countNodes(self, root):
        """
        必须要完全二叉树才有这个特点，差1
        """
        def count(root):
            l=r=root
            hl=hr=0
            while(l):
                l=l.left
                hl+=1
            while(r):
                r=r.right
                hr+=1
            if hr==hl:
                return 2**hl-1
            else:
                return 1+count(root.left)+count(root.right)
        return count(root)


    def main(self):
        nums = [1, 2, 3, 4, 5, 6]
        root=Tree().build_tree_from_list(nums)
        Tree().mid_recur_tree(root)
        self.countNodes(root)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
