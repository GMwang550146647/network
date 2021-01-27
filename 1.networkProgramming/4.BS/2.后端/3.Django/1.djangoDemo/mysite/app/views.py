import os
import datetime
import logging
import json
from django.shortcuts import render, HttpResponse, redirect, reverse
from django.http import JsonResponse
from .models import SingleTableManagement, user_add, user_login, get, delete, edit
from django.views import View
from django.utils.decorators import method_decorator
from django import forms
from django.forms import widgets
from app import models
from django.core.validators import RegexValidator

PATH = 'path'
# Create your views here.
PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))



class SignupForm(forms.Form):
    username=forms.CharField(
        min_length=4,
        max_length=20,
        label="username",
        error_messages = {
            "required": "不能为空",
            "invalid": "格式错误",
            "min_length": "用户名最短4位最多20位"
        },
        validators=[RegexValidator("^[a-zA-Z]")],
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'})
    )
    password=forms.CharField(
        min_length=4,
        max_length=20,
        label="password",
        widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}, render_value=True),
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
            "min_length": "密码最短4位最多20位"
        },
    )
    normal = forms.fields.ChoiceField(  #注意，单选框用的是ChoiceField，并且里面的插件是Select，不然验证的时候会报错， Select a valid choice的错误。
        choices=((1, "Yes"), (2, "No") ),
        label="normal",
        initial=1,
        widget=forms.widgets.Select()
    )
    hobby = forms.fields.MultipleChoiceField( #多选框的时候用MultipleChoiceField，并且里面的插件用的是SelectMultiple，不然验证的时候会报错。
        choices=((1, "Python"), (2, "C++"), (3, "Java"), ),
        label="hobby",
        initial=[1],
        widget=forms.widgets.SelectMultiple()
    )
    date = forms.DateField(widget=widgets.TextInput(attrs={'type': 'date'}))

def signup_form(request):
    form_obj = SignupForm()
    if request.method == "POST":
        # 实例化form对象的时候，把post提交过来的数据直接传进去
        form_obj = SignupForm(data=request.POST)  #既然传过来的input标签的name属性值和form类对应的字段名是一样的，所以接过来后，form就取出对应的form字段名相同的数据进行form校验
        # 调用form_obj校验数据的方法
        if form_obj.is_valid():
            return HttpResponse("注册成功")
    return render(request, "signup_form.html", {"form_obj": form_obj})

def cookie_decorator(f):
    def cookie_wrapper(request, *args, **kwargs):
        # if request.COOKIES.get('is_login', False):
        """
        1.从cookie中拿出session_id字符串
        2.去django-session表格查询对应数据
        3.反解加密的数据
        """
        if request.session.get('is_login', False):
            print("Login User:{}".format(request.session.get('username',"Nobody")))
            return f(request, *args, **kwargs)
        else:
            return redirect('/login/')

    return cookie_wrapper


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
        logging.warning('username:{}'.format(username))
        logging.warning('password:{}'.format(password))
        login_success = user_login(username, password)
        if login_success:
            ret = redirect('/user_management/')
            #cookie
            ret.set_cookie('is_login', True)
            #session
            request.session['is_login']=True
            request.session['username']=username
            request.session['last_time']=ctime
            return ret
    data = {
        "ctime": ctime,
        "flag": "Success!" if login_success else "Failure!"
    }
    # return HttpResponse('other message')
    return render(request, "login.html", data)  # render，渲染html页面文件并返回给浏览器


