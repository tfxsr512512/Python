# 函数基础

## 1. 什么是函数&作用

**函数是一种仅在调用时运行的代码块。**

**您可以将数据（称为参数）传递到函数中。**

**函数可以把数据作为结果返回。**

函数的优点：

- 代码可复用
- 代码可维护性高
- 容易排错
- 可读性好
- 利于团队开发

### 1.1 创建函数

```python
def 函数名（[参数1],[参数2]....[参数n]）:
	函数体
```

```python
def my_function():   # 函数名
  print("Hello from a function")
```

### 1.2 调用函数

```python
def my_function():
  print("Hello from a function")

my_function()   # 调用函数
```

### 1.3 **形参和实参**

```python
def my_function(name):   # name是形参
    print(f"Hello, {name}, valar morghulis...")


my_function("Rabbit")   # Rabbit是实参
```

**形参变量：** 只有在函数被调用时才分配内存单元，在调用结束时，即刻释放所分配的内存单元。因此，形参只在函数内部有效。函数调用结束返回后则不能再使用该形参变量

**实参：** 可以是常量、变量、表达式、函数等，无论实参是何种类型的量，在进行函数调用时，它们都必须有确定的值，以便把这些值传送给形参，因此应预先给实参赋值

### 1.4 返回值

可以通过return语句返回计算结果。语法：  return 表达式

- return的作用一个是终止函数的执行，所有执行了return后，其后的语句不会被执行

- 如果没有return语句，则默认返回的是None

- return还可以返回给调用者数值

- return可以返回一个值，如果要返回多个值，那么返回的是一个元组

```python
def demo2():
    return 1
def demo3():
    return 1,2,3
print(demo2())
print(demo3())  #(1,2,3)
```

```python
def stu_registration_form():   # 注册表单
    form = {
        "name":input("Name:").strip(),
        "age":input("Age:").strip(),
        "phone":input("Phone:").strip()
    }

    info_pass_flag = True
    for k,v in form.items():
        if len(v) == 0:
            info_pass_flag = False
            break
    return form, info_pass_flag


stu_info, flag = stu_registration_form()
print(stu_info)
print(flag)
if not flag:
    print("表单填写有误...")
else:
    print("欢迎来到王者荣耀!!!")

```



## 2. 函数参数

### 2.1 传值类型

* ==不可变类型==
  * 在函数内修改外部传进来的不可变类型(string、元组)时，会在函数内部生成一个该参数的copy，并不会影响原来函数外部的值
* ==可变类型==
  * 可变类型，如列表、dict，传到函数内部，其实只是传递了该列表\dict的整体内存地址，函数内部可直接修改函数外部的这个list or dict.

```python
def change_data(name, hobbies):
    name = "花城"   # 修改只在函数内生效
    hobbies.append("打游戏")   # 在函数内往外部列表添加值
    hobbies[1] = "WeiQing"   # 修改列表元素
    print("in func:", name, hobbies)


my_name = "Rabbit"   # 不可变类型
my_hobbies = ["Monky", "BlackGirl"]   # 可变类型
change_data(my_name, my_hobbies)

print(my_name, my_hobbies)

```

输出

```
in func: 花城 ['Monky', 'WeiQing', '打游戏']
Rabbit ['Monky', 'WeiQing', '打游戏']

Process finished with exit code 0
```

### 2.2 参数类型

**必备参数 (位置参数)**

* 必备，不传值会报错
* 传的值是有顺序的，从左到右，每个参数一一对应

```python
def stu_form(name, age, major, phone):
    info = f'''
    Name :{name},
    Age  :{age},
    Major:{major},
    Phone:{phone}
    '''
    print(info)


stu_form("Rabbit", 22, "IT", 18655721386)
```

**关键字参数**

* 赋值时指定参数名，不按位置顺序了
* 如果和必备参数混用，必须放在位置参数后边

```python
def stu_form(name, age, major, phone):
    info = f'''
    Name :{name},
    Age  :{age},
    Major:{major},
    Phone:{phone}
    '''
    print(info)


stu_form(major="Computer Science", name="Rabbit", phone=18655721386, age=22)
stu_form("Rabbit", 22, major="Computer Science", phone=18655721386) 
```

