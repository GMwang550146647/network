from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def LIS(self, arr):
        def gt(s1, s2):
            if len(s1) == len(s2):
                for i in range(len(s1)):
                    if s1[i] > s2[i]:
                        return False
                return True
            return len(s1) > len(s2)

        def max_seq(arr):
            result = arr[0]
            for i in range(1, len(arr)):
                result = arr[i] if gt(arr[i], result) else result
            return result

        # write code here
        dp = [[ai] for ai in arr]
        for i in range(1, len(arr)):
            for j in range(i):
                if arr[i] > arr[j]:
                    new_seq = dp[j] + [arr[i]]
                    if gt(new_seq, dp[i]):
                        dp[i] = new_seq
        return max_seq(dp)

    def main(self):
        nums = [186, 13, 322, 264, 328, 110, 120, 73, 20, 35, 240, 97, 150, 221, 284, 324, 46, 219, 239, 284, 128, 251,
                298, 319, 304, 36, 144, 236, 163, 122]
        # nums=list(range(1000))
        print(self.LIS(nums))


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
