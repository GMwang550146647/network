# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkList():
    @staticmethod
    def build_link_list(arr):
        head = pt = ListNode()
        for numi in arr:
            pt.next = ListNode(numi)
            pt = pt.next
        return head.next

    @staticmethod
    def show(head):
        while head:
            print(head.val, end=' ')
            head = head.next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = pre = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                pre.next = l1
                pre = l1
                l1 = l1.next
            else:
                pre.next = l2
                pre = l2
                l2 = l2.next
        if not l1:
            pre.next = l2
        else:
            pre.next = l1
        return head.next


if __name__ == '__main__':
    l1 = [1,1,1,1,1,1,1,1,1]
    l2 = [0,1,1,1,2,2,2,2,2,4,4,4,5]
    head1 = LinkList().build_link_list(l1)
    head2 = LinkList().build_link_list(l2)
    combined_head = Solution().mergeTwoLists(head1, head2)
    LinkList().show(combined_head)



