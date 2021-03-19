from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def calculate_recur(self, s):
        """
        带上符号一起丢进去栈，最后相加就行了
        """

        def solve(s):
            stk = []
            num = 0
            sign = '+'
            for i in range(len(s)):
                if s[i].isdigit():
                    num = num * 10 + int(s[i])
                # 注意：i==len(s)-1 是为了解决最后一个是数字的情况：、
                # 因为设定是非 数字才把num 加入到计算行列中，但是到了最后以数字结尾，num还有数据没加入到计算，所以要overwrite！
                # 1.如果是数字，则把数值入栈计算
                # 2.如果非数字，则数值为0，即使计算了也不会有问题！（试想一下，除了数字之外只有括号才会结尾吧...）
                if not s[i].isdigit() or i == len(s) - 1:
                    if sign == '+':
                        stk.append(num)
                    else:
                        stk.append(-num)
                    num = 0
                    sign = s[i]

            return sum(stk)

        return solve(s)

    def main(self):
        s = "1+2+3-4+5+6-7+8-9"
        self.calculate_recur(s)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
