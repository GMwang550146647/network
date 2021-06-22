'''
拆包符号：*
例如：*[1,2,3,4]=1,2,3,4
'''


'''1.接收过多数据'''
def func(a,*l,**d):
    print(a)
    print(l)
    print(d)
    return a,l,d,d


a,*b=func(99,22,55,66,77,ak='gmwang',b='kk')
print(a)
print(b)  #[(22, 55, 66, 77), {'ak': 'gmwang', 'b': 'kk'}],由于*b是列表，所以后面的都当列表元素了

a,*b,c=func(99,22,55,66,77,ak='gmwang',b='kk')   #*只能出现一次，在前中后都ok，a和c各匹配一个，中间的用b接收
print(a)
print(b)
print(c)


'''2.解除列表和字典'''
dict1={'a':'gmwang','b':"gmking"}
print(*dict1)
list1=[1,2,3,4]
print(*list1)