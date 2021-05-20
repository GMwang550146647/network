from fundamentals.test_time import test_time
from fundamentals.tree import Tree


class Solution():
    def __init__(self):
        pass

    @test_time
    def lowestCommonAncestor(self, p, q):
        """
        原理：两个链表的最近交点位置
        """
        def count_parents(head):
            count=0
            while head.parent:
                head=head.parent
                count+=1
            return count
        count_p=count_parents(p)
        count_q=count_parents(q)
        p,q=(p,q) if count_p>=count_q else (q,p)
        for i in range(abs(count_p-count_q)):
            p=p.parent
        while p and q:
            if p==q:
                return p
            p=p.parent
            q=q.parent
        return None





if __name__ == '__main__':
    SL = Solution()

