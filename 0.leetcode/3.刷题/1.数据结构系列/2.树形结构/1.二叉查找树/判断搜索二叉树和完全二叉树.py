from fundamentals.test_time import test_time
from fundamentals.tree import Tree

class Solution():
    def __init__(self):
        pass

    @test_time
    def judgeIt(self , root ):
        # write code here
        result=[True,True]
        count=0
        cur_pos=0
        pre_num=-float('inf')
        def dfs(root,pos=1):
            if root:
                dfs(root.left,pos*2)
                nonlocal count,cur_pos,pre_num,result
                count+=1
                cur_pos=max(cur_pos,pos)
                if root.val<pre_num:
                    result[0]=False
                pre_num=root.val
                dfs(root.right,pos*2+1)
        dfs(root)
        if cur_pos!=count:
            result[1]=False
        print(count,cur_pos)
        return result

    def main(self):
        root=[107,29,89,130,12,109,85,86,52,74,121,106,122,141,65,50,28,118,61,99,57,7,25,148,4,69,151,20,142,32,120,71,117,45,83,58,19,53,60,157,101,76,125,35,3,110,96,139,145,108,27,116,135,81,6,8,150,41,127,64,43,156,104,9,1,126,14,51,22,26,67,21,153,75,143,34,2,159,158,154,94,46,147,49,15,123,70,47,16,87,59,62,138,72,97,124,144,80,90,36,149,23,160,33,44,10,114,79,54,134,129,131,82,77,115,55,39,88,68,73,5,92,38,132,24,17,40,98,146,31,100,66,137,13,63,128,84,11,119,102,103,95,152,30,105,37,78,113,91,140,155,111,18,136,42,161,133,93,48,112,56]

        root= Tree().build_tree_from_level_recur_list(root)
        Tree().mid_recur_tree(root)
        self.judgeIt(root)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
