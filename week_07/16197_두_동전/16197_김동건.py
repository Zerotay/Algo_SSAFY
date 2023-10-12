from collections import deque

n, m = map(int, input().split())
inlst = [list(input()) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
pos = []
for i in range(n):
    for j in range(m):
        if inlst[i][j] == "o":
            pos.append((i, j))

count = 0
que = deque()
que.append((pos[0], pos[1], 0))


def move(cur, k):
    nx, ny = cur[0] + dx[k], cur[1] + dy[k]
    if -1 < nx < n and -1 < ny < m:
        if inlst[nx][ny] == "#":
            return cur
        return (nx, ny)
    return (-1, -1)


while que:
    cur1, cur2, cnt = que.popleft()
    if cnt == 11:
        print(-1)
        exit()
    if sum(cur1) == -2 or sum(cur2) == -2:
        print(cnt)
        exit()
    for k in range(4):
        nx1, ny1 = move(cur1, k)
        nx2, ny2 = move(cur2, k)
        if sum((nx1, ny1, nx2, ny2)) == -4:
            continue
        que.append(((nx1, ny1), (nx2, ny2), cnt + 1))
