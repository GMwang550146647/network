from fundamentals.test_time import test_time
from fundamentals.tree import Tree


class Solution():
    def __init__(self):
        pass

    @test_time
    def searchBST(self, root, val):
        def search(root, val):
            if root:
                if val == root.val:
                    return root
                elif val > root.val:
                    return search(root.right, val)
                else:
                    return search(root.left, val)
            else:
                return None

        return search(root, val)

    def main(self):
        tree = [2, 1, 3, None, None, None, 4]
        root = Tree().build_tree_from_list(tree)
        Tree().mid_recur_tree(root)
        self.searchBST(root, 4)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
