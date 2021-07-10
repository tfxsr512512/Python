# **Day 5** **数据类型& **编码

## ⼀、数据类型之-元组tuple

### **1.1** **元组是什么类型？**

⼀句话定义 ，元组是只读列表，==⼀旦创建，不可修改==。

只可进⾏查询、切片、循环操作。

### **1.2** 元组的用法

⽤ `() `来表示

```python
>>> names = ("Alex","Jack","Rain")
>>> type(names) 
<class 'tuple'>
>>> names
('Alex', 'Jack', 'Rain')
```

**查询**

仅有 `count `和 `index 2`个内置⽅法，⽤法跟list⼀致

```python
>>> names = ()
>>> type(names)
<class 'tuple'>
>>> names = ("Alex","Jack","Rain","Peiqi")
>>> names.index("Peiqi")   # 查询
3
>>> names.count("Alex")   # 计数
1
>>> names[0:3]   # 切片
('Alex', 'Jack', 'Rain')
>>> names[0::2]
('Alex', 'Rain')
>>> "Rain" in names
True
```

```python
>>> t = (1,2,3,[3,5,7])
>>> t
(1, 2, 3, [3, 5, 7])
>>> t[3]
[3, 5, 7]
>>> t[3][1]
5
>>> t[3][1] = "Text"
>>> t
(1, 2, 3, [3, 'Text', 7])
```

```python
>>> t = (1)
>>> type(t)
<class 'int'>
>>> t
1
>>> t = (1,)   # 单个的元组要加逗号
>>> type(t)
<class 'tuple'>
>>> t
(1,)
>>>
```

**切片**

切⽚与列表⽤法⼀致

**删除**

`del names`

**循环**

```python
>>> names
('Alex', 'Jack', 'Rain', 'Peiqi')
>>> for i in names:
...     print(i)
...
Alex
Jack
Rain
Peiqi
```

### **1.3** **什么情况会用元组？**

其实没什么特别要求必须什么时候 ⽤元组的场景，这基本上是⼀个程序员⾃⾏决择的问题。



## ⼆、数据类型之-字典dict

### **2.1** 什么是dict类型

**引子**

我们学了列表 ， 现在有个需求， 把你们公司每个员⼯的姓名、年龄、职务、⼯资存到列表⾥，你怎么存？

```python
staff_list = [
 ["Alex",23,"CEO",66000],
 ["⿊姑娘",24,"⾏政",4000],
 ["佩奇",26,"讲师",40000],
 # [xxx,xx,xx,xxx]
 # [xxx,xx,xx,xxx]
 # [xxx,xx,xx,xxx] 
]
```

这样存没问题，不过你要查⼀个⼈的⼯资的话， 是不是得把列表遍历⼀遍

```python
for i in staff_list:
 if i[0] == '⿊姑娘':
 print(i)
 break
```

但假如你公司有2万⼈，如果你要找的⿊姑娘正好在列表末尾，那意味着你要遍历2万次，才能找到这个信息。列

表越⼤，查找速度越慢。

好了，现在福⾳来了， 接下来学要的字典可以 查询数据⼜快、操作⼜⽅便，是⽇后开发中必备神器

```python
staff_list = {
 "alex": [23, "CEO", 66000],
 "⿊姑娘": [24, "⾏政", 4000],
 # ....
}
print(staff_list["⿊姑娘"]) # 即可取出来
```

### 2.2 dict定义

**｛key1:value1, key2:value2｝**

```python
>>> info = {
 "name":"Alex Li",
 "age" : 26,
 "name":"Jacke"
}
>>> info
{'name': 'Jacke', 'age': 26}
>>> info['age']
26
>>> info['age'] = 28
>>> info
{'name': 'Jacke', 'age': 28}
key -> value
```

`:`号左边是key, 右边是value

**dict特性**

1. key-value结构

2. key必须为不可变数据类型（字符串、数字、元组）， (hashtable)

3. ==key 必须唯⼀==,(hashtable)

4. ⼀个key对应的==value==可存放任意数据类型，==可修改==、可以不唯⼀

5. 可嵌套，即value也可是dict

6. py3.7之前是⽆序的, 3.7开始变成有序的了， ordered_dict

