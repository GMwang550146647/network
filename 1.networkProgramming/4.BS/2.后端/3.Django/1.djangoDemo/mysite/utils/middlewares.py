from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, reverse, HttpResponse
from app import models
import numpy as np
import re
import json
import logging

def filter(value, target_value, keep_if_match=True, match_type='any', regex=False):
    """
    To tell 'value' match target_value or not !
    :param value:           The value to be tested,it can be list, tuple or string
    :param target_value:    target value, list of items or regex(if regex=True)
    :param keep_if_match:   keep if 'value' match the conditions in 'target_value'
    :param match_type:      all-> all of the patterns in target_value should be match; any-> at least one match
    :param regex:           if the items in target_value should be regarded as regex expression
    :return:
    """
    if type(value) == str and value.strip()[0] in ['(', '[']:
        try:
            value = json.loads(value)
        except Exception as err:
            logging.error(f"Filter Error ->  Value: {value}  Details : {err}")
    if type(value) in [list, tuple]:
        if regex:
            keep_flags = [[len(re.findall(tar_i, val_i)) >= 0 for val_i in value] for tar_i in target_value]
            keep_flag = np.array(keep_flags).all() if match_type == 'all' else np.array(keep_flags).any()
        else:
            if match_type == 'all':
                keep_flag = (len(set(value) & set(target_value)) == len(set(target_value)))
            else:
                keep_flag = len(set(value) & set(target_value)) > 0
    else:
        if regex:
            keep_flags = [len(re.findall(target_value_i, value)) > 0 for target_value_i in target_value]
            keep_flag = np.array(keep_flags).all() if match_type == 'all' else np.array(keep_flags).any()
        else:
            keep_flag = value in target_value
    # if keep_if_match==True : rowi is kept when "condition" in "condition ^ keep_if_match" is False
    return (not keep_flag) ^ keep_if_match


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
        if filter(request.path, white_list):
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


class PermissionAuth(MiddlewareMixin):

    def process_request(self, request):
        if request.session.get('is_login', False):
            auth_urls = [urli['url'] for urli in models.Permission.objects.all().values('url').distinct()]
            if filter([request.path], auth_urls):
                username = request.session.get('username', "None")
                users = models.UserInfo.objects.filter(username=username)
                if users:
                    user = users[0]
                    # 需要等级认证的url
                    if np.array([re.search(pattern_i, request.path) for pattern_i in auth_urls]).any():
                        # 该用户拥有的url权限
                        legal_urls = [urli['permission__url'] for urli in
                                      user.roles.values("permission__url").distinct()]
                        if filter([request.path], legal_urls):
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
