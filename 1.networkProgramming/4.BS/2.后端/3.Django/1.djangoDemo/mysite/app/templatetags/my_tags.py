from django import template
from django.utils.safestring import mark_safe

register = template.Library()  # register的名字是固定的,不可改变
"""
　　1、在settings中的INSTALLED_APPS配置当前app，不然django无法找到自定义的simple_tag.

　　2、在app中创建templatetags模块(模块名只能是templatetags)

　　3、创建任意 .py 文件，如：my_tags.py

   4.在settings 的'libraries'加入此文件的路径
"""


@register.filter
def filter_multi(v1, v2):
    return v1 * v2


@register.simple_tag  # 和自定义filter类似，只不过接收更灵活的参数，没有个数限制。
def simple_tag_multi(v1, v2):
    return v1 * v2


@register.simple_tag
def my_input(id, arg):
    result = "<input type='text' id='%s' class='%s' />" % (id, arg,)
    return mark_safe(result)
