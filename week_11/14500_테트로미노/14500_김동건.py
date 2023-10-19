# 14500 테트로미노 (G4)
# https://www.acmicpc.net/problem/14500
# 정답

import sys

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
inlst = [[*map(int, input().split())] for _ in range(n)]

ans = 0
visited = [[0 for _ in range(m)] for _ in range(n)]


def tetris(x, y, dep, val):
    global ans
    if dep == 4:
        ans = max(ans, val)
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if -1 < nx < n and -1 < ny < m and not visited[nx][ny]:
            visited[nx][ny] = 1
            tetris(nx, ny, dep + 1, val + inlst[nx][ny])
            visited[nx][ny] = 0


def fu(x, y):
    global ans
    if (x, y) in {(0, 0), (0, m - 1), (n - 1, 0), (n - 1, m - 1)}:
        return

    if y == 0:
        tmp = inlst[x][y] + inlst[x - 1][y] + inlst[x + 1][y] + inlst[x][y + 1]
        ans = max(ans, tmp)
    elif y == m - 1:
        tmp = inlst[x][y] + inlst[x - 1][y] + inlst[x + 1][y] + inlst[x][y - 1]
        ans = max(ans, tmp)
    elif x == 0:
        tmp = inlst[x][y] + inlst[x + 1][y] + inlst[x][y - 1] + inlst[x][y + 1]
        ans = max(ans, tmp)
    elif x == n - 1:
        tmp = inlst[x][y] + inlst[x - 1][y] + inlst[x][y - 1] + inlst[x][y + 1]
        ans = max(ans, tmp)
    else:
        tmp = (
            inlst[x][y]
            + inlst[x - 1][y]
            + inlst[x + 1][y]
            + inlst[x][y - 1]
            + inlst[x][y + 1]
        )
        tmp -= min(inlst[x - 1][y], inlst[x + 1][y], inlst[x][y - 1], inlst[x][y + 1])
        ans = max(ans, tmp)
    return


for i in range(n):
    for j in range(m):
        tetris(i, j, 0, 0)
        fu(i, j)

print(ans)


# 완탐 구현
# 빠큐 모양 빼고는 한 점에서 출발해서 만들 수 있는 모양들이다.
# 모든 점에서 만들 수 있는 모든 모양을 만들어본다.
# 한 점에서 출발해서 만들 수 있는 모든 모양은 4 * 3 * 3, 빠큐 모양 4개.
# 즉 한 점에서는 중복 다 포함 최대 40개의 모양이 나온다.
# 500 * 500 * 40 = 천만
# 완탐 쌉가넝~
