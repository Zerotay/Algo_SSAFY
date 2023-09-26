# 16724 피리 부는 사나이(G3)
# https://www.acmicpc.net/problem/16724
# 정답

import sys

sys.setrecursionlimit(1000 * 1000)
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [list(input().rstrip()) for _ in range(n)]
dir = {"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1)}
ans = 0
par = [i for i in range(n * m)]


def find(a):
    if par[a] == a:
        return a
    par[a] = find(par[a])
    return par[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False
    elif a > b:
        par[b] = a
    else:
        par[a] = b
    return True


for i in range(n * m):
    cx, cy = divmod(i, m)
    des = dir[lst[cx][cy]]
    dx, dy = cx + des[0], cy + des[1]
    union(i, dx * m + dy)
for i in range(n * m):
    find(i)
print(len(set(par)))


# 접근 1
# 그냥 방문 안 되는 놈들 진행시켜 영차
# 접근 순서 고려가 안 돼서 값이 높게 나옴

# 접근 2
# 결국 어디론가로 모이게 돼있다. 뺑뺑이를 돌 수도 있고
# 그래프에서 유니온 파인드하는 거랑 같다
# 진행시켜 영차 => 성공
