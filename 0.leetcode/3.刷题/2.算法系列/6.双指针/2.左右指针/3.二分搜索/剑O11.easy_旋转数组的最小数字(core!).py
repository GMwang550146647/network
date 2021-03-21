from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def func(self, numbers):
        low, high = 0, len(numbers) - 1
        while low < high:
            pivot = low + (high - low) // 2
            # 终点在右支
            if numbers[pivot] < numbers[high]:
                high = pivot
            # 终点在左支
            elif numbers[pivot] > numbers[high]:
                low = pivot + 1
            # 分不清了向中间走吧
            else:
                high -= 1
        return numbers[low]

    def main(self):
        nums = [3, 4, 5, 1, 2]
        self.func(nums)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
