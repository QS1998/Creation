def gcd(a, b):
    while a != 0:
        a, b = b % a, a
 
    return b

while 1:
    x,y = input("请输入两个整数：").split(',')
    X,Y = int(x),int(y)
    print("%d与%d的最大公约数为:%d"%(X,Y,gcd(X,Y)))
