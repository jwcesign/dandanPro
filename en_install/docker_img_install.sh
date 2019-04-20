#!/bin/bash

docker pull duckll/lnmp

mkdir /home/wwwroot/

docker run -idt --name webserver -p 80:80 -v /home/wwwroot/:/home/wwwroot/default/web/ duckll/lnmp