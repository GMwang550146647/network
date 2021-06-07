class Node(object):
    def __init__(self, name=None, value=None):
        self.name = name
        self.val = value
        self.left = None
        self.right = None


class HuffmanTree(object):
    def __init__(self, word_freq):
        self.record = {}
        self.root = self.build_tree(word_freq)
        self.get_code()

    def build_tree(self, word_freq):
        def insert_node(arr, node):
            """
            把node插入arr中适合的位置，使其val按递减排序
            """
            i=0
            while i< len(arr):
                if arr[i].val <= node.val:
                    break
                i+=1
            arr.insert(i, node)
            return arr

        def build_tree(nodes):
            """
            建立霍夫曼树
            """
            if len(nodes) <= 1:
                return nodes[0]
            else:
                node1 = nodes.pop()
                node2 = nodes.pop()
                new_node = Node(node1.name + node2.name, node1.val + node2.val)
                new_node.left = node1
                new_node.right = node2
                nodes = insert_node(nodes, new_node)
                return build_tree(nodes)

        words = sorted(word_freq.items(), key=lambda a: a[1], reverse=True)
        nodes = [Node(item[0], item[1]) for item in words]
        return build_tree(nodes)

    def get_code(self):
        """
        解释霍夫曼树
        """
        def dfs(root,cur=''):
            if root:
                if not root.left and not root.right:
                    self.record[root.name]=cur
                else:
                    dfs(root.left,cur+'0')
                    dfs(root.right,cur+'1')
        dfs(self.root)




if __name__ == '__main__':
    char_weights = {'a': 5, 'b': 4, 'c': 10, 'd': 8, 'f': 15, 'g': 2}
    tree = HuffmanTree(char_weights)
    print(tree.record)
