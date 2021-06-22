#1.读取文本文件
with open('/path/to/file', 'r') as f:
    print(f.read())
#2.读取二进制文件
with open('/path/to/file', 'rb') as f:
    print(f.read().decode('gbk'))  #要解码
#3.写文件
with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')