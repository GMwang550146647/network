'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1. 1
2. 11
3. 21
4. 1211
5. 111221

1 is read off as "one 1" or 11 .
11 is read off as "two 1s" or 21 .
21 is read off as "one 2 , then one 1" or 1211 .

Given an integer n , generate the n th term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"

Example 2:

Input: 4
Output: "1211"
'''
import time
class Solution():
    def __init__(self):
        self.num=100

    '''我的方法'''
    def myFun(self,n):
        stri='1'
        if n==1:
            return stri
        for i in range(1,n):
            pre=stri[0]
            tempt = []
            count=0
            length=len(stri)
            for j in range(length):
                #如果是最后一个
                if j==length-1 and pre==stri[j]:
                    count+=1
                    tempt.append(str(count))
                    tempt.append(pre)
                elif j==length-1 and pre!=stri[j]:
                    tempt.extend([str(count),pre,'1',stri[j]])
                elif pre==stri[j]:
                    count+=1
                else:
                    tempt.extend([str(count),pre])
                    pre=stri[j]
                    count=1
            stri=''.join(tempt)
            # print(i,":",stri)
        return stri



    '''答案方法1'''
    def countAndSay(self,n):
        ans='1'
        n-=1
        while n>0:
            res=''
            pre=ans[0]
            count=1
            for i in range(1,len(ans)):
                if pre==ans[i]:
                    count+=1
                else:
                    res+=str(count)+pre
                    pre=ans[i]
                    count=1
            res+=str(count)+pre
            ans=res
            n-=1
        return ans
    def testTime(self,fun,num):
        # 计时
        start = time.process_time()
        result = fun(num)
        elapsed = (time.process_time() - start)
        print(fun.__name__,":")
        print("Time used:", elapsed)
        # print('result:', result)
    def main(self):
        self.testTime(self.myFun,50)
        self.testTime(self.countAndSay,50)
SL=Solution()
SL.main()