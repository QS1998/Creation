def Dec2Bin(dec):
    result = ''
    
    if dec:
        result = Dec2Bin(dec//2)
        return result + str(dec%2)
    else:
        return result

x = int(input("请输入一个十进制数："))
print(Dec2Bin(x))
