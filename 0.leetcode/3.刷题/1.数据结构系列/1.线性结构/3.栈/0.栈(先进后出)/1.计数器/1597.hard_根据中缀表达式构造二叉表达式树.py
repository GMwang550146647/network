from fundamentals.test_time import test_time
from fundamentals.tree import TreeNode

class Solution():
    def __init__(self):
        pass

    @test_time
    def expTree(self, s: str) :
        def get_post_expression(s):
            priority = {'+': 2, '-': 2, '*': 1, '/': 1, '(': 3, ')': 3}
            num_stack = []
            sign_stack = []
            i = 0
            for i in range(len(s)):
                # 符号
                if s[i] in '+-*/':
                    while sign_stack and priority[sign_stack[-1]] <= priority[s[i]]:
                        num_stack.append(sign_stack.pop())
                    sign_stack.append(s[i])
                elif s[i] == '(':
                    sign_stack.append(s[i])
                elif s[i] == ')':
                    while sign_stack[-1] != '(':
                        num_stack.append(sign_stack.pop())
                    sign_stack.pop()
                # 数字
                else:
                    num_stack.append(s[i])
            while sign_stack:
                num_stack.append(sign_stack.pop())
            return num_stack

        def build_tree(expression):
            if not expression:
                return None
            else:
                signi = expression.pop()
                root = TreeNode(signi)
                if signi in '+-*/':
                    root.right = build_tree(expression)
                    root.left = build_tree(expression)
                return root

        expression = get_post_expression(s)
        return build_tree(expression)


    def main(self):
        s="2-3/(5*2)+1"
        self.expTree(s)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
