import sys
input = sys.stdin.readline
global N

def dfs(line):
    size = len(line)
    for i in range(1, (size//2)+1):
        if line[-2*i:-i] == line[-i:]:
            return
    if size == N:
        print(line)
        exit()
    else:
        for i in range(N):
            dfs(line + "1")
            dfs(line + "2")
            dfs(line + "3")
N = int(input())
dfs("")
