# 根据用户输入的正整数输出相应的星星图案
print("请输入一个正整数：", end='')
temp = input()
num = int(temp)

for i in range(num):
    for j in range((num-i) * 2):
        if j < (num-i):
            print(' ', end='')
        else:
            print('*', end='')
    print()
