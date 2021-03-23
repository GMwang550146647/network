from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def isSubStructure(self, A,B):
        def is_same_tree(root1,root2):
            if not root2:
                return True
            elif not root1:
                return False
            else:
                return is_same_tree(root1.left,root2.left) and is_same_tree(root1.right,root2.right)
        def recur_tree(root1,root2):
            if not root1:
                return False
            else:
                if root1.val==root2.val:
                    return is_same_tree(root1,root2)
                else:
                    return recur_tree(root1.left,root2) or recur_tree(root1.right,root2)
        if not B:
            return False
        else:
            return recur_tree(A,B)

    def main(self):
        nums = [2, 7, 9, 3, 1]
        self.isSubStructure(nums)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
