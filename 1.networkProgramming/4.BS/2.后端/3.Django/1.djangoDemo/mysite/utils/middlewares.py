from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, reverse

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
        white_list = [reverse('login'), '/admin/', '/admin/login/']
        if request.path in white_list:
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
