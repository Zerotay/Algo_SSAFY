# 1405 미친 로봇 (G4)
# https://www.acmicpc.net/problem/1405
# 정답

m,e,w,s,n=map(int, input().split())
dir = [[0,1,e*0.01],[0,-1,w*0.01],[1,0,s*0.01],[-1,0,n*0.01]]
visited = set()
sim = 0

def recur(k,x,y, val):
    if k == m:
        global sim
        sim += val
        return
    visited.add((x,y))
    for i,j,d in dir:
        nx,ny=x+i,y+j
        if (nx,ny) in visited: continue
        recur(k+1, nx,ny, val*d)
    visited.discard((x,y))
       
recur(0,0,0,1)
print(sim)

# dfs+backtracking
# 전형적인 dfs에 확률을 추가한 방식
# 대충 생각하는 방식으로 구현하면 되더라