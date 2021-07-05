# 基本语法

## 变量与内存

**计算机为何需要内存？**

CPU运⾏速度快

硬盘慢

**什么是变量？**

变量，是⽤于在内存中存放程序数据的容器，怎么理解呢？

计算机的最核⼼功能就是“计算”， 计算需要数据源，数据源要存在内存⾥，⽐如我要把⼩明的姓名、身

⾼、年龄信息存下来，后⾯程序会调⽤，怎么存呢，直接设置⼀个“变量名=值”， 就可以了

* **内存就像一个仓库**
* **变量，是用于在内存中存放程序数据的容器**

```python
name = "huacheng 花城"
age = 22
```

+ 变量名，变量值，内存地址
  + name与age是变量名
  + huacheng 花城与22是变量值
  + id(name)是name的内存地址
  
+ 变量定义&调用
  * 先定义后调用
  
+ **变量定义规则**

  1. 变量名只能是 字⺟、数字或下划线的任意组合

  2. 变量名的==第⼀个字符不能是数字==

  3. 以下关键字不能声明为变量名

     ```python
     ‘and’, ‘as’, ‘assert’, ‘break’, ‘class’, ‘continue’, ‘def’, ‘del’, ‘elif’, ‘else’,‘except’, ‘exec’, ‘finally’, ‘for’, ‘from’, ‘global’, ‘if’, ‘import’, ‘in’, ‘is’, ‘lambda’, ‘not’, ‘or’, ‘pass’, ‘print’,‘raise’, ‘return’, ‘try’, ‘while’, ‘with’, ‘yield’
     ```

+ 变量命名规范

  驼峰体

  ```python
  AgeOfBlackGirl = 56
  NumberOfStudents = 80
  ```

  ==下划线==

  ```python
  age_of_black_girl = 56
  number_of_students = 80
  ```

+ 变量的修改与删除

  ```python
  name = "huacheng"
  直接修改
  name = "花城"
  删除
  del name
  ```

  **常量**

  常量即指不变的量，如pai 3.141592653…, 或在程序运⾏过程中==不会改变的量==

  在Python中没有⼀个专⻔的语法代表常量，程序员约定俗成⽤变量名==全部⼤写代表常量==

  ```python
  MAX_USER_LIMIT = 1000
  ```

  > 在c语⾔中有专⻔的常量定义语法， const int count = 60; ⼀旦定义为常量，更改即会报错

## 基本数据类型

| 文本字符串类型 | str（存储文字） |
| ----------| ---- |
| 数值类型 | int\long\float |
| 序列列表类型： | ==list==, tuple, range |
| 映射(字典)类型： | dict（存储更多信息，加快查询速度） |
| 集合类型： | ==set==, frozenset（处理2组数据间的关系） |
| 布尔类型： | bool（处理逻辑判断） |
| 二进制字节类型： | ==bytes==, bytearray, memoryview（处理图片、视频、数据流等） |

### 数值类型

**int**（整型）

在64位系统上，整数的位数为64位，取值范围为-2^63^～2^63^-1， 

即-9223372036854775808～9223372036854775807

**long**（⻓整型）

跟C语⾔不同，Python的⻓整数没有指定位宽，即：Python没有限制⻓整数数值的⼤⼩，但实际上由于

机器内存有限，我们使⽤的⻓整数数值不可能⽆限⼤。

注意，⾃从Python2.2起，如果整数发⽣溢出，Python会⾃动将整数数据转换为⻓整数，所以如今在⻓

整数数据后⾯不加字⺟L也不会导致严重后果了。

> 注意：在Python3⾥不再有long类型了，全都是int

```python
>>> a= 2**64
>>> type(a) # type()是查看数据类型的⽅法
<class 'int'>
>>> b = 2**60
>>> type(b)
<class 'int'>
```

**float (**浮点型)

即⼩数

```python
>>> type(2.32)
<class 'float'>
```



### 字符串

**字符串str**

==**在Python中，加了引号的字符都被认为是字符串！**==

```python
>>> name = "Alex Li" #双引号
>>> age = "22" #只要加引号就是字符串
>>> age2 = 22 #int
>>>
>>> msg = '''My name is Alex, I am 22 years old!''' #3个引号也可以
>>>
>>> hometown = 'ShanDong' #单引号也可以
```

**字符串特性**

1. 不可修改

