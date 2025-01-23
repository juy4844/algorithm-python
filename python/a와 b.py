s = list(input())
t = list(input())

while len(s) != len(t):
    if t[len(t) - 1] == "A":
        t.pop()
    else:
        t.pop()
        t.reverse()

if (s == t):
    print(1)
else:
    print(0)