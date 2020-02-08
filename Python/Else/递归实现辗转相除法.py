def Gcd(x,y):
    if (x == 0 or y == 0):
        return [x,y][x<y]
    else:
        return Gcd(y,x%y)

x,y = map(int,input("请输入两个参数：").split(','))
print(Gcd(x,y))