7. 查询速度快，且不受dict的⼤⼩影响，⾄于为何快？我们学完hash再解释。=O(1)

### 2.3 dict用法

**创建**

```python
# ⽅法1
>>> info2 = {
 "name":"BlackGirl",
 "age":23
 }
# ⽅法2
>>> info = dict(name="alex",age=22)	
>>> info
{'name': 'alex', 'age': 22}
```

**增**

```python
>>> staff_list
{'alex': [23, 'CEO', 66000], '⿊姑娘': [24, '⾏政', 4000]}
>>>
>>> staff_list["XiaoYun"] = [26,"前端开发",19000] # 新增
>>> staff_list
{'alex': [23, 'CEO', 66000], '⿊姑娘': [24, '⾏政', 4000], 'XiaoYun': [26, '前端开发',
19000]}
```

**检查式新增**   staff_list.setdefault()   已存在不创建，不存在再创建

向dict⾥新增⼀个key,val值 ，如果这个key不存中，如果这个key已存在，就返回已存在的key对应的value

```python
>>> staff_list.setdefault("Celina",[22,"Accountant",12000]) # 新增⼀个k,v值 [22, 'Accountant', 12000]
>>> staff_list
{'alex': [23, 'CEO', 66000], '⿊姑娘': [24, '⾏政', 4000], 'XiaoYun': [26, '前端开发',
19000], 'Celina': [22, 'Accountant', 12000]}

>>> staff_list.setdefault("XiaoYun",[22,"Accountant",12000]) # 新增⼀个，但是XiaoYun已经存在了，所以返回原来的值
[26, '前端开发', 19000]
```

**改**

普通修改

```python
>>> names["xiao_yun"] = [23,"前台", 6000]
>>> names["xiao_yun"][2] = 4500 # 改values列表⾥的值
>>> names
{'xiao_yun': [23, '前台', 4500], 'Celina': [23, 'UE', 9999]}
>>>
```

**合并修改**

把另外⼀个dict合并进来

```python
staff_list = {
 "alex": [23, "CEO", 66000],
 "⿊姑娘": [24, "⾏政", 4000],
 "xiao_yun":[22,"Student",2000],
}
names = {
 "xiao_yun":[25,"前端开发",12000],
 "Celina":[23,"UE", 9999] 
}
staff_list.update(names) # 把names的每个k,v赋值给staff_list, 相当于如下操作
# for k in names:
# 	staff_list[k] = names[k]
print(staff_list)
```

输出：

```python
>>> staff_list
{'alex': [23, 'CEO', 66000], '⿊姑娘': [24, '⾏政', 4000], 'xiao_yun': [25, '前端开发', 12000], 'Celina': [23, 'UE', 9999]}
```



**查**

```python
>>> names
{'xiao_yun': [23, '前台', 4500], 'Celina': [23, 'UE', 9999]}

# get ⽅法
>>> names.get("Jack") # 如果没有，返回None
>>> print(names.get("Jack"))
None
>>> names.get("xiao_yun") # 如果有，则返回值
[23, '前台', 4500]


# 直取
>>> names["Jack"] # 如果没有，报错
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
KeyError: 'Jack'
 
 
>>> names["Celina"] 
[23, 'UE', 9999]
```

判断是否在dict⾥有指定的key

```python
>>> names
{'xiao_yun': [23, '前台', 4500], 'Celina': [23, 'UE', 9999]}
>>>
>>> "Alex" in names
False
```

```python
dic.keys() #返回⼀个包含字典所有KEY的列表； 
dic.values() #返回⼀个包含字典所有value的列表；
dic.items() #返回⼀个包含所有（键，值）元组的列表；
```

```python
>>> staff_list = {
...  "alex": [23, "CEO", 66000],
...  "⿊姑娘": [24, "⾏政", 4000],
...  "xiao_yun":[22,"Student",2000],
... }
>>> names = {
...  "xiao_yun":[25,"前端开发",12000],
...  "Celina":[23,"UE", 9999]
... }
>>> staff_list.keys()
dict_keys(['alex', '⿊姑娘', 'xiao_yun'])
>>> staff_list.values()
dict_values([[23, 'CEO', 66000], [24, '⾏政', 4000], [22, 'Student', 2000]])
>>> staff_list.items()
dict_items([('alex', [23, 'CEO', 66000]), ('⿊姑娘', [24, '⾏政', 4000]), ('xiao_yun', [22, 'Student', 2000])])
>>>
```



