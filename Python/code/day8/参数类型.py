
def stu_form(name, age, major, phone):
    info = f'''
    Name :{name},
    Age  :{age},
    Major:{major},
    Phone:{phone}
    '''
    print(info)


# stu_form("Rabbit", 22, "IT", 18655721386)   # 位置参数

stu_form(major="Computer Science", name="Rabbit", phone=18655721386, age=22)   # 关键字参数
