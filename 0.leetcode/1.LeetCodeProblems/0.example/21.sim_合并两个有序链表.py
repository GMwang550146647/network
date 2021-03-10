"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

"""
import time
class Solution():
    def __init__(self):
        pass
    '''我的方法'''

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur = head = ListNode()
        while l1 and l2:
            if l1.val >= l2.val:
                cur.next = ListNode(l2.val)
                cur = cur.next
                l2 = l2.next
            else:
                cur.next = ListNode(l1.val)
                l1 = l1.next
                cur = cur.next
        if l1 == None:
            cur.next = l2
        else:
            cur.next = l1
        return head.next
    '''答案方法1'''

    def testTime(self,fun,args):
        # 计时
        start = time.process_time()
        result = fun(*args)
        elapsed = (time.process_time() - start)
        print(fun.__name__,":")
        print("Time used:", elapsed)
        print('result:', result)
    def main(self):
        s='dfkljal'
        self.testTime(self.myFun,args=(s,))
if __name__=='__main__':
    SL=Solution()
    SL.main()
