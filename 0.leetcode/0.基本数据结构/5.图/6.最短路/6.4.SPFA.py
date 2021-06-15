"""
SPFA 特点
1.单源
2.无负权圈
原理：
    其实就是Bellman Ford 中只迭代有路径更新的点
"""
from functools import reduce


class SPFA():
    def __init__(self, G):
        self.dim = len(G)
        self.G = G

    def cal_min_dist(self, s, e):

        def update_distance(s):
            stack = [s]
            while stack:
                cur = stack.pop(0)
                for i in range(self.dim):
                    if i != cur:
                        new_d = distance[cur] + self.G[cur][i]
                        if new_d < distance[i]:
                            distance[i] = new_d
                            pre[i] = [cur]
                            stack.append(i)
                        elif new_d == distance[i]:
                            pre[i].append(cur)
                stack=list(set(stack))

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
        update_distance(s)

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

    F = SPFA(G)
    print(F(0, 8))
