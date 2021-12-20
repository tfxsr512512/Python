# 1、PyInstaller简介

PyInstaller是一个跨平台的Python应用打包工具，支持 Windows/Linux/MacOS三大主流平台，能够把 Python 脚本及其所在的 Python 解释器打包成可执行文件，从而允许最终用户在无需安装 Python 的情况下执行应用程序。
PyInstaller 制作出来的执行文件并不是跨平台的，如果需要为不同平台打包，就要在相应平台上运行PyInstaller进行打包。

# 2、PyInstaller安装

pip install Pyinstaller
有时候会安装失败？用以下方式安装

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple Pyinstaller
永久设置

pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple



![image-20210812192159448](C:\Users\花城\AppData\Roaming\Typora\typora-user-images\image-20210812192159448.png)

