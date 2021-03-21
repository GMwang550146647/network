from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    # @test_time
    def slidingPuzzle(self, board):
        def move(cur_path, i, j):
            '''把i和j位置调换'''
            i, j = (i, j) if i < j else (j, i)
            cur_path = cur_path[:i] + cur_path[j] + cur_path[i + 1:j] + cur_path[i] + cur_path[j + 1:]
            return cur_path

        # 0.把二维表压成一维表，记录着每个点的邻居
        neighbours = [
            [1, 3], [0, 4, 2], [1, 5], [0, 4], [3, 1, 5], [4, 2]
        ]
        # 1.初始化栈以及起点终点
        start = ''
        target = '123450'
        for i in range(len(board)):
            for j in range(len(board[0])):
                start += str(board[i][j])
        visited = {start}
        step = 0
        stack = [start]
        # 2.迭代求解
        while stack:
            len_stack = len(stack)
            for i in range(len_stack):
                cur_path = stack.pop(0)
                zero_index = cur_path.index('0')
                if cur_path == target:
                    return step
                for neighbour_i in neighbours[zero_index]:
                    next_move = move(cur_path, neighbour_i, zero_index)
                    if next_move not in visited:
                        stack.append(next_move)
                        visited.add(next_move)
            step += 1
        return -1

    def main(self):
        boards = [
            [[1, 2, 3], [4, 0, 5]], [[1, 2, 3], [5, 4, 0]], [[4, 1, 2], [5, 0, 3]], [[3, 2, 4], [1, 5, 0]],
            [[3, 0, 1], [4, 2, 5]]
        ]
        for board in boards:
            result = self.slidingPuzzle(board)
            print(result)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
