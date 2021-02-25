FROM centos
RUN yum install -y nginx
RUN mkdir -p /data/html
RUN echo 'mynginx' > /usr/share/nginx/html/index.html
COPY gmwangfile.txt /data/html
ENV gmwang='feifei'
WORKDIR /data/html
EXPOSE 80
#CMD /bin/bash -c 'nginx'
CMD /bin/bash -c "nginx -g 'daemon off;'"

#名字改成docker hub的用户名 例如 /gmwnag/mynginx 就能通过  "docker push /gmwnag/mynginx" 上传