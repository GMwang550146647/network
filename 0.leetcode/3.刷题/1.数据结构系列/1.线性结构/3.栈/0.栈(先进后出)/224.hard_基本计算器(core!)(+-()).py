from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    # @test_time
    def calculate_recur(self, s):
        def solve(s):
            """
            核心：
                只计算到 ')'就返回当前算式的结果
            返回:
                当前算式的结果以及后面剩下的算式
            """
            sign = '+'
            num = 0
            stk = []
            while(len(s)>0):

                cur_char=s.pop(0)
                if cur_char.isdigit():
                    num = num * 10 + int(cur_char)
                # 把括号里面的算式计算成一个数再返回
                if cur_char == '(':
                    num=solve(s)
                # 注意：len(s)==1 是为了解决最后一个是数字的情况：、
                # 因为设定是非 数字才把num 加入到计算行列中，但是到了最后以数字结尾，num还有数据没加入到计算，所以要overwrite！
                # 1.如果是数字，则把数值入栈计算
                # 2.如果非数字，则数值为0，即使计算了也不会有问题！（试想一下，除了数字之外只有括号才会结尾吧...）
                if not cur_char.isdigit() or len(s)==0:
                    if sign == '+':
                        stk.append(num)
                    elif sign == '-':
                        stk.append(-num)
                    sign = cur_char
                    num = 0
                # ')'之后的就不包含在这次的计算当中
                if sign == ')':
                    break
                # print(s, stk, num)
            return sum(stk)
        s=list(s.replace(' ',''))

        return solve(s)

    def main(self):
        s = "(1+2+3-4)-2+3+(6-6)+12-10-2"
        print(eval(s))
        print(self.calculate_recur(s))


if __name__ == '__main__':
    SL = Solution()
    SL.main()
