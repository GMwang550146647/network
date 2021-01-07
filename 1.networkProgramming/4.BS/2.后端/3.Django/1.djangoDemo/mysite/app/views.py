import os
import datetime
import logging
from django.shortcuts import render, HttpResponse, redirect
from .models import sql_api_template, user_add, user_login
from django.views import View
from django.utils.decorators import method_decorator

PATH = 'path'
# Create your views here.
PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))


def my_decorator(func):
    def wrapper(*args, **kwargs):
        logging.warning("请求前....")
        ret = func(*args, **kwargs)
        logging.warning("请求后....")
        return ret

    return wrapper


"""

1.Response Method:
    1.HttpResponse ->回复一个字符串
    2.render       ->回复一个网页
    3.redirect     ->重定向: 
        重定向状态码：
            301：永久性转移->资源永久删除，搜索引擎捉取新内容的时候旧网址交换为新网址
            302：暂时性转移->地址A资源还在，只是临时从旧地址A跳转到地址B

2.FBV 与 CBV模式
    FBV  : 函数模式
    CBV  ：类模式
    
"""


def request(request):
    data = {
        'method': request.method,
        'body': request.body,  # post 的内容
        'path': request.path,
        'path_info': request.path_info,
        'get_full_path()': request.get_full_path(),
        'META': request.META,
        'GET': request.GET,
        'POST': request.POST,
    }
    tempt_str = ''
    for key, val in data.items():
        tempt_str += "{}:{}<br>".format(key, val)
    return HttpResponse(tempt_str)


@my_decorator
def login(request):
    logging.warning("Logining")
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
        login_success = user_login(username, password)

    data = {
        "ctime": ctime,
        "flag": "Success!" if login_success else "Failure!"
    }
    # return HttpResponse('other message')
    return render(request, "login.html", data)  # render，渲染html页面文件并返回给浏览器


class Login(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        login_success = False
        now = datetime.datetime.now()
        ctime = now.strftime("%Y-%m-%d %X")
        self.data = {
            "ctime": ctime,
            "flag": "Success!" if login_success else "Failure!"
        }

    @method_decorator(my_decorator)  # 如果是类方法要加这个装饰器
    def dispatch(self, request, *args, **kwargs):
        ret = super().dispatch(request, *args, **kwargs)
        return ret

    def get(self, request):
        logging.warning("GET  方法执行了")
        return render(request, "login.html", self.data)  # render，渲染html页面文件并返回给浏览器

    def post(self, request):
        logging.warning("POST  方法执行了")
        username = request.POST.get('username', "")
        password = request.POST.get('password', "")
        hobby = request.POST.getlist('hobby', [])
        normal = request.POST.get('normal', "")
        upload(request)
        logging.warning('username:{}'.format(username))
        logging.warning('password:{}'.format(password))
        logging.warning('hobby:{}'.format(hobby))
        logging.warning('normal:{}'.format(normal))
        user_add(username, password)
        self.data['flag'] = "Failure!"
        return render(request, "login.html", self.data)  # render，渲染html页面文件并返回给浏览器


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
        user_add(username, password)
        data['flag'] = "Failure!"
        # 1.这个不能重定向（也就是网页url还是signup)
        return render(request, "login.html", data)
        # 2.这个可以重定向
        # return redirect('/login/')
    else:
        # return HttpResponse('other message')
        return render(request, "signup.html", data)  # render，渲染html页面文件并返回给浏览器


def upload(request):
    dest_dir = os.path.join(PROJECT_PATH, 'tempt')
    for filei in request.FILES:
        file_pathi = os.path.join(dest_dir, filei)
        content = request.FILES.get(filei, None)
        with open(file_pathi, 'wb') as f:
            for chunk in content.chunks():
                f.write(chunk)
        logging.warning('{}: Saved to {}'.format(filei, file_pathi))


def database(request):
    sql_api_template()
    return HttpResponse('Database Management')


class IndexView(View):
    def index1(self, request, m, n):
        return HttpResponse("{},{},Index Html!".format(m, n))

    def index2(self, request, year, month):
        return HttpResponse("{}_{}_Index Html!".format(year, month))


def template_system(request):
    import datetime
    num = 99
    string = 'This is a String variable'
    lt = [1, 2, 3, 4, 5]
    dt = {'a': 1, 'b': 2, 'c': 3}
    date = datetime.date(2021, 6, 7)
    time = datetime.datetime.now()
    a_tag = '<a href="https://www.baidu.com">baidu</a>'

    class Person():
        def __init__(self, name='gmwang'):
            self.name = name

        # 如果是函数，只能传入无参函数
        def dream(self):
            return '{} want feifei'.format(self.name)

    person_list = [Person('gmwang'), Person('feifei')]
    # 1.这里返回当前位置的全部局部变量,名字和变量名称一一对应
    # return render(request,'template_system.html',locals())
    # 2.自己制作字典返回
    return render(request, 'template_system.html', {
        'num': num, 'string': string, 'lt': lt, 'dt': dt, 'date': date, 'person_list': person_list, 'time': time,
        'a_tag': a_tag
    })


def template_inherit(request):
    return render(request, 'template_inherit.html')
