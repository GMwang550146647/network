from django.shortcuts import render,HttpResponse
import datetime
# Create your views here.

def login(request):
    USER_NAME='gmwang'
    PASS_WORD='gmwang'
    login_success=False
    '''1.GET  获取数据'''
    '''2.POST 获取数据'''
    if request.GET:
        username=request.GET.get('username',"")
        password=request.GET.get('password',"")
        hobby=request.GET.get('hobby',"")
        normal=request.GET.get('normal',"")
        print('username:{}'.format(username))
        print('password:{}'.format(password))
        print('hobby:{}'.format(hobby))
        print('normal:{}'.format(normal))
        if username==USER_NAME and password==PASS_WORD:
            login_success=True
    elif request.POST:
        username=request.POST.get('username',"")
        password=request.POST.get('password',"")
        hobby=request.POST.get('hobby',"")
        normal=request.POST.get('normal',"")
        print('username:{}'.format(username))
        print('password:{}'.format(password))
        print('hobby:{}'.format(hobby))
        print('normal:{}'.format(normal))
        if username==USER_NAME and password==PASS_WORD:
            login_success=True
    else:
        pass
    now = datetime.datetime.now()
    ctime = now.strftime("%Y-%m-%d %X")

    data={
        "ctime": ctime,
        "flag":login_success
    }
    # return HttpResponse('哈哈，好玩吗？')
    return render(request, "login.html", data)  # render，渲染html页面文件并返回给浏览器