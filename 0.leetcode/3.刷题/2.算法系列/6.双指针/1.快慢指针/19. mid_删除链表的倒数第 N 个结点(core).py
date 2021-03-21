from fundamentals.link_list import LinkList
from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    '''我的方法'''

    @test_time
    def removeNthFromEnd(self, head, n):
        p_slow = p_fast = head
        for _ in range(n): p_fast = p_fast.next
        # 再也不能向后移动了（也就是删除头结点）
        if not p_fast:
            return head.next
        else:
            while (p_fast.next):
                p_fast = p_fast.next
                p_slow = p_slow.next
            p_slow.next = p_slow.next.next
            return head

    def main(self):
        head = [1, 2, 3, 4, 5]
        n = 2
        root = LinkList().build_link_list(head).root
        self.removeNthFromEnd(root, n)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
