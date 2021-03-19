from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    # @test_time
    def pancakeSort(self, arr):
        def reverse(arr, i, j):
            while (i < j):
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        def solve(arr, n):
            if n == 1:
                return
            else:
                max_index = -1
                max_num = -100000
                for i in range(n):
                    if arr[i] > max_num:
                        max_num = arr[i]
                        max_index = i
                # print('n:{},max_index:{},max_int:{},arr:{}'.format(n,max_index,max_num,arr))
                if max_index == n - 1:
                    solve(arr, n - 1)
                else:
                    reverse(arr, 0, max_index)
                    reverse(arr, 0, n - 1)
                    path.append(max_index + 1)
                    path.append(n)
                    solve(arr, n - 1)

        path = []
        solve(arr, len(arr))
        return path

    def main(self):
        arr = [3, 2, 4, 1]
        print(self.pancakeSort(arr))


if __name__ == '__main__':
    SL = Solution()
    SL.main()
