from fundamentals.test_time import test_time
from collections import defaultdict


class Solution():
    def __init__(self):
        pass

    @test_time
    def findWords(self, board, words):
        '''
        不停地找
        '''
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
                        board[x][y] = tempt
                        return True
            board[x][y] = tempt
            return False

        shot = defaultdict(list)
        for i in range(m):
            for j in range(n):
                shot[board[i][j]].append((i, j))
        result = []
        for word_i in words:
            for i, j in shot[word_i[0]]:
                if dfs(i, j, 1, word_i):
                    result.append(word_i)
                    break
        return result

    @test_time
    def findWords_fast(self, board, words):
        """
        不停地找
        """
        n, m = len(board), len(board[0])

        shot = defaultdict(list)
        for i in range(n):
            for j in range(m):
                shot[board[i][j]].append((i, j))

        road = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def go(w, index, x, y):
            if index == len(w):
                return True
            r[x][y] = 0
            for a, b in road:
                i, j = x + a, y + b
                if -1 < i < n and -1 < j < m and r[i][j] and board[i][j] == w[index] and go(w, index + 1, i, j):
                    return True
            r[x][y] = 1
            return False

        res = []
        for w in words:
            for x, y in shot[w[0]]:
                r = [[1] * m for _ in range(n)]
                if go(w, 1, x, y):
                    res.append(w)
                    break
        return res

    def main(self):
        # board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
        # words = ["oath","pea","eat","rain"]
        board = [["a", "a"]]
        words = ['aaa']
        self.findWords(board, words)
        self.findWords_fast(board, words)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
