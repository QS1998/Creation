def trans(string):
    lists = [int(i) if '0' <= i <= '9' else i for i in string]
    return lists

while 1:
    lists0 = input("请输入需要转换的字符串：")
    print("转换后的字符串为:\n",trans(lists0))
