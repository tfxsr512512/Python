
f = open("递归.py", encoding='utf-8')
code = compile(f.read(), '', 'exec')   # 解析代码文件，str
print(code)
exec(code)   # 执行代码块
