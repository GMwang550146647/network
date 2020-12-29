"""
wsgiref模块
    将整个请求信息给封装了起来
WSGI（Web Server Gateway Interface）
    它定义了使用Python编写的web应用程序与web服务器程序之间的接口格式，实现web应用程序与web服务器程序间的解耦
    常用的WSGI服务器有uwsgi、Gunicorn。而Python标准库提供的独立WSGI服务器叫wsgiref，Django开发环境用的就是这个模块来做服务器。
"""
from wsgiref.simple_server import make_server


# wsgiref本身就是个web框架，提供了一些固定的功能（请求和响应信息的封装，不需要我们自己写原生的socket了也不需要咱们自己来完成请求信息的提取了）
def application(environ, start_response):
    """
    :param environ: 是全部加工好的请求信息，加工成了一个字典，通过字典取值的方式就能拿到很多你想要拿到的信息
    :param start_response: 帮你封装响应信息的（响应行和响应头），注意下面的参数
    :return:
    """
    start_response('200 OK', [('k1', 'v1'), ])
    print(environ)
    print(environ['PATH_INFO'])  # 输入地址127.0.0.1:8000，这个打印的是'/',输入的是127.0.0.1:8000/index，打印结果是'/index'
    return [b'<h1>Hello, web!</h1>']


# 与socket server 模块相似
httpd = make_server('127.0.0.1', 8080, application)

print('Serving HTTP on port 8080...')
# 开始监听HTTP请求:
httpd.serve_forever()
