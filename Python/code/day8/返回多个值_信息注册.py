def stu_registration_form():
    form = {
        "name":input("Name:").strip(),
        "age":input("Age:").strip(),
        "phone":input("Phone:").strip()
    }

    info_pass_flag = True
    for k,v in form.items():
        if len(v) == 0:
            info_pass_flag = False
            break
    return form, info_pass_flag


stu_info, flag = stu_registration_form()
print(stu_info)
print(flag)
if not flag:
    print("表单填写有误...")
else:
    print("欢迎来到王者荣耀!!!")
