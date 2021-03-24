from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def validateStackSequences(self, pushed, popped):
        """
        模拟法：一次push一个，一旦该个和pop中的是一样的，同时pop出来！
        """
        stack = []
        i = 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return not stack

    def main(self):
        pushed = [1, 2, 3, 4, 5]
        popped = [4, 5, 3, 2, 1]
        # pushed = [1, 2, 3, 4, 5]
        # popped = [4, 3, 5, 1, 2]
        self.validateStackSequences(pushed, popped)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
