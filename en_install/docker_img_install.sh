#!/bin/bash

docker pull duckll/lnmp

mkdir /home/wwwroot/

docker run -idt --name webserver -p 80:80/tcp -p 3333:3333/udp -v /home/wwwroot/:/home/wwwroot/default/ duckll/lnmp