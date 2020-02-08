secret = "FishC.com"
ans = input("请输入密码:")
times = 5
while ans != secret:
    if times == 1:
        print("您已经5次输错密码，请10分钟后重试！")
        break
    while '*' in ans:
        ans = input('密码中不能含有"*"号！您还有%d次机会！请输入密码：'%times)
    times -= 1
    ans = input("密码输入错误！您还有%d次机会！请输入密码："%times)

if ans == secret:
    print("密码正确，进入程序......")
