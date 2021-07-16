#
#
# def stu_form(name, age, major, phone, nationality='CN', *args):
#     info = f'''
#     Name :{name},
#     Age  :{age},
#     Major:{major},
#     Phone:{phone},
#     Nation:{nationality}
#     '''
#     print(info)
#     print("不定长列表参数:", args)
#
#
# stu_form("XiaoYun", 23, "Finance", 13332, "Thailand", "Rabbit", 'Movies')  # 多写了最后2个参数


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