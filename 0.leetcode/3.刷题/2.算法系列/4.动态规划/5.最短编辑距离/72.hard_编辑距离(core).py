from fundamentals.test_time import test_time

import bisect
import numpy as np


class Solution():
    def __init__(self):
        pass

    @test_time
    def minDistance_recur(self, word1, word2):
        """
        纯递归版本
        """

        def dp(index1, index2):
            if index1 < 0: return index2 + 1
            if index2 < 0: return index1 + 1

            if word1[index1] == word2[index2]:
                return dp(index1 - 1, index2 - 1)
            else:
                return min(
                    dp(index1 - 1, index2 - 1) + 1,
                    dp(index1 - 1, index2) + 1,
                    dp(index1, index2 - 1) + 1,
                )

        return dp(len(word1) - 1, len(word2) - 1)

    @test_time
    def minDistance_recur_record(self, word1, word2):
        """
        自顶而下：有备忘录递归的dp
        """

        def dp(index1, index2):
            if index1 < 0: return index2 + 1
            if index2 < 0: return index1 + 1

            if word1[index1] == word2[index2]:
                return dp(index1 - 1, index2 - 1)
            elif (index1, index2) in memory:
                return memory[(index1, index2)]
            else:
                memory[(index1, index2)] = min(
                    dp(index1 - 1, index2 - 1) + 1,
                    dp(index1 - 1, index2) + 1,
                    dp(index1, index2 - 1) + 1,
                )
                return memory[(index1, index2)]

        memory = {}
        return dp(len(word1) - 1, len(word2) - 1)

    @test_time
    def minDistance_dp(self, word1, word2):
        """
        自底而上：遍历版本的dp
        """
        width = len(word1) + 1
        length = len(word2) + 1
        dp = [[0 for _ in range(length)] for _ in range(width)]
        for i in range(width):
            dp[i][0] = i
        for j in range(length):
            dp[0][j] = j
        for i in range(1, width):
            for j in range(1, length):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        print("#######################")
        print(dp)
        self.draw_path(dp,word1,word2)
        return dp[len(word1)][len(word2)]

    def draw_path(self, dp_table, word1, word2):
        all_solutions = []
        col_bound = len(word2) + 1
        row_bound = len(word1) + 1

        def find_next_step(row, col):
            next_steps = []
            if row + 1 < row_bound and col + 1 < col_bound:
                if dp_table[row][col + 1] > dp_table[row][col]:
                    next_steps.append(((row, col + 1),'insert {}'.format(word2[col])))
                if dp_table[row + 1][col] > dp_table[row][col]:
                    next_steps.append(((row + 1, col),'delete {}'.format(word1[row])))
                if dp_table[row + 1][col + 1] > dp_table[row][col]:
                    next_steps.append(((row + 1, col + 1),'replace {} into {}'.format(word1[row],word2[col])))
                if dp_table[row + 1][col + 1] == dp_table[row][col]:
                    next_steps.append(((row + 1, col + 1),'{} stays'.format(word1[row],word2[col])))
            else:
                if row + 1 < row_bound:
                    if dp_table[row + 1][col] > dp_table[row][col]:
                        next_steps.append(((row + 1, col), 'delete {}'.format(word1[row])))
                elif col + 1 < col_bound:
                    if dp_table[row][col + 1] > dp_table[row][col]:
                        next_steps.append(((row, col + 1), 'insert {}'.format(word2[col])))
            return next_steps

        def find_path(row, col,cur_path):
            if row==row_bound-1 and col==col_bound-1:
                all_solutions.append(cur_path.copy())
            else:
                next_steps=find_next_step(row,col)
                for step_i in next_steps:
                    cur_path.append(step_i[1])
                    find_path(step_i[0][0],step_i[0][1],cur_path)
                    cur_path.pop(-1)
        path=[]
        find_path(0,0,path)
        all_solutions=sorted(all_solutions,key=lambda a:len(a))
        print(all_solutions[0])
    def main(self):
        word1 = "akkce"
        word2 = "apple"
        # self.minDistance_recur(word1, word2)
        # self.minDistance_recur_record(word1, word2)
        self.minDistance_dp(word1, word2)
        # self.draw_path([[0, 1, 2, 3], [1, 1, 2, 3], [2, 2, 1, 2], [3, 2, 2, 2], [4, 3, 3, 2], [5, 4, 4, 3]],word1,word2)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
