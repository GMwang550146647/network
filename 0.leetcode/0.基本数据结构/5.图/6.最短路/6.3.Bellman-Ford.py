"""
BellmanFord 特点
1.单源
2.有负边权，但是没有负环

核心 ： 每次"加多一条边" 看看有没有更短(如果没有，就选之前的策略)
disti[u] 为 源点v到终点只经过i条边的最短路径！
dist[i][v]= min(dist[i-1][v] , dist[i-1][j] + Distance[j][v])
                #经过i-1条边的最短距离   #经过i条边的最短距离
"""
from functools import reduce


class BellmanFord():
    def __init__(self, G):
        self.dim = len(G)
        self.G = G

    def cal_min_dist(self, s, e):
        def update_distance():
            change_flag = False
            # 遍历所有的边(i,j) 去更新 最短距离
            for cur in range(self.dim):
                for i in range(self.dim):
                    if i != cur:
                        new_d = distance[cur] + self.G[cur][i]
                        if new_d < distance[i]:
                            distance[i] = new_d
                            pre[i] = [cur]
                            change_flag = True
                        elif new_d == distance[i]:
                            if cur not in pre[i]:
                                pre[i].append(cur)
            return change_flag

        def get_path(e, cur):
            if pre[e]:
                for ei in pre[e]:
                    get_path(ei, cur + [e])
            else:
                paths.append(list(reversed(cur + [s])))

        # 1.初始化数据结构
        # 记录s到该点的距离
        distance = [float('inf')] * self.dim
        # 记录前置节点
        pre = [[] for _ in range(self.dim)]
        distance[s] = 0

        # 2.每次找到unvisited中最近的节点，然后从unvisited中删除，然后更新由这个节点到所有连通节点的最短距离
        for i in range(self.dim + 1):
            flag = update_distance()
            if flag:
                # 如果经过N条边之后，最短距离还在变化，说明存在负环
                if i >= self.dim:
                    print("Negative Loop Exists!")
                    return None, None
            else:
                break
        # 3. 把路径计算出来
        paths = []

        get_path(e, [])
        return distance[e], paths

    def __call__(self, s, e):
        return self.cal_min_dist(s, e)


if __name__ == '__main__':
    a = 9999999999  # 无穷大
    G1 = [
        [0, -2, 2, 4, a, a, a, a, a],
        [a, 0, 0, a, 4, a, a, a, a],
        [a, a, 0, 2, 4, 4, a, a, a],
        [a, a, a, 0, a, a, 5, a, a],
        [a, a, a, a, 0, 0, 3, a, 6],
        [a, a, a, a, a, 0, a, 3, a],
        [a, a, a, a, a, a, 0, 1, a],
        [a, a, a, a, a, a, a, 0, 1],
        [a, a, a, a, a, a, a, a, 0]]
    G2 = [
        [0, 2, 2, 4, a, a, a, a, a],
        [-10, 0, 0, a, 4, a, a, a, a],
        [a, a, 0, 2, 4, 4, a, a, a],
        [a, a, a, 0, a, a, 5, a, a],
        [a, a, a, a, 0, 0, 3, a, 6],
        [a, a, a, a, a, 0, a, 3, a],
        [a, a, a, a, a, a, 0, 1, a],
        [a, a, a, a, a, a, a, 0, 1],
        [a, a, a, a, a, a, a, a, 0]]
    F1 = BellmanFord(G1)
    print(F1(0, 8))
    F2 = BellmanFord(G2)
    print(F2(0, 8))
