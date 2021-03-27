from fundamentals.test_time import test_time
from fundamentals.tree import Tree

class Solution():
    def __init__(self):
        pass

    @test_time
    def verifyPostorder(self, postorder):
        def build_tree(nums):
            if len(nums)<=1:
                return True
            else:
                mid=nums[-1]
                for i in range(len(nums)):
                    left=nums[:i]
                    right=nums[i:-1]
                    if not left:
                        if min(right)>mid:
                            if build_tree(right):
                                return True
                    elif not right:
                        if max(left)<mid:
                            if build_tree(left):
                                return True
                    else:
                        if min(right)>mid>max(left):
                            if build_tree(left) and build_tree(right):
                                return True
                return False
        return build_tree(postorder)

    def main(self):
        nums =  [1,3,2,6,5]
        self.verifyPostorder(nums)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
