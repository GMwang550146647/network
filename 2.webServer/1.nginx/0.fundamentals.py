"""
1.启动服务
    nginx
2.测试服务
    nginx -t
3.重启服务
    nginx -s reload
4.查看服务
    ps axw -o pid,ppid,user,%cpu,vsz,wchan,command | egrep '(nginx|PID)'
"""
"""
文件：
    html文件在/usr/local/Cellar/nginx/1.19.6
    conf文件在/usr/local/etc/nginx
    log文件在/usr/local/var/log/nginx
"""