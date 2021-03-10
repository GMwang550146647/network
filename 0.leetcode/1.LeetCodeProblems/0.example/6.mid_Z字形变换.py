"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
"""
import time


class Solution():
    def __init__(self):
        pass

    '''1.效率非常低'''

    def myFun(self, s, numRows=3):
        len_s = len(s)
        if len_s <= numRows or numRows==1:
            return s
        total_i = -1

        # 一共有这么多个循环
        for iters in range(1, 100):
            if numRows + iters * (2 * numRows - 2) >= len_s:
                total_i = iters+1
                break
        new_s = ''
        for rowi in range(numRows):
            new_s+=s[rowi]
            for iteri in range(1,total_i):
                if rowi == 0 or rowi == numRows - 1:
                    new_s += s[iteri * (2 * numRows - 2) + rowi] if iteri * (2 * numRows - 2) + rowi < len_s else ''
                else:
                    new_s += s[iteri * (2 * numRows - 2) - rowi] if iteri * (2 * numRows - 2) - rowi < len_s else ''
                    new_s += s[iteri * (2 * numRows - 2) + rowi] if iteri * (2 * numRows - 2) + rowi < len_s else ''
        return new_s
    '''答案方法1,'''
    def convert(self,s,numRows=3):
        rn=['']*numRows
        n_per=2*numRows-2
        for i in range(len(s)):
            target_row=i%n_per
            target_row=target_row if target_row<numRows else n_per-target_row
            rn[target_row]+=s[i]
        return ''.join(rn)
    def testTime(self, fun, args):
        # 计时
        start = time.process_time()
        result = fun(*args)
        elapsed = (time.process_time() - start)
        print(fun.__name__, ":")
        print("Time used:", elapsed)
        print('result:', result)

    def main(self):
        s ="PAYPALISHIRING"
        rows=3
        self.testTime(self.myFun, args=(s,rows))
        self.testTime(self.convert, args=(s,rows))


if __name__ == '__main__':
    SL = Solution()
    SL.main()
