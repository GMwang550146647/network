from fundamentals.test_time import test_time
from fundamentals.tree import Tree


class Solution():
    def __init__(self):
        pass

    @test_time
    def printTree(self, root):
        # 层级遍历
        stack = [[root, 0]]
        level = []
        while stack:
            tempt = []
            for i in range(len(stack)):
                cur, id = stack.pop(0)
                tempt.append((cur.val, id))
                if cur.left:
                    stack.append([cur.left, id * 2])
                if cur.right:
                    stack.append([cur.right, id * 2 + 1])
            level.append(tempt)
        # 再计算各自位置
        n = len(level)
        result = [[''] * (2 ** n - 1) for _ in range(n)]
        for i in range(n):
            for nodei in level[i]:
                indexi = int(2 ** (n - i) * (nodei[1] + 0.5) - 1)
                result[i][indexi] = str(nodei[0])
        return result

    def main(self):
        tree = [1, 2, 3, None, 4, None, None]
        root = Tree().build_tree_from_list(tree)
        Tree().mid_recur_tree(root)
        self.printTree(root)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
