class Graph(object):

    def __init__(self, *args, **kwargs):
        self.node_neighbors = {}
        self.visited = {}
        self.edge_properties = {}  # 记录边的权重
        self.in_degree = {}  # 入度

    def add_nodes(self, nodelist):
        for node in nodelist:
            self.add_node(node)

    def add_node(self, node):
        if not node in self.node_neighbors:
            self.node_neighbors[node] = []

    def add_edge(self, edge, weight=1):
        u, v = edge
        if (v not in self.node_neighbors[u]) and (u not in self.node_neighbors[v]):
            self.node_neighbors[u].append(v)
            if (u != v):
                self.node_neighbors[v].append(u)
                self.edge_properties[edge] = weight
                self.edge_properties[(v, u)] = weight

    def add_arc(self, edge, weight=1):

        """ 加弧，有向"""
        u, v = edge
        if v not in self.node_neighbors[u]:
            self.node_neighbors[u].append(v)
            self.edge_properties[edge] = weight
            if v in self.in_degree:
                self.in_degree[v] = self.in_degree[v] + 1
            else:
                self.in_degree[v] = 1
            if u not in self.in_degree:
                self.in_degree[u] = 0

    def edge_weight(self, edge):
        if edge in self.edge_properties:
            return self.edge_properties[edge]
        return -1

    def nodes(self):
        return self.node_neighbors.keys()

    def depth_first_search(self, root=None):
        order = []

        def dfs(node):
            self.visited[node] = True
            order.append(node)
            for n in self.node_neighbors[node]:
                if not n in self.visited:
                    dfs(n)

        if root:
            dfs(root)
        for node in self.nodes():
            if not node in self.visited:
                dfs(node)
        print(order)
        return order

    def breadth_first_search(self, root=None):
        queue = []
        order = []

        def bfs():
            while len(queue) > 0:
                node = queue.pop(0)
                self.visited[node] = True
                for n in self.node_neighbors[node]:
                    if (not n in self.visited) and (not n in queue):
                        queue.append(n)
                        order.append(n)

        if root:
            queue.append(root)
            order.append(root)
            bfs()
        for node in self.nodes():
            if not node in self.visited:
                queue.append(node)
                order.append(node)
                bfs()
        print(order)

        return order