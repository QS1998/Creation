import random
times = 3
secret = random.randint(0,9)
print('-----------我爱鱼C工作室----------')
guess = 0
print('不妨猜一下小甲鱼现在心里想的是哪个数字(只有3次机会哦!):',end=" ")
while (guess != secret) and (times > 0):
    temp = input()
    guess = int(temp)
    times = times -1
    if guess == secret:
        print("卧槽，你是小甲鱼肚子里的蛔虫吗?!")
        print("哼，猜中了也没有奖励！")
    else:
        if guess > secret:
            print("哎呀呀，大了大了～")
        else:
            print("哎呀呀，小了小了～")
        if times > 0:
            print("再试一次吧:",end=" ")
        else:
            print("机会用光咯o╥﹏╥o")
print("游戏结束，不玩啦┏＾0＾┛")
