from django.shortcuts import render, HttpResponse
import datetime
import logging

# Create your views here.
USER_NAME = 'gmwang'
PASS_WORD = 'gmwang'

def login(request):
    login_success = False
    # 1.通过判断 GET 以及 POST 的携带数据来判断用了何种方法
    method='GET' if request.GET else ('POST' if request.POST else "")
    logging.warning('method:{}'.format(method))
    if method:
        method=getattr(request,method)
        username = method.get('username', "")
        password = method.get('password', "")
        hobby = method.getlist('hobby', [])
        normal = method.get('normal', "")
        logging.warning('username:{}'.format(username))
        logging.warning('password:{}'.format(password))
        logging.warning('hobby:{}'.format(hobby))
        logging.warning('normal:{}'.format(normal))
        if username == USER_NAME and password == PASS_WORD:
            login_success = True
    now = datetime.datetime.now()
    ctime = now.strftime("%Y-%m-%d %X")

    data = {
        "ctime": ctime,
        "flag": "Success!" if login_success else "Failure!"
    }
    # return HttpResponse('other message')
    return render(request, "login.html", data)  # render，渲染html页面文件并返回给浏览器

def signup(request):
    login_success = False
    # 1.通过判断 GET 以及 POST 的携带数据来判断用了何种方法
    method = 'GET' if request.GET else ('POST' if request.POST else "")
    logging.warning('method:{}'.format(method))
    if method:
        method = getattr(request, method)
        username = method.get('username', "")
        password = method.get('password', "")
        hobby = method.getlist('hobby', [])
        normal = method.get('normal', "")
        logging.warning('username:{}'.format(username))
        logging.warning('password:{}'.format(password))
        logging.warning('hobby:{}'.format(hobby))
        logging.warning('normal:{}'.format(normal))
        if username == USER_NAME and password == PASS_WORD:
            login_success = True
    now = datetime.datetime.now()
    ctime = now.strftime("%Y-%m-%d %X")

    data = {
        "ctime": ctime,
        "flag": "Success!" if login_success else "Failure!"
    }
    # return HttpResponse('other message')
    return render(request, "login.html", data)  # render，渲染html页面文件并返回给浏览器