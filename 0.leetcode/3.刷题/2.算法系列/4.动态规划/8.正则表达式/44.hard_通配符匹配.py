from fundamentals.test_time import test_time
import re


class Solution():
    def __init__(self):
        pass

    # @test_time
    def isMatch_recur(self, s, p):
        '''
        这个非常好理解，但是太慢了
        '''

        def compare(ps, pp):
            # 1.base case:
            # 1.1.都到达终点
            if ps == len_s and pp == len_p:
                return True
            # 1.2.如果p已经匹配完了，还没结束，说明匹配失败
            elif pp == len_p:
                return False
            # 1.3.如果p没匹配完，但是s已经结束，p剩下的全是*才可能成功
            elif ps == len_s:
                while pp < len_p:
                    if p[pp] != '*':
                        return False
                    pp += 1
                return True
            # 2.匹配开始
            else:
                # 2.1.能匹配上
                if s[ps] == p[pp] or p[pp] == '?':
                    return compare(ps + 1, pp + 1)
                # 2.2.不能匹配上，但是有*
                elif p[pp] == '*':
                    return compare(ps + 1, pp) or compare(ps + 1, pp + 1) or compare(ps, pp + 1)
                # 2.3.不能匹配上
                else:
                    return False

        p = re.sub('\*+', '*', p)
        len_s = len(s)
        len_p = len(p)
        return compare(0, 0)

    def isMatch_dp(self, s, p):
        p = re.sub('\*+', '*', p)
        dp = [[False for _ in range(len(s) + 1)] for _ in range(len(p) + 1)]
        dp[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i - 1] == '*' and dp[i - 1][0]:
                dp[i][0] = True
        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if s[j - 1] == p[i - 1] or p[i - 1] == '?':
                    # 这个字相同，前面的也要相同才有用！
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[i - 1] == '*':
                    # dp[i][j - 1]->当前的*可以无限匹配  & dp[i-1][j-1]-> 或者一个都不匹配！
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
        return dp[-1][-1]

    def main(self):
        s = "aab"
        p = "c*a*b"
        print(self.isMatch_dp(s, p))
        # print(self.isMatch_recur(s, p))


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
