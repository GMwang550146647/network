from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def combinationSum2(self,candidates,target):
        def dfs(target,cur,s=0):
            if target==0:
                solutions.append(cur.copy())
            else:
                for i in range(s,len(candidates)):
                    if candidates[i]<=target:
                        cur.append(candidates[i])
                        if i==s:
                            dfs(target-candidates[i],cur,i+1)
                        else:
                            if candidates[i]!=candidates[i-1]:
                                dfs(target-candidates[i],cur,i+1)
                        cur.pop(-1)
        candidates=sorted(candidates)
        solutions=[]
        dfs(target,[])
        return solutions

    def main(self):
        candidates = [2, 5, 2, 1, 2]
        target = 5
        self.combinationSum2(candidates,target)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
