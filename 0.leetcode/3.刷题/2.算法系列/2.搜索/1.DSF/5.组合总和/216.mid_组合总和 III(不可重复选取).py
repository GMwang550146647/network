from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def combinationSum3(self,k,n):
        def dfs(target,cur,k,s=1):
            if k==0:
                if target==0:
                    solutions.append(cur.copy())
            else:
                for i in range(s,10):
                    if i<= target:
                        cur.append(i)
                        dfs(target-i,cur,k-1,i+1)
                        cur.pop(-1)
        solutions=[]
        dfs(n,[],k,1)
        return solutions

    def main(self):
        k=3
        n=7
        self.combinationSum3(k,n)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
