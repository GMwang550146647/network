from fundamentals.test_time import test_time
from collections import defaultdict

class Solution():
    def __init__(self):
        pass

    @test_time
    def exist_simplified(self, board, word):
        """
        非常精彩且简洁：
            每个位置都遍历一次！
        细节：
            board[i][j] = '' 防止再走这个（一旦进入就会return False，所以就相当于加入了visited!)

        :param board:
        :param word:
        :return:
        """

        def dfs(i, j, k):
            if k == len(word):
                return True
            if i in [len(board), -1] or j in [len(board[0]), -1] or board[i][j] != word[k]:
                return False

            board[i][j] = ''
            res = dfs(i - 1, j, k + 1) or dfs(i + 1, j, k + 1) or dfs(i, j - 1, k + 1) or dfs(i, j + 1, k + 1)
            board[i][j] = word[k]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False

    @test_time
    def exist_fast(self, board, word):
        """
        这个和 simplify的区别在于 在递归之前就把判断条件弄清，不进入递归函数（就是不增加栈深度，所以快一点）
            core: 提前剪枝了！
        """
        m = len(board)
        n = len(board[0])

        def dfs(x, y, index, wordi):
            if index == len(wordi):
                return True
            tempt = board[x][y]
            board[x][y] = '/'
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == wordi[index]:
                    if dfs(nx, ny, index + 1, wordi):
                        return True
            board[x][y] = tempt
            return False

        shot = defaultdict(list)
        for i in range(m):
            for j in range(n):
                shot[board[i][j]].append((i, j))
        for i, j in shot[word[0]]:
            if dfs(i, j, 1, word):
                return True
        return False

    def main(self):
        board = [["C","A","A"],["A","A","A"],["B","C","D"]]
        word = "AAB"

        self.exist_simplified(board, word)
        self.exist_fast(board, word)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
