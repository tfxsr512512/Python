

data = [9, 10, 26,17,33, 3, 5, 18, 34,4, 32, 25, 2, 11]
data2= [8,3,2,1,-5,19,2,4,6,7,11]
max_n = data[0] # 假设第1个值最大
for i in data:
    if i > max_n: # 交换
        max_n = i

print(max_n)