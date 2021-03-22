from fundamentals.test_time import test_time


class ProductOfNumbers:

    def __init__(self):
        self.arr = [1]

    def add(self, num: int) -> None:
        '''
        遇到0就归一！前面的都是0了
        '''
        if num == 0:
            self.arr = [1]
        else:
            self.arr.append(self.arr[-1] * num)

    def getProduct(self, k: int) -> int:
        return 0 if k >= len(self.arr) else int(self.arr[-1] / self.arr[-k - 1])


class Solution():
    def __init__(self):
        pass

    @test_time
    def func(self, nums):
        pass

    def main(self):
        nums = [2, 7, 9, 3, 1]
        self.func(nums)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
