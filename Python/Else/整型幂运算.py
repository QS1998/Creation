def power(x,y):
    z = 1
    for i in range(y):
        z *= x
    return z

a,b = input("请输入两个参数：").split(',')
A = int(a)
B = int(b)
C = power(A,B)
print("%G ^ %G = %G" %(A,B,C))
