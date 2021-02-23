"""
1.下载
docker pull nginx
2.运行image 为容器
    2.1.普通
        docker run --name nginx1 -d -P nginx
        docker run --name nginx2 -d -P nginx
        docker run --name nginx3 -d -P nginx

        (进入容器： docker exec -it nginx1 /bin/bash)
    2.2.互连容器
        docker network create -d bridge nginx-net
        docker run -itd --name nginx11 --network nginx-net nginx /bin/bash
        docker run -itd --name nginx22 --network nginx-net nginx /bin/bash
        docker exec -it nginx11 /bin/bash
        docker exec -it nginx22 /bin/bash
        apt-get update
        apt install iputils-ping
        ping nginx22

"""