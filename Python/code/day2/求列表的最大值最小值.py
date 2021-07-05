
data = [9, 10, 33, 3, 5, 18, 4, 30, 25, 2, 11]
# print(max(data))
max_n = data[0]
min_n = data[0]
for i in data:
    if i > max_n:
        max_n = i
    if i < min_n:
        min_n = i
print(max_n)
print(min_n)
