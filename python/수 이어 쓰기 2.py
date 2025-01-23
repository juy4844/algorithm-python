n, k = map(int, input().split())

if k <= 9:
    print(k)
    exit()
a = 1
b = 0
while True:
    if k <= b + 9*a*(10**(a-1)):
        break
    b = b + 9*a*(10**(a-1))
    a+=1

if (k-b) % a == 0:
    print((10**(a-1) + ((k-b) // a - 1)) % 10)
else:
    print(((10**(a-1) + ((k-b) // a - 1)) // (10**(a - ((k-b) % a)))) % 10)
