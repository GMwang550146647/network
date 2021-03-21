from fundamentals.test_time import test_time

import bisect
class Solution():
    def __init__(self):
        pass

    '''我的方法'''

    @test_time
    def lengthOfLIS(self, nums):
        record_list=[1]*len(nums)
        #填 record_list 的第i个位置
        for i in range(1,len(nums)):
            #为此要遍历前面i个位置
            for j in range(i):
                if nums[j]<nums[i]:
                    record_list[i]=max(record_list[i],record_list[j]+1)
        return max(record_list)

    @test_time
    def lengthOfLIS1(self, A):
        d = []
        for a in A:
            print(a,d)
            i = bisect.bisect_left(d, a)
            if i < len(d):
                d[i] = a
            elif not d or d[-1] < a:
                d.append(a)
        return len(d)

    def main(self):
        nums = [186,13,322,264,328,110,120,73,20,35,240,97,150,221,284,324,46,219,239,284,128,251,298,319,304,36,144,236,163,122]
        # self.lengthOfLIS(nums)
        self.lengthOfLIS1(nums)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
