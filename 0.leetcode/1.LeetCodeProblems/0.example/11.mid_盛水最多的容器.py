"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

 



图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

 

示例：

输入：[1,8,6,2,5,4,8,3,7]
输出：49

"""

import time
class Solution():
    def __init__(self):
        pass
    '''我的方法'''
    def myFun(self,s):

        len_s=len(s)
        start_list=[0]
        max_s=s[0]
        for s_i in range(1,len_s):
            if s[s_i]>max_s:
                start_list.append(s_i)
                max_s=s[s_i]
        end_list = [len_s - 1]
        max_e=s[-1]
        for s_j in range(len_s-2,-1,-1):
            if s[s_j]>max_e:
                max_e=s[s_j]
                end_list.append(s_j)
        max_volumn = 0
        for s_i in start_list:
            for s_j in end_list:
                volumn=min(s[s_i],s[s_j])*(s_j-s_i)
                volumn=abs(volumn)
                if volumn>max_volumn:
                    max_volumn=volumn
        return max_volumn

    '''答案方法1'''
    def maxArea(self, s):
        p1=len(s)-1
        p2=0
        max_area=0
        while p1!=p2:
            area=min(s[p1],s[p2])*(p1-p2)
            if area>max_area:
                max_area=area
            if s[p1]>s[p2]:
                p2+=1
            else:
                p1-=1
        return max_area
    def testTime(self,fun,args):
        # 计时
        start = time.process_time()
        result = fun(*args)
        elapsed = (time.process_time() - start)
        print(fun.__name__,":")
        print("Time used:", elapsed)
        print('result:', result)
    def main(self):
        s=[1,8,6,2,5,4,8,3,7]
        self.testTime(self.myFun,args=(s,))
        self.testTime(self.maxArea, args=(s,))
if __name__=='__main__':
    SL=Solution()
    SL.main()
