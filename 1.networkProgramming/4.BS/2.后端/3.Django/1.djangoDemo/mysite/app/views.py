import os
import datetime
import logging
from django.shortcuts import render, HttpResponse
from .models import sql_api_template,user_add,user_login

# Create your views here.
USER_NAME = 'gmwang'
PASS_WORD = 'gmwang'
PROJECT_PATH= os.path.dirname(os.path.dirname(__file__))

def login(request):
    login_success = False
    now = datetime.datetime.now()
    ctime = now.strftime("%Y-%m-%d %X")

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
        login_success=user_login(username,password)

    data = {
        "ctime": ctime,
        "flag": "Success!" if login_success else "Failure!"
    }
    # return HttpResponse('other message')
    return render(request, "login.html", data)  # render，渲染html页面文件并返回给浏览器


def signup(request):
    now = datetime.datetime.now()
    ctime = now.strftime("%Y-%m-%d %X")
    data = {
        "ctime": ctime,
    }
    # 1.通过判断 GET 以及 POST 的携带数据来判断用了何种方法
    method = 'GET' if request.GET else ('POST' if request.POST else "")
    logging.warning('method:{}'.format(method))

    if method:
        method = getattr(request, method)
        username = method.get('username', "")
        password = method.get('password', "")
        hobby = method.getlist('hobby', [])
        normal = method.get('normal', "")
        upload(request)
        logging.warning('username:{}'.format(username))
        logging.warning('password:{}'.format(password))
        logging.warning('hobby:{}'.format(hobby))
        logging.warning('normal:{}'.format(normal))
        user_add(username,password)
        data['flag'] = "Failure!"
        return render(request, "login.html", data)
    else:
        # return HttpResponse('other message')
        return render(request, "signup.html", data)  # render，渲染html页面文件并返回给浏览器

def upload(request):
    dest_dir=os.path.join(PROJECT_PATH,'tempt')
    for filei in request.FILES:
        file_pathi=os.path.join(dest_dir,filei)
        content=request.FILES.get(filei,None)
        with open(file_pathi,'wb') as f:
            for chunk in content.chunks():
                f.write(chunk)
        logging.warning('{}: Saved to {}'.format(filei,file_pathi))

def database(request):
    sql_api_template()
    return HttpResponse('Database Management')