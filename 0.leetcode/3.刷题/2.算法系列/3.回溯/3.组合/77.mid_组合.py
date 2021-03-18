from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def combine(self, n,k):
        """
        每一层代表
            两层的时候相当于：
                for i in arr[0:]:
                    for j in arr[i:]:
                        result.append([i,j]) ->每次都是从i
        """
        def backtrack(cur_sol,start,k):
            if k==0:
                solutions.append(cur_sol.copy())
            else:
                for i in range(start,n-k+1):
                    cur_sol.append(i+1)
                    backtrack(cur_sol,i+1,k-1)
                    cur_sol.pop(-1)

        solutions=[]
        backtrack([],0,k)
        return solutions

    def main(self):
        n=4
        k=2
        self.combine(n,k)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
