class Solution:
    def LIS(self , arr ):
        def gt(s1,s2):
            if len(s1)==len(s2):
                for i in range(len(s1)):
                    if s1[i]>s2[i]:
                        return False
                return True
            return len(s1)>len(s2)
        def max_seq(arr):
            result=arr[0]
            for i in range(1,len(arr)):
                result= arr[i] if gt(arr[i],result) else result
            return result

        # write code here
        dp=[[ai] for ai in arr]
        for i in range(1,len(arr)):
            for j in range(i):
                if dp[i]>dp[j]:
                    new_seq=dp[j]+[arr[i]]
                    if gt(new_seq,dp[i]):
                        dp[i]=new_seq
        return max_seq(dp)


if __name__ == '__main__':
    arr = [2, 1, 5, 3, 6, 4, 8, 9, 7]

    result = Solution().LIS(arr)
    print(result)
