# -*- coding:utf-8 -*-
"""
作者:花城
日期:2021年07月04日
"""

age_of_black_girl = 25
print("你猜猜黑姑娘的年龄是多少：")
for age in range(100):
    age = int(input("black_girl age:"))
    if age < age_of_black_girl:
        print("猜的太小了，往大猜试试...")
    elif age > age_of_black_girl:
        print("猜的太大了，黑姑娘有这么老吗？往小猜试试...")
    elif age == age_of_black_girl:
        print("恭喜你，猜对了...")
        exit()
