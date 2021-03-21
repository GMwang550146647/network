from fundamentals.tree import TreeNode,Tree
import time
class Solution():
    def __init__(self):
        pass
    '''我的方法'''
    max_route = -1000
    def buildTree(self, preorder, inorder):
        def build_tree_assist(ps, pe, ins, ine):
            if (ps >= pe or ins >= ine):
                return None
            root = TreeNode(preorder[ps])
            root_pos = in_map[root.val]
            root.left = build_tree_assist(ps + 1, ps + root_pos - ins+1, ins, root_pos)
            root.right = build_tree_assist(ps + root_pos - ins+1, pe, root_pos + 1, ine)
            return root

        in_map = {val: key for key, val in enumerate(inorder)}
        ps = ins = 0
        pe = ine = len(preorder)
        return build_tree_assist(ps, pe, ins, ine)

    '''答案方法1'''

    def testTime(self,fun,args,test_times=100):
        # 计时
        start = time.process_time()
        for i in range(test_times):
            result = fun(*args)
        elapsed = (time.process_time() - start)
        print(fun.__name__,":")
        print("Time used:", elapsed)
        print(Tree().mid_recur_tree(result))
    def main(self):
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        self.testTime(self.buildTree,args=(preorder,inorder))

if __name__=='__main__':
    SL=Solution()
    SL.main()