**默认参数**

对于一些调用时非必选的参数，可设置成默认参数，这样，即使用户不填，也不影响函数正常运行。

* 默认值，如果形参在定义的时候给定一个值，那么函数在调用时就可以不传实参，可以简化调用

  * 默认值参数必须放到最右边

  * 如果传了实参，那么实参优先，不会使用默认值

  * 默认值只计算一次

  * 默认值必须是不可变对象

```python

def stu_form(name, age, major, phone, nationality='CN'):
    info = f'''
    Name :{name},
    Age  :{age},
    Major:{major},
    Phone:{phone},
    Nation:{nationality}
    '''
    print(info)


stu_form("BlackGirl", major="Computer Science", phone=18655721386, age=22, nationality='JP')
stu_form("Rabbit", major="IT", age=22, phone='17305525102')  # nationality默认是CN

```

**不定长参数**

***args** **元组传值**

多给的值，都会给到`*args`参数里，以元组形式

```python

def stu_form(name, age, major, phone, nationality='CN', *args):
    info = f'''
    Name :{name},
    Age  :{age},
    Major:{major},
    Phone:{phone},
    Nation:{nationality}
    '''
    print(info)
    print("不定长列表参数:", args)

stu_form("XiaoYun", 23, "Finance", 13332, "Thailand", "Rabbit", 'Movies')  # 多写了最后2个参数

```
运行结果
```
    Name :XiaoYun,
    Age  :23,
    Major:Finance,
    Phone:13332,
    Nation:Thailand
    
不定长列表参数: ('Rabbit', 'Movies')
```

`**kwargs` 

```python
def stu_form(name, age, major, phone, nationality='CN', *args, **kwargs):
    info = f'''
    Name :{name},
    Age  :{age},
    Major:{major},
    Phone:{phone},
    Nation:{nationality}
    '''
    print(info)
    print("不定长列表参数:", args)
    print("不定长列表参数dict:", kwargs)


stu_form("XiaoYun", 23, "Finance", 13332, "Thailand", "Rabbit", 'Movies', hometown="安徽", university="安徽理工大学")  
```

运行结果

```python
    Name :XiaoYun,
    Age  :23,
    Major:Finance,
    Phone:13332,
    Nation:Thailand
    
不定长列表参数: ('Rabbit', 'Movies')
不定长列表参数dict: {'hometown': '安徽', 'university': '安徽理工大学'}
```

进阶

```python
def stu_form(name, age, major, phone, nationality='CN', *args, **kwargs):
    info = f'''
    Name :{name},
    Age  :{age},
    Major:{major},
    Phone:{phone},
    Nation:{nationality}
    '''
    print(info)
    print("不定长列表参数:", args)
    print("不定长列表参数dict:", kwargs)


stu_form("XiaoYun", 23, "Finance", 13332, "Thailand", "Rabbit", 'Movies', hometown="安徽", university="安徽理工大学")

my_info = ["Rabbit", 23, "HR", 186, "Chinese", "Girl"]

my_dict = {
    "name": "Rabbit",
    "age": 22,
    "major": "IT",
    "phone": 173,
    "hobbie": "girl"
}

stu_form(*my_info)
stu_form(**my_dict)
```

## 3. 函数嵌套

列表里可以嵌套子列表、字典里可以嵌入子字典、函数里也可以嵌子函数

==子函数只能在函数内部调用。==

## 4.全局变量vs局部变量

```python
def change_name():
    name = "Rabbit"  # 局部变量，只在函数内部生效
    print("in func:", name)


name = "金角大王"  # 全局变量， 整个代码文件全局生效

change_name()
print("global var:", name)

```

输出

```
in func: Rabbit
global var: 金角大王

Process finished with exit code 0
```

变量的查找顺序是 ==**局部变量>全局变量**==

**global声明全局变量**

global语法告诉解释器，我要在函数内部引用并修改全局变量

