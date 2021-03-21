from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def dailyTemperatures(self, T):
        # 存放的是index
        result = [0 for _ in range(len(T))]
        stack = []
        for i in range(len(T) - 1, -1, -1):
            while stack and T[i] >= stack[-1][0]:
                stack.pop(-1)
            if stack:
                result[i] = stack[-1][1] - i
                stack.append([T[i], i])
            else:
                result[i] = 0
                stack.append([T[i], i])
        return result

    def main(self):
        nums = [73, 74, 75, 71, 69, 72, 76, 73]
        self.dailyTemperatures(nums)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
