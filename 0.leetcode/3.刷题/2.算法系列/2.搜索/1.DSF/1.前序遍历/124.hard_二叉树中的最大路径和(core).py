from fundamentals.tree import Tree
import time
class Solution():
    def __init__(self):
        pass
    '''我的方法'''
    max_route = -1000



    def maxPathSum(self, root) -> int:
        def oneSideMax(root):
            if root is None:
                return 0
            else:
                max_left = oneSideMax(root.left)
                max_right = oneSideMax(root.right)
                max_left = 0 if max_left < 0 else max_left
                max_right = 0 if max_right < 0 else max_right
                self.max_route = max(self.max_route, max_left + max_right + root.val)
                return max(max_left, max_right) + root.val
        oneSideMax(root)
        return self.max_route

    '''答案方法1'''

    def testTime(self,fun,args,test_times=100):
        # 计时
        start = time.process_time()
        for i in range(test_times):
            result = fun(*args)
        elapsed = (time.process_time() - start)
        print(fun.__name__,":")
        print("Time used:", elapsed)
        print('result:', result)
    def main(self):
        s=[-10,9,20,None,None,15,7]
        tree=Tree().build_tree_from_list(s)
        self.testTime(self.maxPathSum,args=(tree,))

if __name__=='__main__':
    SL=Solution()
    SL.main()
