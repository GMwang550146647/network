from fundamentals.test_time import test_time
from fundamentals.link_list import LinkList, ListNode


class Solution():
    def __init__(self):
        pass

    @test_time
    def deleteDuplicates(self, head):
        # write code here
        new_node = ListNode('Head')
        new_node.next = head
        cur = new_node
        same_val = None
        while cur:
            if cur.next and cur.next.next and cur.next.val == cur.next.next.val:
                same_val = cur.next.val
                while cur.next and cur.next.val == same_val:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return new_node.next

    def main(self):
        head = LinkList().build_link_list([-50,-50,-49,-49,-49,-47,-46])
        result = self.deleteDuplicates(head)
        LinkList().show(result)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
