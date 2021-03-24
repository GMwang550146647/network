from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def combinationSum(self,candidates,target):
        solutions=[]
        def dfs(cur,target):
            if target<0:
                return
            elif target==0:
                solutions.append(cur.copy())
            else:
                for cand_i in candidates:
                    if not cur or cand_i>=cur[-1]:
                        cur.append(cand_i)
                        dfs(cur,target-cand_i)
                        cur.pop(-1)
        candidates=sorted(candidates)
        dfs([],target)
        return solutions

    def main(self):
        candidates = [2, 3, 6, 7]
        target = 7
        self.combinationSum(candidates,target)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
