'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

import time
class Solution():
    def __init__(self):
        self.sortedlist1=[1,4,6,7,8,10,19]
        self.sortedlist2=[2,3,5,6,7,8,9,18,50]

    '''我的方法'''
    def myFun(self):
        P1=0
        P2=0
        result=[]
        len1=len(self.sortedlist1)
        len2=len(self.sortedlist2)
        while(P1<len1 and P2<len2):
            if self.sortedlist1[P1]>=self.sortedlist2[P2]:
                result.append(self.sortedlist2[P2])
                P2+=1
            else:
                result.append(self.sortedlist1[P1])
                P1+=1
            if P2==len2:
                result.extend(self.sortedlist1[P1:])
            if P1==len1:
                result.extend(self.sortedlist2[P2:])
        return result
    '''答案方法1'''

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