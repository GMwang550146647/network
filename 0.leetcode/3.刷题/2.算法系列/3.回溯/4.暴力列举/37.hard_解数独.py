from fundamentals.test_time import test_time
import copy


class Solution():
    def __init__(self):
        pass

    def solveSudoku(self, board):
        """
        全列举法：
            每一层递归：对每个格子都进行遍历 1-9的数字，适合就开启下一层（下一格）
        """

        def isValid(board, r, c, n):
            for i in range(9):
                if board[r][i] == n:
                    return False
                if board[i][c] == n:
                    return False
                if board[(r // 3) * 3 + i % 3][(c // 3) * 3 + i // 3] == n:
                    return False
            return True

        def backtrack(board, i, j):
            if j == len(board):
                return backtrack(board, i + 1, 0)
            if i == len(board):
                return True
            if board[i][j] == '.':
                for k in range(1,10):
                    if isValid(board, i, j, str(k)):
                        board[i][j] = str(k)
                        if backtrack(board, i, j + 1):
                            return True
                        board[i][j] = '.'
                return False
            else:
                return backtrack(board, i, j + 1)
        backtrack(board, 0, 0)
        return board

    def print(self, board):
        for i in range(len(board)):
            if i == 0:
                print("-------------------------")
            for j in range(len(board)):
                if j == 0:
                    print("| ", end='')
                print(board[i][j], end=' ')
                if (j + 1) % 3 == 0:
                    print("| ", end='')
            print()
            if (i + 1) % 3 == 0:
                print("-------------------------")

    def main(self):
        board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        self.print(board)
        solution = self.solveSudoku(board)
        self.print(solution)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
