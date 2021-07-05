## 一、for循环

## **1.1** **语法**

```python
for i in range(10): 
    print(i)
```

​		上⾯代码，会从0-9，共循环10次，这个range(10),其实是相当于产⽣了⼀个从0到9的列表，每循环⼀次，就会把列表⾥的下⼀个元素取出来给临时变量i.

示例：

```python
for count in range(10):
    print("hello I love this world!", count)

for name in ["alex", "rabbit", "black_girl"]:
    print(name)

for i in "Rabbit and me":
    print(i)
```

运行结果：

```
D:\PycharmProjects\pythonProjects\venv\Scripts\python.exe D:/PycharmProjects/pythonProjects/day2/for.py
hello I love this world! 0
hello I love this world! 1
hello I love this world! 2
hello I love this world! 3
hello I love this world! 4
hello I love this world! 5
hello I love this world! 6
hello I love this world! 7
hello I love this world! 8
hello I love this world! 9
alex
rabbit
black_girl
R
a
b
b
i
t
 
a
n
d
 
m
e

Process finished with exit code 0
```

## 1.2 打印奇偶数

```python
# for i in range(100):
#     if i >= 50:
#         if i % 2 == 0 : # 偶数
#             print(i)

# for i in range(50, 100):
#     if i % 2 == 0 : # 偶数
#         print(i)

for i in range(100, 50, -1):
    if i % 2 == 0 : # 偶数
        print(i)
```

## 1.3 循环嵌套

⼀栋楼有7层，每层9间屋⼦，要求你把本楼所有的房间号打印⼀遍， 格式“303”

```python
for floor in range(1,7):
    print(f"当前在{floor}层".center(50,'-'))
    for room in range(1,10):
        print(f"当前的房间是{floor}0{room}室.")
```

## break&continue

```python
for floor in range(1,7):
    print(f"当前在{floor}层".center(50,'-'))
    if floor == 3 :
        print("不走三层......")
        continue   # 停止本次循环，进入下次循环
    for room in range(1,10):
        if floor == 4 and room == 4:
            print("见鬼了......die at young......")
            exit()    # 退出程序
            # break   # 结束整个循环...(仅限当前一层)
        print(f"当前的房间是{floor}0{room}室.")

# 标志位.....
print("ha ha ha, still here......")
```

## 打印99乘法表

法一：

```python
for i in range(1, 10):
    for j in range(1, 10):
        if j <= i :
            num = i*j
            print(f"{i}x{j}={num}",end = " ")
    print()
```
法二：

```python
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{i}x{j}={i*j}",end = " ")
    print()
```



## 1.4 素数练习

100以内的素数

```python
for i in range(2,101):
    is_prime_num = True   # 假设i是素数，标志位
    for j in range(2,i):
        if i % j == 0:
            is_prime_num = False   # 证伪
    if is_prime_num == True:
        print(i,"是素数")
```



## 1.5 打印三角形

```python
for i in range(11):
    if i <= 5:
        print("* " * i )
    else:
        print("* " * (10-i) )
```
运行结果：
```

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 


Process finished with exit code 0
```



# 二、while循环

与for必须指定循环多少次不⼀样的是， while 循环的次数可以是不定的，只要条件满⾜就可以永远循环下去

## 2.1 语法

```python
while 条件: # 只要条件为真， 就会不断的循环
 print(xxxxx)
```

示例：

```python
count = 0
while count < 10 :
    count += 1
    print("loop",count)
```

## 2.2 死循环

```python
count = 0
while True:   # 条件永远为真
    print(f"第{count}次循环")
    count += 1
```



## 2.3 用while实现循环猜年龄

需求： 允许⽤户猜3次，若还不对，告诉他，你真笨，还想继续猜么？ 如果⽤户选择yes, 就让他继续，如果选择no, 就退出。

```python
count = 0
black_girl_age = 25
while count < 3:
    guess = input("猜黑姑娘的年龄：")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("不识别的指令，重新输入...")
        continue
    if guess > black_girl_age:
        print("猜大了，往小了试...")
    elif guess < black_girl_age:
        print("猜小了，往大了试...")
    else:
        print("恭喜你猜对了...")
        break
    count += 1
    if count == 3:
        cmd = input("你这么笨，是找不到对象的，还要不要试一把？(y/n)").strip()
        if cmd in ["Y","y","yes"]:
            count = 0 # 把count重置为0
        else:
            print("bey......see u...")
```

# 三、for...else

```python
for i in range(10):
 print(i)
else:
 print("done") # 循环正常执⾏结束后，会⾛else...			
```

若循环中间被 break了， 则else...不会执⾏

```python
for i in range(10):
    print(i)
    if i == 5:
        break
else: # 当循环正常结束时(没有被break，exit()...)，则执行。。。
    print("loop done...")
print("done......")
```



# 四、实战

1. 存款多少年才能翻倍？

   1万本金，利息0.0325每年，问连本带息多少年能翻倍？

   ```python
   year = 0
   count = 10000
   while True:
       year += 1
       count *= 1.0325
       print(year,count)
       if count >= 20000:
           print(f"10000元连本带息{year}年能翻倍......")
           break
   
   ```

2. 小球坠落长度计算

   一个小球，从100米高空坠落，每次反弹回来一半高度，问第10次反弹完，小球经过多少米？

   ```python
   height = 100
   distance = 0
   count = 0
   while count < 10:
       distance += height # 记录坠落时经过的长度
       height /= 2   # 反弹回的高度
       distance += height # 记录反弹经过的长度
       count += 1
       print(f"第{count}次反弹完，小球经过{distance}米......")
   
   ```

   

3. 猴子吃桃

   有一堆桃子，猴子每天吃桃子总数的一半并多吃一个。吃了10天，到第11天只剩一个桃子。问，猴子吃之前一共是多少个桃子？

   ```python
   n = 1
   day = 11
   while day > 1:
       n = (n + 1) * 2 # 上一天吃之前的桃子数量
       day -= 1
       print(day, n)
   
   ```
   
4. 计算从1-2+3-4+5-6+7......100的和

   ```
   
   ```

5. 寻找列表中的最大值，最小值

   ```python
   data = [9, 10, 33, 3, 5, 18, 4, 30, 25, 2, 11]
   # print(max(data))
   max_n = data[0]
   min_n = data[0]
   for i in data:
       if i > max_n:
           max_n = i
       if i < min_n:
           min_n = i
   print(max_n)
   print(min_n)
   ```

6. 寻找组合

   从两个列表里各取1个数，如果这两个数的和等于10，则以列表的方式输出这两个数

   ```python
   data = [9, 10, 33, 3, 5, 18, 4, 30, 25, 2, 11]
   data2 = [8, 3, 2, 1, -5, 19, 2, 4, 6, 7, 11]
   for i in data:
       for j in data2:
           if i + j == 10:
               print([i, j])
   ```



# 五、作业

   **年会抽奖程序**

   路⻜学城有限公司作为沙河500强企业，有300员⼯，开年会抽奖，奖项如下：

   ⼀等奖 3名， 泰国5⽇游+iPhone plus 12手机

   ⼆等奖6名，Iphone Plus 12⼿机

   三等奖30名，士力架20盒

**规则：**

1. 共抽3次，第⼀次抽3等奖，第2次抽2等奖，第3次压轴抽1等奖

2. 每个员⼯限中奖⼀次，不能重复

**解题思路：**

1. ⽣成⼀个员⼯列表，⽤random模块从⾥⾯取随机值

2. 取完值之后，⽴刻从员⼯⼤列表⾥把中奖⼈删掉，即可防⽌其再次中奖

