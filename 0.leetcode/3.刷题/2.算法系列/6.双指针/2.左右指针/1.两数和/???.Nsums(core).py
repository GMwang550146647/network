from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    # @test_time
    def twoSum_two_pointers(self, nums, target, start=0, sort=False):
        """
        字典记录
            空间： o(N)
            时间： o(N2) ->主要是排序的时间
        注意： 这个返回的是
        """
        if sort:
            nums = sorted(nums)
        l = start
        r = len(nums) - 1
        res = []
        while l < r:
            left, right = nums[l], nums[r]
            sum = left + right
            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:
                res.append([nums[l], nums[r]])
                while (l < r and left == nums[l]):
                    l += 1
                while (l < r and right == nums[r]):
                    r -= 1
        return res

    @test_time
    def three_sums(self, nums, target):
        nums = sorted(nums)
        res = []
        i = 0
        while i < len(nums) - 2:
            # 对于每一个数， 都在剩下的数里面抽两个 令其等于target - nums[i]
            res_i = self.twoSum_two_pointers(nums, target - nums[i], i + 1)
            if res_i:
                res_i = [item + [nums[i]] for item in res_i]
                res.extend(res_i)
            while (i < len(nums) - 1 and nums[i] == nums[i + 1]):
                i += 1
            i += 1
        return res

    @test_time
    def n_sums(self, nums, target, n=4):
        def solve(nums, target, n, start=0):
            res = []
            i = start
            len_nums = len(nums)
            if n < 2 or len_nums < n:
                return res
            if n == 2:
                res = self.twoSum_two_pointers(nums, target, i)
            else:
                while i < len_nums:
                    res_i = solve(nums, target - nums[i], n - 1, i + 1)

                    for res_i_j in res_i:
                        res_i_j.append(nums[i])
                        res.append(res_i_j)
                    while (i < len_nums - 1 and nums[i] == nums[i + 1]):
                        i += 1
                    i += 1
            return res

        nums = sorted(nums)
        return solve(nums, target, n)

    def main(self):
        nums = [-1,0,1,2,-1,-4]
        target = -1
        result = self.twoSum_two_pointers(nums, target, sort=True)
        print(result)
        self.three_sums(nums, target)
        self.n_sums(nums, target, 3)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
