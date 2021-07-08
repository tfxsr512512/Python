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
# 二、列表方法精讲

列表特性

有序

有索引、可切⽚、可遍历

```python
>>> li
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## **2.1** **增**

names.append()

names.insert()

```python
>>> li
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> li.append(10)
>>> li
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> li.insert(4,33)
>>> li
[0, 1, 2, 3, 33, 4, 5, 6, 7, 8, 9, 10]
```

## **2.2** **删除**

names.clear( ) 将列表清空

names.pop( ）默认删除最后一个

names.remove(）删除从左数第一个

del names 删除指定一个

```python
>>> li.clear()
>>> li
[]
>>> li = list()
>>> type(li)
<class 'list'>
>>> a = "Rabbit22"
>>> li = list(a)    # 直接将字符串转化为列表
>>> li
['R', 'a', 'b', 'b', 'i', 't', '2', '2']
>>> li.pop()
'2'
>>> li
['R', 'a', 'b', 'b', 'i', 't', '2']
>>> li = list(a)
>>> li
['R', 'a', 'b', 'b', 'i', 't', '2', '2']
>>> li.pop(-3)   # 删除倒数第三个
't'
>>> li
['R', 'a', 'b', 'b', 'i', '2', '2']
>>> li.remove("2")
>>> li
['R', 'a', 'b', 'b', 'i', '2']
>>> li.insert(-1,'2')
>>> li
['R', 'a', 'b', 'b', 'i', '2', '2']
>>> li.insert(-1,'H')
>>> li
['R', 'a', 'b', 'b', 'i', '2', 'H', '2']
>>> li.remove("2")
>>> li
['R', 'a', 'b', 'b', 'i', 'H', '2']
>>> del li[-1]
>>> li
['R', 'a', 'b', 'b', 'i', 'H']
```



## **2.3** **改**

切⽚

正切

步⻓

倒切

反转

```python
>>> b = "0123456789"
>>> li = list(b)
>>> li
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> li[2] = ""
>>> li[2] = "A"   # 直接改
>>> li
['0', '1', 'A', '3', '4', '5', '6', '7', '8', '9']
>>> li[0:5]   # 切片
['0', '1', 'A', '3', '4']
>>> li[0:9]
['0', '1', 'A', '3', '4', '5', '6', '7', '8']
>>> li[0:]
['0', '1', 'A', '3', '4', '5', '6', '7', '8', '9']
>>> li[:]
['0', '1', 'A', '3', '4', '5', '6', '7', '8', '9']
>>> li
['0', '1', 'A', '3', '4', '5', '6', '7', '8', '9']
>>> li[0:8:2]   # 2是步长
['0', 'A', '4', '6']
>>> li[0::2]
['0', 'A', '4', '6', '8']
>>> li[::2]
['0', 'A', '4', '6', '8']
>>> li[::3]
['0', '3', '6', '9']
>>> li[-4:]
['6', '7', '8', '9']
>>> li[-4:-1]
['6', '7', '8']
>>> li[-4::2]
['6', '8']
>>> li[::-1]   # 反转
['9', '8', '7', '6', '5', '4', '3', 'A', '1', '0']
>>> li[9:0:-1]
['9', '8', '7', '6', '5', '4', '3', 'A', '1']
```



## **2.4** **查**

'element' in names

names.count( )

names.index( )

```python
>>> li
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> '2' in li
False
>>> 2 in li
True
>>> li.count(2)
1
>>> li.append(6)
>>> li.count(6)
2
>>> li
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 6]
>>> li[2] = "A"
>>> li
[0, 1, 'A', 3, 4, 5, 6, 7, 8, 9, 6]
>>> li.index("A")
2
```



## **2.5** **特殊**

names.reverse( )      将整个列表反转

```python
>>> li
[0, 1, 'A', 3, 4, 5, 6, 7, 8, 9, 6]
>>> li.reverse()
>>> li
[6, 9, 8, 7, 6, 5, 4, 3, 'A', 1, 0]
```

names.sort( )   默认正排

```python
>>> li
[0, 1, 'A', 3, 4, 5, 6, 7, 8, 9, 6]
>>> del li[2]
>>> li
[0, 1, 3, 4, 5, 6, 7, 8, 9, 6]
>>> li.sort()
>>> li
[0, 1, 3, 4, 5, 6, 6, 7, 8, 9]
>>> li.sort(reverse=True)   # 反序
>>> li
[9, 8, 7, 6, 6, 5, 4, 3, 1, 0]
```

names.extend( )   合并

li1 + li2 合并成⼀个新列表

```python
>>> a = [2,34,65,93,6,98,15]
>>> a
[2, 34, 65, 93, 6, 98, 15]
>>> a.sort(reverse=True)
>>> a
[98, 93, 65, 34, 15, 6, 2]
>>> li + a
[9, 8, 7, 6, 6, 5, 4, 3, 1, 0, 98, 93, 65, 34, 15, 6, 2]
>>> li3 = li + a
>>> li3
[9, 8, 7, 6, 6, 5, 4, 3, 1, 0, 98, 93, 65, 34, 15, 6, 2]
>>> li.extend(a)   # 合并
>>> li
[9, 8, 7, 6, 6, 5, 4, 3, 1, 0, 98, 93, 65, 34, 15, 6, 2]
```

names.copy( )   浅copy ....

```python
>>> a = [1,2,3,4,['Rabbit','Jack'],6,78]
>>> a
[1, 2, 3, 4, ['Rabbit', 'Jack'], 6, 78]
>>> a.copy()
[1, 2, 3, 4, ['Rabbit', 'Jack'], 6, 78]
>>> b = a.copy()
>>> b
[1, 2, 3, 4, ['Rabbit', 'Jack'], 6, 78]
>>> b[2] = "A"
>>> b
[1, 2, 'A', 4, ['Rabbit', 'Jack'], 6, 78]
>>> b[4]
['Rabbit', 'Jack']
>>> b[4][1]
'Jack'
>>> b[4][1] = "Black girl"
>>> b
[1, 2, 'A', 4, ['Rabbit', 'Black girl'], 6, 78]
>>> a
[1, 2, 3, 4, ['Rabbit', 'Black girl'], 6, 78]
```

copy.deepcopy(a) 深copy

```python
>>> import copy
>>>
>>>
>>> c = copy.deepcopy(a)
>>> c
[1, 2, 3, 4, ['Rabbit', 'Black girl'], 6, 78]
>>> a[4]
['Rabbit', 'Black girl']
>>> a[4][1] = "黑姑娘"
>>> a
[1, 2, 3, 4, ['Rabbit', '黑姑娘'], 6, 78]
>>> c
[1, 2, 3, 4, ['Rabbit', 'Black girl'], 6, 78]
>>> c[4][0] = "Python"
>>> c
[1, 2, 3, 4, ['Python', 'Black girl'], 6, 78]
>>> a
[1, 2, 3, 4, ['Rabbit', '黑姑娘'], 6, 78]
```

## 列表生成式

```python
>>> [f"staff-{i}" for i in range(1,31)]
['staff-1', 'staff-2', 'staff-3', 'staff-4', 'staff-5', 'staff-6', 'staff-7', 'staff-8', 'staff-9', 'staff-10', 'staff-11', 'staff-12', 'staff-13', 'staff-14', 'staff-15', 'staff-16', 'staff-17', 'staff-18', 'staff-19', 'staff-20', 'staff-21', 'staff-22', 'staff-23', 'staff-24', 'staff-25', 'staff-26', 'staff-27', 'staff-28', 'staff-29', 'staff-30']
>>>
```

```python
staff_list = []
for i in range(1,31):
    staff_list.append(f"staff-{i}")

print(staff_list)
```

两个一样效果







