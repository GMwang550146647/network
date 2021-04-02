from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    # @test_time
    def combinationSum4(self, nums,target):
        def dfs(target):
            if target==0:
                nonlocal count
                count+=1
            else:
                for i in nums:
                    if target>=i:
                        dfs(target-i)
        count=0
        dfs(target)
        return count
    def main(self):
        nums = [4,2,1]
        target = 32
        result=self.combinationSum4(nums,target)
        print(result)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
