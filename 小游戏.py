print('----------------我爱鱼C工作室-----------------')
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
guess = int(temp)
if guess == 8:
    print("卧槽，你是小甲鱼心里的蛔虫吗？！")
    print("哼，猜中了也没有奖励！")
else:
    if guess > 8:
        print("哥，大了大了～～～")
    else:
        print("嘿，小了小了～～～")
print("游戏结束，不玩啦O∩_∩O哈哈")
