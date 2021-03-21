from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def isValid(self, s):
        pair = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        stack = []
        for sign_i in s:
            if sign_i in pair:
                if stack and stack[-1] == pair[sign_i]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(sign_i)
        return False if stack else True

    def main(self):
        s = "()[]{}"
        s = "([)]"
        self.isValid(s)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
