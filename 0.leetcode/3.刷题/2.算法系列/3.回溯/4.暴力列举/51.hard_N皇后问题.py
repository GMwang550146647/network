from fundamentals.tree import TreeNode, Tree
import time


class Solution():
    def __init__(self):
        pass

    '''我的方法'''

    def solveNQueens(self, n):
        """
        RECUR  pop insert heavy load (核心：重复的就不分枝了，但是要时刻知道剩下什么数字)
        """

        def gen_solution(q_pos):
            templates = [['.'] * n for i in range(n)]
            for pos_i in q_pos:
                templates[pos_i[0]][pos_i[1]]='Q'

            return [''.join(item) for item in templates]

        def get_legal_pos(current_q_pos,line_index):
            legal_pos = []
            ys = [item[1] for item in current_q_pos]
            sum_list = [x + y for x, y in current_q_pos]
            sub_list = [x - y for x, y in current_q_pos]
            for j in range(n):
                if j not in ys:
                    if line_index + j not in sum_list:
                        if line_index - j not in sub_list:
                            legal_pos.append((line_index, j))
            return legal_pos

        def backtrack(q_pos, n_left,line_i=0):
            if line_i==n:
                solutions.append(gen_solution(q_pos))
                return True
            legal_pos=get_legal_pos(q_pos,line_i)
            for pos_i in legal_pos:
                q_pos.append(pos_i)
                # #这个是只产生一个的情况
                # if backtrack(q_pos,n_left-1,line_i+1):
                #     return True
                backtrack(q_pos,n_left-1,line_i+1)
                q_pos.pop(-1)
        Q_POS = []
        solutions = []
        backtrack(Q_POS, n)
        return solutions

    def testTime(self, fun, args, test_times=1):
        # 计时
        start = time.process_time()
        for i in range(test_times):
            result = fun(*args)
        elapsed = (time.process_time() - start)
        print(fun.__name__, ":")
        print("Time used:", elapsed)
        print("Result:", result)
        print(len(result))

    def main(self):
        n = 8
        self.testTime(self.solveNQueens, args=(n,))


if __name__ == '__main__':
    SL = Solution()
    SL.main()
