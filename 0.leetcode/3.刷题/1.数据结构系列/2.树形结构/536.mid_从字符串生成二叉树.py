from fundamentals.test_time import test_time
from fundamentals.tree import TreeNode,Tree

class Solution():
    def __init__(self):
        pass

    @test_time
    def str2tree(self,s):
        def str_pairs(s):
            record={}
            stack=[]
            for i in range(len(s)):
                if s[i]=='(':
                    stack.append(i)
                elif s[i]==')':
                    record[stack.pop()]=i
            return record

        def parse_str(start,end):
            if start<end:
                i=start
                while i<end and s[i] not in '()':
                    i+=1
                cur_node=TreeNode(int(s[start:i]))
                if i+1<end:
                    left_start,left_end=i+1,record[i]
                    cur_node.left=parse_str(left_start,left_end)
                    if left_end < end-1:
                        right_start,right_end=left_end+2,record[left_end+1]
                        cur_node.right=parse_str(right_start,right_end)
                return cur_node
            else:
                return None
        record=str_pairs(s)
        return parse_str(0,len(s))

    def main(self):
        s="4(2(3)(1))(6(5))"
        self.str2tree(s)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
