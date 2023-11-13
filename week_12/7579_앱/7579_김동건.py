# 7579 앱 (G3)
# https://www.acmicpc.net/problem/7579
# 정답

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
byte = [*map(int, input().split())]
cost = [*map(int, input().split())]

lst =[0 for _ in range(sum(cost))]
answer = sum(cost)
for i in range(n):
	for j in range(len(lst)-1,-1,-1):
		if cost[i] > j: pass
		else: lst[j] = max(lst[j], byte[i] + lst[j-cost[i]])
		if lst[j] >= m: answer = min(answer, j)
print(answer)    


# 냅색