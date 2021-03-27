from fundamentals.test_time import test_time
from fundamentals.link_list import LinkList, ListNode


class Solution():
    def __init__(self):
        pass

    # @test_time
    def reverseKGroup_recur(self, head, k):
        """
        递归比较优美
        """

        def reverse(lp, rp):
            """
            翻转 [lp ,rp) 的序列（不包含rp)
            """
            pre = None
            cur = lp
            while cur != rp:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            return pre

        def reverseK(head, k):
            if head is None:
                return None
            else:
                a = b = head
                # 不足个数的时候结束
                for i in range(k):
                    if not b:
                        return head
                    b = b.next
                new_head = reverse(a, b)
                a.next = reverseK(b, k)
                return new_head

        return reverseK(head, k)

    def reverseKGroup(self, head, k):
        """
        循环比较恶心
        """

        def reverse(lp, rp):
            """
            翻转 [lp ,rp) 的序列（不包含rp)
            """
            pre = None
            cur = lp
            while cur != rp:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            return pre

        def reverseK(head, k):
            a = b = head
            flag = True
            pre_tail = None
            final_head = None
            while flag:
                for i in range(k):
                    if b is None:
                        if pre_tail:
                            pre_tail.next = a
                        else:
                            final_head = a
                        flag = False
                        break
                    b = b.next
                if flag:
                    new_head = reverse(a, b)
                    if pre_tail:
                        pre_tail.next = new_head
                    else:
                        final_head = new_head
                    pre_tail = a
                    a = b
            return final_head

        return reverseK(head, k)

    def main(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        k = 3
        head = LinkList().build_link_list(nums).root
        LinkList().show(head)
        head = self.reverseKGroup_recur(head, k)
        LinkList().show(head)
        head = LinkList().build_link_list(nums).root
        head = self.reverseKGroup(head, k)
        LinkList().show(head)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
