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

    @test_time
    def LIS2(self, arr):
        # write code here
        if len(arr) == 0:
            return []
        # write code here
        pre = [[i] for i in range(len(arr))]
        max_length = 0
        # 确定第i个位置的最优
        for i in range(1, len(arr)):
            # 遍历i之前的位置，找到最好的j
            for j in range(i):
                # 必须是递增才更新
                if arr[i] > arr[j]:
                    new_arr = pre[j] + [i]
                    # 如果比原来的好，更新前导节点
                    if len(new_arr) > len(pre[i]):
                        pre[i] = new_arr
                    # 如果一样，添加该节点
                    elif len(new_arr) == len(pre[i]):
                        pre[i] = pre[i] if arr[pre[i][-2]] < arr[j] else new_arr
                    max_length = max(len(pre[i]), max_length)
        result = []
        for i in range(len(pre)):
            if len(pre[i]) == max_length:
                result.append(pre[i])
        result = [[arr[i] for i in result[j]] for j in range(len(result))]
        return sorted(result)[0]

    @test_time
    def LIS3(self, arr):
        def extract(cur_node, cur_path):
            if cur_node:
                for next_nodei in cur_node:
                    extract(pre[next_nodei], [next_nodei] + cur_path)
            else:
                cur_path = [arr[i] for i in cur_path]
                result.append(cur_path)

        def extract2(cur_node):
            result = [arr[cur_node]]
            while pre[cur_node]:
                result.append(arr[pre[cur_node][0]])
                cur_node = pre[cur_node][0]
            return list(reversed(result))

        if len(arr) == 0:
            return []
        # write code here
        pre = [[] for _ in range(len(arr))]
        longest = [1] * len(arr)
        # 确定第i个位置的最优
        for i in range(1, len(arr)):
            # 遍历i之前的位置，找到最好的j
            for j in range(i):
                # 必须是递增才更新
                if arr[i] > arr[j]:
                    new_count = longest[j] + 1
                    # 如果比原来的好，更新前导节点
                    if new_count > longest[i]:
                        pre[i] = [j]
                        longest[i] = new_count
                    # 如果一样，添加该节点
                    elif new_count == longest[i]:
                        pre[i] = pre[i] if arr[pre[i][0]] < arr[j] else [j]

        max_length = max(longest)
        result = []
        for i in range(len(arr)):
            if longest[i] == max_length:
                result.append(extract2(i))

        return sorted(result)[0]

    @test_time
    def LIS4(self, arr):

        def extract2(cur_node):
            result = [arr[cur_node]]
            while pre[cur_node]:
                result.append(arr[pre[cur_node]])
                cur_node = pre[cur_node]
            return list(reversed(result))

        if len(arr) == 0:
            return []
        # write code here
        pre = [None for _ in range(len(arr))]
        longest = [1] * len(arr)
        # 确定第i个位置的最优
        for i in range(1, len(arr)):
            # 遍历i之前的位置，找到最好的j
            for j in range(i):
                # 必须是递增才更新
                if arr[i] > arr[j]:
                    new_count = longest[j] + 1
                    # 如果比原来的好，更新前导节点
                    if new_count > longest[i]:
                        pre[i] = j
                        longest[i] = new_count
                    # 如果一样，添加该节点
                    elif new_count == longest[i]:
                        pre[i] = pre[i] if arr[pre[i]] < arr[j] else j

        max_length = max(longest)
        result = []
        for i in range(len(arr)):
            if longest[i] == max_length:
                result.append(extract2(i))

        return sorted(result)[0]

    def main(self):
        nums = [186, 13, 322, 264, 328, 110, 120, 73, 20, 35, 240, 97, 150, 221, 284, 324, 46, 219, 239, 284, 128, 251,
                298, 319, 304, 36, 144, 236, 163, 122]
        # nums=list(range(1000))
        nums = [2, 1, 5, 3, 6, 4, 8, 9, 7]
        print(self.LIS(nums))
        print(self.LIS2(nums))
        print(self.LIS3(nums))
        print(self.LIS4(nums))


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
