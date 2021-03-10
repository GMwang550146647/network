
def gnomesort(seq):
    i=0
    while i < len(seq):
        if i==0 or seq[i-1]<seq[i]:
            i+=1
        else:
            seq[i],seq[i-1]=seq[i-1],seq[i]
            i-=1
    return seq

arr=[5,4,3,2,1]
print(gnomesort(arr))