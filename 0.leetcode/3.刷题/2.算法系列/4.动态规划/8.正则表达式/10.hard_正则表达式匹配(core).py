from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def isMatch_recur_record(self, s, p):
        """
        比较难的版本
        """

        def dp(i=0, j=0):
            ###1.base case
            # pattern到头了，
            if j == len_p:
                return i == len_s
            # 字符串到头了（如果pattern还有，只能是*的情况）
            if i == len_s:
                if ((len_p - j) % 2 == 1):
                    return False
                else:
                    for k in range(j + 1, len_p, 2):
                        if p[k] != '*':
                            return False
                    return True
            ###2.in dict
            if (i, j) in dp_table:
                return dp_table[(i, j)]
            ###3.dp
            else:
                if p[j] in [s[i], '.']:
                    # 有*
                    if j < len_p - 1 and p[j + 1] == '*':
                        res = dp(i + 1, j) | dp(i, j + 2)
                    # 无*
                    else:
                        res = dp(i + 1, j + 1)
                # 匹配失败(但是可能有*)
                else:
                    # 有*
                    if j < len_p - 1 and p[j + 1] == '*':
                        res = dp(i, j + 2)
                    # 冇救了
                    else:
                        res = False
                dp_table[(i, j)] = res
                return res

        len_s = len(s)
        len_p = len(p)
        dp_table = {}
        return dp()


    def main(self):
        s = "ab"
        p = ".*"
        self.isMatch_recur_record(s, p)
        self.isMatch_dp(s, p)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
