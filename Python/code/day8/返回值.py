def mobile_check(phone_num):
    if len(phone_num) == 11:
        if phone_num.isdigit():
            if phone_num.startswith('1'):
                return True, phone_num


s = '18655721386'
print(mobile_check(s))
# if mobile_check(s):
#     print("合法的手机号...")
