def quickSort(arr,left,right):
    if left<right:
        low=left
        high=right
        pVal=arr[low]
        while low<high:
            while low<high and arr[high]>=pVal:
                high-=1
            arr[low]=arr[high]
            while low<high and arr[low]<=pVal:
                low+=1
            arr[high]=arr[low]
        arr[low]=pVal
        quickSort(arr,left,low-1)
        quickSort(arr,high+1,right)
    return arr




arr=[9,8,7,6,5,4,3,2,1]
result=quickSort(arr,0,len(arr)-1)
print(result)
























def quickSort(arr,left,right):
    if left<right:
        low=left
        high=right
        pVal=arr[low]
        while low<=high:
            while low<=high and arr[high]>=pVal:
                high-=1
            arr[low]=arr[high]
            while low<=high and arr[low]<=pVal:
                low+=1
            arr[high]=arr[low]
        arr[low]=pVal
        quickSort(arr,left,low-1)
        quickSort(arr,high+1,right)
    return arr