'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "" .

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:

All given inputs are in lowercase letters a-z .'''
import time
class Solution():
    def __init__(self):
        self.ip=['flower','flow','flowjjj']
    '''我的方法'''
    '''原理：一个一个比对'''
    def myFun(self,ip):
        length=len(ip)
        maxi=len(ip[0])
        result=[]
        for i in range(maxi): #第i个字母
            chari=ip[0][i]
            flag=1
            for j in range(1,length):#第j个单词
                if i>=len(ip[j]):
                    return ''.join(result)
                if ip[j][i]!=chari:
                    flag=-1
                    break
            if flag==1:
                result.append(chari)
        return ''.join(result)
    def testTime(self,fun,ip):
        # 计时
        start = time.process_time()
        result = fun(ip)
        elapsed = (time.process_time() - start)
        print(fun.__name__,":")
        print("Time used:", elapsed)
        print('result:', result)
    '''答案方法1'''
    def main(self):
        self.testTime(self.myFun,self.ip)
sl=Solution()
sl.main()