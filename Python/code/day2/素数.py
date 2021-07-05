# -*- coding:utf-8 -*-
"""
作者:花城
日期:2021年07月05日
"""
for i in range(2,101):
    is_prime_num = True   # 假设i是素数，标志位
    for j in range(2,i):
        if i % j == 0:
            is_prime_num = False   # 证伪
    if is_prime_num == True:
        print(i,"是素数")
