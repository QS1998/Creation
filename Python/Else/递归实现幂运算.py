def Power(x,y):
    if y == 1:
        return x
    else:
        return x * Power(x,y-1)

base = int(input("请输入底数："))
exp = int(input("请输入指数："))

print(Power(base,exp))
