# 2805 나무 자르기 (S2)
# https://www.acmicpc.net/problem/2805
# 정답

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
inlst = [*map(int, input().split())]
start = 0
end = max(inlst)
while start <= end:
	mid = (start + end) // 2
	tmp = sum([i - mid for i in inlst if i > mid])
	if tmp < m:
		end = mid - 1
	else:
		start = mid + 1
print(end)