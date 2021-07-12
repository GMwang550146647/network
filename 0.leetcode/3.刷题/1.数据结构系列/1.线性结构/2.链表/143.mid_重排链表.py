from fundamentals.test_time import test_time
from fundamentals.link_list import ListNode, LinkList


class Solution():
    def __init__(self):
        pass

    # @test_time
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def reverse_list(h):
            pre, cur = None, h
            while cur:
                tempt = cur.next
                cur.next = pre
                pre, cur = cur, tempt
            return pre

        def split_linklist(h):
            slow = fast = h
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            if fast:
                slow = slow.next
            return h, reverse_list(slow)

        if not head or not head.next:
            return head
        h1, h2 = split_linklist(head)
        new_head = h1

        while h2:
            # print(h1.val,h2.val)
            h1.next, h1 = h2, h1.next
            h2.next, h2 = h1, h2.next
        if h1.next.next == h1:
            h1.next = None
        if h2 and h2.next == h2:
            h2.next = None
        return new_head

    def main(self):
        arr = [1, 2, 3, 4, 5]
        head = LinkList().build_link_list(arr)
        result = self.reorderList(head)
        LinkList().show(result)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
