import copy,sys
sys.setrecursionlimit=10**6
n = int(input())

ans =0
def dfs(dep,eggs):
    global ans
    if(dep==n):
        cnt =0
        for i in range(n):
            if eggs[i][0] <=0:
                cnt+=1
        ans = max(cnt, ans)
        return
    if eggs[dep][0]>0:
        flag = True
        for i in range(n):
            if eggs[i][0] >0 and i !=dep:
                flag = False
                break
        if flag:
            ans = max(ans,n-1)
            return
        for i in range(n):
            if eggs[i][0] >0 and i !=dep:
                eggs[dep][0] -=eggs[i][1]
                eggs[i][0] -=eggs[dep][1]
                dfs(dep+1, eggs)
                eggs[dep][0] +=eggs[i][1]
                eggs[i][0] +=eggs[dep][1]
            
    else:
        dfs(dep+1, eggs)
        return

eggs = []

for i in range(n):
    eggs.append(list(map(int,input().split())))

dfs(0, eggs)
print(ans)