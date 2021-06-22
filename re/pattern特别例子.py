import re
'''1.开头结尾^$'''
pattern1=r'^gmwang$' #^开头$结尾

'''2.非^'''
str='http:3804830djfajl.com'
pattern2=r'[^\d_]{4}' #表示非数字和下划线
print(re.findall(pattern2,str))

'''3.匹配特殊字符：例如\n'''
'''3.1.匹配文本的特殊字符'''
str1=r"""
name: gmwang\npassword:123456
"""   #实际上其底层格式是\\n
print(str1)
pattern311=re.compile('g\np')   #找不到
result=re.findall(pattern311,str1)
print(result)

pattern312=re.compile(r'g\np') #也找不到
result=re.findall(pattern312,str1)
print(result)

pattern313=re.compile(r'g\\np') #找得到
result=re.findall(pattern313,str1)
print(result)

pattern314=re.compile('g\\\\np') #找得到
result=re.findall(pattern314,str1)
print(result)

'''3.2.匹配文本的特殊字符'''
str2="""
name: gmwang\npassword:123456
"""
print(str2)
pattern321=re.compile('g\\np')   #找到
result=re.findall(pattern321,str2)
print(result)

pattern322=re.compile(r'g\np') #也找到
result=re.findall(pattern322,str2)
print(result)

pattern323=re.compile(r'g\\np') #找不到
result=re.findall(pattern323,str2)
print(result)

pattern324=re.compile('g\\\np')   #找到
result=re.findall(pattern324,str2)
print(result)

'''3.3.匹配同为文本和正则的特殊字符，例如\d'''
str3='''12\dgmwang'''
print(str3)
pattern331=re.compile('\d')   #找不到
result=re.findall(pattern331,str3)
print(result)

pattern332=re.compile(r'\d') #找不到
result=re.findall(pattern332,str3)
print(result)

pattern333=re.compile(r'\\d') #找到
result=re.findall(pattern333,str3)
print(result)

pattern333=re.compile('\\\d') #找到
result=re.findall(pattern333,str3)
print(result)

'''4.或者匹配（非单字母）'''
emailpattern=re.compile(r'\w{5,20}@(163|126|qq).com')  #这个会和分组有冲突
email='gmwang@qq.com'
result=re.match(emailpattern,email)
print(result.group())
print(result.group(1))   #对于分组和或者匹配的冲突，利用group（i)可以提取或者中的内容

'''5.分组：()'''
'''5.1.分组：match'''
phonenum='010-992033 020-384280 030-938489'
pattern=re.compile(r'(\d{3,4})-(\d{5,8})')
result=re.match(pattern,phonenum)
print(result.group()) #默认是0
print(result.group(1))
print(result.group(2))

'''5.2.分组：findall'''
result=re.findall(pattern,phonenum)
print(result)

'''6.引用:\1的意思是引用第一个，同理\2等'''
str='h1.hello.hello.h1'
result=re.match(r'([0-9a-zA-Z]+)\.(.+)\.\2\.\1',str)
print(result.group())
print(result.group(1))
print(result.group(2))