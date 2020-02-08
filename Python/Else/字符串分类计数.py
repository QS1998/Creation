def count(*string):
    length = len(string)
    for i in range(length):
        letter = num = space = symbol = 0
        for j in string[i]:
            if 'A' <= j <= 'z':
                letter += 1
            elif '0' <= j <= '9':
                num += 1
            elif j == ' ':
                space += 1
            else:
                symbol += 1
        print("第%d个字符串共有：英文字母%d个，数字%d个，\
空格%d个，其它字符%d个。" % (i+1, letter, num, space, symbol))
