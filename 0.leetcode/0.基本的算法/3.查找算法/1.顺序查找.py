'''

1.无序表搜索方式
'''
def sequentialSearch(arr,item):
    for i in range(len(arr)):
        if arr[i]==item:
            return True
    return False
arr=[1,3,4,5,6,7,8,9]

print(sequentialSearch(arr,2))
print(sequentialSearch(arr,9))