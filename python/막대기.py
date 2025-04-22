x = int(input())

ans = 0

while x != 1:
    if x % 2 == 1:
        ans += 1
    x = x // 2

print(ans + 1)