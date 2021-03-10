arr=[]
def move(n,x,y,z):
    if n==1:
        str="%s->%s"%(x,z)
        arr.append(str)
    else:
        move(n-1,x,z,y)
        str = "%s->%s" % (x, z)
        move(n-1,y,x,z)
move(22,'1','2','3')
print(len(arr))