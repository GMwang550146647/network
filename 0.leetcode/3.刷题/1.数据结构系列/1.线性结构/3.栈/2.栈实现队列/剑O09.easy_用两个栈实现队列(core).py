from fundamentals.test_time import test_time


class CQueue:

    def __init__(self):
        self.stk_app = []
        self.stk_del = []

    def appendTail(self, value: int) -> None:
        """
        增加的时候
            1.如果stk_app 非空，直接丢在尾部
            2.如果stk_app 是空的，元素可能都在stk_del中，从stk_del中拿回来再加在尾部
        """
        if self.stk_del:
            while self.stk_del:
                self.stk_app.append(self.stk_del.pop(-1))
        self.stk_app.append(value)

    def deleteHead(self) -> int:
        '''
        删除的时候
            1.如果stk_del 非空，直接丢掉最后一个得了
            2.如果stk_del 是空的，元素可能都在stk_app中，从stk_app中拿回来再加在尾部
        '''
        if self.stk_del:
            return self.stk_del.pop(-1)
        elif self.stk_app:
            while self.stk_app:
                self.stk_del.append(self.stk_app.pop(-1))
            return self.stk_del.pop(-1)
        else:
            return -1



