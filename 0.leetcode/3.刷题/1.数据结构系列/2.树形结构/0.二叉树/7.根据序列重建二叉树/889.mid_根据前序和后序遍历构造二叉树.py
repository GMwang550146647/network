from fundamentals.test_time import test_time
from fundamentals.tree import TreeNode

class Solution():
    def __init__(self):
        pass

    @test_time
    def constructFromPrePost(self,pre,post):
        def build_tree(pre,post):
            if len(pre)==1:
                return TreeNode(pre[0])
            elif pre and post:
                root=TreeNode(pre[0])
                pre_index=pre.index(post[-2])
                post_index=post.index(pre[1])
                left_pre=pre[1:pre_index]
                left_post=post[:post_index+1]
                right_pre=pre[pre_index:]
                right_post=post[post_index+1:len(pre)-1]
                if left_pre and left_post:
                    root.left=build_tree(left_pre,left_post)
                    root.right=build_tree(right_pre,right_post)
                elif not left_pre:
                    root.left=build_tree(right_pre,left_post)
                else:
                    root.right=build_tree(left_pre,right_post)
                return root
            else:
                return None
        return build_tree(pre,post)

    def main(self):
        pre = [1, 2, 4, 5, 3, 6, 7]
        post = [4, 5, 2, 6, 7, 3, 1]
        self.constructFromPrePost(pre,post)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
