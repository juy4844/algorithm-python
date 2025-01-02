n = list(input())

ten = False

for i in range(len(n)):
    if n[i] == '0':
        ten = True
        break

sum = 0

for i in range(len(n)):
    sum += int(n[i])

n.sort(reverse=True)
if ten == True and sum % 3 == 0:
    answer = "".join(n)
    print(answer)
else:
    print(-1)