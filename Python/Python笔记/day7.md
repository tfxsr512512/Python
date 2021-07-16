# 文件处理与编码转换

## ⼀、 Python ⽂件操作

对⽂件的操作有2种，文本文件、二进制⽂件（视频、图⽚等）

### **1.1 open**⽅法基本使⽤

```python
open(file, mode='r', encoding=None):
```

几种打开模式

```python
'r' open for reading (default) (只读模式)
'w' open for writing, truncating the file first（写模式，如果⽂件 在，先清空【危险】）
'x' create a new file and open it for writing（创建模式：如果⽂件在，会报错）
'a' open for writing, appending to the end of the file if it exists（⽇志，追加）
'b' binary mode（2进制模式）
't' text mode (default) （⽂本）
'+' open a disk file for updating (reading and writing)
```

**The default mode is 'rt' (open for reading text).** 默认模式

⼀个⽂件对象被open⽅法创建后，这个对象可⽤的有下⾯这些，我们先⼤体过⼀下，后边还会细讲每个⽅法：

```
close   	关闭⽂件
closed  	查看⽂件是否已关闭
encoding 	返回⽂件的编码
flush 		把缓存⾥的写⼊的数据强制刷新硬盘
isatty 		返回⽂件是否是'interactive'数据流,⽐如是个命令⾏终端，（在unix系统，⼀切皆⽂件）
mode 		返回当前⽂件模式
name 		返回⽂件名
read 		读指定⻓度的内容，f.read(1024) 读1024字节, 不指定参数的话，就读所有内容
readable 	⽂件是否可读
readline 	读⼀⾏
readlines 	读所有，每⾏列表形式返回
seek 		把光标移到指定位置
seekable 	该⽂件光标是否可移动
tell 		返回当前光标位置
truncate 	截断⽂件, f.truncate(100), 从⽂件 开头截断100个字符，后边的都扔掉
writable 	是否可写
write 		写内容
writelines 	把⼀个列表写⼊，每个元素是⼀⾏
```

f.flush 把缓存⾥的写⼊的数据强制刷新硬盘

```python
>>> f = open("flush_test.txt","w")
>>> f.write("hello world! welcome to China!\n")
31
>>> f.write("hello world! welcome to China!\n") # flush_test.txt里面还没有任何东西
31
>>> f.flush() # 强制刷新硬盘
```



### **1**、创建模式：创建⽂件

```python
f = open("contacts.txt", 'w') # 创建⼀个⽂件对象（⽂件句柄），存为变量f 
f.write("alex 133332") # 写⼊
f.write("alex 133332") f.close() # 关闭这个⽂件
f.write('dddd') # 关闭后，没办法再写⼊了
```

![](D:\Python\图片\1.png)

**注意：**在 w 模式是创建⼀个⽂件 ，但若该⽂件 已存在，则会清空原⽂件，如果不⾏清空原⽂件，安全起⻅，⽤ 

x 模式，若原⽂件存在，会报错，不会直接清空它

```python
Traceback (most recent call last):
 File "/Users/alex/PycharmProjects/alex96_daydayup/day6/⽂件TEST.py", line 1, in <module>
 f = open("contacts.txt", 'x') # 创建⼀个⽂件对象，存为变量f
FileExistsError: [Errno 17] File exists: 'contacts.txt'
```

**写入多行**

⽣成⼀个随机密码⽂件

```python
import random
import string
names = ["alex",'jack','rain','black_girl','peiqi'] 
f = open("password.txt", 'w') # 创建⼀个⽂件对象，存为变量f
for i in names:
     passwd = random.sample(string.ascii_letters + string.digits, 8) # ⽣成8位随机字符
     line = f"{i}:{''.join(passwd)}\n" # ⼀定要加上\n换⾏符号才会换⾏
     f.write(line) f.close()
```

password.txt

```
alex:amZsGdeM
jack:dGlMNgAB
rain:70E2crty
black_girl:SlH85rjp
peiqi:ZeCtVI4g
```

### **1.2** 读模式：循环读取文件&查找

对 `model_contacts.txt `进⾏循环

```
姓名 地区 身⾼ 体重 电话
况咏蜜 北京 171 48 13651054608
王⼼颜 上海 169 46 13813234424
⻢纤⽻ 深圳 173 50 13744234523
乔亦菲 ⼴州 172 52 15823423525
罗梦⽵ 北京 175 49 18623423421
刘诺涵 北京 170 48 18623423765
岳妮妮 深圳 177 54 18835324553
贺婉萱 深圳 174 52 08933434452
叶梓萱 上海 171 49 18042432324
杜姗姗 北京 167 49 13324523342
```

**按行读取&循环**

```python
f = open("model_contacts.txt", encoding='utf-8') # 默认`rt`模式
print(f.readline()) # 读第1⾏
print(f.readline()) # 读第2⾏
print(f.readline()) # 读第3⾏
print('----循环读后⾯的-----')
for line in f:
 print(f.readline())
```

