# Linux操作系统

## 1.操作系统概念

操作系统（Operating System，简称OS）是==管理和控制计算机硬件与软件资源的计算机程序==，是直接 运行在“裸机”上的==最基本的系统软件==，任何其他软件都必须在操作系统的支持下才能运行。

操作系统是==用户==和计算机的==接口==，同时也是计算机==硬件==和其他==软件==的接口。操作系统的功能包括管理计 算机系统的硬件、软件及数据资源，控制程序运行，改善人机界面，为其它应用软件提供支持，让计算 机系统所有资源最大限度地发挥作用，提供各种形式的用户界面，使用户有一个好的工作环境，为其它 软件的开发提供必要的服务和相应的接口。

操作系统接口示意图：

![image-20210827192336921](C:\Users\花城\AppData\Roaming\Typora\typora-user-images\image-20210827192336921.png)

如果没有安装操作系统的计算机称之为==裸机==，只有一堆硬件。操作系统位于==底层硬件==与==用户==之间，是两者沟通的==桥梁==。用户可以通过操作系统的用户界面，输入命令， 操作系统则对命令进行解释，驱动硬件设备，实现用户要求

## 2. Ubuntu命令格式

```
cd ..   #  进入上一级
ll   #  查看目录
pwd  # 产看当前目录
cd /  # 回到根目录
pwd --help  # 加上 --help 查看该命令功能
```

### 2.1 查看命令的帮助手册

```
1、- -help    command - -help 查看命令的帮助信息
2、man man command 查看命令的使用手册 man 命令可以查看linux绝大部分的命令详细使用手册。
```

```
1、linux常用命令不用死记硬背，用多了自然就记得了 
2、命令可以使用tab补全，输入命令的前几个字母按tab键如果输入的没有歧义，系统会自动补全， 如果有歧义按两次tab键有命令提示。
3、曾经使用过的的命令，可用用上下箭头来回切换。
4、忘记了一些命令的选项参数，可以用刚才讲的--help,man 去查看帮助
5、输入了命令不想执行可以使用ctrl+c取消。或者ctrl+u将输入的内容删除
```

### 2.2 ls查看目录文件

```
-a 显示隐藏的文件
-l 以列表的形式显示
-h 以人性化的方式显示文件内容大小
-R 递归显示子目录
```

![image-20210827204317449](C:\Users\花城\AppData\Roaming\Typora\typora-user-images\image-20210827204317449.png)

### 2.3 cd切换工作目录

```
绝对路径、相对路径：
绝对路径：指的是在输入路径时，最前面是/或者~表示从 根目录/家目录 开始的具体目录位置
相对路径：指的是以当前目录开始，不以/或者~开头，表示不是以根目录或者家目录开始的目录
cd 命令可以跟相对路径或者绝对路径
cd [路径] 切换到指定路径
cd . 切换到当前目录
cd .. 切换到上一级目录
cd ~ 切换到家目录
cd - 上一次工作目录互相切换
```

### 2.4 touch新建文件命令

```
touch [文件名称]
touch 文件名称 [文件名称] touch 新建文件，可以同时新建多个。
```

```
[root@localhost luohuihua]# ls
Desktop  下载  公共  图片  文档  桌面  模板  视频  音乐
[root@localhost luohuihua]# touch test
[root@localhost luohuihua]# ls
Desktop  test  下载  公共  图片  文档  桌面  模板  视频  音乐
[root@localhost luohuihua]# touch t1 t2
[root@localhost luohuihua]# ls
Desktop  t1  t2  test  下载  公共  图片  文档  桌面  模板  视频  音乐
[root@localhost luohuihua]# 
```

### 2.5 mkdir新建目录

```
-p 递归创建
mkdir [目录名]
mkdir -p a/b/c 在b目录不存在时，可以用-p参数同时创建b目录
```

```
[root@localhost luohuihua]# ls
Desktop  t1  t2  test  下载  公共  图片  文档  桌面  模板  视频  音乐
[root@localhost luohuihua]# mkdir test
mkdir: cannot create directory ‘test’: File exists
[root@localhost luohuihua]# mkdir testdir
[root@localhost luohuihua]# ls
Desktop  t1  t2  test  testdir  下载  公共  图片  文档  桌面  模板  视频  音乐
[root@localhost luohuihua]# mkdir -p a/b/c
[root@localhost luohuihua]# ls
a  Desktop  t1  t2  test  testdir  下载  公共  图片  文档  桌面  模板  视频  音乐
```

### 2.6 rmdir删除目录

```
-p 递归删除
rmdir [目录] 注意：rmdir只能删除空目录，非空目录无法删除。
```

```python
root@localhost luohuihua]# ls
a  Desktop  t1  t2  test  testdir  下载  公共  图片  文档  桌面  模板  视频  音乐
[root@localhost luohuihua]# rmdir testdir
[root@localhost luohuihua]# ls
a  Desktop  t1  t2  test  下载  公共  图片  文档  桌面  模板  视频  音乐
[root@localhost luohuihua]# rmdir a
rmdir: failed to remove ‘a’: Directory not empty
[root@localhost luohuihua]# rmdir -p a
rmdir: failed to remove ‘a’: Directory not empty
[root@localhost luohuihua]# rmdir -p a/b/c
[root@localhost luohuihua]# ls
Desktop  t1  t2  test  下载  公共  图片  文档  桌面  模板  视频  音乐
[root@localhost luohuihua]# 
```

### 2.7 rm删除文件或目录

```
-r 递归地删除目录下的内容，删除文件夹时必须加此参数
-f 强制删除，忽略不存在的文件，无需提示
```

