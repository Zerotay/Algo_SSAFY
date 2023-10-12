import sys
input = sys.stdin.readline

ans = 0
H, W = map(int, input().split())
grid = [[0 for j in range(W)] for i in range(H)]
arr = list(map(int, input().split()))
for i in range(W):
    for j in range(arr[i]):
        grid[j][i] = True

tmp = 0

for i in range(H):
    for j in range(W):
        if grid[i][j]:
            while (j+1 < W and not grid[i][j+1]):
                j += 1
                tmp += 1
        if (j+1 < W and grid[i][j+1]):
            ans += tmp
        tmp = 0

print(ans)
