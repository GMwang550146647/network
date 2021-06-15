"""
Floyd方法 特点
1.弗洛伊德算法是解决任意两点间的最短路径的一种算法
2.可以正确处理有向图或有向图或负权（但不可存在负权回路)的最短路径问题，同时也被用于计算有向图的传递闭包。

核心：
    每次都在中间增多一个中转点 v，看看每一条路(i，v, j)有没有变短！ 如果没有就 使用 (i,j) 否则 (i,v,j)更新该距离
"""
from collections import defaultdict
from functools import reduce
import copy


class Floyed():
    def __init__(self, G):

        self.dim = len(G)
        # 最小距离
        self._min_dist = copy.deepcopy(G)
        # 该最小距离的路径
        self._min_path = [[[[j, i]] for i in range(self.dim)] for j in range(self.dim)]
        self.cal_min_dist()

    def cal_min_dist(self):
        # 中接点
        for k in range(self.dim):
            # 起点
            for i in range(self.dim):
                # 终点
                for j in range(self.dim):
                    cur_dist = self._min_dist[i][k] + self._min_dist[k][j]
                    if i != j and k != i and k != j:
                        # 注意： new_path 主要是为了把 各点的路径记录下来，如果只在意distance ，只需要看_min_dist的更新
                        # 这里写得复杂了，是为了把相同长度的路径也考虑上了
                        if cur_dist == self._min_dist[i][j]:
                            new_path = [pathi + [j] for pathi in self._min_path[i][k]]
                            for new_pathi in new_path:
                                if new_pathi not in self._min_path[i][j]:
                                    self._min_path[i][j].append(new_pathi)
                        elif cur_dist < self._min_dist[i][j]:
                            self._min_dist[i][j] = cur_dist
                            self._min_path[i][j] = [pathi + [j] for pathi in self._min_path[i][k]]

    def __call__(self, s, e):
        return self._min_dist[s][e], self._min_path[s][e]


if __name__ == '__main__':
    a = 9999999999  # 无穷大
    G = [
        [0, -2, 2, 4, a, a, a, a, a],
        [a, 0, 0, a, 4, a, a, a, a],
        [a, a, 0, 2, 4, 4, a, a, a],
        [a, a, a, 0, a, a, 5, a, a],
        [a, a, a, a, 0, 0, 3, a, 6],
        [a, a, a, a, a, 0, a, 3, a],
        [a, a, a, a, a, a, 0, 1, a],
        [a, a, a, a, a, a, a, 0, 1],
        [a, a, a, a, a, a, a, a, 0]]

    F = Floyed(G)
    print(F(0, 8))