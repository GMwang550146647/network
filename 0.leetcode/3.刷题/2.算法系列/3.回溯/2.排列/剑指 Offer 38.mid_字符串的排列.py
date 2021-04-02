from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def permutation(self, s):
        def recur(s,cur):
            if not s:
                solutions.append(cur)
            else:
                for i in range(len(s)):
                    if i>0 and s[i-1]==s[i]:
                        continue
                    cur+=s.pop(i)
                    recur(s,cur)
                    s.insert(i,cur[-1])
                    cur = cur[:-1]
        solutions=[]

        s = sorted(s)
        recur(s, '')
        return solutions

    def main(self):
        s = "abbc"
        self.permutation(s)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
