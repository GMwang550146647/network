from fundamentals.test_time import test_time
from fundamentals.link_list import LinkList, ListNode
from functools import reduce

from heapq import *


class Solution():
    def __init__(self):
        pass

    @test_time
    def mergeKLists(self, lists):
        """
        不停地归并排序
        """

        def combine_two_list(head1, head2):
            head = tempt_p = ListNode(0)
            while head1 and head2:
                if head1.val <= head2.val:
                    tempt_p.next = head1
                    tempt_p = head1
                    head1 = head1.next
                else:
                    tempt_p.next = head2
                    tempt_p = head2
                    head2 = head2.next
            if head1:
                tempt_p.next = head1
            else:
                tempt_p.next = head2
            return head.next

        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            lt = lists
            while len(lt) > 1:
                new_lt = []
                for i in range(len(lt) // 2):
                    new_lt.append(combine_two_list(lt[2 * i], lt[2 * i + 1]))
                if len(lt) % 2 == 1:
                    new_lt.append(lt[-1])
                lt = new_lt
        return lt[0]

    @test_time
    def mergeKLists_heap(self, lists):
        """
        全部丢到堆中
        """
        if not lists or len(lists) == 0:
            return None

        heap = []
        # 首先 for 嵌套 while 就是将所有元素都取出放入堆中
        for node in lists:
            while node:
                heappush(heap, node.val)
                node = node.next
        dummy = ListNode(None)
        cur = dummy
        # 依次将堆中的元素取出(因为是小顶堆，所以每次出来的都是目前堆中值最小的元素），然后重新构建一个列表返回
        while heap:
            temp_node = ListNode(heappop(heap))
            cur.next = temp_node
            cur = temp_node
        return dummy.next

    def main(self):
        lists = [[], [-1, 5, 11], [], [6, 10]]
        lists = [LinkList().build_link_list(listi).root for listi in lists]
        result = self.mergeKLists(lists)
        result = self.mergeKLists_heap(lists)
        LinkList().show(result)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
