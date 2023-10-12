import sys
input = sys.stdin.readline

n = int(input())
limit = [*sorted(map(int, input().split()), reverse=True)]
m = int(input())
inlst = [*sorted(map(int, input().split()), reverse=True)]
if inlst[0] > limit[0]:
	print(-1)
	exit(0)

ans = 0
while inlst:
	if not inlst: break
	for i in limit:
		for j in inlst:
			if i < inlst[-1]: break
			if i >= j:
				inlst.remove(j)
				break
	ans += 1
print(ans)