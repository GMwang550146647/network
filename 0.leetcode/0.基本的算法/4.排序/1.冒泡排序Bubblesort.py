'''

1.冒泡排序：
把最大的数一个一个地丢到最前面（期间对比的时候，见到比自己小的就交换相邻两个）
优点：
在非顺序链表都可以用
'''
def bubbleSort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(1,i+1):
            if arr[j-1]>arr[j]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
    return arr
def bubbleSortModified(arr):
    for i in range(len(arr)-1,0,-1):
        modified=False
        for j in range(1,i+1):
            if arr[j-1]>arr[j]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
                modified=True
        if not modified:
            break
    return arr

arr=[9,8,7,6,5,4,3,2,1]
print(bubbleSort(arr.copy()))
print(bubbleSortModified(arr.copy()))