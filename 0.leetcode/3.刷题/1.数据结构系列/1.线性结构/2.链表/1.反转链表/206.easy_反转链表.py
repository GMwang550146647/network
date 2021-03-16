from fundamentals.test_time import test_time
from fundamentals.link_list import LinkList


class Solution():
    def __init__(self):
        pass

    # @test_time
    def reverseList(self, head):
        """
        链表反转，循环法
        """

        def reverse(head):
            cur = head
            pre = None
            while cur:
                tempt_node = cur.next
                cur.next = pre
                pre = cur
                cur = tempt_node
            return pre

        return reverse(head)

    # @test_time
    def my_reverseList_recur(self, head):
        """
        链表反转，递归法（我写的，不太优美）
        """

        def reverse(head):
            nonlocal root
            if head is None:
                return None
            cur = head
            if head.next:
                next = reverse(head.next)
                next.next = cur
            else:
                root=cur
            return cur
        if not head:
            return None
        root=None
        reverse(head)
        head.next=None
        return root
    def reverseList_recur(self, head):
        """
        链表反转，递归法（优美版本，不过不快就是了）
        """
        def reverse(head):
            #1.若head本来就是空的，返回空；如果head.next空了，说明这个是尾部，作为头部返回
            if head is None or head.next is None:
                return head
            last=reverse(head.next)
            head.next.next=head
            head.next=None
            return last
        return  reverse(head)
    def main(self):
        nums = [1, 2, 3, 4, 5, 6]
        ll = LinkList().build_link_list(nums).root
        # head = self.reverseList(ll)
        # LinkList().show(head)
        head = self.reverseList_recur(ll)
        LinkList().show(head)
        # head = self.my_reverseList_recur(ll)
        # LinkList().show(head)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
