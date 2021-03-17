from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def generateParenthesis(self, n):
        """
        记住左括号和右括号的数量，有些枝节不走就行了
        """
        def backtrack(track, left, right):
            if left<0 or right<0:
                return
            if left == 0 and right==0:
                solutions.append(track.copy())
            if right < left:
                return
            else:
                for sign_i in ['(', ')']:
                    if sign_i == '(' :
                        track.append('(')
                        backtrack(track, left -1, right)
                        track.pop(-1)
                    elif sign_i == ')':
                        track.append(')')
                        backtrack(track, left, right -1)
                        track.pop(-1)
        solutions = []
        backtrack([], n, n)
        return [''.join(solui) for solui in solutions]

    def main(self):
        n = 3
        self.generateParenthesis(n)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