```
[root@localhost luohuihua]# ls
Desktop  t1  t2  test  下载  公共  图片  文档  桌面  模板  视频  音乐
[root@localhost luohuihua]# rm t1
rm: remove regular empty file ‘t1’? y
[root@localhost luohuihua]# ls
Desktop  t2  test  下载  公共  图片  文档  桌面  模板  视频  音乐
[root@localhost luohuihua]# rm -f t2
[root@localhost luohuihua]# ls
Desktop  test  下载  公共  图片  文档  桌面  模板  视频  音乐
[root@localhost luohuihua]# mkdir -p a/b/c
[root@localhost luohuihua]# ls
a  Desktop  test  下载  公共  图片  文档  桌面  模板  视频  音乐
[root@localhost luohuihua]# rm -rf a
[root@localhost luohuihua]# ls
Desktop  test  下载  公共  图片  文档  桌面  模板  视频  音乐
[root@localhost luohuihua]# 
```

### 2.8 mv移动和重命名

```
-f 覆盖前不询问
-i 覆盖前询问
-n 不覆盖已经存在的文件
mv命令在同一个文件夹下移动文件，即重命名功能。
```

```
[root@localhost luohuihua]# ls
Desktop  test  下载  公共  图片  文档  桌面  模板  视频  音乐
[root@localhost luohuihua]# mkdir testdir
[root@localhost luohuihua]# ls
Desktop  test  testdir  下载  公共  图片  文档  桌面  模板  视频  音乐
[root@localhost luohuihua]# mv test testdir
[root@localhost luohuihua]# ls
Desktop  testdir  下载  公共  图片  文档  桌面  模板  视频  音乐
[root@localhost luohuihua]# cd testdir
[root@localhost testdir]# ls
test
[root@localhost testdir]# 
```



### 2.9 cp复制

```
-i 覆盖前提示 -r 若给出的源文件是目录文件，则cp将递归复制该目录下的所有子目录和文件， 目标文件必须为一个
目录名 cp src des 如果是复制文件夹，则加上-r选项	
```

```
[root@localhost testdir]# cp test ../test1
[root@localhost testdir]# ls
test
[root@localhost testdir]# cd ..
[root@localhost luohuihua]# ls
Desktop  test1  testdir  下载  公共  图片  文档  桌面  模板  视频  音乐
[root@localhost luohuihua]# cp -r testdir testdir2
[root@localhost luohuihua]# ls
Desktop  test1  testdir  testdir2  下载  公共  图片  文档  桌面  模板  视频  音乐
[root@localhost luohuihua]# 
```

### 2.10 cat查看文件内容、合并文件(1)

```
-n 输出行编号
-s 不输出多行空行
-b 对非空行进行编号
cat [-nsb] filename 查看文件的内容
cat filename1 filename2 > filename 将filename1 和filename2 的文件合并写入到filename 文件中
```

```
[root@localhost luohuihua]# ls
Desktop  test1  testdir  testdir2  下载  公共  图片  文档  桌面  模板  视频  音乐
[root@localhost luohuihua]# cat test1
this first line

this second line

this other text


this other line
[root@localhost luohuihua]# cat -n test1
     1	this first line
     2	
     3	this second line
     4	
     5	this other text
     6	
     7	
     8	this other line
```

### 2.11 cat查看文件内容、合并文件(2)

![image-20210827212946316](C:\Users\花城\AppData\Roaming\Typora\typora-user-images\image-20210827212946316.png)

### 2.12 more查看文件内容（分页查看）

more filename 查看filename 文件的内容

![image-20210827213030492](C:\Users\花城\AppData\Roaming\Typora\typora-user-images\image-20210827213030492.png)

### 2.13 history查看历史命令

```
history 查看历史命令
history -c 删除历史命令记录
```

```
[root@localhost luohuihua]# history
    1  passwd luohuihua
    2  ls
    3  exit
    4  yum update -y
    5  ls
    6  cd /home
    7  ls
    8  cd luohuihua/
    9  ls
   10  ls -a
   11  ls -l
   12  ls -h
   13  ls -lh
```

### 2.14 sudo获得root权限

ubuntu 默认是不能以root账号登录系统，那么遇到需要root权限的怎么办？
那么这个时候只要在命令前面加上sudo，就可以获得root权限。

```
sudo su root   # 获取root权限
```

## 3. Linux权限与远程管理

### 3.1 用户、用户组和权限管理

#### 3.1.1 概述

用户：
要登录Linux必须要有一个用户，一台Linux系统下可以有多个用户，并且每个用户可有不同的权限。在Linux中可以指定用户对不同的文件、目录拥有不同的权限。

用户组：
Linux有一个组的概念，不同的用户分配到一个组，那么同组下的用户，都拥有这个组的权限。

权限
Linux权限有三种，读r，写w，执行x。

![image-20210828094237297](C:\Users\花城\AppData\Roaming\Typora\typora-user-images\image-20210828094237297.png)

#### 3.1.2 用户管理

* ==用户管理==包括：创建用户、删除用户、修改用户帐号属性、创建用户组、修改用户组属性。
  其中，创建用户/删除用户/修改其他用户密码 的终端命令都需要通过 ==sudo== 执行。
* ==创建用户==
  * 命令：useradd [用户名]
  * 选项说明：
    -d 指定新账户的主目录
    -g 指定用户的所属组
    -G指定用户附加组
    -s指定用户登录shell
    -m自动创建家目录
* ==删除用户==
  命令：userdel [用户名] 
  -r 删除用户的同时删除家目录
* ==修改==用户帐号属性
  * 命令：usermod
    -u 用户id
    -g 所属组id
    -a -G GID：不使用-a选项，会覆盖此前的附加组；
    -d -m 将家目录内容移至新位置 
    -s该用户帐号的新登录
    -l 新的登录名称
* ==用户切换==
  su - [用户名] 加-同时切换到用户的家目录，不加直接在当前目录切换到新用户。

* ==创建用户组==
  命令：groupadd
* ==删除用户组==
  命令： groupdel 
* ==修改组属性==
  命令：groupmod
  * -g Gid
* 提示：
  创建用户时，会默认创建一个与用户名同名的组名
  创建成功后可在/etc/passwd文件下查看
  新创建的用户没用sudo权限，需要将用户加到 adm,sudo 这两个组中才拥有sudo权限

#### 3.1.3 权限管理

