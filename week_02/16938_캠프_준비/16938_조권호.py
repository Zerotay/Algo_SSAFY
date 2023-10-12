# 시간복잡도 2^n => 전체 부분집합개수 2^n에서 공집합, nC1일때 뺀것으로 2^n-n-1

import itertools

n,l,r,x = map(int,input().split())
difficulty = list(map(int,input().split()))

ans=0
for i in range(2,n+1):
    for c in itertools.combinations(difficulty,i):
        if (l<= sum(c) <=r) and (max(c) - min(c) >=x):
            ans+=1
print(ans)

