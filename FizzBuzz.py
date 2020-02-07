for x in range(1, 101):
    print("fizz"[x % 3 * len('fizz')::]+"buzz"[x % 5 * len('buzz')::] or x)
