"""
示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import time
class Solution():
    def __init__(self):
        pass
    '''1.转换成 char类型'''
    def myFun(self,x):
        str_x = str(x)
        len_x = len(str_x)
        flag = 1
        for i in range(len_x // 2):
            if str_x[i] != str_x[len_x - 1 - i]:
                flag = 0
                break
        return True if flag == 1 else False
    '''答案方法1'''
    def myFun1(self,x):
        lt=[]
        while x>0:
            lt.append(x%10)
            x=x//10
        flag = 1
        len_x=len(lt)
        for i in range(len_x // 2):
            if lt[i] != lt[len_x - 1 - i]:
                flag = 0
                break
        return True if flag == 1 else False
    def testTime(self,fun,args):
        # 计时
        start = time.process_time()
        result = fun(*args)
        elapsed = (time.process_time() - start)
        print(fun.__name__,":")
        print("Time used:", elapsed)
        print('result:', result)
    def main(self):
        x=41221438914797329791837498749817398749812789
        self.testTime(self.myFun, args=(x,))

        self.testTime(self.myFun, args=(x,))
        self.testTime(self.myFun1, args=(x,))



if __name__=='__main__':
    SL=Solution()
    SL.main()
