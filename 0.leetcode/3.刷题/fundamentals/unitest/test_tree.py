import unittest
from tree import Tree

class TestTree(unittest.TestCase):
    def setUp(self):
        pass
    def test_build_tree(self):
        tree_list = [-10, 9, 20, None, None, 15, 7]
        tree=Tree().build_tree_from_list(tree_list)
        Tree().mid_recur_tree(tree)

if __name__ == '__main__':
    unittest.main()