import sys
sys.setrecursionlimit=10**8
n = int(input())

def dfs(dep, st):
    if dep == n:
        print(st)
        exit(0)
    
    for i in range(1,4):
        flag = True
        tmp = st+str(i)
        w = dep+1
        for j in range(1, w//2+1):
            if(st[-j:]==st[-2*j:-j]):
                flag = False
                break
        if flag:
            dfs(dep+1,tmp)
    return

dfs(1, '1')