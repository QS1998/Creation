score = {}
i = 0
j = 0

while i <10:
    j = input("请输入成绩:")
    score[i] = int(j)
    if ( 60 <= score[i] < 80 ):
        print("C")
        i += 1
    elif ( 80 <= score[i] < 90):
        print("B")
        i += 1
    elif ( 90 <= score[i] <= 100):
        print("A")
        i += 1
    elif ( 0 <= score[i] <60 ):
        print("D")
        i += 1
    else:
        print("输入错误，请重新输入:")
print("成绩录入完毕!")

