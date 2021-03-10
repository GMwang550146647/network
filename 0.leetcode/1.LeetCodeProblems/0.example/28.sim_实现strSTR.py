"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1

"""

import time
class Solution():
    def __init__(self):
        pass
    '''我的方法'''
    def myFun(self,haystack, needle):
        pass
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
        haystack='hello'
        needle='ll'
        self.testTime(self.myFun,args=(haystack, needle,))
if __name__=='__main__':
    SL=Solution()
    SL.main()
