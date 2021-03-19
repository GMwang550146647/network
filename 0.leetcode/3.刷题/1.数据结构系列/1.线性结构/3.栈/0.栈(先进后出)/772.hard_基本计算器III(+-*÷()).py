from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def calculate_recur(self, s):
        """
        递归的特点是，非常慢，字符多了就很多层，更加慢
        :param s:
        :return:
        """

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
            while (len(s) > 0):

                cur_char = s.pop(0)
                if cur_char.isdigit():
                    num = num * 10 + int(cur_char)
                # 把括号里面的算式计算成一个数再返回
                if cur_char == '(':
                    num = solve(s)
                # 注意：len(s)==1 是为了解决最后一个是数字的情况：、
                # 因为设定是非 数字才把num 加入到计算行列中，但是到了最后以数字结尾，num还有数据没加入到计算，所以要overwrite！
                # 1.如果是数字，则把数值入栈计算
                # 2.如果非数字，则数值为0，即使计算了也不会有问题！（试想一下，除了数字之外只有括号才会结尾吧...）
                if not cur_char.isdigit() or len(s) == 0:
                    if sign == '+':
                        stk.append(num)
                    elif sign == '-':
                        stk.append(-num)
                    elif sign == '*':
                        stk[-1] = stk[-1] * num
                    elif sign == '/':
                        stk[-1] = int(stk[-1] / float(num))
                    sign = cur_char
                    num = 0
                # ')'之后的就不包含在这次的计算当中
                if sign == ')':
                    break
            return sum(stk)

        s = list(s.replace(' ', ''))

        return solve(s)

    @test_time
    def calculate_back(self, s):
        """
        转换为后缀表达式再进行计算
        origin:        "20*(9+6/3-5)+4"
        splited:       [20, '*', '(', 9, '+', 6, '/', 3, '-', 5, ')', '+', 4]
        backward_exp:  [20, 9, 6, 3, '/', '+', 5, '-', '*', 4, '+']

        """

        def string2list(expression):
            '''转换成list模式'''
            tempt_num = '#'
            result = []
            for char_i in expression:
                if char_i == ' ':
                    continue
                elif char_i.isdigit():
                    tempt_num = (tempt_num if tempt_num != '#' else 0) * 10 + int(char_i)
                else:
                    if tempt_num != '#':
                        result.append(tempt_num)
                        tempt_num = '#'
                    if result and result[-1] == '(':
                        result.append(0)
                    result.append(char_i)
            if tempt_num != '#':
                result.append(int(tempt_num))
            if type(result[0]) != int:
                result.insert(0, 0)
            return result

        def convert2Backward(exp):
            '''转换为后缀表达式'''
            opt_stack = []
            backward_stack = []
            for expi in exp:
                if expi in cal_sign:
                    while (opt_stack and sign_priority[opt_stack[-1]] >= sign_priority[expi]):
                        backward_stack.append(opt_stack.pop(-1))
                    opt_stack.append(expi)
                elif expi == '(':
                    opt_stack.append(expi)
                elif expi == ')':
                    while (opt_stack and opt_stack[-1] != '('):
                        backward_stack.append(opt_stack.pop(-1))
                    opt_stack.pop(-1)
                else:
                    backward_stack.append(expi)
            while (opt_stack):
                backward_stack.append(opt_stack.pop(-1))
            return backward_stack

        def calBackward(backward_exp):
            '''后缀表达式的计算'''
            stack = []
            for expi in backward_exp:
                if expi in cal_sign:
                    nex = stack.pop(-1)
                    pre = stack.pop(-1)
                    if expi == '+':
                        stack.append(pre + nex)
                    elif expi == '-':
                        stack.append(pre - nex)
                    elif expi == '*':
                        stack.append(pre * nex)
                    elif expi == '/':
                        stack.append(int(pre / float(nex)))
                else:
                    stack.append(expi)
            return stack[-1]

        sign_priority = {
            # '('设置为0的原因是，让其不能被pop出去，因为只能由')'触发 '('的pop
            '+': 1, '-': 1, '*': 2, '/': 2, '(': 0
        }
        cal_sign = ['+', '-', '*', '/']
        s = string2list(s)
        backward_exp = convert2Backward(s)
        result = calBackward(backward_exp)
        return result

    def main(self):
        s = "20*(9+6/3-5)+4"
        print(eval(s))
        self.calculate_recur(s)
        self.calculate_back(s)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
