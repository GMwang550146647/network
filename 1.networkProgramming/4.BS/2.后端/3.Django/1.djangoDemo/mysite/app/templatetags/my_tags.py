from django import template
from django.utils.safestring import mark_safe

register = template.Library()  # register的名字是固定的,不可改变
"""
　　1、在settings中的INSTALLED_APPS配置当前app，不然django无法找到自定义的simple_tag.

　　2、在app中创建templatetags模块(模块名只能是templatetags)

　　3、创建任意 .py 文件，如：my_tags.py

"""


@register.filter
def filter_multi(v1, v2):
    print(v1)
    print(v2)
    return v1 + v2


@register.simple_tag  # 和自定义filter类似，只不过接收更灵活的参数，没有个数限制。
def simple_tag_multi(v1, v2, v3, v4):
    return v1 + v2 + v3 + v4


@register.simple_tag
def my_input(id, arg):
    result = "<input type='text' id='%s' class='%s' />" % (id, arg,)
    return mark_safe(result)


# template_include..html里面的内容用下面函数的返回值渲染，然后作为一个组件一样，加载到使用这个函数的html文件里面
@register.inclusion_tag('template_include.html')
def show_include(n):  # 参数可以传多个进来
    n = 1 if n < 1 else int(n)
    data = ["第{}项".format(i) for i in range(1, n + 1)]
    # 这里可以穿多个值，和render的感觉是一样的{'data1':data1,'data2':data2....}
    return {"data": data}
