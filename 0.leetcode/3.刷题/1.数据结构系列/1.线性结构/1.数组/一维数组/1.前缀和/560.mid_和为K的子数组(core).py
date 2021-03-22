from fundamentals.test_time import test_time

'''
问题描述：
    求 k=sum(arr[i:j])的解个数！
'''


class Solution():
    def __init__(self):
        pass

    @test_time
    def subarraySum(self, nums, k):
        """
        迭代求解
        """
        pre_sum = [0 for i in range(len(nums) + 1)]
        for i in range(len(nums)):
            pre_sum[i + 1] = nums[i] + pre_sum[i]
        count = 0
        for i in range(len(pre_sum)):
            for j in range(i + 1, len(pre_sum)):
                if pre_sum[j] - pre_sum[i] == k:
                    count += 1

        return count

    @test_time
    def subarraySum_record_dict(self, nums, k):
        """
        前缀和+ 字典
        """
        pre_sum = [0 for i in range(len(nums) + 1)]
        for i in range(len(nums)):
            pre_sum[i + 1] = nums[i] + pre_sum[i]
        count = 0
        record_dict = {}
        for i in range(len(pre_sum)):
            if pre_sum[i] in record_dict:
                count += record_dict[pre_sum[i]]
            tempt_sum = pre_sum[i] + k
            record_dict[tempt_sum] = record_dict.get(tempt_sum, 0) + 1
        return count

    @test_time
    def subarraySum_record_dict_advances(self, nums, k):
        """
        一边计算前缀和一边计算dict(省了保存前缀和的数组空间)
        """
        pre_sum = 0
        count = 0
        record_dict = {k: 1}
        for i in range(len(nums)):
            pre_sum = pre_sum + nums[i]
            if pre_sum in record_dict:
                count += record_dict[pre_sum]
            tempt_sum = pre_sum + k
            record_dict[tempt_sum] = record_dict.get(tempt_sum, 0) + 1
        return count

    def main(self):
        nums = [-916, -132, -202, -524, 739, 57, 938, 546, 948, -181, -315, 921, 792, -992, -69, 588, 712, 509, -406,
                302, -637, 169, 407, 993, -263, 54, -512, -950, -930, 66, 147, -9, -136, -205, 274, 992, -304, -835,
                659, -792, -288, 146, 182, -672, -374, -943, -85, 958, -19, 33, -676, 232, 92, -132, -121, -944, -526,
                -869, -423, -855, 818, 46, 401, 633, -457, 63, 824, -172, 237, 360, 43, 831, -432, 213, -330, -788,
                -472, -70, -507, 615, -953, 457, -89, -756, 477, 445, 153, -779, 710, 484, -20, 802, -261, -481, -309,
                -992, -240, 275, -302, -137, 295, -232, 529, 691, 873, 787, 229, 677, -388, 996, 301, -641, -983, 108,
                -247, 431, -668, 877, 528, -69, -15, 278, -334, 775, 770, -720, 232, -607, 896, 496, 485, 350, 772,
                -656, 379, 730, -445, -152, 295, 99, -945, -170, -594, 271, 894, -451, -455, 636, -210, 674, 554, 183,
                446, -709, -599, 521, 711, -739, -712, -947, -940, -577, 71, 672, -512, -216, 669, 137, -61, -901, -867,
                -168, -838, -653, -503, -535, -423, -922, 281, 544, -373, -935, -485, 760, -203, -656, -241, 493, -290,
                -298, 756, -871, -525, 614, 230, -910, -395, -308, -237, 289, 975, -215]
        # nums = [1, 1, 1]
        k = 2
        self.subarraySum(nums, k)
        self.subarraySum_record_dict(nums, k)
        self.subarraySum_record_dict_advances(nums, k)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
