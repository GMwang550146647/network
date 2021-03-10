import unittest
from link_list import LinkList

class TestLinkList(unittest.TestCase):
    def setUp(self):
        pass
    def test_build_link_list(self):
        head = [3, 2, 0, -4]
        pos = 1
        link_list=LinkList().build_link_list(head,recur_index=pos)
        link_list.show(limit=20)

if __name__ == '__main__':
    unittest.main()