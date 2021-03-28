from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass
    @test_time
    def my_removeOuterParentheses(self, S):
        stack=[]
        del_index=[]
        for i in range(len(S)):
            if not stack:
                stack.append(S[i])
                del_index.append(i)
            elif stack[-1]=='(' and S[i]==')':
                stack.pop(-1)
                if not stack:
                    del_index.append(i)
            else:
                stack.append(S[i])
        s=''
        for i in range(0,len(del_index),2):
            s+=S[(del_index[i]+1):del_index[i+1]]
        return s

    @test_time
    def removeOuterParentheses(self, S):
        """
        遇到左括号，+1，遇到右括号，-1
        遇到左括号，计数值大于0，有效左括号
        遇到右括号，计数值大于1，有效右括号
        """
        count=0
        s=''
        for si in S:
            if si=='(' and count>0:
                s+=si
            if si==')' and count>1:
                s+=si
            count+= -1 if si==')' else 1
        return s



    def main(self):
        s = "(()())(())"
        s = "(()())(())(()(()))"
        self.my_removeOuterParentheses(s)
        self.removeOuterParentheses(s)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
