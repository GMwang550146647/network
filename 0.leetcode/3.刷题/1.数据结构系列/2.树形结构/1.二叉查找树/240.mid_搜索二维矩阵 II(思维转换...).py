from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def searchMatrix(self, matrix,target):
        """
        矩阵左旋45度， 有点像二叉搜索树！
        :param matrix:
        :param target:
        :return:
        """
        n_col=len(matrix[0])
        n_row=len(matrix)
        i=0
        j=n_col-1
        while(i<n_row and j>=0):
            if matrix[i][j]<target:
                i+=1
            elif matrix[i][j]>target:
                j-=1
            else:
                return True
        return False

    def main(self):
        matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
        target = 5
        self.searchMatrix(matrix,target)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