* 命令：chmod +/- rwx 文件名|目录名 +增加权限，-取消权限  
* 每个文件，都有三组不同的权限，第一组文件所有者，第二组是文件所属组，第三组是其他用户。 
  第一组：u 文件所有者 修改所有者权限：chmod u+/-/= rwx filename  
  第二组：g 文件所有组 修改所属组权限： chmod g+/-/= rwx filename  
  第三组：o 其他用户 修改所属组权限： chmod o+/-/= rwx filename 

![image-20210828094935105](C:\Users\花城\AppData\Roaming\Typora\typora-user-images\image-20210828094935105.png)

* 命令：chmod ==755== 文件名|目录名 指定权限修改
* chmod中第一个数字代表所有者权限，第二个数字代表所属组权限，第三个数字代表其他人权限。

| 权限 | 数字表示法 |
| ---- | ---------- |
| r    | 4          |
| w    | 2          |
| x    | 1          |

![image-20210828104726967](C:\Users\花城\AppData\Roaming\Typora\typora-user-images\image-20210828104726967.png)

### 3.2 远程管理

#### 3.2.1 ifconfig 查看系统ip地址

![image-20210828105901721](C:\Users\花城\AppData\Roaming\Typora\typora-user-images\image-20210828105901721.png)

#### 3.2.2 ping 命令

* 检查网络是否正常通信,Linux下默认ping不会结束，使用ctrl+c强制结束
* 示例：ping www.baidu.com
  * 其他选项
    * ping -c 指定ping几个数据包结束
    * ping -i 指定发送数据包的间隔，单位是秒
    * ping -s 指定发送数据的大小，单位字节
    * ping -t 设置TTL的大小，TTL 网络调数大小

#### 3.2.3 ssh 远程连接

* SSH是一种网络协议，用于计算机之间的加密登录。Linux 下默认开启sshd服务，只有开启sshd服务才能进行ssh连接。
* 可以使用 service sshd status 查看是否开启sshd服务。active(running)表示已经开启。

![image-20210828110622956](C:\Users\花城\AppData\Roaming\Typora\typora-user-images\image-20210828110622956.png)

* Windows下连接方式
  Windows下我们借助第三方软件，xshell或者putty来连接。
  xshell和putty下载地址：链接：https://pan.baidu.com/s/1kUCyM2r 密码：zypl
  ssh端口号默认：22
* Linux下ssh命令连接方式
  ssh -p 端口 主机#-p可以指定端口。ssh一般使用默认的22。看到提示welcome表示已经连接成功

![image-20210828110652345](C:\Users\花城\AppData\Roaming\Typora\typora-user-images\image-20210828110652345.png)

#### 3.2.4 scp文件复制

scp就是secure copy，是一个在Linux下用来进行远程拷贝文件的命令
使用示例1：把远程的e.txt 文件拷贝到本地/home/python/Desktop下

```
scp python@192.168.254.131:/home/python/a/e.txt /home/python/Desktop
```

使用示例2：将本地 Desktop/requirements.txt 文件拷贝到远程主机的家目录下

```
scp Desktop/requirements.txt python@192.168.254.131:/home/python
```


使用示例3：scp -r 可以复制文件夹。把当前目录下的demo文件夹 复制到远程目录下的Desktop

```
scp -r demo user@remote:Desktop
```

使用示例4：将远程主机的a文件夹包括子文件，复制到本机的桌面

```
scp -r python@192.168.254.131:/home/python/a Desktop
```

scp只能在Linux中使用，那我们在Windows下该怎么传文件到Linux呢？
Windows下往Linux上传下载文件我们可以使用 winscp.
winscp 下载地址：https://winscp.net/eng/download.php

### 3.3 系统信息管理

==查看系统时间==

date 查看系统当前时间

==查看磁盘空间==

df -TH 查看磁盘分区，以及挂载情况

du -sh [目录名]查看目录大小

du -h [文件名] 查看文件大小

==查看内核/操作系统/CPU信息==

uname -a # 查看内核/操作系统/CPU信息

uname -i 查看硬件平台
uname -m 查看cpu
uname -n 节点名称
uname -o 操作系统
uname -v 内核版本
uname -r 发行版本号

==查看进程==

top 查看进程实时运行情况，即系统资源实时使用情况，退出top界面输入q

| 符号    | 说明                                                         |
| ------- | ------------------------------------------------------------ |
| PID     | 进程id                                                       |
| USER    | 进程所有者                                                   |
| PR      | 进程优先级                                                   |
| NI      | nice值。负值表示高优先级，正值表示低优先级                   |
| VIRT    | 进程使用的虚拟内存总量，单位kb。VIRT=SWAP+RES                |
| RES     | 进程使用的、未被换出的物理内存大小，单位kb。RES=CODE+DATA    |
| SHR     | 共享内存大小，单位kb                                         |
| S       | 进程状态。D=不可中断的睡眠状态R=运行S=睡眠T=跟踪/停止Z=僵尸进程 |
| %CPU    | 上次更新到现在的CPU时间占用百分比                            |
| %MEM    | 进程使用的物理内存百分比                                     |
| TIME+   | 进程使用的CPU时间总计，单位1/100秒                           |
| COMMAND | 进程名称（命令名/命令行）                                    |

ps 查看系统所有进程的状态
命令：ps -ajx 一般使用ps命令带选项ajx 一起使用  -aux

![image-20210828140531311](C:\Users\花城\AppData\Roaming\Typora\typora-user-images\image-20210828140531311.png)

==结束进程==

命令：kill [参数] [进程号]  
kill -9 [进程号] ：强制结束进程
kill -15 [进程号] ：结束进程，等级没有-9高 

提示：
在Linux中1号进程（init进程）是有所有进程的祖先进程，是不能被结束的。

## 4. Linux文件查找与编辑器使用

### 4.1 文件查找命令（上）

添加环境变量

![image-20210901195958897](C:\Users\花城\AppData\Roaming\Typora\typora-user-images\image-20210901195958897.png)

#### 4.1.1 which命令

