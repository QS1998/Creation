def hwl(string):
    list0 = list(string)
    list1 = list0[::-1]
    if list1 == list0:
        print("是回文联！")
    else:
        print("不是回文联！")


temp = input("请输入一句话：")
hwl(temp)
