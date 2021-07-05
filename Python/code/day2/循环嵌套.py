# -*- coding:utf-8 -*-
"""
作者:花城
日期:2021年07月05日
"""
for floor in range(1,7):
    print(f"当前在{floor}层".center(50,'-'))
    for room in range(1,10):
        print(f"当前的房间是{floor}0{room}室.")