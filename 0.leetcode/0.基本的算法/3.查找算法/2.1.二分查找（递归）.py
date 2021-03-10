'''2.1有序表查找方式'''

arr=list(range(100))
def sequenceBinarySearch(arr,item,begin,end):
    if begin<=end:
        mid=int((begin+end)/2)
        if arr[mid]==item:
            return mid
        elif arr[mid]>item:
            return sequenceBinarySearch(arr,item,begin,mid-1)
        else:
            return sequenceBinarySearch(arr,item,mid+1,end)
    else:
        return False


for i in range(200):
    print(sequenceBinarySearch(arr,i,0,len(arr)-1))