2. 有索引，可切片

   ```python
   >>> name = "huacheng"
   >>> name
   'huacheng'
   >>> type(name)
   <class 'str'>
   >>> name[6]   # 索引 从零开始
   'n'
   >>> name[2:4]  # 切块 只顾头不顾尾
   'ac'
   ```

**多行字符串**

```python
>>> tfx = '''
... hello
... my name is hua cheng
... good at python,and making money
... '''
>>> tfx
'\nhello\nmy name is hua cheng\ngood at python,and making money\n'
>>> print(tfx)

hello
my name is hua cheng
good at python,and making money

>>>
```

**字符串拼接**

```python
>>> school = "安徽理工大学"
>>> Motto = "校训是团结、奋进、博学、奉献"
>>> school
'安徽理工大学'
>>> Motto
'校训是团结、奋进、博学、奉献'
>>> school + Motto   #相加其实就是简单拼接
'安徽理工大学校训是团结、奋进、博学、奉献'
>>>
```

### **字符串内引用外部变量**

* %s       # 旧版本
* f           # 新版本

2.的版本

```python
name = "Rabbit"
age = 22
hobby = "basketball"

msg = '''
------------%s information------------
name: %s
age: %s
hobby: %s
'''%(name,name,age,hobby)

print(msg)

# %s str
# %d digit
# %f float
```

运行结果

```
------------Rabbit information------------
name: Rabbit
age: 22
hobby: basketball
```

​	3.的版本

```python
name = "Rabbit"
age = 22
hobby = "basketball"

msg = f'''
------------{name} information------------
name: {name}
age:{age}
hobby: {hobby}
------------end------------
'''

print(msg)
```

运行结果

```
name: Rabbit
age:22
hobby: basketball
------------end------------

```



### 布尔类型bool

布尔类型很简单，就两个值 ，⼀个True(真)，⼀个False(假), 它的作⽤主要是⽤作逻辑判断

```python
score = 560
qing_hua_score_benchmark = 680
if score >= qing_hua_score_benchmark: # True
	print("congratulations.你上了北大......")

else: # False
	print("你只能上北大青鸟......")
```



### 列表类型list

```python
>>> girl_list = []
>>> type(girl_list)
<class 'list'>
>>> girl_list = ["Monky","Celina","Coffee","XiaoYun","BlackDirl"]
>>> girl_list
['Monky', 'Celina', 'Coffee', 'XiaoYun', 'BlackDirl']
>>> girl_list[3]
'XiaoYun'
>>> girl_list[3] = "小云"    #可以直接更改
>>> girl_list
['Monky', 'Celina', 'Coffee', '小云', 'BlackDirl']
>>>
>>> for girl in girl_list:
...    print(f"my dear darling...{girl},happy new year,I miss you.") # 注意一定要有空格
...
my dear darling...Monky,happy new year,I miss you.
my dear darling...Celina,happy new year,I miss you.
my dear darling...Coffee,happy new year,I miss you.
my dear darling...小云,happy new year,I miss you.
my dear darling...BlackDirl,happy new year,I miss you.
>>>
```



