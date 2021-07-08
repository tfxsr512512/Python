# li = [1, 3, 5, 3, 1, 6, 8, 5, 1, 9, 67, 89, 3, 66]
#
# 怎么判断某个元素有没有重复？
#     li.count(1) > 1 : 重复
#     想知道列表里每个元素有没有重复，那你就得所有元素count一次，
# 你怎么知道每个重复的值，要删除几次呢？
#     count_num = li.count(1) # 3
#     count_num -1 # 要删除的次数。。。
#     li.remove(1)
#
# 首先得找到所有重复的值。。。
#     把所有重复的值，提出来，单独放一个列表。。。 统一循环删除。。。:
#     方法1:
#     duplicate_nums = [1, 3, 5...]
#
#     for i in duplicate_nums:
#         for j in range(li.count(i)-1)
#             li.remove(i)  # 重复了3次，要删除2次
#
#     方法2:
#     duplicate_nums = [[1,3],[3,3],[5,2]...]

li = [1, 3, 5, 3, 1, 6, 8, 5, 1, 9, 67, 89, 3, 66]
duplicate_nums = []
for i in li:
    i_show_count = li.count(i)   # 每个值 出现了几次
    if i_show_count > 1 and [i, i_show_count] not in duplicate_nums:   # 代表该值 是重复的,且该值不在重复列表里
        duplicate_nums.append([i, i_show_count])
print(duplicate_nums)

for item in duplicate_nums:
    # duplicate_n = item[0]
    # duplicate_times = item[1]
    duplicate_n,duplicate_times = item
    for j in range(duplicate_times-1): # 为何减1？ 因为是去重，而不是把所有的重复值删除，得保留一个重复值
        li.remove(duplicate_n)   # 一次只能删除一个值
        print("删除了一次：", duplicate_n)
print(li)
