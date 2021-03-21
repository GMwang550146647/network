from fundamentals.test_time import test_time
from collections import deque
class MonotonicQueue():
    def __init__(self):
        self.q=deque([])
    def push(self,n):
        while self.q and self.q[-1]<n:
            self.q.pop()
        self.q.append(n)
    def max(self):
        return self.q[0]
    def pop(self,n):
        if self.q[0]==n:
             return self.q.popleft()

class Solution():
    def __init__(self):
        pass

    @test_time
    def maxSlidingWindow(self, nums,k):
        result=[0 for _ in range(len(nums)-k+1)]
        mq=MonotonicQueue()
        for j in range(k-1):
            mq.push(nums[j])
        for i in range(k-1,len(nums)):
            mq.push(nums[i])
            result[i-k+1]=mq.max()
            mq.pop(nums[i-k+1])
        return result

    def main(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        self.maxSlidingWindow(nums,k)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
