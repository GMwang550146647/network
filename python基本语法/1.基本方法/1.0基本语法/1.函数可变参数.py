#1.传入多个参数，按顺序读取
def calc(*numbers): #读进来的numbers是一个list
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
result1=calc(1,2,3,4,5,4,3,2,1)
result2=calc(*[1,2,3,4,5,4,3,2,1])  #*的意思是把list拍平成为一个一个参数传入
#2.传入字典参数
# *args用来接收多余的无名称参数，**用来接收有名称的参数，并转化为字典
def func(a, b, c=0, *args, **kw):
    #结果：a = 1 b = 2 c = 3 args = (4, 5, 5, 4, 3) kw = {'me': 'gmwang', 'others': "i dot'n know"}
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

func(1,2,3,4,5,5,4,3,me="gmwang",others="i dot'n know")
dict={'me':"gmwang",'others':"i dot'n know"}
func(1,2,3,4,5,5,4,3,**dict)  #**dict的意思是相当于传入  me="gmwang",others="i dot'n know"