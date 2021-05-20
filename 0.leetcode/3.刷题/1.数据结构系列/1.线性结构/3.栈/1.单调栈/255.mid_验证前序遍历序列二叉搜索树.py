from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def verifyPreorder(self, preorder):
        first_largest = [0] * len(preorder)
        stack = []
        for i in range(len(preorder) - 1, -1, -1):
            while stack and stack[-1][0] <= preorder[i]:
                stack.pop(-1)
            if not stack:
                first_largest[i] = len(preorder)
            else:
                first_largest[i] = stack[-1][1]
            stack.append([preorder[i], i])

        def build_tree(s, e, lower=None, upper=None):
            if s == e:
                return True
            else:
                if lower is not None:
                    if preorder[s] < lower:
                        return False
                elif upper is not None:
                    if preorder[s] > upper:
                        return False
                divided_point = first_largest[s]
                divided_point = min(divided_point, e)
                return build_tree(s + 1, divided_point, upper=preorder[s], lower=lower) and \
                       build_tree(divided_point, e,lower=preorder[s],upper=upper)

        return build_tree(0, len(preorder))

    def verifyPreorder_answer(self, preorder):
        """
        1.这个题真怪

        2.局部递减，整体递增

        3.单调递减栈

        4.时刻更新左侧最上的点
        """
        # 局部递减  整体递增
        dec_stack = []
        pre_max = -0x3f3f3f3f  # 左下点的位置（一条左上至右下的斜线分割，斜线上最左上的点）
        for x in preorder:
            if pre_max > x:  # 右侧的，要比左边的大（整体递增）
                return False
            while dec_stack and dec_stack[-1] <= x:  # （维持局部递减）
                pre_max = dec_stack.pop()

            dec_stack.append(x)

        return True


    def main(self):
        preorder = [5, 2, 6, 1, 3]
        self.verifyPreorder(preorder)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
    print()