which命令用于查找并显示给定命令的绝对路径，环境变量PATH中保存了查找命令时需要遍历的目录。which指令会在环境变量==$PATH==设置的目录里查找符合条件的文件。也就是说，使用which命令，就可以看到某个系统命令是否存在，以及执行的到底是哪一个位置的命令，此命令会去搜索==$PATH==环境变量中的目录路径：可以使用 echo $PATH 查看,如

```linux
luohuihua@ubuntu:~$ echo $PATH
/home/luohuihua/bin:/home/luohuihua/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
luohuihua@ubuntu:~$
```

路径使用”:”号分隔，which 命令会在这些路径下去搜索。

**语法:**  which [系统命令]

```
luohuihua@ubuntu:~$ which pwd
/bin/pwd
luohuihua@ubuntu:~$ which adduser
/usr/sbin/adduser
luohuihua@ubuntu:~$
```

**说明：** which是根据使用者所配置的 PATH 变量内的目录去搜寻可运行档的！所以，不同的 PATH 配置内容所找到的命令当然不一样的！

#### 4.1.2 whereis命令

与which 功能相似的还有一条命令 whereis 也可以查找到命令的绝对路径
与whereis不同,which会列出这个命令的别名记录,而whereis会显示出这个命令的帮助文档所在位置

* ==语法：==whereis(选项)(参数)
* ==选项：==-b：只查找二进制文件；
   -B<目录>：只在设置的目录下查找二进制文件；
   -f：不显示文件名前的路径名称；
   -m：只查找说明文件；
   -M<目录>：只在设置的目录下查找说明文件；
   -s：只查找原始代码文件；
   -S<目录>只在设置的目录下查找原始代码文件；
   -u：查找不包含指定类型的文件。
* **whereis命令只能用于程序名的搜索，如果省略选项，则返回所有信息**

```
luohuihua@ubuntu:~$ whereis pwd
pwd: /bin/pwd /usr/include/pwd.h /usr/share/man/man1/pwd.1.gz
luohuihua@ubuntu:~$ whereis -b pwd
pwd: /bin/pwd /usr/include/pwd.h
luohuihua@ubuntu:~$ whereis svn
svn:
luohuihua@ubuntu:~$
```

**说明：**svn没安装，找不出来

#### 4.1.3 locate命令

**格式:**locate [搜索关键字]  
**说明:**

1. 是Linux所特有的命令,寻找文件或目录，最好用于快速定位系统命令，配置文件等
2. 虽然搜索速度很快，但有时候会找不到
3. locate是在文件数据库中查找的，所以速度会很快
4. 但是如果数据库没有包含这个文件的话，他就会找不到；

```
luohuihua@ubuntu:~$ locate /etc/sh
/etc/shadow
/etc/shadow-
/etc/shells
luohuihua@ubuntu:~$
```

配合:updatedb 建立整个系统目录文件的数据库  **注意：其执行权限为：root！！！**

```
备注：当在某些目录下创建文件，然后更新数据库之后，并不能用locate命令查找到,原因是系统在更新数据库的配置文件中，设置了一些搜索限制，所以搜索不到，输入如下命令可以看到：
[root@localhost ~]# vi /etc/updatedb.conf
PRUNE_BIND_MOUNTS = “yes” 表示开启搜索限制，如果为’no’则表示不开启搜索限制；
PRUNEFS = 表示搜索时，不搜索的文件系统；
PRUNENAMES = 表示搜索时，不搜索的文件类型；
PRUNEPATHS = 表示搜索时，不搜索的路径； 
不只locate命令遵循搜索限制，whereis 与 which 也遵循
```

### 4.2 文件查找命令（下）

#### 4.2.1 find命令(1)

find 命令用于：在一个目录（及子目录）中搜索文件，你可以指定一些匹配条件，如按文件名、文件类型、用户等条件查找文件

**语法：**find [搜索路径] [搜索选项] filename
path 路径，表示从这个路径下开始查找

**选项说明：**
	-name filename 查找名为filename的文件
	-size +/-大小 按照文件大小来查找，+大于，-小于
	-user username 按文件所属查找
	通过时间值查找
	-ctime -atime -mtime （以天为单位）
	-cmin -amin -mmin （以分钟为单位）
	-type 按文件的类型
	-inum 根据i节点进行查找 
	-group 组名 按所属组来查找
	-a and 逻辑与 -o or 逻辑或
	-exec 或 -ok command {} \; 将查到的文件执行command操作,{} 和 \;之间有空格，固定格式。  提示：如果find命令省略路径	不写，表示从当前路径开始查找。find还可以结合通配符使用

#### 4.2.2 find命令(2)

linux 下的通配符

![image-20210828152306374](C:\Users\花城\AppData\Roaming\Typora\typora-user-images\image-20210828152306374.png)

#### 4.2.3 find命令 -name **选项**

find /etc -name 文件名 #-name 最常见的选项 find /etc -name init // 在目录/etc中查找文件init文件

**注意：**

* 尽量缩小查找范围，不要在根目录下查找,不然:
  	1、查找速度非常慢；
  	2、占用大量系统资源.
* 占用系统资源越少越好,而且尽量在服务器压力较小时用find进行查找.
* find .. -name 查找结果与Windows不同，如:Windows会把所有包含init关键词的文件全都列出来而Linux则只会匹配init关键词

**使用通配符：**

==*：==用于匹配任意字符
     find /etc -name init*   #查找所有以init开头的文件
     find /etc -name *init*  #init左右都没有空格，用于查找所有包含init关键词的文件
==?：==用于匹配单个字符
     find /etc -name init??? #这个文件会有七个字符。
     find /etc -name ?init?? 

```
root@ubuntu:~# find /etc -name init
/etc/apparmor/init
/etc/init
root@ubuntu:~# find /etc -name init*
/etc/init.d
/etc/apparmor/init
/etc/kernel/postinst.d/initramfs-tools
/etc/kernel/postrm.d/initramfs-tools
/etc/initramfs-tools
/etc/initramfs-tools/scripts/init-bottom
/etc/initramfs-tools/scripts/init-premount
/etc/initramfs-tools/scripts/init-top
/etc/initramfs-tools/initramfs.conf
/etc/init
root@ubuntu:~# find /etc -name init??
/etc/init.d
root@ubuntu:~#
```

