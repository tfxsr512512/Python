# -*- coding:utf-8 -*-
"""
作者:花城
日期:2021年07月05日
"""
# for i in range(10):
#     print(i)
# else:
#     print("loop done...")

# for i in range(10):
#     print(i)
#     if i == 5:
#         break
# else: # 当循环正常结束时(没有被break，exit()...)，则执行。。。
#     print("loop done...")
# print("done......")

count = 0
while count < 10:
    print(count)
    count += 1
    if count > 5:
        break
else:
    print("while...done...")