def login_ajax(request):
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
        logging.warning('username:{}'.format(username))
        logging.warning('password:{}'.format(password))
        login_success = user_login(username, password)
        data = {
            "ctime": ctime,
            "flag": "Success!" if login_success else "Failure!"
        }
        # 1.直接使用JsonResponse（远端收到的是json对象）
        # return JsonResponse(data, safe=False)
        # 2.转化为字符串再发送（但是远端收到的是字符串）
        data_json = json.dumps(data)
        # return HttpResponse(data_json)
        # 3.直接传送json，远端收到json（同JsonResponse)
        return HttpResponse(data_json, content_type='application/json')
    else:
        data = {
            'ctime': ctime,
            'flag': 'Failure!'
        }
        return render(request, "login_ajax.html", data)


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
        logging.warning('username:{}'.format(username))
        logging.warning('password:{}'.format(password))
        login_success = user_login(username, password)
        if login_success:
            ret = redirect('/user_management/')
            #cookie
            ret.set_cookie('is_login', True,max_age=1000)
            #session
            """
            1.生成了session_id： 随机字符串1
            2.在cookie里面加上了一个键值对 session_id:随机字符串1
            3.将用户数据加密并保存到django-session表里面（session_key,session_data,expire_date）
            """
            request.session['is_login']=True
            request.session['username']=username
            request.session['last_time']=self.data['ctime']
            request.session.set_expiry(1000)
            # request.session.setdefault('k1', 123)  # 存在则不设置
            return ret
        else:
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
        user_add(username, password, hobby, normal)
        data['flag'] = "Failure!"
        # 1.这个不能重定向（也就是网页url还是signup)
        # return render(request, "login.html", data)
        # 2.这个可以重定向
        # return redirect('/login/')
        # 也可以使用反向解释技术，前提是 view中使用了 name字段
        print("reverse('lg')={}".format(reverse('lg')))
        return redirect(reverse('lg'))
    else:
        # return HttpResponse('other message')
        return render(request, "signup.html", data)  # render，渲染html页面文件并返回给浏览器


@cookie_decorator
def user_management(request):
    users = get()
    return render(request, 'user_management.html', {'users': users})


def delete_user(request, id):
    delete(id=id)
    return redirect('/user_management/')


def edit_user(request):
    method = 'GET' if request.GET else ('POST' if request.POST else "")
    if method:
        method = getattr(request, method)
        user_info = {
            'id': method.get('id', -1),
            'username': method.get('username', ""),
            'password': method.get('password', ""),
            'hobby': method.getlist('hobby', []),
            'normal': method.get('normal', "")
        }
        edit(**user_info)
        return redirect('/user_management/')
    else:
        return HttpResponse('Error Occurs When Editing Userinfo !')


def upload(request):
    """
    上传文件数据的时候必须要加这个enctype属性，不然只会在post出现 文件名字，不会在FILE中出现文件信息！
    <form action="" method="post" enctype="multipart/form-data">
    """
    dest_dir = os.path.join(PROJECT_PATH, 'tempt')
    for filei in request.FILES:
        file_obj = request.FILES.get(filei, None)
        file_pathi = os.path.join(dest_dir, file_obj.name)
        logging.warning("Receive Name: {} -> File : {}".format(filei, file_obj.name))
        if file_obj:
            with open(file_pathi, 'wb') as f:
                for chunk in file_obj.chunks():
                    f.write(chunk)
            logging.warning('{}: Saved to {}'.format(filei, file_pathi))
        else:
            logging.error("No File To Save!")


def database(request):
    SingleTableManagement().run()
    return HttpResponse('Database Management: Single Table Management')


class IndexView(View):
    def get(self, request, m, n):
        return HttpResponse("{},{},Index Html!".format(m, n))


def index2(request, year, month):
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


def template_inherit1(request):
    return render(request, 'template_inherit1.html')


def template_inherit2(request):
    return render(request, 'template_inherit2.html')


class UploadFile(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request):
        return render(request, 'upload_file_ajax.html')

    def post(self, request):
        try:
            logging.warning("Received POST DATA: {}".format(request.POST))
            logging.warning("Received FILES DATA: {}".format(request.FILES))
            upload(request)
            return HttpResponse("Upload Success!")
        except Exception as err:
            logging.error(err)
            return HttpResponse("Upload Failure!")
