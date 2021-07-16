f = open("model_contacts.txt", encoding='utf-8')
# data = f.read()  # 读所有
# print(data)
# data = f.read(10)  # 代表是个字符
# print(data)
print(f.readline())
print(f.readline())
print(f.readline())
print('--------中间--------')

# f.seek(0)  # 光标移到开头
# print(f.readline())

for line in f:
    if "梓萱" in line:
        print(line)
