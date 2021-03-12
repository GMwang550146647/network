from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def maxA_recur_record(self, n):
        """
        三种策略
            1.按A
            2.CV
            3.CA+CC
        """
        dp_table = {}

        def dp(n_step, a_num=0, copy_a=0):
            if n_step <= 0:
                return a_num
            elif (n_step, a_num, copy_a) in dp_table:
                return dp_table[(n_step, a_num, copy_a)]
            else:
                dp_table[(n_step, a_num, copy_a)] = max(
                    dp(n_step - 1, a_num + 1, copy_a),
                    dp(n_step - 1, a_num + copy_a, copy_a),
                    dp(n_step - 2, a_num, a_num),
                )
                return dp_table[(n_step, a_num, copy_a)]

        return dp(n)

    @test_time
    def maxA_dp(self, n):
        """
        两种策略：
            1.按A
            2.CA-CC之后 n个 CV
        """
        dp = [1 for i in range(n)]
        for i in range(1,n):
            # 按A
            dp[i] = dp[i - 1] + 1
            # i-2的时候按CA+CC，然后按 CV i-j次
            for j in range(2,i):
                dp[i] = max(dp[i], dp[j - 2] * (i - j + 1))
        return dp[-1]

    def main(self):
        N = 3
        self.maxA_recur_record(N)
        self.maxA_dp(N)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
