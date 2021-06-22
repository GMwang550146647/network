'''
4.子进程subprocess：
    很多时候子进程不是自己（以上的都是fork出来的）
    subprocess启动一个子进程然后控制其输入输出
'''
import subprocess
print('$ nslookup www.python.org')
r=subprocess.call(['nslookup','www.python.org'])
print("Exit code:",r)

'''
4.1.如果子进程还需要输入，利益利用communicate()方法输入
'''
import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
# 上面的代码相当于在命令行执行命令nslookup，然后手动输入：
# set q=mx
# python.org
# exit


''''''