**删**

```python
names.pop("alex") # 删除指定key
del names["black_girl"] # 删除指定key,同pop⽅法
names.popitem() # 以LIFO的⽅式删除⼀对值
names.clear() # 清空dict
```

**循环**

```python
1、for k in dic.keys()
2、for k,v in dic.items() 
3、for k in dic # 推荐⽤这种，效率速度最快
info = {
 "name":"路⻜学城",
 "mission": "帮⼀千万b粉⽩嫖学好编程",
 "website": "https://luffycity.com"
}
for k in info:
 print(k,info[k])
```

输出

```python
name 路⻜学城
mission 帮⼀千万b粉⽩嫖学好编程
website https://luffycity.com
```

```python
>>> for k in staff_list:
...     print(staff_list[k])
...
[23, 'CEO', 66000]
[24, '⾏政', 4000]
[22, 'Student', 2000]
>>> for k in staff_list:
...     print(k)
...
alex
⿊姑娘
xiao_yun
>>>
```



**特殊⽅法**

**fromkeys :** 批量⽣成多个k,v的dict

```python
>>> n 
['alex', 'jack', 'rain']
>>> dict.fromkeys(n, 0) 
{'alex': 0, 'jack': 0, 'rain': 0}
```

**Copy:** 浅copy ,同列表的copy⼀样

```python
>>> staff_list
{'alex': [23, 'CEO', 66000], '⿊姑娘': [24, '⾏政', 4000], 'xiao_yun': [22, 'Student', 2000]}
>>> list_one = staff_list.copy()
>>> list_one
{'alex': [23, 'CEO', 66000], '⿊姑娘': [24, '⾏政', 4000], 'xiao_yun': [22, 'Student', 2000]}
```



**求⻓度**

```python
len(info) # len()⽅法可同时⽤于列表、字符串
```

解释器⾃带函数



### **2.4 dict** 为何查询速度快？

因为dict是基于hashtable实现的， hashtable的原理导致你查询速度就是O(1)， 意思就是你即使有1亿个数据，查询某个值也只需1次搞定 

### 2.5 dict练习题

1. ⽣成⼀个包含100个key的字典，每个value的值不能⼀样

2. {‘k0’: 0, ‘k1’: 1, ‘k2’: 2, ‘k3’: 3, ‘k4’: 4, ‘k5’: 5, ‘k6’: 6, ‘k7’: 7, ‘k8’: 8, ‘k9’: 9} 请把这个dict中key⼤于5的值value打印出来。

3. 把题2中value是偶数的统⼀改成-1

4. 把下⾯列表中的值进⾏分类 ，变成dict,

   ```python
   Input : test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
   Output : {4: [4, 4, 4], 6: [6, 6], 2: [2, 2], 8: [8, 8], 5: [5]}
   需求 : 值⼀样的要分类存在⼀个key⾥
   ```

   ```python
   
   test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
   
   test_dic = {}
   for i in test_list:
       if i not in test_dic:  # 第一次遇到4
           test_dic[i] = [i, ]  # 创建一个key
       else:  # 下次遇到4
           test_dic[i].append(i)  # 追加
   
   print(test_dic)
   
   ```

   

5. 把⼀段话⾥重复的单词去掉

   ```python
   Input : Python is great and Java is also great
   Output : is also Java Python and great
   ```

6. 写程序输出dict中values⾥唯⼀的值

   ```python
   dic = {'gfg': [5, 6, 7, 8], 'best': [6, 12, 10, 8], 'is': [10, 11, 7, 5], 'for': [1,
   2, 5]}
   结果 : [1, 2, 5, 6, 7, 8, 10, 11, 12]
   ```

7. 把所有下表中同字⺟异序词找出来

   ```python
   arr = ['cat', 'dog', 'tac', 'god', 'act']
   ```

   结果：

   ```python
    [ ['cat','tac','act'],['god','dog']]
   ```



