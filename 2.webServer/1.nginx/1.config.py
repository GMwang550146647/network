"""
html文件在/usr/local/Cellar/nginx/1.19.6
conf文件在/usr/local/etc/nginx
"""
"""

#user  nobody;                  #使用的用户来启动子进程
worker_processes  1;            #进程数（cpu数-2 或者-1）

#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

#pid        logs/nginx.pid;


events {
    #use [epoll|select|poll];
    worker_connections  1024;   #每一个子进程能处理的连接数
}


http {
    include       mime.types;     #导入
    default_type  application/octet-stream; #默认的请求方式

    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';
    #定义日志并定义日志格式
    #access_log  logs/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;  #保持长连接的时间

    #gzip  on;

    server {
        listen       8080;
        server_name  gmwang.com;  #设置域名  ,要在/etc/host 中添加  "{ip} gmwang.com "

        #charset koi8-r;

        #access_log  logs/host.access.log  main;
        location / {
            root   html;
            index  index.html index.htm;
        }
        location /img{
            alias i;    #直接写localhost/i就行了 (前提是要有这个目录...)
        }

        error_page  404              /i/404.html;  #错误页面，客户端错误

        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;   #错误页面，服务端错误
        location = /50x.html {
            root   html;
        }

        # proxy the PHP scripts to Apache listening on 127.0.0.1:80
        #
        #location ~ \.php$ {
        #    proxy_pass   http://127.0.0.1;
        #}

        # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
        #
        #location ~ \.php$ {
        #    root           html;
        #    fastcgi_pass   127.0.0.1:9000;
        #    fastcgi_index  index.php;
        #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
        #    include        fastcgi_params;
        #}

        # deny access to .htaccess files, if Apache's document root
        # concurs with nginx's one
        #
        #location ~ /\.ht {
        #    deny  all;
        #}
    }


    # another virtual host using mix of IP-, name-, and port-based configuration
    #
    #server {
    #    listen       8000;
    #    listen       somename:8080;
    #    server_name  somename  alias  another.alias;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}


    # HTTPS server
    #
    #server {
    #    listen       443 ssl;
    #    server_name  localhost;

    #    ssl_certificate      cert.pem;
    #    ssl_certificate_key  cert.key;

    #    ssl_session_cache    shared:SSL:1m;
    #    ssl_session_timeout  5m;

    #    ssl_ciphers  HIGH:!aNULL:!MD5;
    #    ssl_prefer_server_ciphers  on;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}
    include servers/*;
}

"""
