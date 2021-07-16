
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
