
def change_name():
    global name  # 声明要引用全局变量
    name = "Rabbit"  # 这时改的是全局变量
    print("in func:", name)


name = "金角大王"  # 全局变量， 整个代码文件全局生效

change_name()
print("global var:", name)
