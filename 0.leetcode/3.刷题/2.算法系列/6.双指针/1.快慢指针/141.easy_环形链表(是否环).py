from fundamentals.link_list import LinkList
from fundamentals.test_time import test_time

class Solution():
    def __init__(self):
        pass

    '''我的方法'''
    @test_time
    def hasCycle(self, head):
        p_fast=head
        p_slow=head
        while(p_fast and p_fast.next and p_slow):
            p_fast=p_fast.next.next
            p_slow=p_slow.next
            if p_fast==p_slow:
                return True
        return False

    def main(self):
        head = [3, 2, 0, -4]
        pos = 1
        root=LinkList().build_link_list(head,pos).root
        self.hasCycle(root)
if __name__ == '__main__':
    SL = Solution()
    SL.main()