打开⽂件后，光标位置在⽂件开头，每读⼀⾏，光标向下移动⼀⾏，因此可以⼀⾏⾏的往后读，已读了的内容不会重复被读取

**读取指定字符个数**

```python
f = open("model_contacts.txt",) # 默认`rt`模式
print(f.read(3)) # 读取3个字符
```

**注意：**在⽂本模式下，这个3是代表3个字符，在2进制模式，这个3是指3个字节

**文件里查找内容**

要想在⽂件内找某个词，并打印出所在⾏，只能循环⼀遍⽂件，每⾏依次判断⼀下

```python
f = open("model_contacts.txt")
for line in f:
 if "梦⽵" in line:
 print(line)
```

### **1.3** **追加模式**

只会往⽂件最后追加，⼀般⽤于写⽇志的场景

```python
f = open("model_contacts.txt", "a", encoding='utf-8') 
f.write("⿊姑娘 北京 165 50 18834252322\n") 
f.write("⿊姑娘2 北京 165 50 18834252322\n")
```

注意： 追加模式，即使通过f.seek()把光标移到其它位置 ，再f.write()的时候 ，依然是写到最后的、

但是f.seek(10),然后再f.truncate()，会实现⽂件截断，只保留10个字符。



### **1.4** **修改**

`r+`是修改模式

直接调⽤f.write(),会从开头开始写, 然后会往后覆盖... 如果只覆盖了后边某个⽂字的⼀半，就会出现 乱码

**seek** **是移动字节**

**tell** **返回字节数**

想把数据源⾥的`伍小仪`换成`刘翠花TracyLiu`, 怎么搞？

```
⻢纤⽻ 深圳 173 50 13744234523
乔亦菲 ⼴州 172 52 15823423525
伍⼩仪 深圳 175 49 18623423421
刘诺涵 北京 170 48 18623423765
岳妮妮 深圳 177 54 18835324553
```



如果能移动到伍小仪的位置，直接从那个位置替换整⾏是可以的。

但问题就在于，你不知道她所在的位置， 注意，`f.seek(100)`移动到第100个字节的位置 ， 但是你的⽂件是utf8的编码，每个中⽂占3个字符，⾥⾯还掺杂了数字、空格、换行，你不可能⼀个个的字符换算成字节的⻓度的。你说我通过循环到这一行，然后`f.tell()`不就可以知道她的位置 了么？

理论上可以，但实际也不行，循环时，`f.tell()`被禁⽤啦,(因为⽂件循环是⽤的迭代器写的,这个后边会学)

所以怎么办呢？

你只能，把⽂件先读到内存，在内存⾥改掉这个数据，然后重写回⽂件 。

```python
f = open("model_contacts.txt", "r+")
data = f.read() # 先把⽂件内容全读到内存
data_new = data.replace("伍⼩仪","刘翠花TracyLiu") # 替换
f.seek(0) # 光标移到0 f.truncate() # 清空
f.write(data_new) # 写⼊新内容
f.close()
```

```python
f = open("model_contacts.txt", "r+", encoding='utf-8')

# 1. 先把文件内容加载到内存
# 2. 替换要改的部分
# 3. 清空原文件内容
# 4. 把新内容写回去

data = f.read()
# 备份
back_file = open("model_contacts.txt.bak", "w", encoding='utf-8')
back_file.write(data)
back_file.close()

data_new = data.replace("刘翠花TracyLiu", "伍小仪", )
f.seek(0)
f.truncate()  # 清空原文件
f.write(data_new)
f.close()

import os

os.remove("model_contacts.txt.bak")

```



### 1.5 删除

```python
import os
os.remove("model_contacts.txt")
```

### **1.6** **处理不同编码的文件**

#### 创建模式

```python
f = open("my_first_file2.txt", "x", encoding='utf-8') 
f.write("My name is Alex, 哈哈哈\n")
f.write("昨天下班去酒吧...\n")
f.write("有个9分的漂亮学生跟我们一起玩.")

f.close()  # 关闭

```

#### 处理二进制文件

**编码**

```python

# f = open("qrcode.png", 'rb')
# print(f.read())

# 字节类型
f = open("2进制写文件.txt",'wb') # 只能以2进制形式写...
s = "我是Alex金角大王" # unicode 要编码成utf-8后才能存
# s_gbk = s.encode("gbk")
# print("gbk:",s_gbk)
# f.write(s_gbk)
f.write(s.encode("utf-8")) # 编码后，数据变成字节类型

```

**解码**

```python
f = open("2进制写文件.txt",'rb')
data = f.read()
print(data.decode("utf-8"))
```

#### **编码转换**

在什么情况下会⽤到编码转换呢？

以后我们在开发⽹络程序时，如果远程⼀台电脑发送过来的消息是GBK的， 你的电脑是utf-8的，你想把对⽅的消息正确显示，就要按gbk来 decode 解码.

![](D:\Python\图片\2.png)

