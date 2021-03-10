"""
给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。

重复出现的子串要计算它们出现的次数。

示例 1 :

输入: "00110011"
输出: 6
解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。

请注意，一些重复出现的子串要计算它们出现的次数。

另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。
示例 2 :

输入: "10101"
输出: 4
解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。
"""

import time
class Solution():
    def __init__(self):
        pass
    '''我的方法:连续和非连续的'''
    # def myFun(self,s):
    #     count = 0
    #     for s_i in range(len(s) - 1):
    #         lt = [0, 0]
    #         for e_i in range(s_i, len(s)):
    #             lt[0 if s[e_i] == '0' else 1] += 1
    #             if lt[0] == lt[1]:
    #                 count += 1
    #     return count
    def myFun(self,s):
        d={'0':-1,'1':1}
        cur_num=s[0]
        cur_count=0
        arr=[]
        len_s=len(s)
        for i in range(len_s):
            if s[i]==cur_num:
                cur_count+=1
            else:
                arr.append(d[cur_num]*cur_count)
                cur_num=s[i]
                cur_count=1
            if i==len_s-1:
                arr.append(d[cur_num] * cur_count)
        print(arr)
        count=0
        for i in range(len(arr)-1):
            if sum(arr[i:i + 2]) == 0:
                count+= 1  if abs(arr[i])==1 else 2
        return count
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
        s='00110'
        self.testTime(self.myFun,args=(s,))
if __name__=='__main__':
    SL=Solution()
    SL.main()
