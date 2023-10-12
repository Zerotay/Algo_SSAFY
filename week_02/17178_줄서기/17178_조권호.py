# 시간복잡도 n => std 리스트 한번 돌고(5n) 그 때 stack 쓰므로 최대 n이 더해질 수 있다.
import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(str,input().split())))

std = []
for i in range(n):
    for j in range(5):
        std.append(graph[i][j])
std.sort(key = lambda x : (x[:1], int(x[2:])), reverse=True)
stk = []    # max=4

idx = 0
x,y=0,0
flag=True
while std:
    while(stk and std[-1]==stk[-1]):
        stk.pop()
        std.pop()
    if (x<n and y<5):
        if std[-1] == graph[x][y]:
            std.pop()
        else:
            stk.append(graph[x][y])
    else:
        while (stk and std[-1] == stk[-1]):
            stk.pop()
            std.pop()
        if stk:
            flag=False
            break
    y+=1
    if y==5:
        y=0
        x+=1

if flag:
    print('GOOD')
else: print("BAD")
