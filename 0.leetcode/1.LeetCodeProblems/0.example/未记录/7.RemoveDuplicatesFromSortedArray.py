'''
such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.

Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference , which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
'''
import time
class Solution():
    def __init__(self):
        self.arr=[0,0,0,1,1,1,1,2,2,2,2,2,3,3,3,3,3,5,5,5,6,6,6,6,6,7,7,7,8]

    '''我的方法'''
    def myFun(self):
        pre=self.arr[0]
        count=1
        result=[pre]
        for i in range(len(self.arr)):
            if self.arr[i]!=pre:
                pre=self.arr[i]
                count+=1
                result.append(pre)
        return result
    '''答案方法1'''

    def testTime(self,fun):
        # 计时
        start = time.process_time()
        result = fun()
        elapsed = (time.process_time() - start)
        print(fun.__name__,":")
        print("Time used:", elapsed)
        print('result:', result)
    def main(self):
        self.testTime(self.myFun)
SL=Solution()
SL.main()