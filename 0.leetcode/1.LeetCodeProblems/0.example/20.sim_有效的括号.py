"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
"""
import time
class Solution():
    def __init__(self):
        pass
    '''我的方法'''
    def myFun(self,s):
        pair = {
            '{': '}',
            '[': ']',
            '(': ')',
            '}': '{',
            ']': '[',
            ')': '(',
        }
        stack = []
        for item in s:
            if len(stack) == 0 or pair[item] != stack[-1]:
                stack.append(item)
            else:
                stack.pop(-1)
        return True if len(stack) == 0 else False
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
        s="{[[]}"
        self.testTime(self.myFun,args=(s,))
if __name__=='__main__':
    SL=Solution()
    SL.main()