## 三、数据类型之-集合set

### **3.1** **定义和作用**

集合跟我们学的列表有点像，也是可以存⼀堆数据，不过它有⼏个独特的特点，令其在整个Python语⾔中占有⼀席之地，

1. ⾥⾯的元素不可变，代表你不能存⼀个list、dict 在集合⾥，字符串、数字、元组等不可变类型可以存
2. ==天⽣去重==，在集合⾥没办法存重复的元素
3. ⽆序，不像列表⼀样通过索引来标记在列表中的位置 ，元素是⽆序的，集合中的元素没有先后之分，如集合{3,4,5}和{3,5,4}算作同⼀个集合
4. ==打印自动排序==
   1. 关系测试（作⽤）

基于上⾯的特性，我们可以⽤集合来⼲2件事，==**去重和关系运算**==



### **3.2** **语法**

**创建**

**创建集合**

注意也是 `{} `，但不是dict, 不是k,v结构

```python
>>> a = {1,2,3,4,2,'alex',3,'rain','alex'}
>>> a 
{1, 2, 3, 4, 'alex', 'rain'}
```

由于它是天⽣去重的，重复的值根本存不进去

**帮列表去重**

帮列表去重最快速的办法是什么？ 就是把它转成集合，去重完，再转回列表

```python
>>> b 
[1, 2, 3, 4, 2, 'alex', 3, 'rain', 'alex']
>>> set(b) 
{1, 2, 3, 4, 'alex', 'rain'}
>>>
>>> b = list(set(b)) #⼀句代码搞定
>>> b 
[1, 2, 3, 4, 'alex', 'rain']
```

**增**

```python
>>> a = {1, 2, 3, 4, 5}
>>> a.add(9)
>>> a
{1, 2, 3, 4, 5, 9}
```

**查**

```python
>>> a
{1, 2, 3, 4, 5, 9}
>>> 8 in a
False
```

**改**

不能修改，⼀旦创建，不可修改⾥⾯的值

**删除**

```python
>>> a.pop() # 随机删除⼀个值，并返回该值
2
>>> a.remove(3) # 删除3这个元素，若3不在，报KeyError
>>> a
{3, 4, 5}
>>> a.discard(8) # 删除指定的值 ，若该值不存在,do nothing.
>>> a.discard(9)
>>> a.discard(5)
>>> a
{3, 4}
```



### **3.3** **关系测试**

```python
five_man_fight_1girl = {"Alex","peiqi","PyYu","OldVillageMaster","Egon","BlackGirl"}
girls_game={"BlackGirl","XiaoYun","Celina","Alex"}
```

**交集**

```python
>>> five_man_fight_1girl & girls_game # & 符号
{'BlackGirl', 'Alex'}
>>> five_man_fight_1girl.intersection(girls_game) 
{'BlackGirl', 'Alex'}
```

**并集**

```python
>>> five_man_fight_1girl | girls_game # | 符号
{'Celina', 'Alex', 'Egon', 'BlackGirl', 'peiqi', 'PyYu', 'OldVillageMaster',
'XiaoYun'}
>>> five_man_fight_1girl.union(girls_game) 
{'Celina', 'Alex', 'Egon', 'BlackGirl', 'peiqi', 'PyYu', 'OldVillageMaster',
'XiaoYun'}
```

**差集**

```python
>>> five_man_fight_1girl - girls_game # - 符号代表 差集 , only in five_man_fight_1girl
{'PyYu', 'peiqi', 'OldVillageMaster', 'Egon'}
>>> girls_game - five_man_fight_1girl # only in girls_game
{'Celina', 'XiaoYun'}
>>> five_man_fight_1girl.difference(girls_game) 
{'PyYu', 'peiqi', 'OldVillageMaster', 'Egon'}
```

**对称差集**

```python
>>> five_man_fight_1girl ^ girls_game # ^ 符号， 把同时在2个电影⾥都出演过的⼈T出去
{'Celina', 'Egon', 'peiqi', 'PyYu', 'OldVillageMaster', 'XiaoYun'}
>>> five_man_fight_1girl.symmetric_difference(girls_game) {'Celina', 'Egon', 'peiqi', 'PyYu', 'OldVillageMaster', 'XiaoYun'}
```

