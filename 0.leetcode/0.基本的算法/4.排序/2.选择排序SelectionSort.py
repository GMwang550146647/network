'''

2.选择排序：
每次选择最大的放在前面（或者最小的放在后面）
'''
def insertionSort(arr):
    for i in range(len(arr)-1,0,-1):
        max=-1
        maxj=-1
        for j in range(i+1):
            if arr[j]>max:
                max=arr[j]
                maxj=j
        if maxj!=-1:
            arr[maxj],arr[i]=arr[i],arr[maxj]
    return arr


arr=[9,8,7,6,5,4,3,2,1]
print(insertionSort(arr.copy()))
