import sys
input = sys.stdin.readline

n = int(input())

li = []
for _ in range(n):
    a,b = map(int,input().split())
    li.append([-a,b])

li.append([0,sys.maxsize])
li.sort()

ans =0
for i in range(len(li)-1):
    if li[i+1][1]-li[i][1]>=0:
        ans+= (li[i+1][0]-li[i][0])*(li[i][1])
    else:
        li[i + 1][0]= li[i][0]
        li[i + 1][1] = li[i][1]
print(ans)