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
        left = head

        def tranverse(right):
            nonlocal left
            if not right:
                return True
            else:
                res = tranverse(right.next)
                res = res and (left.val == right.val)
                left = left.next
                return res

        return tranverse(head)

    @test_time
    def isPalindrome_o1(self, head):
        '''
        先反转链表，再计算是否相同
        '''

        def reverse(head):
            cur = head
            pre = None
            while cur:
                tempt_node = cur.next
                cur.next = pre
                pre = cur
                cur = tempt_node
            return pre

        fast_pt = slow_pt = head
        while (fast_pt and fast_pt.next):
            fast_pt = fast_pt.next.next
            slow_pt = slow_pt.next
        # 奇数情况的时候，slow要再向前一步
        if fast_pt:
            slow_pt = slow_pt.next
        tail = reverse(slow_pt)
        while tail is not None:
            if tail.val != head.val:
                return False
            tail = tail.next
            head = head.next
        return True

    def main(self):
        nums = [1, 2, 3, 4, 2, 1]
        ll = LinkList().build_link_list(nums).root
        self.isPalindrome(ll)
        self.isPalindrome_o1(ll)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
