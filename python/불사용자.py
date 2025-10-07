from itertools import permutations

def check(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False

        for j in range(len(users[i])):
            if banned_id[i][j] == "*":
                continue
            if banned_id[i][j] != users[i][j]:
                return False
    return True

def customPermutation(user_id, r):

    results = []

    visited = [False] * len(user_id)

    def dfs(current_permutation):
        if len(current_permutation) == r:
            results.append(current_permutation[:])
            return

        for i in range(len(user_id)):
            if not visited[i]:
                visited[i] = True
                current_permutation.append(user_id[i])

                dfs(current_permutation)

                current_permutation.pop()
                visited[i] = False

    dfs([])
    return results


def solution(user_id, banned_id):
    user_permutation = customPermutation(user_id, len(banned_id))
    ban_set = []

    for users in user_permutation:
        if not check(users, banned_id):
            continue
        else:
            users = set(users)
            if users not in ban_set:
                ban_set.append(users)

    return len(ban_set)