"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
import time
from utility.linklist import *
class Solution():
    def __init__(self):
        self.num=19235713

    '''我的方法'''
    def myFun(self,l1,l2):
        current=head=Node(0)
        carry=0
        # carry 是进位，如果l1和l2都空，但是有进位的话还是要进位！
        while l1 or l2 or carry:
            tempt_value=(l1.value if l1!=None else 0)+(l2.value if l2!=None else 0)+carry
            carry=tempt_value//10
            current.next=Node(tempt_value%10)
            l1=l1.next if l1!=None else None
            l2=l2.next if l2!=None else None
            current=current.next
        return head.next
    '''答案方法1'''

    def addTwoNumbers(self, l1, l2):
        p = dummy = Node(-1)
        carry = 0
        while l1 or l2 or carry:
            value = (l1 and l1.value or 0) + (l2 and l2.value or 0) + carry
            carry = value // 10
            p.next = Node(value % 10)
            l1 = l1 and l1.next
            l2 = l2 and l2.next
            p = p.next
        return dummy.next

    def testTime(self,fun,args):
        # 计时
        start = time.process_time()
        result = fun(*args)
        elapsed = (time.process_time() - start)
        print(fun.__name__,":")
        print("Time used:", elapsed)
        print('result:', result)
        while result !=None:
            print(result.value)
            result=result.next
    def main(self):
        l1=[2,4,3]
        l2=[5,9,8,9,3]
        ll1=UnorderedList()
        ll2=UnorderedList()
        for item in l1:
            ll1.append(item)
        for item in l2:
            ll2.append(item)
        self.testTime(self.addTwoNumbers,args=(ll1.head,ll2.head))
        self.testTime(self.myFun, args=(ll1.head, ll2.head))
if __name__=='__main__':
    SL=Solution()
    SL.main()