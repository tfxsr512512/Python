height = 100
distance = 0
count = 0
while count < 10:
    distance += height # 记录坠落时经过的长度
    height /= 2   # 反弹回的高度
    distance += height # 记录反弹经过的长度
    count += 1
    print(f"第{count}次反弹完，小球经过{distance}米......")
