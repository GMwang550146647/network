"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""
import time
class Solution():
    def __init__(self):
        pass
    '''1.中心扩展算法'''
    def expandAroundCenter(self,s,left,right):
        len_s=len(s)
        while left>=0 and right<len_s and s[left]==s[right]:
            left-=1
            right+=1
        return left+1,right-1
    def longestPalindrome1(self,s):
        g_s,g_e=0,0
        len_s=len(s)
        for i in range(len_s-1):
            left1,right1=self.expandAroundCenter(s,i,i)
            left2,right2=self.expandAroundCenter(s,i,i+1)
            if right1-left1>g_e-g_s:
                g_s,g_e=left1,right1
            if right2-left2>g_e-g_s:
                g_s,g_e=left2,right2
        return s[g_s:g_e+1]
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
        s='dfkafabcdeedcbadkljflk'
        self.testTime(self.longestPalindrome1,args=(s,))
if __name__=='__main__':
    SL=Solution()
    SL.main()