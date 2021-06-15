from collections import defaultdict


def Prim(graph):
    """
    原理：每次都在 visited 和 unvisited的 点 组合路径中找到最短的那一条，然后把新的点加入visited，并从unvisited中删除
    """
    def find_next_node():
        min_distance = float('inf')
        min_edge = None
        new_node = None
        for nodei in visited:
            for neighbori in neighbors[nodei]:
                if neighbori not in visited:
                    edge = (neighbori, nodei) if (neighbori, nodei) in graph else (nodei, neighbori)
                    distance = graph[edge]
                    if distance < min_distance:
                        min_distance = distance
                        min_edge = edge
                        new_node = neighbori
        return min_edge, new_node

    # 1.构建连接关系表
    neighbors = defaultdict(list)
    for edgei in graph:
        neighbors[edgei[0]].append(edgei[1])
        neighbors[edgei[1]].append(edgei[0])
    unvisited = set(neighbors.keys())
    visited = {unvisited.pop(), }
    min_tree = {}

    # 2.每次找到 visited与unvisited间的一条最小的边
    while len(visited) < len(neighbors):
        new_edge, new_node = find_next_node()
        min_tree[new_edge] = graph[new_edge]
        visited.add(new_node)
        unvisited.remove(new_node)
    return min_tree


if __name__ == '__main__':
    G = {
        (1, 2): 6, (1, 3): 1, (1, 4): 5, (2, 3): 3, (2, 5): 5, (3, 4): 5, (3, 5): 6, (3, 6): 4, (4, 6): 2, (5, 6): 6
    }
    print(Prim(G))
