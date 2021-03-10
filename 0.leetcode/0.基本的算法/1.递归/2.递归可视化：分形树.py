import turtle
t=turtle.Turtle()
'''
turtle是一个划线的包
爬行： forward(n);backward(n)
转向： left(a)   ;right(a)
抬笔放笔：penup(); pendown()
笔属性： pensize(s);pencolor(c)
'''
'''1.螺旋线'''
def drawSpiral(t,lineLen):
    if lineLen>0:
        t.forward(lineLen)
        t.right(90)
        drawSpiral(t,lineLen-5)
# drawSpiral(t,200)
# turtle.done()

'''2.分形树(雪花）'''
def tree(t,branch_len,angle=60,ndiv=6):
    if branch_len>5:
        for i in range(ndiv):
            t.forward(branch_len)
            tree(t,branch_len/3,angle,ndiv)
            t.backward(branch_len)
            t.right(angle)



t=turtle.Turtle()
tree(t,120)
turtle.done()