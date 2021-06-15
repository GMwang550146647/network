from collections import defaultdict
from functools import reduce


def CPM(nn, ss, tt, edges):
    def dfs_earliest(cur):
        '''
        计算出最早出现时间中最迟的时间，就是这个事情有好多前导事件，要这些事件陆续做完才能做
        '''
        for nexti in next_nodes[cur]:
            et[nexti] = max(et[nexti], et[cur] + path_val[(cur, nexti)])
            dfs_earliest(nexti)

    def dfs_latest(cur):
        '''
        计算出最迟出现时刻中最早的时间，就是这个事件后面接很多后续事件(有deadline)，要最早把这个前导事件做了，后面才能陆续进行！
        '''
        for prei in pre_nodes[cur]:
            lt[prei] = min(lt[prei], lt[cur] - path_val[(prei, cur)])
            dfs_latest(prei)

    def extract_path(cur, path, cur_val=0):
        """
        根据前导后后续的时间要求，恢复关键路径
        """
        if not next_nodes[cur]:
            result.append(path.copy())
        else:
            for nexti in next_nodes[cur]:
                new_path_val = cur_val + path_val[cur, nexti]
                # new_path_val==et[nexti] 要求当前关键路径的值等于et
                if et[nexti] == lt[nexti] and new_path_val == et[nexti]:
                    path.append(nexti)
                    extract_path(nexti, path, new_path_val)
                    path.pop()

    # 1.数据结构准备
    # 所有的点
    nodes = reduce(lambda x, y: set(x) | set(y), [edgei[:2] for edgei in edges])
    # 前接点集
    pre_nodes = defaultdict(list)
    for edgei in edges:
        pre_nodes[edgei[1]].append(edgei[0])
    # 后接点集
    next_nodes = defaultdict(list)
    for edgei in edges:
        next_nodes[edgei[0]].append(edgei[1])
    # {path:val}的字典
    path_val = {(item[0], item[1]): item[2] for item in edges}

    # 2. 前向后向算法，计算出最早最迟时间，et&lt
    pre_seq = defaultdict(list)
    et = {ki: -float('inf') for ki in nodes}
    lt = {ki: float('inf') for ki in nodes}
    et[ss] = 0
    dfs_earliest(ss)
    lt[tt] = et[tt]
    dfs_latest(tt)
    print(pre_nodes)
    print(next_nodes)
    print('et:', et)
    print('lt', lt)

    # 3.根据et，lt计算出路径
    result = []
    extract_path(ss, [ss])
    return result


if __name__ == '__main__':
    """
    第一行是四个由空格隔开的整数 nn (节点个数), ss (源点), tt (终点)。此后的 mm 行，
    每行三个正整数 aa, bb, cc, 表示一条从节点 aa 到节点 bb 的一条长度为 cc 的边。（节点个数小于 1515 个）
    """
    nn, ss, tt = (9, 0, 8)
    edges = [(0, 1, 2), (0, 2, 2), (0, 3, 4), (1, 4, 4), (1, 2, 0), (2, 4, 4), (2, 5, 4), (2, 3, 2), (3, 6, 5),
             (4, 8, 6), (4, 6, 3), (4, 5, 0), (5, 7, 3), (7, 8, 1), (6, 7, 1)]
    print(CPM(nn, ss, tt, edges))
