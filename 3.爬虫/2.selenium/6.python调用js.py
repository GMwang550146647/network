"""
1.安装 pyexecjs : pip install PyExecJS
2.安装 nodejs   : brew install nodejs
"""

import execjs
node = execjs.get()
file = '6.script.js'
#编译一个文件中的js
ctx = node.compile(open(file,encoding='utf-8').read())
#调用该文件中的js
js='myFunction(1,2)'
result=ctx.eval(js)
print(result)