from fundamentals.tree import TreeNode, Tree
import time


class Solution():
    def __init__(self):
        pass

    '''我的方法'''

    def fib(self, n):
        """
        RECUR
        """
        if n <= 1: return n if n >= 0 else 0
        return self.fib(n - 1) + self.fib(n - 2)

    def fib_dp_dict(self, n):
        """
        DP DICT RECORD (RECUR)
        """

        def fibAssist(n):
            if n < 0:
                return 0
            elif n in record_dict:
                return record_dict.get(n, record_dict[n])
            else:
                record_dict[n] = self.fib(n - 1) + self.fib(n - 2)
                return record_dict[n]

        record_dict = {0: 0, 1: 1}
        return fibAssist(n)

    def fib_dp_list(self, n):
        """
        DP LIST RECORD (RECUR)
        """

        def fibAssist(n):
            if n <= 1:
                return n if n >= 0 else 0
            elif n < len(record_list):
                return record_list[n]
            else:
                record_list.append(self.fib(n - 1) + self.fib(n - 2))
                return record_list[-1]

        record_list = [0, 1]
        return fibAssist(n)

    def fib_dp_compress(self, n):
        """
        DP RECORD (COMPRESS)
            只需记录前面两个状态即可
        """
        if n <= 1:
            return n if n >= 0 else 0
        else:
            f1, f2 = [0, 1]
            for i in range(n - 1):
                f1, f2 = [f2, f1 + f2]
            return f2

    def testTime(self, fun, args, test_times=10):
        # 计时
        start = time.process_time()
        for i in range(test_times):
            result = fun(*args)
        elapsed = (time.process_time() - start)
        print(fun.__name__, ":")
        print("Time used:", elapsed)
        print("Result:", result)

    def main(self):
        n = 20
        self.testTime(self.fib, args=(n,))
        self.testTime(self.fib_dp_dict, args=(n,))
        self.testTime(self.fib_dp_list, args=(n,))
        self.testTime(self.fib_sim, args=(n,))


if __name__ == '__main__':
    SL = Solution()
    SL.main()
