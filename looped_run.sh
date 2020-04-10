#!/bin/bash
# 请在此处预先设置好分享链接，延时
cookie=$1
# 你的Cookie，请以形参形式传入 e.g.
# $ ./qd [cookie]
share=""
# Q群分享链接
interval=100
# 执行延时（秒）

if [$share -eq ""];then
    echo 您没有配置【分享链接】
    echo 请使用 vi / nano / pico 等编辑器    
    echo 编辑本脚本中 share= 以设置该项
    sleep 2
    exit 1
fi

echo QQSolitaire 依赖安装脚本

echo 克隆项目
rm -rf qqsolitaire
git clone https://github.com/greats3an/qqsolitaire

echo 开始执行
echo 分享链接：$share
echo 循环周期：$interval s
while true
do
    python qqsolitaire/qqsolitaire.py "$cookie" "$share"
    echo 将在 $interval s 后继续执行
    sleep $interval
done