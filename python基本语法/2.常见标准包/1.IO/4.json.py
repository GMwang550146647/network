import json
# 有一点需要注意，就是反序列化得到的所有字符串对象默认都是unicode而不是str。
# 由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str或unicode与JSON的字符串之间转换。
d = dict(name='Bob', age=20, score=88)
js_str=json.dumps(d)
print(js_str)
di=json.loads(js_str)
print(di)
