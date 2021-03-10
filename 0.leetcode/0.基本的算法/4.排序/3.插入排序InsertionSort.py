'''

3.插入排序排序：
每次地把后面的一个插入到前面的序列中
'''
def insertionSort(arr):
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[j]>arr[i]:
                tempt=arr[i]
                for k in range(i,j,-1):
                    arr[k]=arr[k-1]
                arr[j]=tempt
    return arr

'''标准版本：从最后一个开始比对，直到找到位置才停止'''
def insertionSortS(arr):
    for index in range(1,len(arr)):
        currentvalue=arr[index]
        position=index
        while position>0 and arr[position-1]>currentvalue:
            arr[position]=arr[position-1]
            position-=1
        arr[position]=currentvalue
    return arr
arr=[9,8,7,6,5,4,3,2,1]
print(insertionSortS(arr.copy()))
