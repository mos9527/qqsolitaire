#!/bin/bash

cookie=$1
# 你的Cookie，请自己配置
share=$2
# Q群分享链接

echo QQSolitaire 依赖安装脚本
echo 正在安装系统依赖
pkg install -y git python

echo 克隆项目
rm -rf qqsolitaire
git clone https://github.com/greats3an/qqsolitaire

echo 正在安装 pip 依赖
python -m pip install requests coloredlogs qqlib

echo 开始执行
echo 分享链接：$share
python qqsolitaire/qqsolitaire.py "$share" "$cookie"