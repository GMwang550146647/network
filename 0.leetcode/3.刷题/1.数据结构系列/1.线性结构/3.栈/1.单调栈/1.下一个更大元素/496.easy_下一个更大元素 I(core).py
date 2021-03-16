from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    @test_time
    def nextGreaterElement(self, nums1,nums2):
        stack = []
        record = {}
        # 从后往前处理
        for i in range(len(nums2) - 1, -1, -1):
            # 2.1.如果比栈顶要大：一直pop到比当前值要大的值为止，如果空了，就返回-1，如果没空，返回栈顶，并加入当前值到stack
            while stack and stack[-1] <= nums2[i]:
                stack.pop(-1)
            if not stack:
                record[nums2[i]]=-1
                stack.append(nums2[i])
            else:
                record[nums2[i]]=stack[-1]
                stack.append(nums2[i])
        result=[record[i] for i in nums1]
        return result

    def main(self):
        nums1 = [4, 1, 2]
        nums2 = [1, 3, 4, 2]
        self.nextGreaterElement(nums1,nums2)


if __name__ == '__main__':
    SL = Solution()
    SL.main()
