f = open("model_contacts.txt", "a", encoding='utf-8')
f.write("黑姑娘  北京  165   50    18834252322\n")
f.write("黑姑娘2 北京  165   50    18834252322\n")
f.seek(0)
print(f.read())

