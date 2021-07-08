# 列表练习题

## 1. 列表如何去重

```python
# li = [1, 3, 5, 3, 1, 6, 8, 5, 1, 9, 67, 89, 3, 66]
#
# 怎么判断某个元素有没有重复？
#     li.count(1) > 1 : 重复
#     想知道列表里每个元素有没有重复，那你就得所有元素count一次，
# 你怎么知道每个重复的值，要删除几次呢？
#     count_num = li.count(1) # 3
#     count_num -1 # 要删除的次数。。。
#     li.remove(1)
#
# 首先得找到所有重复的值。。。
#     把所有重复的值，提出来，单独放一个列表。。。 统一循环删除。。。:
#     方法1:
#     duplicate_nums = [1, 3, 5...]
#
#     for i in duplicate_nums:
#         for j in range(li.count(i)-1)
#             li.remove(i)  # 重复了3次，要删除2次
#
#     方法2:
#     duplicate_nums = [[1,3],[3,3],[5,2]...]

li = [1, 3, 5, 3, 1, 6, 8, 5, 1, 9, 67, 89, 3, 66]
duplicate_nums = []
for i in li:
    i_show_count = li.count(i)   # 每个值 出现了几次
    if i_show_count > 1 and [i, i_show_count] not in duplicate_nums:   # 代表该值 是重复的,且该值不在重复列表里
        duplicate_nums.append([i, i_show_count])
print(duplicate_nums)

for item in duplicate_nums:
    # duplicate_n = item[0]
    # duplicate_times = item[1]
    duplicate_n,duplicate_times = item
    for j in range(duplicate_times-1): # 为何减1？ 因为是去重，而不是把所有的重复值删除，得保留一个重复值
        li.remove(duplicate_n)   # 一次只能删除一个值
        print("删除了一次：", duplicate_n)
print(li)

```

## 2. 找到列表中第二大的值

```python
li = [8, 3, 12,1, 2, 34, 90, 12, 34, 11, 12,14, 9, 1, 10,15, 17, 18, 99, 1, 3, 5, 10]

for n in range(2):
    for index in range(len(li)-1):
        # 让当前索引值index, 跟index+1进行比较
        i = li[index] # 拿到当前索引的值 8

        if i > li[index+1] : # 8>3 , 得换
            li[index] = li[index+1]  # 把3换到8的位置
            li[index+1] = i # 把原来临时存的8，放到3的位置
    print(li)
print(f"列表中第2大的值是{li[-2]}")

```



## 3. 判断一个列表是不是另一个列表的子列表

```python
li = [8, 3, 12, 1, 2, 34, 54, 12, 34, 11, 51, 12, 14, 9, 1, 10, 15, 17, 18, 99, 1, 3, 5, 10]
l2 = [5, 99, 12]

is_sub_list = True
for i in l2:
    if i not in li:
        is_sub_list = False
        print("不是子列表....")

if is_sub_list:  # true
    print("是子列表")

```



## 4. 求出列表中，离最大值和最小值的平均值最接近的值

```python
li = [8, 3, 12,1, 2, 34, 54, 12, 34, 11,50.1,51, 12,14, 9, 1, 10,15, 17, 18, 99, 1, 3, 5, 10]

max_n = li[0]
min_n = li[1]

for i in li:
    if i > max_n:max_n = i
    if i < min_n:min_n = i

avg_n = (max_n + min_n) / 2

print(max_n,min_n,avg_n)
closest_n = li[0] # 假设

for n in li: # 12
    if abs(avg_n - n) < abs(avg_n - closest_n ) : # 代表找到了更近的值 , 需要把最近的值 ，给到closet_n
        closest_n = n
        print("找到更近的了",closest_n)

print(closest_n)
```



# 实战

## 双色球

```python

red_balls = []
blue_balls = []

count = 0
while count < 6:
    choice = input(f"输入第{count+1}个红球>:").strip()
    if not choice.isdigit(): #
        print("不合法")
        continue
    choice = int(choice)
    if 0 < choice <= 33 and choice not in red_balls:
        red_balls.append(choice)
        count += 1

count = 0
while count < 1:
    choice = input(f"输入第{count+1}个blue球>:").strip()
    if not choice.isdigit(): #
        print("不合法")
        continue
    choice = int(choice)
    if 0 < choice <= 16 and choice not in blue_balls:
        blue_balls.append(choice)
        count += 1


print(red_balls,blue_balls)
```

## 双色球进阶

```python
red_balls = []
blue_balls = []

li = [
    [6, 33, "红球", red_balls],
    [1, 16, "蓝球", blue_balls]
]
for item in li:
    print(f"开始选择{item[2]}".center(50, '-'))
    count = 0
    while count < item[0]:
        choice = input(f"选择第{count + 1}个{item[2]}>>:").strip()
        if not choice.isdigit():
            print("不合法的选择...")
            continue
        choice = int(choice)
        if 0 < choice < item[1] and choice not in item[3]:  # 合法的球
            item[3].append(choice)  # 动态的往每个球色的列表里加球...
            count += 1
print(red_balls)
print(blue_balls)

```

# 作业

## 购物车程序

**需求：**

  		1. 你和女朋友去逛街，程序实现打印商品列表，用户可通过商品编号来选购商品，允许不断的买商品
  		2. 程序启动时，让用户先输入自己的工资，总购物的商品价格不得超过工资
  		3. 用户随时可退出程序，退出时，打印，分别买了哪些商品，及余额



**规则：**

* 不能用dict、set

