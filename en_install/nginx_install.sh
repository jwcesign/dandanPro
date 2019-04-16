#!/bin/bash


# change dir
cd ./software_tar
dir_root=`pwd`

yum -y install pcre-devel
yum install -y zlib-devel

cd $dir_root
tar -zxvf nginx-1.12.2.tar.gz
cd nginx-1.12.2
./configure --prefix=/usr/local/nginx/
make -j && make install
