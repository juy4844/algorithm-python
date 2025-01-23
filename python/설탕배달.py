n = int(input())

a = n // 5
b = n % 5

if b == 0:
    print(a)
elif b == 3:
    print(a+1)
elif b == 1:
    if a == 0:
        print(-1)
    else:
        print(a+1)
elif b == 2:
    if a < 2:
        print(-1)
    else:
        print(a+2)
elif b == 4:
    if a == 0:
        print(-1)
    else:
        print(a+2)