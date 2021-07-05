name = input("Your name:").strip() # 加上.strip()有空格会忽略掉
# age = int(input("Age:"))
age = input("Age:")
if age.isdigit():
	age = int(age)
else:
	print("错误地输入...")
	exit()
print(type(age))
hobby = input("Your hobby:")
job = input("Your job:")


msg = f'''
-------------{name}--------------
Name:{name}
Age:{age} , wow still young , in {30-age} you will 30
hobby:{hobby}
job:{job}
-----------end---------------
'''

print(msg)
