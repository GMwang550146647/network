'''Given an array nums and a value val , remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.

Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference , which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
'''
import time
class Solution():
    def __init__(self):
        self.arr=[0,1,2,3,2,4,5,6,5,2,4,3,2,1,0,2,3,4,5,6,2,2,2,4,4,2,2]
        self.deleteNum=2
    '''我的方法'''
    def myFun(self):
        arr=self.arr.copy()
        i=0
        length=len(arr)
        while(i<length):
            if arr[i]==self.deleteNum:
                arr.pop(i)
                length-=1
            else:
                i+=1
        return arr

    '''答案方法1'''
    def removeElement(self):
        slow=-1
        arr=self.arr.copy()
        for i in range(len(arr)):
            if arr[i]!=self.deleteNum:
                slow+=1
                arr[slow]=arr[i]
        return arr[:slow+1]

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
        self.testTime(self.removeElement)
SL=Solution()
SL.main()