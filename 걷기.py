x, y, w, s = map(int, input().split())

if 2 * w <= s:
    print(w*(x+y))
elif 2*w > s:
    if x > y:
        if w < s:
            print(y * s + (x-y)*w)
        else:
            if (x-y) % 2 == 0:
                print(y * s + (x-y)*s)
            else:
                print(y * s + (x - y -1) * s + w)
    else:
        if w < s:
            print(x * s + (y-x)*w)
        else:
            if (x-y) % 2 == 0:
                print(x * s + (y-x)*s)
            else:
                print(x * s + (y - x -1) * s + w)

