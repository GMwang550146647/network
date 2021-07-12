from fundamentals.test_time import test_time
from fundamentals.link_list import LinkList, ListNode


class Solution():
    def __init__(self):
        pass

    @test_time
    def oddEvenList(self, head):
        '''
        把值交换
        '''
        even_vals = []
        fast = slow = head
        i = 1
        while fast:
            # 奇数应该令 slow.val=
            if i % 2 == 1:
                slow.val = fast.val
                slow = slow.next
            else:
                even_vals.append(fast.val)
            i += 1
            fast = fast.next
        j = 0
        while slow:
            slow.val = even_vals[j]
            j += 1
            slow = slow.next
        return head

    def oddEvenList2(self, head: ListNode) -> ListNode:
        '''
        把链表节点交换
        '''
        # write code here
        if not head or not head.next:
            return head
        odd_point = head
        e_head = even_point = head.next
        cur_point = head.next.next
        i = 3
        while cur_point:
            if i % 2 == 0:
                even_point.next = cur_point
                even_point = cur_point
            else:
                odd_point.next = cur_point
                odd_point = cur_point
            i += 1
            cur_point = cur_point.next
        odd_point.next = e_head
        even_point.next = None
        return head

    def main(self):
        head = LinkList().build_link_list([1, 2, 3, 4, 5, 6])
        result = self.oddEvenList(head)
        result = self.oddEvenList2(head)
        LinkList().show(result)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
