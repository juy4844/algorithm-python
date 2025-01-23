from collections import defaultdict

n, m = map(int, input().split())

w = input()
s = input()

check = defaultdict(int)
for i in w:
    check[i] += 1

a = sorted(w)

ans = 0

for i in range(len(s)):
    tmp = s[i:i + len(w)]
    x = sorted(tmp)
    if x == a:
        ans += 1

print(ans)
