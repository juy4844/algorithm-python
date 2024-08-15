S = input()
T = input()

def dfs(T):
    if len(S) == len(T):
        if S == T:
            return 1
        else:
            return 0
    if T[-1] == 'A':
        if dfs(T[:-1:]) == 1:
            return 1
    if T[0] == 'B':
        if dfs(T[1::][::-1]) == 1:
            return 1
    
    return 0

print(dfs(T))