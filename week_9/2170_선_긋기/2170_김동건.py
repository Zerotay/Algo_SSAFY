# 2170 선 긋기(G5)
# https://www.acmicpc.net/problem/2170
# 정답

import sys

input = sys.stdin.readline
n = int(input())
lst = [[*map(int, input().split())] for _ in range(n)]
lst.sort()
pe = -1000000000
ans = 0
for s, e in lst:
    if e <= pe:
        continue
    small = pe if s < pe else s
    ans += e - small
    pe = max(pe, e)
print(ans)

# 앞쪽을 기준으로 정렬한다.
# 하나하나 살펴가면서 이전 선분과 현재 선분이 겹치는지 확인한다
# 겹치면 ? 겹친 부분만큼 정답에서 빼준다
# 안 겹치면 ? 정답에 그냥 다 더한다
# 이때 겹치는 게 완전히 포함하는 관계일 수도 있음을 유의한다

# 시간 초과가 잘 난다.
# 우선순위큐는 시간초과.
