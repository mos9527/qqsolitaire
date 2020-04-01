#!/bin/bash

echo 正在安装系统依赖
pkg install -y git python
echo 正在安装 pip 依赖
python -m pip install requests coloredlogs

echo 下载脚本
mkdir -p ~/.termux/tasker
cd ~/.termux/tasker
rm qqsolitaire.sh
curl -o qqsolitaire.sh "https://mos9527.tooo.top/share/QQSolitaire/clone_and_run.sh"

echo 配置权限
chmod +x qqsolitaire.sh

echo 预配置完毕，请在 Tasker 继续操作