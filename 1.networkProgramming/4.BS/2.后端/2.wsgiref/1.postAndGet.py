from urllib.parse import parse_qs
from wsgiref.simple_server import make_server

def application(environ, start_response):

    # start_response('200 OK', [('Content-Type', 'text/html'),('k1','v1')])
    # start_response('200 OK', [('Content-Type', 'text/html'),('charset','utf-8')])
    start_response('200 OK', [('Content-Type', 'text/html')])
    print(environ)
    print(environ['PATH_INFO'])
    path = environ['PATH_INFO']
    #用户获取login页面的请求路径
    if path == '/login':
        with open('web.html','rb') as f:
            data = f.read()
    #针对form表单提交的auth路径，进行对应的逻辑处理
    elif path == '/auth/':
        #登陆认证
        #1.获取用户输入的用户名和密码

        #2.去数据库做数据的校验，查看用户提交的是否合法
        # user_information = environ['']
        if environ.get("REQUEST_METHOD") == "POST":
            #获取请求体数据的长度,因为提交过来的数据需要用它来提取,注意POST请求和GET请求的获取数据的方式不同
            try:
                request_body_size = int(environ.get('CONTENT_LENGTH', 0))
            except (ValueError):
                request_body_size = 0
            #POST请求获取数据的方式
            request_data = environ['wsgi.input'].read(request_body_size)
            print('>>>>>',request_data) # >>>>> b'username=chao&password=123'，是个bytes类型数据
            print('?????',environ['QUERY_STRING']) #????? 空的，因为post请求只能按照上面这种方式取数据
            #parse_qs可以帮我们解析数据
            re_data = parse_qs(request_data)
            print('拆解后的数据',re_data) #拆解后的数据 {b'password': [b'123'], b'username': [b'chao']}            #post请求的返回数据我就不写啦　　　　　　  pass
        if environ.get("REQUEST_METHOD") == "GET":
            #GET请求获取数据的方式，只能按照这种方式取
            print('?????',environ['QUERY_STRING']) #????? username=chao&password=123,是个字符串类型数据
            request_data = environ['QUERY_STRING']

            # parse_qs可以帮我们解析数据
            re_data = parse_qs(request_data)
            print('拆解后的数据', re_data) #拆解后的数据 {'password': ['123'], 'username': ['chao']}
            username = re_data['username'][0]
            password = re_data['password'][0]
            print(username,password)

        # 但是不管是post还是get请求都不能直接拿到数据，拿到的数据还需要我们来进行分解提取，所以我们引入urllib模块来帮我们分解



        #注意昂，我们如果直接返回中文，没有给浏览器指定编码格式，默认是gbk，所以我们需要gbk来编码一下，浏览器才能识别
        # data='登陆成功！'.encode('gbk')
    else:
        data = b'sorry 404!,not found the page'
    return [data]



#和咱们学的socketserver那个模块很像啊
httpd = make_server('127.0.0.1', 8080, application)

print('Serving HTTP on port 8080...')
# 开始监听HTTP请求:
httpd.serve_forever()