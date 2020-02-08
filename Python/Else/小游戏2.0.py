import random
print("----------------我爱鱼C工作室------------------")
secret = random.randint(0,9)
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字:")
#while not isinstance(guess,int):
#    temp = input("格式错误，请重新输入:")
guess = int(temp)
i = 3
if guess == secret:
    print("卧槽，你是小甲鱼肚子里的蛔虫吗？！\n哼，猜中了也没奖励！")
while (guess != secret) & (i > 0):
    if guess <secret:
        print("嘿，小了小了~~~")
        temp = input("请重新输入吧:")
        #while ( isinstance(temp,int)):
          #  temp = input("格式错误，请重新输入:")
        guess =int(temp)
    else:
        print("哥，大了大了~~~")
        temp = input("请重新输入吧:")
        #while ( isinstance(temp,int)):
            #temp = input("格式错误，请重新输入:")
        guess = int(temp)
    i -= 1
    if guess == secret:
        print("恭喜你，猜对啦！\n哼，猜中了也没奖励！")
        break
    if ( guess != secret ) & ( i == 0 ):
        print("看来咱们真是心无灵犀啊┭┮﹏┭┮")
print("游戏结束，不玩啦●◡●")