#### 4.2.4 find命令 -size 选项

find /etc -size 文件大小 
文件大小：他是以数据块为单位的！512字节 = 0.5KB, 1K = 2Blocks
100M=？blocks 100M = 102400K = 102400*2blocks

* find /etc -size +204800 #在/etc下查找大于80MB大于100MB的文件 
* find /etc -size -204800 #在/etc下查找大于80MB小于100MB的文件 
* find /etc -size 204800  #在/etc下查找等于100MB的文件,不常用! 
* find /etc -size +10k    #在/etc下查找大于10K的文件

```
root@ubuntu:~# find /etc/ -size +100k
/etc/apparmor.d/cache/usr.bin.webbrowser-app
/etc/apparmor.d/cache/usr.bin.evince
/etc/ssh/moduli
/etc/vmware-tools/locations
/etc/ssl/certs/ca-certificates.crt
/etc/brltty/Contraction/zh-tw-ucb.ctb
/etc/brltty/Contraction/ko.ctb
/etc/brltty/Contraction/zh-tw.ctb
/etc/ImageMagick-6/mime.xml
root@ubuntu:~# 
```

#### 4.2.5 find命令 -user 选项

find /etc -user username 查找属于username的文件 

```
root@ubuntu:/home/luohuihua# pwd
/home/luohuihua
root@ubuntu:/home/luohuihua# ls
Downloads  examples.desktop  下载  公共的  图片  文档  桌面  模板  视频  音乐
root@ubuntu:/home/luohuihua# touch test.txt
root@ubuntu:/home/luohuihua# ls -l test.txt 
-rw-r--r-- 1 root root 0 6月  28 11:03 test.txt
root@ubuntu:/home/luohuihua# find /home/luohuihua -user root
/home/luohuihua/test.txt
root@ubuntu:/home/luohuihua#
```

#### 4.2.6 find命令 - 时间选项

以天为单位： ctime，atime，mtime 
以分钟为单位： cmin，amin，mmin #更为常用  

* c-change 改变：表示文件的属性被修改过，比如：所有者，所属组，权限  

* access 访问：文件被浏览过  


* m-modify 修改：文件内容被修改过  

**-** 多长时间之内
**+** 超过多少时间

find /etc -mtime -1    //查找/etc目录下一天之内文件内容被修改过的文件 
find /etc -amin -60    //查找/etc目录下60分钟内被浏览过的文件 
find /home -cmin -120  //查找/home目录下2小时内文件属性属性被修改过的文件

```
root@ubuntu:/home/luohuihua# mkdir test
root@ubuntu:/home/luohuihua# cd test
root@ubuntu:/home/luohuihua/test# touch test.txt
root@ubuntu:/home/luohuihua/test# ls
test.txt
root@ubuntu:/home/luohuihua/test# find ./ -cmin -10
./
./test.txt
root@ubuntu:/home/luohuihua/test# find ./ -cmin +10
root@ubuntu:/home/luohuihua/test#
```

#### 4.2.7 find命令 -type选项

find /etc -type 文件类型 #根据文件类型查找 
**文件类型：**  

1. f 二进制文件  
2. l 软链接文件  
3. d 目录  

find /etc -type f 
find /etc -type l

```
root@ubuntu:/home/luohuihua# pwd
/home/luohuihua
root@ubuntu:/home/luohuihua# ls
Downloads  examples.desktop  test  test.txt  下载  公共的  图片  文档  桌面  模板  视频  音乐
root@ubuntu:/home/luohuihua# find ./ -maxdepth 1 -type f
./.bashrc
./.bash_history
./.sudo_as_admin_successful
./.pam_environment
./.xsession-errors
./.profile
./.ICEauthority
./.bash_logout
./test.txt
./.Xauthority
./.dmrc
./.xsession-errors.old
./examples.desktop
./.xinputrc
root@ubuntu:/home/luohuihua#
```

#### 4.2.8 find命令 -inum选项

-inum #根据i节点进行查找 
touch abc #删除:rm abc 
touch “a b” #删除:rm “a b” 
find . -inum 159341 
find . -inum 159341 -exec rm -f {} \; #找到i节点为159341的文件，并删除它

```
root@ubuntu:/home/luohuihua# pwd
/home/luohuihua
root@ubuntu:/home/luohuihua# ls -li
总用量 52
2361647 drwxr-xr-x 2 luohuihua luohuihua 4096 5月   7 11:53 Downloads
2378249 -rw-r--r-- 1 luohuihua luohuihua 8980 4月  24 16:52 examples.desktop
2491109 drwxr-xr-x 2 root      root      4096 6月  28 11:25 test
2364019 -rw-r--r-- 1 root      root         0 6月  28 11:24 test.txt
2490875 drwxr-xr-x 2 luohuihua luohuihua 4096 5月   7 12:42 下载
2490978 drwxr-xr-x 2 luohuihua luohuihua 4096 5月   7 12:42 公共的
2491100 drwxr-xr-x 2 luohuihua luohuihua 4096 5月   7 12:42 图片
2491098 drwxr-xr-x 2 luohuihua luohuihua 4096 5月   7 12:42 文档
2490744 drwxr-xr-x 2 luohuihua luohuihua 4096 5月   7 12:42 桌面
2490958 drwxr-xr-x 2 luohuihua luohuihua 4096 5月   7 12:42 模板
2491101 drwxr-xr-x 2 luohuihua luohuihua 4096 5月   7 12:42 视频
2491099 drwxr-xr-x 2 luohuihua luohuihua 4096 5月   7 12:42 音乐
root@ubuntu:/home/luohuihua# find . -inum 2361647
./Downloads
root@ubuntu:/home/luohuihua#
```

#### 4.2.9 find命令 -group 选项 

