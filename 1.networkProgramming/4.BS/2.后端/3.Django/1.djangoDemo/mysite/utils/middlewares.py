from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, reverse, HttpResponse
from app import models
from app.utility import filter
from django.db.models import CharField

class MyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("MyMiddleware Request")
        # 如果返回 HTTP response就直接返回，其后面的中间件也不走了

    def process_response(self, request, response):
        print("MyMiddleware Response")
        return response


class SessionAuth(MiddlewareMixin):
    def process_request(self, request):
        # 设置全局登录验证设置白名单
        white_list = [reverse('login'), '/admin/', '/admin/login/', '/get_check_code/', '/signup/']
        if filter(request.path, white_list, regex=True):
            return None
        is_login = request.session.get('is_login', False)
        if is_login:
            return None
        else:
            return redirect('/login/')

    def process_response(self, request, response):
        """
        如果不想处理可以完全不写这个函数
        :param request:
        :param response:
        :return:
        """
        return response
from django.db.models import Aggregate

class Concat(Aggregate):
    function = 'GROUP_CONCAT'
    template = '%(function)s(%(distinct)s%(expressions)s)'

    def __init__(self, expression, distinct=False, **extra):
        super(Concat, self).__init__(
            expression,
            distinct='DISTINCT ' if distinct else '',
            output_field=CharField(),
            **extra)

class PermissionAuth(MiddlewareMixin):

    def process_request(self, request):
        if request.session.get('is_login', False):
            auth_urls = [urli['url'] for urli in models.Permission.objects.all().values('url').distinct()]
            if filter(request.path, auth_urls, regex=True):
                username = request.session.get('username', "None")
                users = models.UserInfo.objects.filter(username=username)
                if users:
                    user = users[0]
                    # 需要等级认证的url
                    if filter(request.path, auth_urls, regex=True):
                        #legal urls
                        # 该用户拥有的url权限
                        legal_urls = [urli['permission__url'] for urli in
                                      user.roles.values("permission__url").distinct()]
                        request.session['legal_urls'] = legal_urls

                        #legal menus
                        menu_objs = user.roles.values('permission__menus__title').distinct().annotate(
                            titles=Concat('permission__title'),urls=Concat('permission__url'))
                        menu_list=[]
                        for menu_obj_i in menu_objs:
                            menu_i={
                                'title':menu_obj_i['permission__menus__title'],
                                'options':[{
                                    'title':title_i,
                                    'url':url_i,
                                } for title_i,url_i in zip(menu_obj_i['titles'].split(','),menu_obj_i['urls'].split(','))]
                            }
                            menu_list.append(menu_i)
                        request.session['menu_list']=menu_list
                        print(request.session['menu_list'])
                        if filter(request.path, legal_urls, regex=True):
                            return None
                        else:
                            return HttpResponse("You Are Not Authorized To Browse This Page!")
                else:
                    return HttpResponse("Error! User Doesn't Exist!")
            else:
                return None
        else:
            return None

    def process_response(self, request, response):
        return response
