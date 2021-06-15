def toposort(graph):
    """
    原理：不停删除入度为0的节点
    """
    def cal_ingree(graph):
        ingree = {item: 0 for item in graph}
        for nodei in graph:
            for nodej in graph[nodei]:
                ingree[nodej] += 1
        return ingree

    ingree = cal_ingree(graph)
    stack = [item for item in ingree if ingree[item] == 0]
    result = ''
    while stack:
        cur_node = stack.pop()
        result += cur_node
        for next_nodei in graph[cur_node]:
            ingree[next_nodei] -= 1
            if ingree[next_nodei] == 0:
                stack.append(next_nodei)

    return "There's a Circle!" if len(result) != len(graph) else result


if __name__ == '__main__':
    G1 = {
        'a': 'bce',
        'b': 'd',
        'c': 'd',
        'd': '',
        'e': 'cd'
    }
    G2 = {'a': 'bce', 'b': 'd', 'c': 'd', 'd': 'e', 'e': 'cd'}
    G3={
        '1':'234',
        '2':'53',
        '3':'564',
        '4':'7',
        '5':'679',
        '6':'8',
        '7':'8',
        '8':'9',
        '9':'',
    }
    print(toposort(G1))
    print(toposort(G2))
    print(toposort(G3))
