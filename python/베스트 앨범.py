from collections import defaultdict


def solution(genres, plays):
    answer = []

    genresCount = defaultdict(int)
    genresdict = defaultdict(list)

    for i in range(len(genres)):
        genresCount[genres[i]] += plays[i]
        genresdict[genres[i]].append((plays[i], i))

    ls = sorted(genresCount.items(), key=lambda x: -x[1])

    for key in genresdict:
        genresdict[key].sort(key=lambda x: (-x[0], x[1]))

    for genre, cnt in ls:

        if len(genresdict[genre]) >= 2:
            answer.append(genresdict[genre][0][1])
            answer.append(genresdict[genre][1][1])
        else:
            answer.append(genresdict[genre][0][1])

    return answer