-group 组名 #根据用户组的名称查找
find . -group luohuihua #查找当前目录下属于 luohuihua用户组的所有文件

```
root@ubuntu:/home/luohuihua# pwd
/home/luohuihua
root@ubuntu:/home/luohuihua# ls -l
总用量 52
drwxr-xr-x 2 luohuihua luohuihua 4096 5月   7 11:53 Downloads
-rw-r--r-- 1 luohuihua luohuihua 8980 4月  24 16:52 examples.desktop
drwxr-xr-x 2 root      root      4096 6月  28 11:25 test
-rw-r--r-- 1 root      root         0 6月  28 11:24 test.txt
drwxr-xr-x 2 luohuihua luohuihua 4096 5月   7 12:42 下载
drwxr-xr-x 2 luohuihua luohuihua 4096 5月   7 12:42 公共的
drwxr-xr-x 2 luohuihua luohuihua 4096 5月   7 12:42 图片
drwxr-xr-x 2 luohuihua luohuihua 4096 5月   7 12:42 文档
drwxr-xr-x 2 luohuihua luohuihua 4096 5月   7 12:42 桌面
drwxr-xr-x 2 luohuihua luohuihua 4096 5月   7 12:42 模板
drwxr-xr-x 2 luohuihua luohuihua 4096 5月   7 12:42 视频
drwxr-xr-x 2 luohuihua luohuihua 4096 5月   7 12:42 音乐
root@ubuntu:/home/luohuihua# find . -maxdepth 1 ! -name ".*" -group luohuihua
./Downloads
./音乐
./公共的
./图片
./视频
./文档
./桌面
./模板
./下载
./examples.desktop
root@ubuntu:/home/luohuihua#
```

#### 4.2.10 find命令 -逻辑与、逻辑或 选项

-a：and 逻辑与 
-o：or 逻辑或
find /etc -size +163840 -a -size 204800 #查找>80M,<100M的文件 
find /etc -name init* -a -type f #查找名为init并且为二进制的文件,并不包含目录

```
root@ubuntu:/home/luohuihua# find /etc -maxdepth 1 -size +10k -a -size -20k
/etc
/etc/sensors3.conf
/etc/login.defs
/etc/ltrace.conf
root@ubuntu:/home/luohuihua#
```

#### 4.2.11 find命令 -exec 选项

find ….. -exec 命令 {} \; #固定格式,只能这样来写  

* {} :find的查询结果  
* \ :转义符-使得符号命令使用本身的含义  

* ; :语句结束

find /etc -name inittab -exec ls -l {} \; #在/etc下查找inittab文件并显示其详细信息 
find /home -user sax -exec rm -rf {} \; #删除用户sax所有的文件 
find /home -user sax -ok rm -rf {} \; #-ok连接符删除用户sax所有的文件,他会提示你是否确认 
find /etc -name init* -ok rm -rf {} \;
-ok和-exec行为一样，不过它会给出提示，是否执行相应的操作

```
root@ubuntu:/home/luohuihua# ls 
Downloads  examples.desktop  test  test.txt  下载  公共的  图片  文档  桌面  模板  视频  音乐
root@ubuntu:/home/luohuihua# find . -name test.txt
./test/test.txt
./test.txt
root@ubuntu:/home/luohuihua# find . -name test.txt -exec ls -l {} \;
-rw-r--r-- 1 root root 0 6月  28 11:25 ./test/test.txt
-rw-r--r-- 1 root root 0 6月  28 11:24 ./test.txt
root@ubuntu:/home/luohuihua# find . -name test.txt -exec rm -rf {} \;
root@ubuntu:/home/luohuihua# ls
Downloads  examples.desktop  test  下载  公共的  图片  文档  桌面  模板  视频  音乐
root@ubuntu:/home/luohuihua#
```

#### 4.2.12 which,whereis,locate,find的区别

**which：**常用于查找可直接执行的命令。只能查找可执行文件，该命令基本只在==$PATH==路径中搜索，查找范围最小，查找速度快。默认只返回第一个匹配的文件路径，通过选项 -a 可以返回所有匹配结果。
**whereis：**不只可以查找命令，其他文件类型都可以（man中说只能查命令、源文件和man文件，实际测试可以查大多数文件）。在$PATH路径基础上增加了一些系统目录的查找，查找范围比which稍大，查找速度快。可以通过 -b 选项，限定只搜索二进制文件。
**locate：**超快速查找任意文件。它会从linux内置的索引数据库查找文件的路径，索引速度超快。刚刚新建的文件可能需要一定时间才能加入该索引数据库，可以通过执行updatedb命令来强制更新一次索引，这样确保不会遗漏文件。该命令通常会返回大量匹配项，可以使用 -r 选项通过正则表达式来精确匹配。
**find：**直接搜索整个文件目录，默认直接从根目录开始搜索，建议在以上命令都无法解决问题时才用它，功能最强大但速度超慢。除非你指定一个很小的搜索范围。通过 -name 选项指定要查找的文件名，支持通配符。

### 4.3 grep、管道、重定向

#### 4.3.1 grep 命令（1）

grep 命令是一种强大的文本搜索工具，它能使用正则表达式搜索文本，并把匹配的行打印出来。
grep “python” filename  #在filename 文件中查找python，并且将结果打印出来
grep "python" filename filename1 filename2 #在多个文件中查找python，并且将结果打印出来

**-E 选项使用正则表达式**
grep -E "[a-c]+" filename #加上-E选项可以使用正则表达式

```
root@ubuntu:/home/luohuihua# grep home /etc/passwd
syslog:x:104:108::/home/syslog:/bin/false
luohuihua:x:1000:1000:luohuihua,,,:/home/luohuihua:/bin/bash
root@ubuntu:/home/luohuihua# grep -E "(home)|(sbin)" /etc/passwd
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
syslog:x:104:108::/home/syslog:/bin/false
luohuihua:x:1000:1000:luohuihua,,,:/home/luohuihua:/bin/bash
sshd:x:121:65534::/var/run/sshd:/usr/sbin/nologin
root@ubuntu:/home/luohuihua#
```

