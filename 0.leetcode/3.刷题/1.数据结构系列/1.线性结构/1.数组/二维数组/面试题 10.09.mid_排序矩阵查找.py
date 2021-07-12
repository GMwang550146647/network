from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def searchMatrix(self,matrix,target):
        def search(pos,target):
            if pos[0]<len(matrix) and pos[1]>=0:
                if matrix[pos[0]][pos[1]]==target:
                    return True
                elif target>matrix[pos[0]][pos[1]]:
                    return search([pos[0]+1,pos[1]],target)
                else:
                    return search([pos[0],pos[1]-1],target)
            else:
                return False
        if not matrix:
            return False
        return search([0,len(matrix[0])-1],target)

    def main(self):
        matrix, target=[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5
        self.searchMatrix(matrix, target)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
