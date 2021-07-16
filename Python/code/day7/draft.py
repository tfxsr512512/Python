li = [1, 3, 5, 3, 1, 6, 8, 5, 1, 9, 67, 89, 3, 66]
duplicate_nums = []

for i in li:
    if li.count(i) > 1 and [i, li.count(i)] not in duplicate_nums:
        duplicate_nums.append([i, li.count(i)])
print(duplicate_nums)

for i in duplicate_nums:
    duplicate_n = i[0]
    duplicate_num = i[1]
    for j in range(duplicate_num-1):
        li.remove(duplicate_n)
print(li)