#### 4.3.2 grep 命令（2）

在多个文件中查找 grep "match_pattern" file_1 file_2 file_3 ...

```
root@ubuntu:/home/luohuihua# grep luohuihua /etc/passwd /etc/group
/etc/passwd:luohuihua:x:1000:1000:luohuihua,,,:/home/luohuihua:/bin/bash
/etc/group:adm:x:4:syslog,luohuihua
/etc/group:cdrom:x:24:luohuihua
/etc/group:sudo:x:27:luohuihua
/etc/group:dip:x:30:luohuihua
/etc/group:plugdev:x:46:luohuihua
/etc/group:lpadmin:x:113:luohuihua
/etc/group:luohuihua:x:1000:
/etc/group:sambashare:x:128:luohuihua
root@ubuntu:/home/luohuihua#
```

#### 4.3.3 grep 命令（3）

输出包含匹配字符串的行数 -n 选项：

```
root@ubuntu:/home/luohuihua# grep luohuihua -n /etc/passwd /etc/group
/etc/passwd:40:luohuihua:x:1000:1000:luohuihua,,,:/home/luohuihua:/bin/bash
/etc/group:5:adm:x:4:syslog,luohuihua
/etc/group:18:cdrom:x:24:luohuihua
/etc/group:21:sudo:x:27:luohuihua
/etc/group:23:dip:x:30:luohuihua
/etc/group:35:plugdev:x:46:luohuihua
/etc/group:52:lpadmin:x:113:luohuihua
/etc/group:67:luohuihua:x:1000:
/etc/group:68:sambashare:x:128:luohuihua
```

统计文件或者文本中包含匹配字符串的行数 -c 选项：

```
root@ubuntu:/home/luohuihua# grep luohuihua -c /etc/passwd /etc/group
/etc/passwd:1
/etc/group:8
root@ubuntu:/home/luohuihua#
```

#### 4.3.4 管道符 |

| 管道符的作用，将左边的输出当右边的输入
ps -ajx |grep ssh 将ps 命令的输出结果当grep的输入过滤

```
root@ubuntu:/home/luohuihua# ps -ajx | grep ssh
     1   1281   1281   1281 ?            -1 Ss       0   0:00 /usr/sbin/sshd -D
  1281   3162   3162   3162 ?            -1 Ss       0   0:00 sshd: luohuihua [priv]
  3162   3191   3162   3162 ?            -1 S     1000   0:03 sshd: luohuihua@pts/0
  4403   7495   7494   3192 pts/0      7494 S+       0   0:00 grep --color=auto ssh
```

显示 /etc 目录下的文件或目录的总数量

```
root@ubuntu:/home/luohuihua# ll /etc | grep -E ".*" -c 
235
```

#### 4.3.5 输出重定向： >

```
root@ubuntu:/home/luohuihua# ls
Downloads  examples.desktop  test  下载  公共的  图片  文档  桌面  模板  视频  音乐
root@ubuntu:/home/luohuihua# ls > test.txt
root@ubuntu:/home/luohuihua# ls
Downloads  examples.desktop  test  test.txt  下载  公共的  图片  文档  桌面  模板  视频  音乐
root@ubuntu:/home/luohuihua#
```

==> 将输出重定向到文件==
==ls > test.txt #将ls命令的输出重定向到test.txt文件==
test.txt的内容如下：

```
root@ubuntu:/home/luohuihua# cat test.txt
Downloads
examples.desktop
test
test.txt
下载
公共的
图片
文档
桌面
模板
视频
音乐
```

#### 4.3.6 输出重定向：追加 >>

追加内容
**>> 将输出重定向追加到文件
ls >> text.txt #将ls命令的输出追加到test.txt **

```
root@ubuntu:/home/luohuihua# echo "好的" >> test.txt
root@ubuntu:/home/luohuihua# cat test.txt
Downloads
examples.desktop
test
test.txt
下载
公共的
图片
文档
桌面
模板
视频
音乐
好的 
```

#### 4.3.7 输入重定向：<

```
root@ubuntu:/home/luohuihua# ls
Downloads  examples.desktop  test  test.txt  下载  公共的  图片  文档  桌面  模板  视频  音乐
root@ubuntu:/home/luohuihua# cat test.txt
/etc
root@ubuntu:/home/luohuihua# ls < test.txt
Downloads  examples.desktop  test  test.txt  下载  公共的  图片  文档  桌面  模板  视频  音乐
```

### 4.4 文件打包解包命令 

#### 4.4.1 文件打包

tar -cvf 打包文件名.tar 被打包的文件/路径
-c 创建一个新的归档
-v 详细地列出处理的文件
-f 使用归档文件 

```
root@ubuntu:/home/luohuihua# tar -cvf luohuihua.tar ./
root@ubuntu:/home/luohuihua# ls
Downloads  examples.desktop  luohuihua.tar  test  test.txt  下载  公共的  图片  文档  桌面  模板  视频  音乐
```

#### 4.4.2 文件解包

tar -xvf 打包过的文件.tar
-x 将打包过的文件解包
提示：-f 选项必须放在最后面

```apl
root@ubuntu:/home/luohuihua/test# pwd
/home/luohuihua/test
root@ubuntu:/home/luohuihua/test# ls
test.txt
root@ubuntu:/home/luohuihua/test# tar -cvf test.tar .  
./
tar: ./test.tar: 文件是归档文件；未输出
./test.txt
root@ubuntu:/home/luohuihua/test# ls
test.tar  test.txt
root@ubuntu:/home/luohuihua/test# rm -rf test.txt
root@ubuntu:/home/luohuihua/test# ls
test.tar
root@ubuntu:/home/luohuihua/test# tar -xvf test.tar
./
./test.txt
root@ubuntu:/home/luohuihua/test# ls
test.tar  test.txt 
```

### 4.5 压缩解压命令

#### 4.5.1 gzip命令

