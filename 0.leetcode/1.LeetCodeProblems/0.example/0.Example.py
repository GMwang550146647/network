from fundamentals.link_list import LinkList
import time
from fundamentals.test_time import test_time

class Solution():
    def __init__(self):
        pass

    '''我的方法'''

    @test_time
    def myFun1(self,s):
        for i in range(1000):
            a=10000**2

    @test_time
    def myFun2(self,s):
        for i in range(1000):
            a=100000000**0.5

    def main(self):
        s='dfkljal'
        self.myFun1(s)
        self.myFun2(s)

if __name__=='__main__':
    SL=Solution()
    SL.main()
