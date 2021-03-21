from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def longestPalindrome(self, s):
        def palindrome(s,l,r):
            while(l>=0 and r<len(s) and s[l]==s[r]):
                l-=1
                r+=1
            return s[l+1:r]
        res=''
        for i in range(0,len(s)):
            s1=palindrome(s,i,i+1)
            s2=palindrome(s,i,i)
            res=s1 if len(s1)>len(res) else res
            res=s2 if len(s2)>len(res) else res
        return res


    def main(self):
        s = "a"
        self.longestPalindrome(s)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