* **列表的操作**

  * ==增== girl_list.append(x), girl_list.insert(i,x)

    ```python
    >>> girl_list.append("GangNiang")
    >>> girl_list
    ['Monky', 'Celina', 'Coffee', '小云', 'BlackDirl', 'GangNiang']
    >>> girl_list.insert(4,"Rabbit")
    >>> girl_list
    ['Monky', 'Celina', 'Coffee', '小云', 'Rabbit', 'BlackDirl', 'GangNiang']
    ```

  * ==改== girl_list[1] = "Good boy"

    ```python
    >>> girl_list[4]
    'Rabbit'
    >>> girl_list[4] = "亚历山大Rabbit"
    >>> girl_list
    ['Monky', 'Celina', 'Coffee', '小云', '亚历山大Rabbit', 'BlackDirl', 'GangNiang']
    ```

  * ==查== girl_list.index(x)

    ```python
    >>> girl_list.index("GangNiang")
    6
    >>> girl_list[6]
    'GangNiang'
    >>>
    >>> g_index = girl_list.index("GangNiang")
    >>>
    >>> girl_list[g_index]
    'GangNiang'
    ```

  * ==删== del girl_list [i]           girl_list.remove(x)

    ```python
    >>> girl_list
    ['Monky', 'Celina', 'Coffee', '小云', '亚历山大Rabbit', 'BlackDirl', 'GangNiang']
    >>> del girl_list[4]
    >>> girl_list
    ['Monky', 'Celina', 'Coffee', '小云', 'BlackDirl', 'GangNiang']
    >>> girl_list.remove("小云")
    >>> girl_list
    ['Monky', 'Celina', 'Coffee', 'BlackDirl', 'GangNiang']
    ```

    

  * 切片、嵌套

    切片

    ```python
    >>> girl_list
    ['Monky', 'Celina', 'Coffee', 'BlackDirl', 'GangNiang']
    >>> girl_list[0:3]
    ['Monky', 'Celina', 'Coffee']
    >>> girl_list.append("Racheal")
    >>> girl_list.append("ShanShan")
    >>> girl_list.append("XiaoMin")
    >>>
    >>> girl_list
    ['Monky', 'Celina', 'Coffee', 'BlackDirl', 'GangNiang', 'Racheal', 'ShanShan', 'XiaoMin']
    >>>
    >>> girl_list[-1]
    'XiaoMin'
    >>> girl_list[-2]
    'ShanShan'
    >>> girl_list[-2:-1]
    ['ShanShan']
    >>> girl_list[-2:]
    ['ShanShan', 'XiaoMin']
    >>> girl_list[:3]
    ['Monky', 'Celina', 'Coffee']
    >>> girl_list
    ['Monky', 'Celina', 'Coffee', 'BlackDirl', 'GangNiang', 'Racheal', 'ShanShan', 'XiaoMin']
    >>> girl_list[0:5:2]   # 第三个2是步长
    ['Monky', 'Coffee', 'GangNiang']
    ```

    嵌套

    ```python
    >>> girl_list.append(["JunJun",168,48,23])
    >>> girl_list
    ['Monky', 'Celina', 'Coffee', 'BlackDirl', 'GangNiang', 'Racheal', 'ShanShan', 'XiaoMin', ['JunJun', 168, 48, 23]]
    >>> girl_list[-1]
    ['JunJun', 168, 48, 23]
    >>> girl_list[-1][2]
    48
    >>> girl_list[-1][2] = 52
    >>> girl_list
    ['Monky', 'Celina', 'Coffee', 'BlackDirl', 'GangNiang', 'Racheal', 'ShanShan', 'XiaoMin', ['JunJun', 168, 52, 23]]
    ```

    

## 常用运算符

**Python 算术运算符**

算术运算符与数值一起使用来执行常见的数学运算：

| 运算符 | 名称                        | 实例   |
| ------ | --------------------------- | ------ |
| +      | 加                          | x + y  |
| -      | 减                          | x - y  |
| *      | 乘                          | x * y  |
| /      | 除                          | x / y  |
| %      | 取模                        | x % y  |
| **     | 幂     2**8   2的8次方      | x ** y |
| //     | 地板除（取整除）   9//2   4 | x // y |

```python
>>> for i in range(20):
...     if i % 2 != 0:   # 奇数
...       print(i)
...
1
3
5
7
9
11
13
15
17
19
>>>
```



**Python 赋值运算符**

赋值运算符用于为变量赋值：

| 运算符 | 实例    | 等同于     |
| ------ | ------- | ---------- |
| =      | x = 5   | x = 5      |
| +=     | x += 3  | x = x + 3  |
| -=     | x -= 3  | x = x - 3  |
| *=     | x *= 3  | x = x * 3  |
| /=     | x /= 3  | x = x / 3  |
| %=     | x %= 3  | x = x % 3  |
| //=    | x //= 3 | x = x // 3 |
| **=    | x **= 3 | x = x ** 3 |
| &=     | x &= 3  | x = x & 3  |
| \|=    | x \|= 3 | x = x \| 3 |
| ^=     | x ^= 3  | x = x ^ 3  |
| >>=    | x >>= 3 | x = x >> 3 |
| <<=    | x <<= 3 | x = x << 3 |

**Python 比较运算符**

比较运算符用于比较两个值：

成立是True

不成立是False

| 运算符 | 名称       | 实例   |
| ------ | ---------- | ------ |
| ==     | 等于       | x == y |
| !=     | 不等于     | x != y |
| >      | 大于       | x > y  |
| <      | 小于       | x < y  |
| >=     | 大于或等于 | x >= y |
| <=     | 小于或等于 | x <= y |

**Python 逻辑运算符**

逻辑运算符用于组合条件语句：

| 运算符 | 描述                                    | 实例                  |
| ------ | --------------------------------------- | --------------------- |
| and    | 如果两个语句都为真，则返回 True。       | x > 3 and x < 10      |
| or     | 如果其中一个语句为真，则返回 True。     | x > 3 or x < 4        |
| not    | 反转结果，如果结果为 true，则返回 False | not(x > 3 and x < 10) |

