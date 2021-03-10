'''

4.希尔排序：
是插入排序的延伸，将间隔为k的子列表分别进行插入排序，k从n/2,n/4。。。直至1进行排序
'''

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentVal=alist[i]
        position=i
        while position>=gap and alist[position-gap]>=currentVal:
            alist[position]=alist[position-gap]
            position-=gap
        alist[position]=currentVal
def shellSort(alist):
    sublistcout=len(alist)//2
    while sublistcout>0:
        for startposition in range(sublistcout):
            gapInsertionSort(alist,startposition,sublistcout)
        print("After increments of size:",sublistcout,",The list is:",alist)
        sublistcout//=2
    return alist
arr=[9,8,7,6,5,4,3,2,1]
result=shellSort(arr)
print(result)