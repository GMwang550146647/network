from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def trap(self, height):
        """
        原理是把左右的最大值都记下来，然后一个一个计算
        """
        len_height = len(height)
        max_left = [0 for _ in range(len_height)]
        max_right = [0 for _ in range(len_height)]
        tempt_max_left = 0
        tempt_max_right = 0
        for i in range(len(height)):
            max_left[i] = tempt_max_left
            tempt_max_left = max(height[i], tempt_max_left)
            max_right[len_height - 1 - i] = tempt_max_right
            tempt_max_right = max(height[len_height - 1 - i], tempt_max_right)

        sum = 0
        for i in range(len_height):
            sum += max(min(max_left[i], max_right[i]) - height[i], 0)
        return sum

    def main(self):
        height = [4, 2, 0, 3, 2, 5]
        self.trap(height)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
