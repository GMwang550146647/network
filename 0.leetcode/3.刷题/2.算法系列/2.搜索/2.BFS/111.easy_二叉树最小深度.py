from fundamentals.tree import TreeNode, Tree
import time


class Solution():
    def __init__(self):
        pass

    '''我的方法'''
    max_route = -1000

    def minDepth(self, root):

        def level_traversal(root):
            queue = [root]
            steps=1
            while len(queue) != 0:
                for i in range(len(queue)):
                    current_node = queue.pop(0)
                    count = 0
                    if current_node.left:
                        queue.append(current_node.left)
                        count += 1
                    if current_node.right:
                        queue.append(current_node.right)
                        count += 1
                    if count == 0:
                        return steps
                steps+=1
        return level_traversal(root)

    '''答案方法1'''

    def testTime(self, fun, args, test_times=100):
        # 计时
        start = time.process_time()
        for i in range(test_times):
            result = fun(*args)
        elapsed = (time.process_time() - start)
        print(fun.__name__, ":", result)
        print("Time used:", elapsed)

    def main(self):
        root = [3,9,20,None,None,15,7]
        root = Tree().build_tree_from_list(root)
        Tree().mid_recur_tree(root)
        self.testTime(self.minDepth, args=(root,))


if __name__ == '__main__':
    SL = Solution()
    SL.main()
