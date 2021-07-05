# -*- coding:utf-8 -*-
"""
作者:花城
日期:2021年07月05日
"""
# for i in range(1, 10):
#     for j in range(1, 10):
#         if j <= i :
#             num = i*j
#             print(f"{i}x{j}={num}",end = "  ")
#     print()

for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{i}x{j}={i*j}",end = " ")
    print()