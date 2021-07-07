# 字符串方法精讲

## 1. 字符串的定义

 	1. 字符串是由零个或多个字符组成的有限序列
 	2. 不可变、有索引、可切片、可遍历

## 2. 一切字符串皆对象

## 3. 字符串类型方法

	### 1. 格式化方法

```python
>>> a ="jack li"
>>> a
'jack li'
```

a.capitalize( ）⾸字符改成⼤写

```python
>>> a ="jack li"
>>> a
'jack li'
>>> a.capitalize()
'Jack li'
```

a.casefold( ）为了⽅便字符串之前对⽐，都改成⼩写

```python
>>> a1 = "Jack Li"
>>> a1
'Jack Li'
>>> a1 == a
False
>>> a1.casefold() == a
True
```

a.center( ）字符串两边填充

```python
>>> a.center(50,'-')
'---------------------jack li----------------------'
```

a.expandtabs( ）

```python
>>> s = "alex\tli"
>>> s
'alex\tli'
>>> print(s)
alex    li
>>> s.expandtabs()
'alex    li'
>>> s.expandtabs(20)
'alex                li'
```

a.ljust( )字符串左边填充

a.rjust( )字符串右填充

```python
>>> a.ljust(30,'-')
'jack li-----------------------'
>>> a.rjust(30,'-')
'-----------------------jack li'
>>>
```

a.lower( )全变⼩写

```python
>>> a = "Alex Good"
>>> a
'Alex Good'
>>> a.lower()
'alex good'
```

a.swapcase( )⼤⼩写互换

```python
>>> a.swapcase()
'aLEX gOOD'
```

a.title( ) 改成标题，即每个单词⾸字⺟⼤写

```python
>>> a = "rabbit is a tuzi"
>>> a.title()
'Rabbit Is A Tuzi'
```

a.upper( )改⼤写

```python
>>> a.title()
'Rabbit Is A Tuzi'
>>> a = a.title()
>>> a
'Rabbit Is A Tuzi'
>>> a.upper()
'RABBIT IS A TUZI'
```

a.zfill( ) 字符串空的地⽅填0

```python
>>> a.zfill(50)
'0000000000000000000000000000000000Rabbit Is A Tuzi'
```

a.strip( )两边去死⽪

```python
>>> a = " jack ma \n "
>>> a
' jack ma \n '
>>> a.strip()
'jack ma'
>>>
```

a.lstrip( )左边去死⽪

a.rstrip( )右边去

```python
>>> a.lstrip()
'jack ma \n '
>>> a.rstrip()
' jack ma'
```

a.format( )引⽤外部变量

靠变量

```python
>>> msg = "my name is {name}, I am {age} years old. "
>>> msg.format(name = "Jack", age = 23)
'my name is Jack, I am 23 years old. '
```

靠位置0,1,2

```python
>>> msg1 = "my name is {0}, I am {1} years old. "
>>> msg1.format("Rabbit", 23)
'my name is Rabbit, I am 23 years old. '
```



### 2. 判断方法

a.startswith( ) 开头判断

```python
>>> a
'Rabbit boy'
>>> a.startswith("R")
True
>>> a.startswith('R')
True
>>> a.startswith("Rab")
True
```

a.endswith( ) 结尾判断

```python
>>> a.endswith("y")
True
>>> a.endswith("ay")
False
>>> a.endswith("boy")
True
```

a.isalnum( ）是不是字⺟or数字

```python
>>> a2 = "Rabbit22"
>>> a2.isalnum()
True
>>> a2.isalpha()
False
```

a.isalpha( ）是不是字⺟

```python
>>> a2.isalpha()
False
```

a.isascii(） 暂不⽤，没学

```

```

a.isdecimal( ）不要⽤， 垃圾

a.isdigit( ）是不是数字

```python
>>> n = "23"
>>> n.isdigit()
True
>>> n = "23.6"
>>> n.isdigit()
False
```

a.isidentifier( ）是不是合法的可以做变量的名字

```python
>>> s = "ddd"
>>> s
'ddd'
>>> s.isidentifier()
True
>>> s = "1"
>>> s.isidentifier()
False
```

a.islower( ）

```python
>>> s = "Rabbit"
>>> s.islower()
False
```

a.isnumeric( ）是不是数字，跟isdigit有何关系 呢？

```python
>>> age = "22"
>>> age.isnumeric()
True
>>> age1 = "二十二"
>>> age1.isnumeric()
True
```

a.isprintable( ）是否可打印

```python
>>> age.isprintable()
True
```

a.isspace( ）是不是空格

```python
>>> ' '.isspace()
True
```

a.istitle( ）

```python
>>> name = "The First"
>>> name.istitle()
True
```

a.isupper( ）

```python
>>> name.isupper()
False
```

### 3. 查、改、计数、替换

a.find( ）

a.rfind( ）

```python
>>> name = "The First Chairman In China"
>>> name
'The First Chairman In China'
>>> name.find("F")
4
>>> name.find("i")
5
>>> help(name.find)
Help on built-in function find:

find(...) method of builtins.str instance
    S.find(sub[, start[, end]]) -> int

    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.

    Return -1 on failure.

>>> name.find("i", 6, -1)
13
>>> name.rfind("i")
24
>>> name.rfind("in")
24
```

a.index( ）

a.rindex( ）

```python
>>> name.find("A")
-1
>>> name.index("F")
4
>>> name.index("A")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
>>> name.rindex("F")
4
```

a.count( ）

```python
>>> name.count("i")
3
>>> name.count("i", 6, 13)
0
>>> name.count("i", 6, 15)
1
```

a.rsplit( ）

```python
>>> name.split(maxsplit=2)
['The', 'First', 'Chairman In China']
>>> name.rsplit()
['The', 'First', 'Chairman', 'In', 'China']
>>> name.rsplit(maxsplit=2)
['The First Chairman', 'In', 'China']
>>>
```

a.split( ）

```python
>>> name.split()
['The', 'First', 'Chairman', 'In', 'China']
>>> name.split("i")
['The F', 'rst Cha', 'rman In Ch', 'na']
```

a.splitlines( ）

```python
>>> msg = "hello,\neveryone\n haha\nddd"
>>> msg
'hello,\neveryone\n haha\nddd'
>>> print(msg)
hello,
everyone
 haha
ddd
>>> msg.splitlines()
['hello,', 'everyone', ' haha', 'ddd']
```

a.removeprefix( ）去掉前面的

a.removesuffix( ）去掉后面的

```python
>>> name
'The First Chairman In China'
>>> name.removeprefix("The")
' First Chairman In China'
>>> name.removesuffix("The")
'The First Chairman In China'
>>> name.removesuffix("ina")
'The First Chairman In Ch'
```

a.replace( ）

```python
>>> name.replace("i","A")
'The FArst ChaArman In ChAna'
>>> name.replace("i","A",2)
'The FArst ChaArman In China'
```



### 4. 特殊变态方法

a.encode( ）字符编码相关，还没学

a.join( ）把列表 转成字符串，每个元素拼接起来，按指定格式

```python
>>> names = ["Monky","Yu Ge","Xue Fei"]
>>> names
['Monky', 'Yu Ge', 'Xue Fei']
>>> "-".join(names)
'Monky-Yu Ge-Xue Fei'
>>> " ".join(names)
'Monky Yu Ge Xue Fei'
>>> ",".join(names)
'Monky,Yu Ge,Xue Fei'
```

a.maketrans( ）⽣成密码本

a.translate( ）加密

```python
>>> source = "abcdefghi"
>>> output = "012345678"
>>> str.maketrans(source,output)
{97: 48, 98: 49, 99: 50, 100: 51, 101: 52, 102: 53, 103: 54, 104: 55, 105: 56}
>>> password_table = str.maketrans(source,output)
>>> msg = "Hello baby"
>>> msg
'Hello baby'
>>> msg.translate(password_table)
'H4llo 101y'
>>> msg
'Hello baby'
>>>
>>> import string
>>> string.digits
'0123456789'
>>> string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.printable
'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
>>>
>>> source2 = string.printable
>>>
>>> string.printable[::-1]   # 反转
'\x0c\x0b\r\n\t ~}|{`_^]\\[@?>=<;:/.-,+*)(\'&%$#"!ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba9876543210'
>>> output2 = string.printable[::-1]
>>>
>>> passwd_tab2 = str.maketrans(source2,output2)
>>> passwd_tab2
{48: 12, 49: 11, 50: 13, 51: 10, 52: 9, 53: 32, 54: 126, 55: 125, 56: 124, 57: 123, 97: 96, 98: 95, 99: 94, 100: 93, 101: 92, 102: 91, 103: 64, 104: 63, 105: 62, 106: 61, 107: 60, 108: 59, 109: 58, 110: 47, 111: 46, 112: 45, 113: 44, 114: 43, 115: 42, 116: 41, 117: 40, 118: 39, 119: 38, 120: 37, 121: 36, 122: 35, 65: 34, 66: 33, 67: 90, 68: 89, 69: 88, 70: 87, 71: 86, 72: 85, 73: 84, 74: 83, 75: 82, 76: 81, 77: 80, 78: 79, 79: 78, 80: 77, 81: 76, 82: 75, 83: 74, 84: 73, 85: 72, 86: 71, 87: 70, 88: 69, 89: 68, 90: 67, 33: 66, 34: 65, 35: 122, 36: 121, 37: 120, 38: 119, 39: 118, 40: 117, 41: 116, 42: 115, 43: 114, 44: 113, 45: 112, 46: 111, 47: 110, 58: 109, 59: 108, 60: 107, 61: 106, 62: 105, 63: 104, 64: 103, 91: 102, 92: 101, 93: 100, 94: 99, 95: 98, 96: 97, 123: 57, 124: 56, 125: 55, 126: 54, 32: 53, 9: 52, 10: 51, 13: 50, 11: 49, 12: 48}
>>>
>>>
>>> msg = "Hello baby, I miss you so much, want to see you, but afraid the female tiger find out ..."
>>>
>>> msg.translate(passwd_tab2)
'U\\;;.5_`_$q5T5:>**5$.(5*.5:(^?q5&`/)5).5*\\\\5$.(q5_()5`[+`>]5)?\\5[\\:`;\\5)>@\\+5[>/]5.()5ooo'
>>> msg
'Hello baby, I miss you so much, want to see you, but afraid the female tiger find out ...'
>>> encrypt_msg = msg.translate(passwd_tab2)   # 加密
>>> encrypt_msg
'U\\;;.5_`_$q5T5:>**5$.(5*.5:(^?q5&`/)5).5*\\\\5$.(q5_()5`[+`>]5)?\\5[\\:`;\\5)>@\\+5[>/]5.()5ooo'
>>> passwd_tab3 = str.maketrans(output2,source2)    # 解密
>>> encrypt_msg .translate(passwd_tab3)
'Hello baby, I miss you so much, want to see you, but afraid the female tiger find out ...'
>>>
```



## 4. 练习、统计字符个数小程序

```python
while True:
    msg = input(">:").strip()
    if not msg:
        continue   # if len(msg) == 0
    # 'Hello baby, I miss you so much, want to see you, but afraid the female tiger find out ...'
    str_count = 0
    int_count = 0
    space_count = 0
    special_count = 0
    for i in msg:
        if i.isalpha():
            str_count += 1
        elif i.isdigit():
            int_count += 1
        elif i.isspace():
            space_count += 1
        else:
            special_count += 1
    print(f"str count:{str_count}, int count:{int_count}, space count:{space_count}, special count:{special_count}.")
```





