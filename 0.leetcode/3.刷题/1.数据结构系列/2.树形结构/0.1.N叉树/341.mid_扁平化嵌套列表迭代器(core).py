from fundamentals.test_time import test_time

"""
实际解法：
    
class NestedInteger:
   def isInteger(self) -> bool:
       "
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       "

   def getInteger(self) -> int:
       "
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       "

   def getList(self) -> [NestedInteger]:
       "
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       "

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
        self.it = self.create_iterator(nestedList)
        self.nt = None

    def create_iterator(self, nestedList):
        def tranverse(nl):
            if nl.isInteger():
                yield nl.getInteger()
            else:
                for nli in nl.getList():
                    yield from tranverse(nli)

        for nli in nestedList:
            yield from tranverse(nli)

    def next(self) -> int:
        return self.nt

    def hasNext(self) -> bool:
        try:
            self.nt = self.it.__next__()
            return True
        except:
            return False
"""

"""
以下是模拟解法 ，不构建NestedInteger 实例
"""


class Solution():
    def __init__(self):
        pass

    def flat_iterator(self, s):
        '''
        仅仅为了展示 yield from 和 yield 的区别！
            yield from 当返回的是迭代器时，一个个返回迭代器的内容
            yield 如果返回的是迭代器，直接把迭代器返回！（不把里面内容拆分一个个返回）
        :param s:
        :return:
        '''

        def tranverse(nested_list):
            if type(nested_list) != list:
                yield nested_list
            else:
                for nl in nested_list:
                    yield from tranverse(nl)

        # 1.这个仅供理解 yield from使用（嵌套多一层让你迷糊一下，理解就好了！）
        # for nli in s:
        #     yield from tranverse(nli)
        # 2.这个就清晰多了是吧 (等价的）
        yield from tranverse(s)

    def main(self):
        s = [[1, 1], 2, [1, 2, [2, 3, 4]]]
        it = self.flat_iterator(s)
        for i in it:
            print(i, end=' ')


if __name__ == '__main__':
    SL = Solution()
    SL.main()
