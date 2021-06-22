'''time模块'''
import time
'''1.时间戳:单位是秒(从某年某日开始计起）'''
t1=time.time()
time.sleep(0.1)
t2=time.time()
print(t1)
print(t2)
print(t2-t1)

'''2.时间戳转换（人能看懂的）'''
#2.1.转换字符串模式
s=time.ctime(t1)
print(s)

#2.2.转换元组的方式
#time.struct_time(tm_year=2020, tm_mon=3, tm_mday=3, tm_hour=16, tm_min=56, tm_sec=9, tm_wday=1, tm_yday=63, tm_isdst=0)
t=time.localtime(t1)  #转换成元组
t1=time.mktime(t)       #元组转换成时间戳
print(t)
print(t1)
print(t.tm_hour)   #输出元组中的元素


#2.3.转换自定义字符串模式
strTime=time.strftime('%Y-%m-%d %H:%M:%S')  #更多格式自己看源代码
print(strTime)

#2.4.其他模式的字符串转换成元组方式：
tupleTime=time.strptime("2019/06/20","%Y/%m/%d")
print(tupleTime)