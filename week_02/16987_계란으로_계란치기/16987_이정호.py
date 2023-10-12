import sys
input = sys.stdin.readline

n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]
max_num = 0


def dfs(cnt):
    global max_num
    if cnt == n:
        sum = 0
        for i in range(n):
            if eggs[i][1] > 0:
                sum += 1

        max_num = max(max_num, sum)
        return

    if eggs[cnt][0] <= 0:
        dfs(cnt+1)
        return

    for i in range(n):
        if eggs[i][0] > 0 and i != cnt:
            eggs[i][0] -= eggs[cnt][1]
            eggs[cnt][0] -= eggs[i][1]
            dfs(cnt+1)
            eggs[i][0] += eggs[cnt][1]
            eggs[cnt][0] += eggs[i][1]
    dfs(cnt+1)
dfs(0)
print(max_num)
