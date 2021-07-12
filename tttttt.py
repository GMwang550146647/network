class Solution:
    def maximalSquare(self, matrix) -> int:
        max_side=0
        dp=[[0]*len(matrix[0]) for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='1':
                    if i==0 or j==0:
                        dp[i][j]=1
                    else:
                        dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    max_side=max(dp[i][j],max_side)
        return max_side**2


if __name__ == '__main__':
    matrix=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    result=Solution().maximalSquare(matrix)
    print(result)