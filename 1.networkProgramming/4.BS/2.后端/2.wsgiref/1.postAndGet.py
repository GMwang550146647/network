import os
from urllib.parse import parse_qs
from wsgiref.simple_server import make_server
from jinja2 import Template

"""
environ={
    'PATH': '/Users/gmwang/opt/anaconda3/bin: /Users/gmwang/opt/anaconda3/condabin: /usr/local/bin: /usr/bin: /bin: /usr/sbin: /sbin',
    'LC_MONETARY': 'en_US.UTF-8',
    'LC_TIME': 'en_US.UTF-8',
    'CONDA_DEFAULT_ENV': 'base',
    'CONDA_EXE': '/Users/gmwang/opt/anaconda3/bin/conda',
    'LC_MESSAGES': 'en_US.UTF-8',
    'CONDA_PYTHON_EXE': '/Users/gmwang/opt/anaconda3/bin/python',
    'LANG': 'en_US.UTF-8',
    'CONDA_PREFIX': '/Users/gmwang/opt/anaconda3',
    '_CE_M': '',
    'LC_COLLATE': 'en_US.UTF-8',
    'LOGNAME': 'gmwang',
    'XPC_SERVICE_NAME': 'com.jetbrains.pycharm.96692',
    'PWD': '/Users/gmwang/Desktop/network/1.networkProgramming/4.BS/2.后端/2.wsgiref',
    'PYCHARM_HOSTED': '1',
    'CONDA_SHLVL': '1',
    'PYCHARM_DISPLAY_PORT': '63342',
    'PYTHONPATH': '/Users/gmwang/Desktop/network: /Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_matplotlib_backend: /Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_display',
    'SHELL': '/bin/bash',
    'PYTHONIOENCODING': 'UTF-8',
    'USER': 'gmwang',
    'TMPDIR': '/var/folders/4_/3xtwy0rj2k30spny5gxtpwz00000gn/T/',
    'LC_NUMERIC': 'en_US.UTF-8',
    'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.RWMZpxSB1j/Listeners',
    '_CE_CONDA': '',
    'XPC_FLAGS': '0x0',
    'PYTHONUNBUFFERED': '1',
    'LC_ALL': 'en_US.UTF-8',
    '__CF_USER_TEXT_ENCODING': '0x1F5: 0x0: 0x0',
    'CONDA_PROMPT_MODIFIER': '(base)',
    'LC_CTYPE': 'en_US.UTF-8',
    'HOME': '/Users/gmwang',
    'SERVER_NAME': '1.0.0.127.in-addr.arpa',
    'GATEWAY_INTERFACE': 'CGI/1.1',
    'SERVER_PORT': '8080',
    'REMOTE_HOST': '',
    'CONTENT_LENGTH': '',
    'SCRIPT_NAME': '',
    'SERVER_PROTOCOL': 'HTTP/1.1',
    'SERVER_SOFTWARE': 'WSGIServer/0.2',
    'REQUEST_METHOD': 'GET',
    'PATH_INFO': '/',
    'QUERY_STRING': '',
    'REMOTE_ADDR': '127.0.0.1',
    'CONTENT_TYPE': 'text/plain',
    'HTTP_HOST': '127.0.0.1: 8080',
    'HTTP_UPGRADE_INSECURE_REQUESTS': '1',
    'HTTP_ACCEPT': 'text/html,
    application/xhtml+xml,
    application/xml;q=0.9,
    */*;q=0.8',
    'HTTP_USER_AGENT': 'Mozilla/5.0(Macintosh;IntelMacOSX10_15_7)AppleWebKit/605.1.15(KHTML,
    likeGecko)Version/14.0Safari/605.1.15',
    'HTTP_ACCEPT_LANGUAGE': 'en-us',
    'HTTP_ACCEPT_ENCODING': 'gzip,
    deflate',
    'HTTP_CONNECTION': 'keep-alive',
    'wsgi.input': <_io.BufferedReadername=5>,
    'wsgi.errors': <_io.TextIOWrappername='<stderr>'mode='w'encoding='UTF-8'>,
    'wsgi.version': (1,
    0),
    'wsgi.run_once': False,
    'wsgi.url_scheme': 'http',
    'wsgi.multithread': True,
    'wsgi.multiprocess': False,
    'wsgi.file_wrapper': <class'wsgiref.util.FileWrapper'>
}
"""
CURRENT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
USER_NAME = 'gmwang'
PASSWORD = 'gmwang'


