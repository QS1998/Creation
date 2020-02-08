# 004.1.py
"""输入一个正整数，打印从1到这个正整数之间的正整数"""
print("请输入一个正整数:", end='')
temp = input()
num = int(temp)
i = 1

while i <= num:
    print(i)
    i += 1