```python
def change_name():
    global name  # 声明要引用全局变量
    name = "Rabbit"  # 这时改的是全局变量
    print("in func:", name)


name = "金角大王"  # 全局变量， 整个代码文件全局生效

change_name()
print("global var:", name)

```

输出

```
in func: Rabbit
global var: Rabbit

Process finished with exit code 0
```

## 5. 匿名函数lambda

匿名函数就是不需要显示的指定函数名的函数

```python
>>> func = lambda x,y:x*y
>>> func(8,9)
72

# 相当于传统函数
def func(x,y):
    return x*y
```


```python
>>> names_age = [22,23,24,26,29]
>>> def add_age(n):
	return n+1

>>> map(add_age, names_age)
<map object at 0x000001ACF8CF5E80>
>>> list(map(add_age, names_age))
[23, 24, 25, 27, 30]

# 相当于
>>> names_age = [22,23,24,26,29]
>>> map(lambda n:n+1, names_age)
<map object at 0x000001ACF8CF5D30>
>>> list(map(lambda n:n+1, names_age))
[23, 24, 25, 27, 30]
```

## 6. 高阶函数

==变量可以指向函数名==，函数的参数能接受变量，那么一个函数就可以接受另一个函数作为参数，这种函数就称之为高阶函数。

```python
>>> def get_square(n):
...     return n*n
...
>>> get_square
<function get_square at 0x000002030944F160>
>>> f = get_square   # 把一个函数名，赋值给变量
>>> f(3)
9
```

把函数当作参数，传递给另一个函数

```python
def get_abs(n):
    if n < 0:
        n = int(str(n).strip("-"))
    return n
def add(x, y, f):
    return f(x) + f(y)
res = add(3, -6, get_abs)
print(res)

# 输出
9
```

## 7. 递归

```python
def calc(n):
    n = int(n/2)
    print(n)
    if n > 0:
        calc(n)  # 调用自己
calc(100)
```

练习题

用递归实现2分查找的算法，以从列表a = [1,3,4,6,7,8,9,11,15,17,1,21,22,25,29,33,38,69,107]查找指定的值。

## 8. 内置函数