gzip一般跟tar一起使用，完成打包压缩
tar 只负责打包并为做压缩，使用-z 选项可以调用gzip压缩，完成打包压缩。
使用tar打包压缩的文件名，一般命名成 xxx.tar.gz 区别与其他文件。
压缩文件：
tar -zcvf py.tar.gz a.txt b.txt c.txt 
解压缩文件：
tar -zxvf py.tar.gz 
解压缩到指定路径
tar -zxvf 打包文件.tar.gz -C 目标路径        
-C 指定解压到那里，解压的目录必须存在

**案例**

```apl
root@ubuntu:/home/luohuihua/test# pwd
/home/luohuihua/test
root@ubuntu:/home/luohuihua/test# ls
a.txt  b.txt  c.txt
root@ubuntu:/home/luohuihua/test# tar -zcvf test.tar.gz a.txt b.txt c.txt
a.txt
b.txt
c.txt
root@ubuntu:/home/luohuihua/test# ls
a.txt  b.txt  c.txt  test.tar.gz
```

#### 4.5.2 bzip2命令

bzip2使用方式跟gzip差不多，也是由tar去调用，使用-j选项
bzip2 压缩的文件命名采用 xxx.tar.bz2 
压缩文件：
		tar -jcvf py.tar.bz2 a.txt b.txt c.txt 

```
root@ubuntu:/home/luohuihua/test# pwd
/home/luohuihua/test
root@ubuntu:/home/luohuihua/test# ls
a.txt  b.txt  c.txt
root@ubuntu:/home/luohuihua/test# tar -jcvf test.tar.bz2 a.txt b.txt c.txt 
a.txt
b.txt
c.txt
root@ubuntu:/home/luohuihua/test# ls
a.txt  b.txt  c.txt  test.tar.bz2
```

tar –jxvf test.tar.bz2

```
root@ubuntu:/home/luohuihua/test# ls
test.tar.bz2
root@ubuntu:/home/luohuihua/test# tar -jxvf test.tar.bz2 
a.txt
b.txt
c.txt
root@ubuntu:/home/luohuihua/test# ls
a.txt  b.txt  c.txt  test.tar.bz2
```

### 4.6 ubunt软件管理

#### 4.6.1 软件安装

==sudo apt install软件包==

如： 安装ssh服务

```
root@ubuntu:/home/luohuihua/test# sudo apt install ssh
```

#### 4.6.2 软件更新

==sudo apt upgrade [软件包]==  #如果没有软件包将会更新所有已安装的软件

如：更新ssh服务

```
root@ubuntu:/home/luohuihua/test# sudo apt upgrade ssh
```

#### 4.6.3 软件卸载

==sudo apt remove 软件包==

如：卸载ssh服务

```
root@ubuntu:/home/luohuihua/test# sudo apt remove ssh
```

### 4.7 vim编辑器（上）

#### 4.7.1 vim三种模式

命令模式
插入模式
末行模式

三种模式切换与关系

![image-20210828162251508](C:\Users\花城\AppData\Roaming\Typora\typora-user-images\image-20210828162251508.png)

#### 4.7.2 命令模式

使用vim打开文件的时候，就进到命令模式。
vim filename :打开或新建文件，并将光标置于第一行首
vim+n filename ：打开文件，并将光标置于第n行首
vim + filename ：打开文件，并将光标置于最后一行首
vim +/pattern filename：打开文件，并将光标置于第一个与pattern匹配的串处
vim -r filename ：在上次正用vi编辑时发生系统崩溃，恢复filename
vim filename....filename ：打开多个文件，依次进行编辑
命令模式下只能输入命令不能进行编辑，只有进入输入模式才能做文件编辑。

#### 4.7.3 移动光标命令

```
h ：光标左移一个字符
l ：光标右移一个字符
k或Ctrl+p：光标上移一行
j或Ctrl+n ：光标下移一行
w或W ：光标右移一个字至字首
b或B ：光标左移一个字至字首
0：（注意是数字零）光标移至当前行首
$：光标移至当前行尾
Ctrl+f 向文件尾翻一屏
Ctrl＋b 向文件首翻一屏
home 移动至行首
end 移动至行末
G 跳转至文档最末尾
gg 跳转至文档首行
nG n是一个数字，表示跳转至第几行。
```

### 4.8 vim编辑器（下）

#### 4.8.1 删除复制命令

```
dd 删除光标所在行
do 删除光标所在行光标前面的内容(数字0)
d$ 删除光标所在行光标末尾的内容
3 dd 删除光标所在行包含当前行后面3行内容（数字可以替换成自己想要删除的行数多少）
yy 复制
2 yy 复制光标所在行开始2行内容
p 粘贴，删除的内容也可以直接用p粘贴
u 撤销
ctrl r 反撤销
```

#### 4.8.2 进入输入模式

```
插入文本类命令：
i ：在光标前
I ：在当前行首
a：光标后
A：在当前行尾
o：在当前行之下新开一行
O：在当前行之上新开一行
```

#### 4.8.3 进入末行模式

在命令模式下，用户按":"键即可进入末行模式

**退出及保存：**
:q 退出
:q! 退出并不保存
:w 保存
:wq 退出并保存
:x 退出并保存

**查找替换：**
/string 在文本中查找string
n 下一个
N 上一个
:n1,n2s /word1/word2/g 将n1行到n2行中word1替换成word2, g表示全部替换，不加g则只替换匹配中的第一个
:1,$s /word1/word2/g 从第一行到最后一行寻找 word1 字符串，并将该字符串取代为 word2 (常用) 

:1,$s /word1/word2/gc 从第一行到最后一行寻找 word1 字符串，并将该字符串取代为 word2 ！且在取代前显示提示字符给用户确认 是否需要替换(常用)

#### 4.8.4 显示行号

：set nu 显示行号
：set nonu 取消显示行号

![image-20210828162929056](C:\Users\花城\AppData\Roaming\Typora\typora-user-images\image-20210828162929056.png)

#### 4.8.5 可视模式

v:按字符移动,选中文本
V:按行移动,选中文本可视模式可以配合d,y,>>,<<实现对文本块的删除,复制,左右移动

