import sys
from itertools import combinations
input = sys.stdin.readline

N, L, R, X = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
for i in range(2, N+1):
    comb = list(combinations(lst, i))
    for combi in comb:
        if ((L <= sum(combi) <= R) and ((max(combi)-min(combi)) >= X)):
            cnt += 1
print(cnt)
