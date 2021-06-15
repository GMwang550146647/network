"""
Dijkstra 特点
1.单源
2.无负权边

核心：
    每次都把当前最短的点抽出来，再去计算下一个除了当前点外，最近的点
"""
from functools import reduce


class Dijkstra():
    def __init__(self, G):
        self.dim = len(G)
        self.G = G

    def cal_min_dist(self, s, e):
        def get_min_index(index_set, arr):
            min_val, min_index = float('inf'), -1
            for i in index_set:
                if arr[i] < min_val:
                    min_val = arr[i]
                    min_index = i
            return min_index

        def get_path(e, cur):
            if pre[e]:
                for ei in pre[e]:
                    get_path(ei, cur + [e])
            else:
                paths.append(list(reversed(cur + [s])))

        # 1.初始化数据结构
        # 记录还没考虑的点
        unvisited = set(range(self.dim))
        # 记录s到该点的距离
        distance = [float('inf')] * self.dim
        # 记录前置节点
        pre = [[] for _ in range(self.dim)]
        distance[s] = 0

        # 2.每次找到unvisited中最近的节点，然后从unvisited中删除，然后更新由这个节点到所有连通节点的最短距离
        cur = s
        while unvisited:
            unvisited.remove(cur)
            for i in unvisited:
                new_d = distance[cur] + self.G[cur][i]
                if new_d < distance[i]:
                    distance[i] = new_d
                    pre[i] = [cur]
                elif new_d == distance[i]:
                    pre[i].append(cur)

            cur = get_min_index(unvisited, distance)

        # 3. 把路径计算出来
        paths = []
        get_path(e, [])
        return distance[e], paths

    def __call__(self, s, e):
        return self.cal_min_dist(s, e)


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

    F = Dijkstra(G)
    print(F(0, 8))
