from fundamentals.test_time import test_time
from fundamentals.link_list import LinkList


class Solution():
    def __init__(self):
        pass

    # @test_time
    def reverseList_N_recur(self, head, n=4):
        def reverse(head, n):
            nonlocal successor
            if n == 1:
                successor = head.next
                return head
            last = reverse(head.next, n - 1)
            head.next.next = head
            head.next = successor
            return last

        successor = None
        return reverse(head, n)

    def reverseList_N(self, head, n=4):
        pre = None
        cur = head
        while n > 0:
            n -= 1
            tempt_node = cur.next
            cur.next = pre
            pre = cur
            cur = tempt_node
        head.next=cur
        return pre

    def reverseList_Between_recur(self, head, s=2, e=5):
        def reverse(head, m, n):
            if m == 1:
                return self.reverseList_N_recur(head, n)
            head.next = reverse(head.next, m - 1, n - 1)
            return head

        return reverse(head, s, e)

    def reverseList_Between(self, head, s=2, e=5):
        if s==1:
            return self.reverseList_N(head,e)
        else:
            pt=head
            while(s>2):
                pt=pt.next
                s-=1
                e-=1
            pt.next=self.reverseList_N(pt.next,e-1)
            return head


    def run(self, func):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ll = LinkList().build_link_list(nums).root
        head = func(ll)
        LinkList().show(head)

    def main(self):
        self.run(self.reverseList_N_recur)
        self.run(self.reverseList_Between_recur)
        self.run(self.reverseList_N)
        self.run(self.reverseList_Between)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
