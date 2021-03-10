'''
Given a string containing just the characters '(' , ')' , '{' , '}' , '[' and ']' , determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true

Example 2:

Input: "()[]{}"
Output: true

Example 3:

Input: "(]"
Output: false

Example 4:

Input: "([)]"
Output: false

Example 5:

Input: "{[]}"
Output: true
'''
import time
class Solution():
    def __init__(self):
        self.str='({[([[{]})]})'
        self.chars1=['[','(','{']
        self.chars2=[']',')','}']
    '''我的方法(错误示范！例如："[(])"我认为这种是可以的，而题目认为不可以，理解错题目了！！！)'''
    def myFun(self):
        deletedIndex=[]
        for i in range(len(self.chars1)): #对于每个符号，例如{[(
            for j in range(len(self.str)-1):  #对于self.str的每一个字母
                if j in deletedIndex: #如果已经是删掉的字母了，就不访问了
                    continue
                elif self.str[j]==self.chars1[i]:
                    flag=-1  #-1代表找不到对应的
                    for k in range(j+1,len(self.str)):
                        if self.str[k]==self.chars2[i]:
                            flag=1
                            deletedIndex.append(j)
                            deletedIndex.append(k)
                            break
                    if flag==-1:
                        return False
        if len(deletedIndex)!=len(self.str):
            return False
        else:
            return True

    '''答案方法'''
    '''
    原理：如果末尾加入的两个是一对的，一起丢掉！
    '''
    def isValid(self):
        stack=[]
        d=["()","[]","{}"]
        for i in range(len(self.str)):
            stack.append(self.str[i])
            if len(stack)>=2 and stack[-2]+stack[-1] in d:
                stack.pop()
                stack.pop()
        return len(stack)==0

    def testTime(self,fun):
        # 计时
        start = time.process_time()
        result = fun()
        elapsed = (time.process_time() - start)
        print(fun.__name__,":")
        print("Time used:", elapsed)
        print('result:', result)
    def main(self):
        pass
        self.testTime(self.myFun)
        self.testTime(self.isValid)
SL=Solution()
SL.main()