```python
>>> 3 > 5 and 3 < 2 or 3 > 33 or 3 > 2.9 or 3 < 8 and 3 == 9
True   # and的优先级大于or，先算and
>>>
```



**Python 身份运算符**

身份运算符用于比较对象，不是比较它们是否相等，但如果它们实际上是同一个对象，则具有相同的内存位置：

| 运算符 | 描述                                            | 实例       |
| ------ | ----------------------------------------------- | ---------- |
| in     | 如果对象中存在具有指定值的序列，则返回 True。   | x in y     |
| not in | 如果对象中不存在具有指定值的序列，则返回 True。 | x not in y |

```python
>>> girl_list
['Monky', 'Celina', 'Coffee', 'BlackDirl', 'GangNiang', 'Racheal', 'ShanShan', 'XiaoMin', ['JunJun', 168, 52, 23]]
>>> 'Monky' in girl_list
True
>>> 'Monky' not in girl_list
False
>>>
```

**Python 位运算符**

位运算符用于比较（二进制）数字：

| 运算符 | 描述                 | 实例                                                     |
| ------ | -------------------- | -------------------------------------------------------- |
| &      | AND                  | 如果两个位均为 1，则将每个位设为 1。                     |
| \|     | OR                   | 如果两位中的一位为 1，则将每个位设为 1。                 |
| ^      | XOR                  | 如果两个位中只有一位为 1，则将每个位设为 1。             |
| ~      | NOT                  | 反转所有位。                                             |
| <<     | Zero fill left shift | 通过从右侧推入零来向左移动，推掉最左边的位。             |
| >>     | Signed right shift   | 通过从左侧推入最左边的位的副本向右移动，推掉最右边的位。 |



## 读取用户指令

```python
name = input("Your name:").strip()       # 加上.strip()有空格会忽略掉
# age = int(input("Age:"))      #   强制转化为整数
age = input("Age:")
if age.isdigit():        #   是否是整数的判断
	age = int(age)
else:
	print("错误地输入...")
	exit()
print(type(age))
hobby = input("Your hobby:")
job = input("Your job:")


msg = f'''
-------------{name}--------------
Name:{name}
Age:{age} , wow still young , in {30-age} you will 30
hobby:{hobby}
job:{job}
-----------end---------------
'''

print(msg)


```

运行结果

```python
Your name:Rabbit
Age:22
<class 'int'>
Your hobby:basketball
Your job:CEO

-------------Rabbit--------------
Name:Rabbit
Age:22 , wow still young , in 8 you will 30
hobby:basketball
job:CEO
-----------end---------------


进程已结束，退出代码为 0
```

## 流程控制

**单分支**

```python
loneliness = 75
if loneliness > 70:
	print("I am lonely , go to do massage...")
```

**双分支**

```python
budget = 1300
if budget >= 1300:
	print("可以尝试1298的，服务好...")
else:
	print("688的性价比高......")
```

**多分支**

```python
budget = 1000
if budget < 500:
 print("这个预算没得选...")
elif budget < 800:
 print("6分楼凤⽔平...")
elif budget < 1500:
 print("7分还不错")
elif budget < 2000:
 print("深圳...")
elif budget < 3000:
 print("⾹..")
```

**嵌套分支**

注意if嵌套最多不超过4层，不是不⾏，⽽是层级太多会使你的程序笨拙，后续不易扩展，相当于把代码

写死了。

```python
loneliness = 80
money = 1000
if loneliness > 70 :
 print("very loneliness...")
 if money < 1000:
 print("loneliness...")
```



## 今日作业

* 作业一: 猜年龄游戏

  ```python
  # -*- coding:utf-8 -*-
  """
  作者:花城
  日期:2021年07月04日
  """
  
  age_of_black_girl = 25
  print("你猜猜黑姑娘的年龄是多少：")
  for age in range(100):
      age = int(input("black_girl age:"))
      if age < age_of_black_girl:
          print("猜的太小了，往大猜试试...")
      elif age > age_of_black_girl:
          print("猜的太大了，黑姑娘有这么老吗？往小猜试试...")
      elif age == age_of_black_girl:
          print("恭喜你，猜对了...")
          exit()
  
  ```

* 作业二: 写一段程序，读取用户输入的工资，根据工资多少打印相应的文字

  ```
  ```

  
