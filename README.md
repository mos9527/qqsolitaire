# QQSolitare
## 安装:
- Termux:
	`bash <(curl -s https://raw.githubusercontent.com/greats3an/qqsolitaire/master/installer.sh)`
- Others
	1. 安装 git (可选，可以zip形式下载) , Python 3.x
	2. 安装 pip 依赖：requests coloredlogs

## 使用
### 1. 需要 QQ系应用 Cookies
#### Android:
下载本人修改过的 [Jelly 浏览器](https://github.com/greats3an/qqsolitaire/blob/master/jellybrowser.apk?raw=true "Jelly 浏览器") ，登录 [QQ空间](https://qzone.qq.com/ "QQ空间")、[QQ邮箱](https://mail.qq.com/ "QQ邮箱") 等网站后在菜单内找到 `复制 Cookies`
#### PC / Mac
在你使用的浏览器 Console 里输入 `document.cookie` 即可取得
### 2. 配置 & 开始
#### Android
在 Termux 中，您需要先执行 [安装](##安装) 中的脚本以完成预配置
-	若只使用一次：
	    `python qqsolitaire/qqsolitaire.py "[你复制的cookie]" "[加群分享链接]"`
-	若后台常驻使用
	1.	让 Termux 取得 Wakelock（可选）
	2.	编辑 `qd` 以指定签到群和延时
	3.	开始执行：
	    `./qd "[你复制的cookie]"`
				
#### PC
同 [Android](####Android) 使用方法，暂无 Windows 常驻使用脚本

## 使用的其他项目
[Jelly](https://github.com/LineageOS/android_packages_apps_Jelly)

[Jelly Mod](https://github.com/greats3an/android_packages_apps_Jelly)
