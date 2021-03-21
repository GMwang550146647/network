from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        col_dim = len(matrix[0])
        row_dim=len(matrix)
        col_set = set()
        row_set = set()

        for i in range(row_dim):
            for j in range(col_dim):
                if matrix[i][j] == 0:
                    col_set.add(j)
                    row_set.add(i)
        print(col_set, row_set)
        for coli in col_set:
            for i in range(row_dim):
                matrix[i][coli] = 0
        for rowi in row_set:
            for i in range(col_dim):
                matrix[rowi][i] = 0
        return matrix

    def main(self):
        maxtrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        self.setZeroes(maxtrix)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
