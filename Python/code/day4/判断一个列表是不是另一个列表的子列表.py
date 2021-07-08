li = [8, 3, 12, 1, 2, 34, 54, 12, 34, 11, 51, 12, 14, 9, 1, 10, 15, 17, 18, 99, 1, 3, 5, 10]
l2 = [5, 99, 12]

is_sub_list = True
for i in l2:
    if i not in li:
        is_sub_list = False
        print("不是子列表....")

if is_sub_list:  # true
    print("是子列表")
