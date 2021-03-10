'''
Implement strStr() .

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf() .
'''
import time
class Solution():
    def __init__(self):
        self.haystack='afjlajldjncv,ndkhaljekjafnkeljelrjlndmn,mcnzkjhfaflkjajljiuieonaknjlkjhello'
        self.needle='ll'

    '''我的方法'''
    def myFun(self):
        lenHay=len(self.haystack)
        lenNee=len(self.needle)
        for i in range(lenHay-lenNee+1):
            flag=1
            for j in range(lenNee):
                if self.needle[j]!=self.haystack[i+j]:
                    flag=-1
                    break
            if flag==1:
                return i
        return -1

    '''答案方法1'''
    def strStr(self):
        lenHay = len(self.haystack)
        lenNee = len(self.needle)
        if lenHay==lenNee:
            if self.haystack==self.needle:
                return 0
            else:
                return -1
        for i in range(lenHay):
            k=i
            j=0
            while(j<lenNee) and k<lenHay and self.haystack[k]==self.needle[j]:
                j+=1
                k+=1
            if j==lenNee:
                return i
        return -1 if self.needle else 0
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
        self.testTime(self.strStr)
SL=Solution()
SL.main()