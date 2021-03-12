from fundamentals.test_time import test_time

import sys

sys.setrecursionlimit(10000)


class Solution():
    def __init__(self):
        pass

    @test_time
    def maxCoins(self, nums):

        def get_score(cur_balls, i):
            return (cur_balls[i] * (cur_balls[i - 1] if i - 1 >= 0 else 1) * (
                cur_balls[i + 1] if i + 1 < len(nums) else 1))

        def backtrack(cur_balls, cur_score):
            nonlocal max_score
            if len(cur_balls) == 0:
                if cur_score > max_score:
                    max_score = cur_score
            else:
                for i in range(len(cur_balls)):
                    score_add = get_score(cur_balls, i)
                    tempt_ball = cur_balls.pop(i)
                    backtrack(cur_balls, cur_score + score_add)
                    cur_balls.insert(i, tempt_ball)

        max_score = -1

        backtrack(nums, 0)
        return max_score

    def main(self):
        nums = [3, 1, 5, 8]
        self.maxCoins(nums)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