[](https://blog.csdn.net/qq_44923097/article/details/100989937?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522162641667416780274146727%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=162641667416780274146727&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_click~default-2-100989937.first_rank_v2_pc_rank_v29&utm_term=python%E5%86%85%E7%BD%AE%E5%87%BD%E6%95%B0&spm=1018.2226.3001.4187)

1、abs() #返回数字的绝对值。

```python
>>> abs(-1)
1
```

2、all() #all() 用于判断给定的参数中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
元素除了是 0、空、None、False 外都算 True。

```python
>>> all([1,2,3,4,5,6,0])
False
```

3、any() #用于判断给定的参数是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
元素除了是 0、空、FALSE 外都算 TRUE。

4、ascii() #返回一个表示对象的字符串

5、bin() #返回一个整数 int 或者长整数 long int 的二进制表示。

6、bool() #函数用于将给定参数转换为布尔类型，如果没有参数，返回 False。

7、bytearray() #返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256。

```python
>>> s = b'alex'
>>> s
b'alex'
>>> type(s)
<class 'bytes'>
>>> s[0]
97
>>> s[0] = 98
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'bytes' object does not support item assignment
>>> b_arr = bytearray(s)
>>> b_arr[0]
97
>>> b_arr[0] = 98
>>> b_arr
bytearray(b'blex')
```

8、bytes() #函数返回一个新的 bytes 对象，该对象是一个 0 <= x < 256 区间内的整数不可变序列。

9、callable() #用于检查一个对象是否是可调用的。如果返回 True，object 仍然可能调用失败；但如果返回 False，调用对象 object 绝对不会成功。

10、chr() #用一个整数作参数，返回一个对应的字符。

11、classmethod() #修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
12、compile() #将一个字符串编译为字节代码。
13、complex() #用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数

14、delattr() #用于删除属性。
15、dict() #用于创建一个字典。

16、dir() #不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。

17、divmod() #接收两个数字类型（非复数）参数，返回一个包含商和余数的元组(a // b, a % b)。在 python 3.x 版本该函数不支持复数。

18、 enumerate() #用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

19、eval() #用来执行一个字符串表达式，并返回表达式的值。

可以把字符串形式的list，dict，set，tuple，再转换成其原有的数据类型。

```python
>>> s = "[1,2,3,4,5,6]"
>>> s
'[1,2,3,4,5,6]'
>>> eval(s)
[1, 2, 3, 4, 5, 6]
```

20、exec() #执行储存在字符串或文件中的 Python 语句

```python
>>> exec("print('helloworld')")
helloworld
>>> exec("name = 'rabbit'")
>>> name
'rabbit'
```

21、filter() # 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。

```python
>>> s = [0,1,23,3,4,5,6,7,89,7,6,6,666]
>>> filter(lambda n:n>10, s)
<filter object at 0x0000020309539400>
>>> list(filter(lambda n:n>10, s))
[23, 89, 666]
```

22、float() #用于将整数和字符串转换成浮点数。

23、format() #格式化字符串的函数
24、frozenset() #返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
25、getattr() #用于返回一个对象属性值。
26、globals() #会以字典类型返回当前位置的全部全局变量。

27、hash() #用于获取取一个对象（字符串或者数值等）的哈希值。

28、help() #用于查看函数或模块用途的详细说明。

29、hex() #用于将一个指定数字转换为 16 进制数。

30、id() #用于获取对象的内存地址。

31、input() #从键盘接入字符

32、int() #用于将一个字符串或数字转换为整型。

33、isinstance() #判断一个对象是否是一个已知的类型，类似 type()。
34、issubclass() #用于判断参数 class 是否是类型参数 classinfo 的子类
35、iter() #用来生成迭代器。
36、len() #返回对象（字符、列表、元组等）长度或项目个数。

37、list() #用于将元组或字符串转换为列表。

38、locals() #会以字典类型返回当前位置的全部局部变量。
39、map() #据提供的函数对指定序列做映射。
40、max() #返回给定参数的最大值，参数可以为序列。

41、min() #返回给定参数的最小值，参数可以为序列。

42、next() #返回迭代器的下一个项目。
43、oct() #将一个整数转换成8进制字符串。

44、 pow() #返回 xy（x的y次方） 的值。

45、print() #用于打印输出，最常见的一个函数。
46、 repr() #将对象转化为供解释器读取的形式。
47、str() #将对象转化为适于人阅读的形式。

48、sum() #对系列进行求和计算。

49、sorted() # 排序

```python
scores = [
    ["alex", 99],
    ["rain", 19],
    ["jack", 23],
    ["lame", 26],
    ["make", 76],
    ["dd", 29],
    ["gg", 30]
]

s1 = sorted(scores, key=lambda i: i[1])
s2 = sorted(scores, key=lambda i: i[1], reverse=True)
print(scores)
print(s1)
print(s2)

# 输出
[['alex', 99], ['rain', 19], ['jack', 23], ['lame', 26], ['make', 76], ['dd', 29], ['gg', 30]]
[['rain', 19], ['jack', 23], ['lame', 26], ['dd', 29], ['gg', 30], ['make', 76], ['alex', 99]]
[['alex', 99], ['make', 76], ['gg', 30], ['dd', 29], ['lame', 26], ['jack', 23], ['rain', 19]]
```

50、zip()：聚合传入的每个迭代器中相同位置的元素，返回一个新的元组类型迭代器

```python
>>> x = [1,2,3] #长度3
>>> y = [4,5,6,7,8] #长度5
>>> list(zip(x,y)) # 取最小长度3
[(1, 4), (2, 5), (3, 6)]
```

**特殊内置函数**

compile() #将一个字符串编译为字节代码。

```python
f = open("递归.py", encoding='utf-8')
code = compile(f.read(), '', 'exec')   # 解析代码文件，str
print(code)
exec(code)   # 执行代码块
```

print() # 直接将消息打印到文件里

```python
msg = "又回到最初的起点"
f = open("tofile.txt", "w", encoding='utf-8')
print(msg, "记忆中你青涩的脸", sep="|", end="", file=f)
```

## 9. 作业-员工信息表



