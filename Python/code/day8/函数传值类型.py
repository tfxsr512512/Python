
def change_data(name, hobbies):
    name = "花城"   # 修改只在函数内生效
    hobbies.append("打游戏")   # 在函数内往外部列表添加值
    hobbies[1] = "WeiQing"   # 修改列表元素
    print("in func:", name, hobbies)


my_name = "Rabbit"   # 不可变类型
my_hobbies = ["Monky", "BlackGirl"]   # 可变类型
change_data(my_name, my_hobbies)

print(my_name, my_hobbies)
