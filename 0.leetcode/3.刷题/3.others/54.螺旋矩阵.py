from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def spiralOrder(self, matrix):
        n_rows=len(matrix)
        n_cols=len(matrix[0])
        if n_cols==0:
            return []
        visited_rows={-1,n_rows}
        visited_cols={-1,n_cols}
        i,j=0,0
        row_dir=True
        pos_dir=True
        spiral_list=[matrix[i][j]]
        while len(visited_cols)<n_cols+2 and len(visited_rows)<n_rows+2:
            if row_dir:
                step=1 if pos_dir else -1
                while(j+step not in visited_cols):
                    j+=step
                    spiral_list.append(matrix[i][j])
                visited_rows.add(i)
            else:
                step=1 if pos_dir else -1
                while(i+step not in visited_rows):
                    i+=step
                    spiral_list.append(matrix[i][j])
                visited_cols.add(j)
            row_dir= not row_dir
            if row_dir:
                pos_dir= True if j+1 not in visited_cols else False
            else:
                pos_dir= True if i+1 not in visited_rows else False
        return spiral_list

    def main(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.spiralOrder(matrix)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
