#!/bin/bash
sysreq="git python"
pipreq="requests coloredlogs"
echo 正在安装系统依赖 $sysreq
pkg install -y $sysreq
echo 正在安装 pip 依赖 $pipreq
python -m pip install $pipreq

echo 下载脚本
curl -o qd "https://raw.githubusercontent.com/greats3an/qqsolitaire/master/looped_run.sh"

echo 配置权限
chmod +x qd

echo 预配置完毕，请编辑文件 qd 中的 【Cookies,分享链接】
echo 以继续操作

echo 执行： $ ./qd
