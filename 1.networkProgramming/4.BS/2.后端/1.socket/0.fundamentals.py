"""
1.http协议：
    1.基于 请求-响应 的模式 ：　肯定是先从客户端开始建立通信的,服务器端在没有 接收到请求之前不会发送响应
    2.无状态保存 ：           HTTP协议 自身不对请求和响应之间的通信状态进行保存
    3.无连接  ：             无连接的含义是限制每次连接只处理一个请求。服务器处理完客户的请求，并收到客户的应答后，即断开连接

2.HTTP请求方法：
    1.GET
    2.POST
    3.HEAD PUT DELETE TRACE OPTION CONNECT PATCH

3.HTTP状态码
    状态代码的第一个数字代表当前响应的类型：
        1xx消息——请求已被服务器接收，继续处理
        2xx成功——请求已成功被服务器接收、理解、并接受
        3xx重定向——需要后续操作才能完成这一请求
        4xx请求错误——请求含有词法错误或者无法被执行
        5xx服务器错误——服务器在处理某个正确请求时发生错误

4.URL
    传送协议。
    层级URL标记符号(为[//],固定不变)
    访问资源需要的凭证信息（可省略）
    服务器。（通常为域名，有时为IP地址）
    端口号。（以数字方式表示，若为HTTP的默认值“:80”可省略）
    路径。（以“/”字符区别路径中的每一个目录名称）
    查询。（GET模式的窗体参数，以“?”字符为起点，每个参数以“&”隔开，再以“=”分开参数名称与数据，通常以UTF8的URL编码，避开字符冲突的问题）
    片段。以“#”字符为起点
    例子：
        以http://www.luffycity.com:80/news/index.html?id=250&page=1 为例, 其中：
        http，是协议；
        www.luffycity.com，是服务器；
        80，是服务器上的默认网络端口号，默认不显示；
        /news/index.html，是路径（URI：直接定位到对应的资源）；
        ?id=250&page=1，是查询。

5.HTTP请求格式(请求协议)
    POST:
        POST /somepath HTTP/1.1
        KEY1: VALUE1
        KEY2: VALUE2
        ...

        name=xxx&passwd=xxx&....
    GET
        GET /somepath/?name=xxx&passwd=xxx&.... HTTP/1.1
        KEY1: VALUE1
        KEY2: VALUE2
        ...

        (发送的数据为空，所以空两行)

6.HTTP响应格式（响应协议）
    HTTP/1.1 200 OK
    KEY1: VALUE1
    KEY2: VALUE2
    ...

    <html>
    ...
    </html>
"""