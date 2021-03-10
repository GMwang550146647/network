'''2.0.有序表查找方式'''

arr=list(range(100))
def sequenceBinarySearch(arr,item,begin=0,end=-1):
    if end==-1:
        end=len(arr)-1
    index=False
    while(begin<=end and not index):
        mid = int((begin + end) / 2)
        if arr[mid]==item:
            index=mid
            break
        elif arr[mid]<item:
            begin=mid+1
        else:
            end=mid-1
    return index
for i in range(100):
    print(sequenceBinarySearch(arr,i))