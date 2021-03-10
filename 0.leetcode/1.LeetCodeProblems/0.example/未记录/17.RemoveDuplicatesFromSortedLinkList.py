'''
Given a sorted linked list, delete all duplicates such that each element appear only once .

Example 1:

Input: 1->1->2
Output: 1->2

Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
'''
import time
class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution():
    def __init__(self):
        self.num=[1,2,2,3,4,4,4,5,5,5,6,6,7,7]
    '''我的方法'''
    def myFun(self):
        pass
    '''答案方法1'''
    def deleteDuplicates(self,head):
        dummy=ListNode(None)
        dummy.next=head
        p=dummy
        while p and p.next:
            if p.val==p.next.val:
                p.next=p.next.next
            else:
                p=p.next
        return dummy.next
    def testTime(self,fun):
        # 计时
        start = time.process_time()
        result = fun()
        elapsed = (time.process_time() - start)
        print(fun.__name__,":")
        print("Time used:", elapsed)
        print('result:', result)
    def main(self):
        self.testTime(self.myFun)
SL=Solution()
SL.main()