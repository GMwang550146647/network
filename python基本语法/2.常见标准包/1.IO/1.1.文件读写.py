'''
文本基本操作：
打开，关闭，读写
权限位：
r:  默认只读
w：  覆盖写
a:  追加
x:   新建文件，不存在则创建，存在则报错
r+：可读可写，但是文件不存在会报错
+: 添加读写功能

os模块
'''

'''
1.打开
注意：打开的相对路径或者是绝对路径
'''
file=open('data.html')

'''
2.关闭文件
'''
file.close()



'''
3.读取文件
'''
'''3.1.一次性读取文件：文件可能比较大'''
with open("data.html") as file:
    data=file.read()
'''3.2.分次读取文件：不会那么占内存
        注意：1.可以指定读取的数量(中英文符号都当一个，例如"我"，"j","！"都是)
             2.如果读到行末会返回\n（都当一个）
             3.如果读到文件末尾，会返回NULL并返回
'''
with open("data.html") as file:
    li=[]
    while True:
        data1=file.read(30)
        if data1:
            li.append(data1)
        else:
            break
'''3.3.按行读取文件'''

with open("data.html") as file:
    li=[]
    while True:
        data1=file.readline()
        if data1:
            li.append(data1)
        else:
            break
#或者
with open("data.html") as file:
    for linei in file.readlines():
        # print(linei)
        pass


'''
4.文件写操作
'''
'''
4.1.文件覆盖写：文件不存在会创建文件，如果存在则会覆盖文件（所有内容删除）
返回值：成功写入的个数
注意：不会自动换行
'''
with open('data.html','w') as f:
    for i in range(100):
        f.write("这个是加入的内容\n")
        pass


'''4.2.文件追加写'''
with open('data.html','a') as f:
    for i in range(100):
        f.write("这个是加入的内容\n")
        pass

''''''
##################################以上为文本文件，以下为二进制文件#####################

'''
5.二进制文件操作
'''
'''
读取模式：rb
写模式：wb
读取大小单位：字节
注意：中文对应三个字节，所以中文的个数要除以3
'''
with open('music.mp3','rb') as f:
    trunk=f.read(10000)
    with open("copy.mp3",'wb') as fnew:
        fnew.write(trunk)


'''
6.查找和修改读写位置
tell()：当前位置
seek(index): 跳到这个位置

这个是字节位置：所以中文的会报错
'''
with open('music.mp3','rb') as f:
    for i in range(100):
        content=f.read(9)
        seat=f.tell()
        f.seek(seat-6)
        print(content)
        print("~~~~~~~~~~")
