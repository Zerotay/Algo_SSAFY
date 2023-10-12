from itertools import combinations as cb

inlst = [[*map(int, input().split())] for _ in range(4)]
country = [i * 3 for i in range(6)]
case = [[0, 2], [1, 1], [2, 0]]
ans = [0 for i in range(4)]


def recur(leg, k):
    if ans[leg] == 1:
        return
    if k == 15:
        for i in range(6):
            if inlst[leg][i * 3] + inlst[leg][i * 3 + 1] + inlst[leg][i * 3 + 2]:
                return
        ans[leg] = 1
        return
    first, second = total[k][0], total[k][1]
    for i, j in case:
        if inlst[leg][first + i] > 0 and inlst[leg][second + j] > 0:
            inlst[leg][first + i] -= 1
            inlst[leg][second + j] -= 1
            recur(leg, k + 1)
            inlst[leg][first + i] += 1
            inlst[leg][second + j] += 1


total = list(cb(country, 2))
for i in range(4):
    recur(i, 0)
print(*ans)