def auth(username, password):
    if username == USER_NAME and password == PASSWORD:
        return True
    else:
        return False


def application(environ, start_response):
    '''1.接收请求并发送成功回应，并提取出请求的页面'''
    # start_response('200 OK', [('Content-Type', 'text/html'),('k1','v1')])
    # start_response('200 OK', [('Content-Type', 'text/html'),('charset','utf-8')])
    start_response('200 OK', [('Content-Type', 'text/html')])
    path = environ['PATH_INFO']

    '''2.根据不同的请求提供不同服务'''
    if path in ['/login', '/']:
        file_path = os.path.join(CURRENT_PATH, '0.data', 'html/wsgiref_login.html')
        with open(file_path, 'rb') as f:
            data = f.read()
    # 针对form表单提交的auth路径，进行对应的逻辑处理
    elif path == '/auth/':
        # 登陆认证
        # 1.获取用户输入的用户名和密码

        # 2.去数据库做数据的校验，查看用户提交的是否合法
        re_data = None
        if environ.get("REQUEST_METHOD") == "POST":
            # 获取请求体数据的长度,因为提交过来的数据需要用它来提取,注意POST请求和GET请求的获取数据的方式不同
            try:
                request_body_size = int(environ.get('CONTENT_LENGTH', 0))
            except (ValueError):
                request_body_size = 0
            # POST请求获取数据的方式
            print(environ['wsgi.input'])
            request_data = environ['wsgi.input'].read(request_body_size)
            print('>>>>>', request_data)  # >>>>> b'username=chao&password=123'，是个bytes类型数据
            print('?????', environ['QUERY_STRING'])  # ????? 空的，因为post请求只能按照上面这种方式取数据
            # parse_qs可以帮我们解析数据
            re_data = parse_qs(request_data)
            print('拆解后的数据', re_data)  # 拆解后的数据 {b'password': [b'123'], b'username': [b'chao']}
        if environ.get("REQUEST_METHOD") == "GET":
            # GET请求获取数据的方式，只能按照这种方式取
            print('?????', environ['QUERY_STRING'])  # ????? username=chao&password=123,是个字符串类型数据
            request_data = environ['QUERY_STRING']

            # parse_qs可以帮我们解析数据
            re_data = parse_qs(request_data)
            print('拆解后的数据', re_data)  # 拆解后的数据 {'password': ['123'], 'username': ['chao']}
        username = re_data['username'][0]
        password = re_data['password'][0]
        print(username, password)

        # 但是不管是post还是get请求都不能直接拿到数据，拿到的数据还需要我们来进行分解提取，所以我们引入urllib模块来帮我们分解
        # 注意昂，我们如果直接返回中文，没有给浏览器指定编码格式，默认是gbk，所以我们需要gbk来编码一下，浏览器才能识别
        # data='登陆成功！'.encode('gbk')
        flag = True if username == USER_NAME and password == PASSWORD else False
        file_path = os.path.join(CURRENT_PATH, '0.data', 'html','wsgiref_home.html')
        '''3.jinja2 Template'''
        with open(file_path, 'r',encoding='utf-8') as f:
            content = f.read()
        tem=Template(content)
        data=tem.render({'username':username,'password':password,'success':'成功' if flag else '失败'})
        data=bytes(data,encoding='utf-8')
    else:
        file_path = os.path.join(CURRENT_PATH, '0.data', path[1:])
        with open(file_path, 'rb') as f:
            data = f.read()
    return [data]


# 和咱们学的socketserver那个模块很像啊
httpd = make_server('127.0.0.1', 8080, application)

print('Serving HTTP on port 8080...')
# 开始监听HTTP请求:
httpd.serve_forever()
