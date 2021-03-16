from fundamentals.test_time import test_time
from fundamentals.link_list import LinkList

class Solution():
    def __init__(self):
        pass

    @test_time
    def isPalindrome(self, head):
        """
        非常精彩，但是空间复杂度还是O(N)
        """
        left=head
        def tranverse(right):
            nonlocal left
            if not right:
                return True
            else:
                res=tranverse(right.next)
                res=res and (left.val==right.val)
                left=left.next
                return res
        return tranverse(head)
    def main(self):
        nums = [1,2,3,4,2,1]
        ll=LinkList().build_link_list(nums).root
        self.isPalindrome(ll)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
