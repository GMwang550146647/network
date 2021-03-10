def mergeAssis(arr1,arr2):
    i=0
    j=0
    arr=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<= arr2[j]:
            arr.append(arr1[i])
            i+=1
        else:
            arr.append(arr2[j])
            j+=1
    if j==len(arr2):
        arr.extend(arr1[i:])
    else:
        arr.extend(arr2[j:])
    return arr
def mergeSort(arr):
    if len(arr)==1:
        return arr
    else:
        middle=len(arr)//2
        left=mergeSort(arr[:middle])
        right=mergeSort(arr[middle:])
        arr=mergeAssis(left,right)
        return arr


arr=[9,8,7,6,5,4,3,2,1]
result=mergeSort(arr)
print(result)