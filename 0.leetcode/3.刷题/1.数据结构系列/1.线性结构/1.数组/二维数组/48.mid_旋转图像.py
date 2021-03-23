from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def rotate(self, matrix):
        base = len(matrix) - 1
        for i in range(len(matrix) // 2):
            for j in range(i, len(matrix) - 1 - i):
                matrix[i][j], matrix[base - j][i], matrix[base - i][base - j], matrix[j][base - i] = \
                    matrix[base - j][i], matrix[base - i][base - j], matrix[j][base - i], matrix[i][j]
        return matrix

    def main(self):
        matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        self.rotate(matrix)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
