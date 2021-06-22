from fundamentals.test_time import test_time
from fundamentals.link_list import LinkList

class Solution():
    def __init__(self):
        pass

    # @test_time
    def func(self, head , m , n):
        def reverse(h,t):
            tempt_h=h
            pre,cur,next=None,h,h.next
            cur.next=pre
            while next!=t:
                pre,cur,next=cur,next,next.next
                cur.next=pre
            tempt_h.next=next
            return cur
        # write code here
        slow=fast=head
        if m==n:
            return head
        elif m==1:
            for i in range(n):
                fast=fast.next
            new_head=reverse(head,fast)
            return new_head
        else:
            for i in range(n-m):
                fast=fast.next
            for i in range(m-2):
                fast=fast.next
                slow=slow.next
            next_head=fast.next.next
            new_head=reverse(slow.next,next_head)
            slow.next=new_head
            return head

    def main(self):
        ll=LinkList().build_link_list([1,2,3,4,5])
        result=self.func(ll,2,3)
        result.show()




if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