**子集、父集**

```python
>>> five_man_fight_1girl.issubset(girls_game) # 是不是girls_game的子集，即five_man...⾥的每个值都在girls_game⾥存在
False
>>> five_man_fight_1girl.issuperset(girls_game) # 是不是girls_game的⽗集
False
```



**测试后修改**

three_some = {'⾦⻆', '银⻆', '⿊姑娘'}

four_p = {'⾦⻆', '银⻆',"⿊姑娘", "XiaoYun"}

```python
>>> four_p.difference(three_some) # {'XiaoYun'}
>>> four_p.difference_update(three_some) # 把差集的结果赋值给four_p
>>> four_p
{'XiaoYun'}
>>> four_p
{'XiaoYun'}
>>> four_p.update(three_some) # 把合并后的结果赋值给four_p
>>> four_p
{'XiaoYun', '⾦⻆', '银⻆', '⿊姑娘'}
```

## 四、二进制位运算



​		程序中的所有数在内存中都是以⼆进制的形式储存的。位运算就是直接对整数在内存中的⼆进制位进⾏操作

下表中变量 a 为 60，b 为 13，⼆进制格式如下：

```python
a = 0011 1100
b = 0000 1101
```



| 运算符 | 描述                                                         | 实例                                                         |
| ------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| &      | 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0（快记法：==与运算， 位相乘==） | (a & b) 输出结果 12 ，⼆进制解释： 00001100                  |
| \|     | 按位或运算符：只要对应的⼆个⼆进位有⼀个为1时，结果位就为1。（快记：==或运算， 位相加==） | (a \| b) 输出结果 61 ，⼆进制解释： 00111101                 |
| ^      | 按位异或运算符：当两对应的⼆进位相异时，结果为1（快记：位相减） | (a ^ b) 输出结果 49 ，⼆进制解释： 00110001                  |
| ~      | 按位取反运算符：对数据的每个⼆进制位取反,即把1变为0,把0变为1 。（快记：~x=-(x+1) | (~a ) 输出结果 -61 ，⼆进制解释： 11000011，在⼀个有符号⼆进制数的补码形式。 |
| <<     | 左移动运算符：运算数的各⼆进位全部左移若⼲位，由 **<<**右边的数字指定了移动的位数，⾼位丢弃，低位补0。 | a << 2 输出结果 240 ，⼆进制解释： 11110000                  |
| >>     | 右移动运算符：把">>"左边的运算数的各⼆进位全部右移若⼲位，**>>** 右边的数字指定了移动的位数 | a >> 2 输出结果 15 ，⼆进制解释： 00001111                   |



## 五、三元运算

⼜称三⽬运算，是对if...else...的⼀种简写

假设现在有两个数字，我们希望获得其中较⼤的⼀个，那么可以使⽤ if else 语句，例如：

```python
if a>b: 
 max = a
else: 
 max = b
```

⽤三元运算的写法就是

```python
max = a if a > b else b
```

上⾯语句的含义是：

* 如果 a>b 成⽴，就把 a 作为整个表达式的值，并赋给变量 max；

* 如果 a> b 不成⽴，就把 b 作为整个表达式的值，并赋给变量 max。

**三元嵌套**

Python 三元运算符⽀持嵌套，就可以构成更加复杂的表达式。在嵌套时需要注意 if 和 else 的配对，例如：

```python
>>> a,b,c,d = 3,5,7,9
>>>
>>> a if a > b else c if c > d else d
9
```

应该理解为

```python
a if a > b else (c if c > d else d)
```

## 六、作业

**三级菜单**

数据源

```python
menu = {
    '北京': {
        '海淀': {
            '五道⼝': {
                'soho': {},
                '⽹易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽⻋之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '路⻜学城': {},
                '北航': {},
            },
            '天通苑': {},
            '回⻰观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵⾏': {
            "⼈⺠⼴场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '⽕⻋站': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '⼭东': {},
}

```

**需求：**

* 可依次选择进⼊各⼦菜单
* 可从任意⼀层往回退到上⼀层
* 可从任意⼀层退出程序

> 所需新知识点：列表、字典、循环

