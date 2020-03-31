#!/bin/bash

cookie=""
# 你的Cookie，请自己配置
share="https://jq.qq.com/?_wv=1027&k=52P5RqJ"
# Q群分享链接

echo QQSolitaire 依赖安装脚本
echo 正在安装系统依赖
pkg install -y git python

echo 克隆项目
rm -rf qqsolitaire
git clone https://github.com/greats3an/qqsolitaire

echo 正在安装 pip 依赖
cd qqsolitaire
python -m pip install requests coloredlogs

echo 开始执行
python qqsolitaire/qqsolitaire.py "$share" "$cookie"