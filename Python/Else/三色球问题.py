print("红    黄    绿")
for i in range(4):
    for j in range(4):
        for k in range(2,7):
            if (i + j + k == 8):
                print(i,"    ",j,"    ",k)
